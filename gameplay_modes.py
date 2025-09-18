"""
Enhanced Gameplay Modes

Implements stealth missions, investigative tasks, and team-based battles
for varied gameplay experiences.
"""

from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
import random
from character import Player, Enemy, Trait


class MissionType(Enum):
    """Different types of missions available."""
    STEALTH = "stealth"
    INVESTIGATION = "investigation"
    TEAM_BATTLE = "team_battle"
    ESCORT = "escort"
    SURVIVAL = "survival"
    RESCUE = "rescue"


class StealthSystem:
    """Manages stealth-based gameplay mechanics."""
    
    def __init__(self):
        self.detection_level = 0  # 0-100, higher means more likely to be detected
        self.stealth_points = 100  # Resource for stealth actions
        self.noise_level = 0  # Accumulated noise affects detection
        
    def calculate_stealth_success(self, player: Player, action_difficulty: int) -> bool:
        """Calculate if a stealth action succeeds."""
        # Base stealth skill from traits
        stealth_skill = 50
        
        # Trait bonuses
        dominant_traits = player.get_dominant_traits()
        for trait in dominant_traits:
            if trait == Trait.CAUTIOUS:
                stealth_skill += 20
            elif trait == Trait.ANALYTICAL:
                stealth_skill += 15
            elif trait == Trait.FOCUSED:
                stealth_skill += 10
            elif trait == Trait.RECKLESS:
                stealth_skill -= 15
        
        # Environmental and state modifiers
        fatigue_penalty = getattr(player, 'stamina_system', None)
        if fatigue_penalty and hasattr(fatigue_penalty, 'fatigue_level'):
            stealth_skill -= fatigue_penalty.fatigue_level // 5
        
        # Noise penalty
        stealth_skill -= self.noise_level
        
        # Calculate success chance
        success_chance = max(10, stealth_skill - action_difficulty)
        return random.randint(1, 100) <= success_chance
    
    def perform_stealth_action(self, player: Player, action: str) -> Dict[str, Any]:
        """Perform a stealth action."""
        actions = {
            "sneak_past": {"difficulty": 30, "noise": 5, "cost": 15},
            "pickpocket": {"difficulty": 50, "noise": 10, "cost": 20},
            "silent_takedown": {"difficulty": 70, "noise": 15, "cost": 30},
            "hide": {"difficulty": 20, "noise": 0, "cost": 10},
            "observe": {"difficulty": 25, "noise": 0, "cost": 5}
        }
        
        if action not in actions:
            return {"success": False, "message": "Unknown stealth action"}
        
        action_data = actions[action]
        
        # Check stealth points
        if self.stealth_points < action_data["cost"]:
            return {"success": False, "message": "Not enough stealth points"}
        
        # Attempt the action
        success = self.calculate_stealth_success(player, action_data["difficulty"])
        
        if success:
            self.stealth_points -= action_data["cost"]
            self.noise_level += action_data["noise"] // 2  # Reduced noise on success
            
            return {
                "success": True,
                "message": f"Successfully performed {action.replace('_', ' ')}",
                "result": self._get_action_result(action)
            }
        else:
            self.stealth_points -= action_data["cost"]
            self.noise_level += action_data["noise"]
            self.detection_level += 20
            
            return {
                "success": False,
                "message": f"Failed {action.replace('_', ' ')} - increased detection risk",
                "detected": self.detection_level >= 80
            }
    
    def _get_action_result(self, action: str) -> Dict[str, Any]:
        """Get specific results for successful stealth actions."""
        results = {
            "sneak_past": {"bypass_enemy": True, "experience": 25},
            "pickpocket": {"item_found": "cursed_tool_fragment", "experience": 30},
            "silent_takedown": {"enemy_eliminated": True, "experience": 50},
            "hide": {"detection_reduced": 30, "experience": 15},
            "observe": {"intel_gained": True, "experience": 20}
        }
        return results.get(action, {})


