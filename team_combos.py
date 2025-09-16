"""
Team Combo System

Manages powerful combination techniques that become available through
strong relationships and emotional bonds between characters.
"""

from typing import Dict, List, Any, Optional
import random


class TeamCombo:
    """Represents a team combination technique."""
    
    def __init__(self, name: str, participants: List[str], 
                 relationship_requirement: int, damage_multiplier: float,
                 description: str, special_effects: List[str]):
        self.name = name
        self.participants = participants
        self.relationship_requirement = relationship_requirement
        self.damage_multiplier = damage_multiplier
        self.description = description
        self.special_effects = special_effects


class TeamComboManager:
    """Manages team combination techniques and their requirements."""
    
    def __init__(self):
        self.combos = {}
        self._initialize_combos()
    
    def _initialize_combos(self):
        """Initialize all team combination techniques."""
        
        # Yuji + Player combos
        self.combos["black_flash_synchronization"] = TeamCombo(
            "Black Flash Synchronization",
            ["player", "yuji"],
            80,
            2.5,
            """⚡ You and Yuji move as one, your cursed energy synchronizing perfectly. 
Two Black Flashes connect simultaneously, creating a resonance that shakes reality itself. 
The combined impact transcends what either of you could achieve alone.""",
            ["guaranteed_critical", "energy_restoration", "stun_chance"]
        )
        
        self.combos["brotherhood_strike"] = TeamCombo(
            "Brotherhood Strike",
            ["player", "yuji"],
            60,
            2.0,
            """🤝 Drawing strength from your unbreakable bond, you and Yuji launch a 
coordinated assault. Your shared determination amplifies each blow, turning friendship 
into devastating power.""",
            ["damage_boost", "healing", "trait_enhancement"]
        )
        
        # Megumi + Player combos
        self.combos["shadow_technique_fusion"] = TeamCombo(
            "Shadow Technique Fusion",
            ["player", "megumi"],
            85,
            2.2,
            """🌑 Your cursed energy merges with Megumi's shadows, creating techniques 
neither of you could perform alone. The darkness responds to both your wills, 
weaving attacks that ignore conventional defenses.""",
            ["ignore_defenses", "confusion", "shadow_bind"]
        )
        
        self.combos["tactical_precision"] = TeamCombo(
            "Tactical Precision",
            ["player", "megumi"],
            70,
            1.8,
            """🎯 Megumi's strategic mind guides your attack with perfect timing. 
Every strike hits exactly where it needs to, exploiting weaknesses with surgical precision.""",
            ["weakness_exploitation", "accuracy_boost", "technique_enhancement"]
        )
        
        # Nobara + Player combos
        self.combos["resonance_destruction"] = TeamCombo(
            "Resonance Destruction",
            ["player", "nobara"],
            90,
            2.8,
            """💥 You and Nobara create a resonance between your cursed techniques that 
amplifies destruction exponentially. The enemy is struck not just physically, 
but at the very core of their spiritual existence.""",
            ["true_damage", "spiritual_damage", "resonance_effect"]
        )
        
        self.combos["fierce_determination"] = TeamCombo(
            "Fierce Determination",
            ["player", "nobara"],
            65,
            2.1,
            """🔥 Your combined fighting spirit burns brighter than any flame. 
Nobara's fierce confidence amplifies your own resolve, creating attacks that 
refuse to be denied.""",
            ["unstoppable", "confidence_boost", "critical_enhancement"]
        )
        
        # Todo + Player combos
        self.combos["brotherhood_ultimate"] = TeamCombo(
            "Brotherhood Ultimate Strike",
            ["player", "todo"],
            95,
            3.0,
            """🌟 The ultimate expression of brotherhood transcends mere technique. 
You and Todo fight as extensions of the same soul, your combined power 
reaching levels that defy comprehension.""",
            ["massive_damage", "soul_resonance", "technique_evolution"]
        )
        
        self.combos["boogie_woogie_combo"] = TeamCombo(
            "Boogie Woogie Combination",
            ["player", "todo"],
            75,
            2.3,
            """🔄 Todo's position-switching technique creates impossible attack angles. 
You appear where enemies least expect, striking from directions that shouldn't exist.""",
            ["position_advantage", "surprise_attack", "disorientation"]
        )
        
        # Triple combinations
        self.combos["first_year_trinity"] = TeamCombo(
            "First Year Trinity Strike",
            ["player", "yuji", "megumi", "nobara"],
            70,  # Average relationship requirement
            3.5,
            """✨ The first-year students unite as one unstoppable force. Years of shared 
trials, victories, and bonds culminate in perfect synchronization. This isn't just 
a combination attack - it's the physical manifestation of friendship itself.""",
            ["area_damage", "friendship_power", "ultimate_technique", "status_immunity"]
        )
        
        # Gojo-inspired combinations (rare, high level)
        self.combos["limitless_mastery"] = TeamCombo(
            "Limitless Technique Mastery",
            ["player", "gojo"],
            100,
            4.0,
            """♾️ Under Gojo's guidance, you briefly touch the true nature of the Limitless. 
Space bends to your combined will as master and student achieve perfect harmony. 
This is power that approaches the divine.""",
            ["space_manipulation", "limitless_power", "master_student_bond", "reality_alteration"]
        )
        
        # Special awakening combos (unlock through emotional moments)
        self.combos["shared_awakening"] = TeamCombo(
            "Shared Cursed Technique Awakening",
            ["player", "any_ally"],
            85,
            3.2,
            """💫 Your emotional connection with your ally triggers simultaneous technique 
evolution. Two souls resonate as one, awakening power neither could achieve alone. 
This is the true meaning of fighting alongside someone you trust completely.""",
            ["technique_awakening", "shared_power", "emotional_resonance", "permanent_bond"]
        )
    
    def get_available_combos(self, relationships: Dict[str, int], 
                           available_allies: List[str]) -> List[TeamCombo]:
        """Get list of team combos currently available."""
        available_combos = []
        
        for combo_name, combo in self.combos.items():
            # Check if all required participants are available
            required_allies = [p for p in combo.participants if p != "player"]
            
            # Handle "any_ally" requirement
            if "any_ally" in required_allies:
                if not available_allies:
                    continue
                # Find best relationship among available allies
                best_relationship = max(relationships.get(ally, 0) for ally in available_allies)
                if best_relationship >= combo.relationship_requirement:
                    available_combos.append(combo)
                continue
            
            # Check specific ally requirements
            combo_available = True
            for ally in required_allies:
                if ally not in available_allies:
                    combo_available = False
                    break
                if relationships.get(ally, 0) < combo.relationship_requirement:
                    combo_available = False
                    break
            
            if combo_available:
                available_combos.append(combo)
        
        return available_combos
    
    def execute_combo(self, combo: TeamCombo, base_damage: int, 
                     participants: List[str]) -> Dict[str, Any]:
        """Execute a team combination technique."""
        final_damage = int(base_damage * combo.damage_multiplier)
        
        result = {
            "name": combo.name,
            "damage": final_damage,
            "participants": participants,
            "description": combo.description,
            "special_effects": combo.special_effects,
            "success": True
        }
        
        # Display the combo execution
        self._display_combo_execution(combo, participants)
        
        return result
    
    def _display_combo_execution(self, combo: TeamCombo, participants: List[str]):
        """Display the dramatic execution of a team combo."""
        print(f"\n🌟 TEAM COMBINATION TECHNIQUE 🌟")
        print("=" * 70)
        print(f"✨ {combo.name}")
        print("-" * 70)
        
        # Show participants
        participant_text = " & ".join(participants)
        print(f"👥 Participants: {participant_text}")
        print("-" * 70)
        
        # Show description with dramatic pauses
        lines = combo.description.split(". ")
        for line in lines:
            if line.strip():
                print(f"{line.strip()}.")
                print()  # Empty line for dramatic effect
        
        # Show special effects
        print("✨ Special Effects:")
        for effect in combo.special_effects:
            effect_name = effect.replace("_", " ").title()
            print(f"  • {effect_name}")
        
        print("=" * 70)
    
    def get_combo_by_name(self, combo_name: str) -> Optional[TeamCombo]:
        """Get a specific combo by name."""
        return self.combos.get(combo_name.lower().replace(" ", "_"))
    
    def unlock_special_combo(self, combo_name: str, game_state):
        """Unlock a special combo through story progression."""
        combo = self.get_combo_by_name(combo_name)
        if combo:
            game_state.add_story_flag(f"unlocked_combo_{combo_name.lower().replace(' ', '_')}", True)
            print(f"\n🔓 Special Combo Unlocked: {combo.name}")
            print(f"   {combo.description}")
            return True
        return False
    
    def check_combo_unlocks(self, game_state, recent_events: List[str]) -> List[str]:
        """Check if any special combos should be unlocked based on story events."""
        unlocked_combos = []
        
        # Check for brotherhood moment with Yuji
        if ("brotherhood_with_yuji" in game_state.story_flags and 
            not game_state.get_story_flag("unlocked_combo_black_flash_synchronization", False)):
            unlocked_combos.append("black_flash_synchronization")
        
        # Check for tactical bond with Megumi
        if (game_state.get_relationship("megumi") >= 85 and 
            game_state.get_story_flag("strategic_shibuya_entry", False) and
            not game_state.get_story_flag("unlocked_combo_shadow_technique_fusion", False)):
            unlocked_combos.append("shadow_technique_fusion")
        
        # Check for fierce friendship with Nobara
        if (game_state.get_relationship("nobara") >= 90 and 
            "protected_ally" in recent_events and
            not game_state.get_story_flag("unlocked_combo_resonance_destruction", False)):
            unlocked_combos.append("resonance_destruction")
        
        # Check for Todo's brotherhood
        if (game_state.get_relationship("todo") >= 95 and 
            game_state.get_story_flag("todo_approves", False) and
            not game_state.get_story_flag("unlocked_combo_brotherhood_ultimate", False)):
            unlocked_combos.append("brotherhood_ultimate")
        
        # Check for first year unity
        yuji_rel = game_state.get_relationship("yuji")
        megumi_rel = game_state.get_relationship("megumi") 
        nobara_rel = game_state.get_relationship("nobara")
        
        if (yuji_rel >= 70 and megumi_rel >= 70 and nobara_rel >= 70 and
            not game_state.get_story_flag("unlocked_combo_first_year_trinity", False)):
            unlocked_combos.append("first_year_trinity")
        
        return unlocked_combos
    
    def create_custom_combo(self, player_name: str, ally_name: str, 
                          relationship_level: int) -> Optional[TeamCombo]:
        """Create a custom combo based on relationship level and traits."""
        if relationship_level < 50:
            return None
        
        # Determine combo strength based on relationship
        if relationship_level >= 90:
            multiplier = 2.5 + (relationship_level - 90) * 0.05
            effects = ["ultimate_bond", "shared_soul", "transcendent_power"]
        elif relationship_level >= 70:
            multiplier = 2.0 + (relationship_level - 70) * 0.025
            effects = ["strong_bond", "shared_will", "enhanced_power"]
        else:
            multiplier = 1.5 + (relationship_level - 50) * 0.025
            effects = ["friendship", "cooperation", "teamwork"]
        
        custom_combo = TeamCombo(
            f"{player_name} & {ally_name.title()} Unity Strike",
            ["player", ally_name],
            relationship_level - 10,  # Slightly lower requirement
            multiplier,
            f"""🤝 {player_name} and {ally_name.title()} fight as one, their bond 
transforming individual strength into something greater. This is the power 
that comes from true understanding and trust.""",
            effects
        )
        
        return custom_combo


def get_team_combo_manager() -> TeamComboManager:
    """Get the global team combo manager instance."""
    return TeamComboManager()