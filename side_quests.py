"""
Side Quest System

Manages character-specific side quests that deepen relationships and 
provide additional character development opportunities.
"""

from typing import Dict, List, Any, Optional
from enum import Enum
from character import Trait
import random


class QuestStatus(Enum):
    """Quest completion status."""
    NOT_STARTED = "not_started"
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"


class SideQuest:
    """Represents a side quest with objectives and rewards."""
    
    def __init__(self, quest_id: str, title: str, description: str, 
                 npc_giver: str, requirements: Dict[str, Any] = None,
                 objectives: List[str] = None, rewards: Dict[str, Any] = None):
        self.quest_id = quest_id
        self.title = title
        self.description = description
        self.npc_giver = npc_giver
        self.requirements = requirements or {}
        self.objectives = objectives or []
        self.completed_objectives = []
        self.rewards = rewards or {}
        self.status = QuestStatus.NOT_STARTED
    
    def can_start(self, game_state) -> bool:
        """Check if the quest can be started."""
        # Check relationship requirements
        if "min_relationship" in self.requirements:
            npc_relationship = game_state.get_relationship(self.npc_giver)
            if npc_relationship < self.requirements["min_relationship"]:
                return False
        
        # Check level requirements
        if "min_level" in self.requirements:
            if game_state.player.level < self.requirements["min_level"]:
                return False
        
        # Check story flags
        if "required_flags" in self.requirements:
            for flag in self.requirements["required_flags"]:
                if not game_state.get_story_flag(flag, False):
                    return False
        
        return True
    
    def complete_objective(self, objective_index: int):
        """Mark an objective as completed."""
        if objective_index < len(self.objectives):
            objective = self.objectives[objective_index]
            if objective not in self.completed_objectives:
                self.completed_objectives.append(objective)
        
        # Check if quest is fully completed
        if len(self.completed_objectives) >= len(self.objectives):
            self.status = QuestStatus.COMPLETED
    
    def get_progress(self) -> str:
        """Get quest progress description."""
        completed = len(self.completed_objectives)
        total = len(self.objectives)
        return f"{completed}/{total} objectives completed"