class InvestigationSystem:
    """Manages investigation and detective gameplay."""
    
    def __init__(self):
        self.clues_found = []
        self.investigation_points = 100
        self.case_progress = 0  # 0-100%
        
    def search_area(self, player: Player, area: str) -> Dict[str, Any]:
        """Search an area for clues."""
        search_difficulty = random.randint(20, 60)
        
        # Analytical trait bonus
        search_skill = 40
        dominant_traits = player.get_dominant_traits()
        
        for trait in dominant_traits:
            if trait == Trait.ANALYTICAL:
                search_skill += 25
            elif trait == Trait.FOCUSED:
                search_skill += 15
            elif trait == Trait.CAUTIOUS:
                search_skill += 10
        
        # Level bonus
        search_skill += player.level * 2
        
        success_chance = max(20, search_skill - search_difficulty)
        success = random.randint(1, 100) <= success_chance
        
        if success:
            clue = self._generate_clue(area)
            self.clues_found.append(clue)
            self.case_progress += random.randint(10, 25)
            self.investigation_points -= 15
            
            return {
                "success": True,
                "clue": clue,
                "progress": min(100, self.case_progress),
                "message": f"Found clue: {clue['name']}"
            }
        else:
            self.investigation_points -= 10
            return {
                "success": False,
                "message": "Nothing of interest found in this area",
                "progress": self.case_progress
            }
    
    def _generate_clue(self, area: str) -> Dict[str, Any]:
        """Generate a clue based on the area being searched."""
        clue_types = {
            "crime_scene": [
                {"name": "Cursed Energy Residue", "type": "physical", "value": "recent_curse_activity"},
                {"name": "Torn Fabric", "type": "physical", "value": "victim_struggled"},
                {"name": "Strange Markings", "type": "magical", "value": "ritual_performed"}
            ],
            "witness_location": [
                {"name": "Eyewitness Account", "type": "testimony", "value": "suspect_description"},
                {"name": "Security Footage", "type": "evidence", "value": "time_of_incident"},
                {"name": "Personal Belongings", "type": "physical", "value": "victim_identity"}
            ],
            "suspect_hideout": [
                {"name": "Cursed Tool", "type": "weapon", "value": "suspect_capability"},
                {"name": "Written Notes", "type": "document", "value": "motive_revealed"},
                {"name": "Ritual Components", "type": "magical", "value": "planned_ceremony"}
            ]
        }
        
        area_clues = clue_types.get(area, clue_types["crime_scene"])
        return random.choice(area_clues)
    
    def analyze_clues(self, player: Player) -> Dict[str, Any]:
        """Analyze collected clues to progress the case."""
        if len(self.clues_found) < 2:
            return {"success": False, "message": "Need more clues to analyze"}
        
        analysis_skill = 30 + (player.level * 3)
        
        # Trait bonuses for analysis
        dominant_traits = player.get_dominant_traits()
        for trait in dominant_traits:
            if trait == Trait.ANALYTICAL:
                analysis_skill += 30
            elif trait == Trait.FOCUSED:
                analysis_skill += 20
        
        # Check if we can solve the case
        if self.case_progress >= 80 and random.randint(1, 100) <= analysis_skill:
            return {
                "success": True,
                "case_solved": True,
                "message": "Case solved! All evidence points to the culprit.",
                "reward": {"experience": 100, "reputation": 50}
            }
        elif self.case_progress >= 50:
            breakthrough = random.randint(1, 100) <= (analysis_skill - 20)
            if breakthrough:
                self.case_progress += 20
                return {
                    "success": True,
                    "breakthrough": True,
                    "message": "Breakthrough! The clues reveal a new lead.",
                    "progress": self.case_progress
                }
        
        return {
            "success": False,
            "message": "The clues don't form a clear picture yet. Need more evidence.",
            "progress": self.case_progress
        }


