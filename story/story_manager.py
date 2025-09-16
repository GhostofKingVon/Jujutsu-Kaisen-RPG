"""
Story Manager for Modular Story System

Manages the overall story progression and exploration by dynamically loading
story content from separate modules for each arc.
"""

from typing import Dict, List, Any, Optional
import random
from character import Player, Enemy, Trait

# Import story arc modules
from . import story1, story2, story3, story4
from .base import StoryChoice, StoryScene


class StoryManager:
    """Manages the overall story progression and exploration."""
    
    def __init__(self):
        self.current_scene = "intro"
        self.story_scenes = {}
        self.exploration_locations = {}
        self._initialize_story()
        self._initialize_locations()
    
    def _initialize_story(self):
        """
        Initialize all story scenes by loading from modular story files.
        
        This method dynamically loads story content from separate arc modules,
        making it easy to add new story arcs or modify existing ones.
        """
        # Load scenes from each story arc module
        self.story_scenes.update(story1.get_story1_scenes())
        self.story_scenes.update(story2.get_story2_scenes())
        self.story_scenes.update(story3.get_story3_scenes())
        self.story_scenes.update(story4.get_story4_scenes())
    
    def _initialize_locations(self):
        """Initialize exploration locations."""
        
        self.exploration_locations = {
            "tokyo_jujutsu_high": {
                "name": "Tokyo Jujutsu High",
                "description": "The main campus where you train and study.",
                "areas": {
                    "courtyard": "The main courtyard with cherry blossom trees.",
                    "training_grounds": "Where students practice combat techniques.",
                    "library": "Contains ancient texts about cursed spirits and techniques.",
                    "dormitories": "Student living quarters.",
                    "teacher_offices": "Faculty offices and meeting rooms."
                },
                "npcs": ["gojo", "nanami", "yuji", "megumi", "nobara"],
                "secrets": ["hidden_technique_scroll", "old_mission_records"]
            },
            
            "shibuya": {
                "name": "Shibuya District",
                "description": "A busy district now overrun with cursed spirits.",
                "areas": {
                    "shibuya_crossing": "The famous intersection, now a battleground.",
                    "shopping_district": "Abandoned shops and cursed spirit nests.",
                    "subway_station": "Underground tunnels with dangerous curses.",
                    "high_rise_buildings": "Tall buildings offering strategic advantages."
                },
                "npcs": ["injured_civilians", "cursed_spirit_users"],
                "secrets": ["hidden_passage", "powerful_curse_tools"]
            },
            
            "kyoto_school": {
                "name": "Kyoto Jujutsu High",
                "description": "The traditional rival school with different philosophies.",
                "areas": {
                    "main_hall": "Traditional Japanese architecture and ceremonies.",
                    "zen_garden": "Peaceful area for meditation and reflection.",
                    "sparring_dojo": "Where Kyoto students train rigorously.",
                    "artifact_vault": "Ancient cursed tools and relics."
                },
                "npcs": ["todo", "mai", "momo", "noritoshi"],
                "secrets": ["ancient_technique_manual", "forbidden_cursed_tool"]
            }
        }
    
    def start_story(self, game_state):
        """Start the story for a new game."""
        game_state.set_location("Tokyo Jujutsu High - Courtyard")
        game_state.advance_chapter(1)
        self.current_scene = "intro"
    
    def load_story_state(self, game_state):
        """Load story state from saved game."""
        # Determine current scene based on game state
        chapter = game_state.current_chapter
        
        if chapter <= 2:
            self.current_scene = "intro"
        elif chapter <= 5:
            self.current_scene = "meet_todo"
        elif chapter <= 10:
            self.current_scene = "shibuya_preparation"
        else:
            self.current_scene = "post_shibuya"
    
    def display_current_scene(self, game_state):
        """Display the current story scene."""
        if self.current_scene not in self.story_scenes:
            print("You explore the area, looking for new adventures...")
            return
        
        scene = self.story_scenes[self.current_scene]
        print(f"\n📖 {scene.title}")
        print("=" * 50)
        print(scene.description)
        
        # Show relevant character status
        if game_state.player:
            dominant_traits = game_state.player.get_dominant_traits()
            if dominant_traits:
                trait_names = [trait.value for trait in dominant_traits]
                print(f"\n🌟 Your dominant traits: {', '.join(trait_names)}")
    
    def get_available_actions(self, game_state) -> List[Dict[str, Any]]:
        """Get available actions for the current scene."""
        if self.current_scene not in self.story_scenes:
            # Default exploration actions
            return [
                {"text": "Explore the area", "type": "explore"},
                {"text": "Talk to NPCs", "type": "social"},
                {"text": "Train your abilities", "type": "training"}
            ]
        
        scene = self.story_scenes[self.current_scene]
        actions = []
        
        for choice in scene.choices:
            # Check if choice is available based on requirements
            if self._check_requirements(choice.consequences, game_state):
                actions.append({"text": choice.text, "choice": choice})
        
        return actions
    
    def _check_requirements(self, consequences: Dict[str, Any], game_state) -> bool:
        """Check if requirements are met for a choice."""
        requirements = consequences.get("requirements", {})
        
        # Check level requirements
        if "min_level" in requirements:
            if game_state.player.level < requirements["min_level"]:
                return False
        
        # Check trait requirements
        if "required_traits" in requirements:
            player_traits = game_state.player.get_dominant_traits()
            for required_trait in requirements["required_traits"]:
                if required_trait not in player_traits:
                    return False
        
        # Check story flag requirements
        if "required_flags" in requirements:
            for flag in requirements["required_flags"]:
                if not game_state.get_story_flag(flag, False):
                    return False
        
        return True
    
    def process_action(self, choice_index: int, game_state) -> Dict[str, Any]:
        """Process the player's choice and return the result."""
        actions = self.get_available_actions(game_state)
        
        if choice_index >= len(actions):
            return {"error": "Invalid choice"}
        
        action = actions[choice_index]
        
        if action.get("type") == "explore":
            return self._handle_exploration(game_state)
        elif action.get("type") == "social":
            return self._handle_social_interaction(game_state)
        elif action.get("type") == "training":
            return self._handle_training(game_state)
        
        # Handle story choice
        choice = action["choice"]
        return self._process_story_choice(choice, game_state)
    
    def _process_story_choice(self, choice: StoryChoice, game_state) -> Dict[str, Any]:
        """Process a story choice and apply its consequences."""
        consequences = choice.consequences
        result = {}
        
        # Apply trait changes
        if "traits" in consequences:
            for trait, change in consequences["traits"].items():
                game_state.player.modify_trait(trait, change)
                print(f"🌟 {trait.value} increased by {change}!")
        
        # Apply relationship changes
        if "relationships" in consequences:
            for npc, change in consequences["relationships"].items():
                game_state.update_relationship(npc, change)
                print(f"💭 Relationship with {npc.title()} changed by {change}")
        
        # Set story flags
        if "story_flags" in consequences:
            for flag, value in consequences["story_flags"].items():
                game_state.add_story_flag(flag, value)
        
        # Handle combat
        if consequences.get("combat"):
            enemy = self._create_enemy(consequences["enemy"], game_state.player.level)
            result["combat"] = True
            result["enemy"] = enemy
        
        # Advance to next scene
        if "next_scene" in consequences:
            self.current_scene = consequences["next_scene"]
            game_state.advance_chapter()
        
        # Grant experience
        if "experience" in consequences:
            game_state.player.gain_experience(consequences["experience"])
        
        return result
    
    def _create_enemy(self, enemy_type: str, player_level: int) -> Enemy:
        """Create an enemy based on type and player level."""
        if enemy_type == "grade_3_curse":
            enemy = Enemy("Grade 3 Cursed Spirit", 80, 40)
            enemy.ai_pattern = "aggressive"
        
        elif enemy_type == "grade_3_curse_weakened":
            enemy = Enemy("Weakened Grade 3 Cursed Spirit", 60, 30)
            enemy.ai_pattern = "defensive"
        
        elif enemy_type == "grade_3_curse_enraged":
            enemy = Enemy("Enraged Grade 3 Cursed Spirit", 100, 50)
            enemy.ai_pattern = "aggressive"
        
        elif enemy_type == "todo_sparring":
            enemy = Enemy("Aoi Todo (Sparring)", 150, 80, "hard")
            enemy.ai_pattern = "mixed"
            enemy.max_phases = 2
            enemy.phase_transition_messages = [
                "Todo grins widely and gets serious!",
                "\"My brother! Show me your true strength!\""
            ]
        
        else:
            # Default enemy
            enemy = Enemy("Unknown Cursed Spirit", 70, 35)
        
        # Scale enemy to player level
        level_modifier = max(1, player_level - 1)
        enemy.max_hp += level_modifier * 10
        enemy.hp = enemy.max_hp
        enemy.max_cursed_energy += level_modifier * 5
        enemy.cursed_energy = enemy.max_cursed_energy
        enemy.level = max(1, player_level - 1)
        
        return enemy
    
    def _handle_exploration(self, game_state) -> Dict[str, Any]:
        """Handle exploration actions."""
        print("You explore the area and discover...")
        
        # Random exploration outcomes
        outcomes = [
            "A hidden cursed tool",
            "An old scroll with technique hints", 
            "A peaceful meditation spot",
            "Traces of cursed energy",
            "Nothing of interest"
        ]
        
        outcome = random.choice(outcomes)
        print(f"✨ {outcome}!")
        
        if "cursed tool" in outcome:
            game_state.add_to_inventory("Cursed Tool Fragment")
        elif "scroll" in outcome:
            game_state.player.gain_experience(25)
        elif "meditation" in outcome:
            restored = game_state.player.restore_cursed_energy(20)
            if restored > 0:
                print(f"Restored {restored} cursed energy from meditation.")
        
        return {}
    
    def _handle_social_interaction(self, game_state) -> Dict[str, Any]:
        """Handle social interactions with NPCs."""
        location = game_state.current_location.lower()
        
        if "tokyo" in location:
            npcs = ["Yuji", "Megumi", "Nobara", "Gojo-sensei"]
        elif "kyoto" in location:
            npcs = ["Todo", "Mai", "Noritoshi"]
        else:
            npcs = ["Local Student", "Faculty Member"]
        
        npc = random.choice(npcs)
        print(f"💬 You have a conversation with {npc}.")
        
        # Random relationship changes
        change = random.randint(1, 5)
        game_state.update_relationship(npc.lower(), change)
        print(f"Your relationship with {npc} improved by {change}!")
        
        return {}
    
    def _handle_training(self, game_state) -> Dict[str, Any]:
        """Handle training actions."""
        print("🥋 You spend time training your abilities...")
        
        # Grant experience and small stat improvements
        exp_gain = random.randint(15, 30)
        game_state.player.gain_experience(exp_gain)
        print(f"Gained {exp_gain} experience from training!")
        
        # Small chance to learn new technique
        if random.random() < 0.1 and game_state.player.level >= 5:
            print("🌟 Your training pays off! You feel ready to learn a new technique!")
            # This would trigger technique learning in a full implementation
        
        return {}