class SideQuestManager:
    """Manages all side quests and their progression."""
    
    def __init__(self):
        self.quests = {}
        self.active_quests = {}
        self._initialize_quests()
    
    def _initialize_quests(self):
        """Initialize all available side quests."""
        
        # Megumi's Shadow Training Quest
        self.quests["megumi_shadow_training"] = SideQuest(
            "megumi_shadow_training",
            "Mastering the Shadows",
            """Megumi has offered to teach you advanced shadow manipulation techniques. 
This intensive training will deepen your understanding of cursed energy and strengthen 
your bond with Megumi.""",
            "megumi",
            requirements={"min_relationship": 40, "min_level": 3},
            objectives=[
                "Complete basic shadow exercises with Megumi",
                "Successfully perform shadow binding technique",
                "Meditate in the shadow realm for 1 hour",
                "Demonstrate shadow clone coordination"
            ],
            rewards={
                "experience": 150,
                "relationship_bonus": {"megumi": 25},
                "learn_technique": "Shadow Mastery",
                "cursed_energy_bonus": 15
            }
        )
        
        # Yuji's Strength Training Quest
        self.quests["yuji_strength_training"] = SideQuest(
            "yuji_strength_training",
            "Building Unbreakable Bonds",
            """Yuji wants to train together to become stronger. His positive attitude 
and determination are infectious, and this training could unlock new potential.""",
            "yuji",
            requirements={"min_relationship": 30},
            objectives=[
                "Complete physical training routine with Yuji",
                "Spar with Yuji without using cursed techniques",
                "Help Yuji with his cursed energy control",
                "Share a meaningful conversation about your goals"
            ],
            rewards={
                "experience": 100,
                "relationship_bonus": {"yuji": 20},
                "trait_bonus": {Trait.DETERMINED: 15, Trait.COMPASSIONATE: 10},
                "hp_bonus": 25
            }
        )
        
        # Nobara's Fashion Quest
        self.quests["nobara_shopping"] = SideQuest(
            "nobara_shopping",
            "A Day in the City",
            """Nobara wants you to accompany her on a shopping trip to Tokyo. This could 
be a chance to see her more relaxed side and understand what drives her confidence.""",
            "nobara",
            requirements={"min_relationship": 25},
            objectives=[
                "Accompany Nobara to Shibuya shopping district",
                "Help her pick out a new outfit",
                "Listen to her talk about her hometown",
                "Stand up for her when others are dismissive"
            ],
            rewards={
                "experience": 75,
                "relationship_bonus": {"nobara": 30},
                "trait_bonus": {Trait.COMPASSIONATE: 10},
                "special_item": "Nobara's Lucky Charm"
            }
        )
        
        # Sukuna's Ancient Knowledge Quest
        self.quests["sukuna_knowledge"] = SideQuest(
            "sukuna_knowledge",
            "Forbidden Knowledge",
            """Sukuna has offered to share ancient jujutsu knowledge that predates modern 
sorcery. This knowledge could be incredibly powerful but may come with a price.""",
            "sukuna",
            requirements={"min_relationship": 50, "required_flags": ["met_sukuna"]},
            objectives=[
                "Listen to Sukuna's teachings about ancient jujutsu",
                "Prove your worth through a trial of strength",
                "Demonstrate understanding of ancient cursed energy theory",
                "Choose between power and morality"
            ],
            rewards={
                "experience": 200,
                "relationship_bonus": {"sukuna": 20},
                "learn_technique": "Ancient Cursed Art",
                "cursed_energy_bonus": 30,
                "trait_bonus": {Trait.FOCUSED: 20}
            }
        )
        
        # Gojo's Special Training Quest
        self.quests["gojo_limitless_training"] = SideQuest(
            "gojo_limitless_training",
            "Beyond Limits",
            """Gojo-sensei has noticed your exceptional potential and wants to provide 
you with special training that goes beyond normal curriculum.""",
            "gojo",
            requirements={"min_relationship": 60, "min_level": 5},
            objectives=[
                "Master advanced cursed energy manipulation",
                "Successfully perform a Black Flash",
                "Understand the theory behind Limitless technique",
                "Demonstrate your unique technique mastery"
            ],
            rewards={
                "experience": 300,
                "relationship_bonus": {"gojo": 25},
                "learn_technique": "Advanced Energy Control",
                "cursed_energy_bonus": 40,
                "special_grade_potential": True
            }
        )
        
        # Todo's Brotherhood Quest
        self.quests["todo_brotherhood"] = SideQuest(
            "todo_brotherhood",
            "My Brother's Path",
            """Todo has declared you his brother and wants to undergo the ultimate 
brotherhood trial together. This intense experience will test your bonds.""",
            "todo",
            requirements={"min_relationship": 70, "required_flags": ["todo_approves"]},
            objectives=[
                "Complete Todo's grueling training regimen",
                "Demonstrate your 'type' philosophy understanding",
                "Fight alongside Todo against a powerful curse",
                "Achieve perfect Boogie Woogie coordination"
            ],
            rewards={
                "experience": 250,
                "relationship_bonus": {"todo": 30},
                "learn_technique": "Brotherhood Strike",
                "trait_bonus": {Trait.AGGRESSIVE: 20, Trait.DETERMINED: 15}
            }
        )
    
    def get_available_quests(self, game_state) -> List[SideQuest]:
        """Get all quests that can be started."""
        available = []
        for quest in self.quests.values():
            if (quest.status == QuestStatus.NOT_STARTED and 
                quest.can_start(game_state) and 
                quest.quest_id not in self.active_quests):
                available.append(quest)
        return available
    
    def start_quest(self, quest_id: str, game_state) -> bool:
        """Start a quest if possible."""
        if quest_id in self.quests:
            quest = self.quests[quest_id]
            if quest.can_start(game_state):
                quest.status = QuestStatus.ACTIVE
                self.active_quests[quest_id] = quest
                game_state.add_story_flag(f"quest_{quest_id}_started", True)
                return True
        return False
    
    def progress_quest(self, quest_id: str, objective_index: int, game_state) -> Dict[str, Any]:
        """Progress a quest objective."""
        if quest_id in self.active_quests:
            quest = self.active_quests[quest_id]
            quest.complete_objective(objective_index)
            
            result = {"quest_progressed": True, "quest": quest}
            
            # If quest is completed, apply rewards
            if quest.status == QuestStatus.COMPLETED:
                result.update(self._apply_quest_rewards(quest, game_state))
                del self.active_quests[quest_id]
                game_state.add_story_flag(f"quest_{quest_id}_completed", True)
            
            return result
        
        return {"quest_progressed": False}
    
    def _apply_quest_rewards(self, quest: SideQuest, game_state) -> Dict[str, Any]:
        """Apply quest completion rewards."""
        rewards_applied = {"rewards": []}
        
        # Experience rewards
        if "experience" in quest.rewards:
            exp = quest.rewards["experience"]
            game_state.player.gain_experience(exp)
            rewards_applied["rewards"].append(f"Gained {exp} experience")
        
        # Relationship bonuses
        if "relationship_bonus" in quest.rewards:
            for npc, bonus in quest.rewards["relationship_bonus"].items():
                game_state.update_relationship(npc, bonus)
                rewards_applied["rewards"].append(f"Relationship with {npc.title()} +{bonus}")
        
        # Trait bonuses
        if "trait_bonus" in quest.rewards:
            for trait, bonus in quest.rewards["trait_bonus"].items():
                game_state.player.modify_trait(trait, bonus)
                rewards_applied["rewards"].append(f"{trait.value} +{bonus}")
        
        # Technique learning
        if "learn_technique" in quest.rewards:
            technique = quest.rewards["learn_technique"]
            context = f"Learned through completing '{quest.title}'"
            game_state.player.learn_story_technique(technique, context)
            rewards_applied["rewards"].append(f"Learned technique: {technique}")
        
        # Cursed energy bonus
        if "cursed_energy_bonus" in quest.rewards:
            bonus = quest.rewards["cursed_energy_bonus"]
            game_state.player.max_cursed_energy += bonus
            game_state.player.cursed_energy = game_state.player.max_cursed_energy
            rewards_applied["rewards"].append(f"Max Cursed Energy +{bonus}")
        
        # HP bonus
        if "hp_bonus" in quest.rewards:
            bonus = quest.rewards["hp_bonus"]
            game_state.player.max_hp += bonus
            game_state.player.hp = game_state.player.max_hp
            rewards_applied["rewards"].append(f"Max HP +{bonus}")
        
        return rewards_applied
    
    def get_active_quests(self) -> List[SideQuest]:
        """Get all currently active quests."""
        return list(self.active_quests.values())
    
    def get_quest_by_npc(self, npc_name: str, game_state) -> Optional[SideQuest]:
        """Get an available quest from a specific NPC."""
        available_quests = self.get_available_quests(game_state)
        for quest in available_quests:
            if quest.npc_giver == npc_name:
                return quest
        return None