class TeamBattleSystem:
    """Manages team-based combat scenarios."""
    
    def __init__(self):
        self.team_members = []
        self.team_synergy = 0  # 0-100, affects combo attacks
        self.formation = "standard"
        
    def add_team_member(self, member: Dict[str, Any]):
        """Add a team member."""
        self.team_members.append(member)
        self._calculate_synergy()
    
    def _calculate_synergy(self):
        """Calculate team synergy based on member compatibility."""
        if len(self.team_members) < 2:
            self.team_synergy = 0
            return
        
        synergy_bonus = 0
        
        # Check for complementary traits
        all_traits = []
        for member in self.team_members:
            all_traits.extend(member.get("traits", []))
        
        # Synergy combinations
        if Trait.PROTECTIVE in all_traits and Trait.AGGRESSIVE in all_traits:
            synergy_bonus += 20  # Tank and DPS combo
        
        if Trait.ANALYTICAL in all_traits and Trait.FOCUSED in all_traits:
            synergy_bonus += 25  # Strategic planning combo
        
        if Trait.DETERMINED in all_traits:
            synergy_bonus += 10 * all_traits.count(Trait.DETERMINED)
        
        # Level balance bonus
        levels = [member.get("level", 1) for member in self.team_members]
        if max(levels) - min(levels) <= 3:
            synergy_bonus += 15  # Balanced team levels
        
        self.team_synergy = min(100, synergy_bonus)
    
    def execute_combo_attack(self, player: Player, allies: List, target: Enemy) -> Dict[str, Any]:
        """Execute a team combo attack."""
        if self.team_synergy < 30:
            return {"success": False, "message": "Team synergy too low for combo attacks"}
        
        # Combo attack power based on synergy and participants
        base_damage = 50
        synergy_multiplier = 1 + (self.team_synergy / 100)
        team_size_bonus = len(self.team_members) * 0.2
        
        total_damage = int(base_damage * synergy_multiplier * (1 + team_size_bonus))
        
        # Apply damage
        actual_damage = target.take_damage(total_damage)
        
        # Generate combo description
        combo_name = self._generate_combo_name()
        
        return {
            "success": True,
            "combo_name": combo_name,
            "damage": actual_damage,
            "message": f"Team executes {combo_name} for {actual_damage} damage!",
            "synergy_bonus": self.team_synergy
        }
    
    def _generate_combo_name(self) -> str:
        """Generate a combo attack name based on team composition."""
        combo_names = [
            "Synchronized Strike",
            "Unity Assault",
            "Harmonic Devastation",
            "Coordinated Chaos",
            "Perfect Formation",
            "Resonance Attack",
            "Combined Technique"
        ]
        
        # Special names based on synergy level
        if self.team_synergy >= 80:
            combo_names.extend(["Divine Coordination", "Transcendent Unity"])
        elif self.team_synergy >= 60:
            combo_names.extend(["Superior Teamwork", "Elite Formation"])
        
        return random.choice(combo_names)
    
    def set_formation(self, formation: str) -> Dict[str, Any]:
        """Set team formation affecting combat bonuses."""
        formations = {
            "defensive": {"defense_bonus": 1.3, "attack_penalty": 0.9},
            "offensive": {"attack_bonus": 1.3, "defense_penalty": 0.9},
            "balanced": {"all_stats_bonus": 1.1},
            "support": {"healing_bonus": 1.5, "team_synergy_bonus": 20}
        }
        
        if formation in formations:
            self.formation = formation
            return {
                "success": True,
                "formation": formation,
                "bonuses": formations[formation]
            }
        
        return {"success": False, "message": "Unknown formation"}


class MissionManager:
    """Manages different mission types and objectives."""
    
    def __init__(self):
        self.active_missions = []
        self.completed_missions = []
        self.stealth_system = StealthSystem()
        self.investigation_system = InvestigationSystem()
        self.team_battle_system = TeamBattleSystem()
    
    def start_mission(self, mission_type: MissionType, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Start a new mission of the specified type."""
        mission = {
            "type": mission_type,
            "parameters": parameters,
            "progress": 0,
            "status": "active",
            "objectives": self._generate_objectives(mission_type, parameters)
        }
        
        self.active_missions.append(mission)
        return mission
    
    def _generate_objectives(self, mission_type: MissionType, parameters: Dict[str, Any]) -> List[str]:
        """Generate objectives based on mission type."""
        objectives = {
            MissionType.STEALTH: [
                "Infiltrate the target location undetected",
                "Retrieve the cursed object",
                "Avoid combat encounters",
                "Escape without raising alarms"
            ],
            MissionType.INVESTIGATION: [
                "Gather clues about the incident",
                "Interview witnesses",
                "Analyze evidence",
                "Identify the culprit"
            ],
            MissionType.TEAM_BATTLE: [
                "Coordinate with allies",
                "Defeat the boss enemy",
                "Protect team members",
                "Execute combo attacks"
            ],
            MissionType.ESCORT: [
                "Protect the VIP",
                "Reach the destination safely",
                "Eliminate threats along the route"
            ],
            MissionType.SURVIVAL: [
                "Survive for the specified duration",
                "Manage limited resources",
                "Adapt to changing conditions"
            ],
            MissionType.RESCUE: [
                "Locate the missing person",
                "Extract them safely",
                "Neutralize captors"
            ]
        }
        
        return objectives.get(mission_type, ["Complete the mission"])
    
    def update_mission_progress(self, mission_id: int, progress_change: int) -> bool:
        """Update progress for an active mission."""
        if 0 <= mission_id < len(self.active_missions):
            mission = self.active_missions[mission_id]
            mission["progress"] = min(100, mission["progress"] + progress_change)
            
            if mission["progress"] >= 100:
                mission["status"] = "completed"
                self.completed_missions.append(mission)
                self.active_missions.remove(mission)
                return True
        
        return False