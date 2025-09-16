"""
Enhanced Story and Exploration System

Manages story progression, character choices, exploration, and narrative branching
following the Jujutsu Kaisen manga with player-driven deviations.
"""

from typing import Dict, List, Any, Optional
import random
from character import Player, Enemy, Trait
from manga_story import MangaStoryManager, StoryArc
from enhanced_npcs import EnhancedNPCManager


class StoryChoice:
    """Represents a story choice with its consequences."""
    
    def __init__(self, text: str, consequences: Dict[str, Any]):
        self.text = text
        self.consequences = consequences  # Effects on traits, relationships, story flags


class StoryScene:
    """Represents a story scene with description and choices."""
    
    def __init__(self, title: str, description: str, choices: List[StoryChoice], 
                 location: str = None, requirements: Dict = None):
        self.title = title
        self.description = description
        self.choices = choices
        self.location = location or "Unknown Location"
        self.requirements = requirements or {}  # Requirements to access this scene


class StoryManager:
    """Enhanced story manager combining original and manga-accurate content."""
    
    def __init__(self):
        self.current_scene = "intro"
        self.story_scenes = {}
        self.exploration_locations = {}
        self.manga_story = MangaStoryManager()
        self.npc_manager = EnhancedNPCManager()
        self._initialize_story()
        self._initialize_locations()
    
    def start_story(self, game_state):
        """Start the story with enhanced manga alignment."""
        game_state.current_chapter = 1
        game_state.current_location = "Tokyo Jujutsu High - Main Gate"
        game_state.add_story_flag("story_started", True)
        
        print("🎌 Your journey as a Jujutsu Sorcerer begins...")
        print("The world of curses awaits...")
    
    def load_story_state(self, game_state):
        """Load story state from saved game."""
        # Restore any story-specific state if needed
        pass
    
    def display_current_scene(self, game_state):
        """Display the current scene using manga story system."""
        # Get scene from manga story manager
        manga_scene = self.manga_story.get_current_scene(game_state)
        
        if manga_scene:
            print(f"\n📖 {manga_scene['title']}")
            print("=" * 50)
            print(manga_scene['description'])
        else:
            # Fallback to original story system
            scene = self.story_scenes.get(self.current_scene)
            if scene:
                print(f"\n📖 {scene.title}")
                print("=" * 50)
                print(scene.description)
    
    def get_available_actions(self, game_state) -> List[Dict[str, Any]]:
        """Get available actions for current scene."""
        # Try to get manga scene actions first
        manga_scene = self.manga_story.get_current_scene(game_state)
        
        if manga_scene and 'choices' in manga_scene:
            return [{"text": choice["text"], "consequences": choice["consequences"]} 
                   for choice in manga_scene['choices']]
        
        # Fallback to original story actions
        scene = self.story_scenes.get(self.current_scene)
        if scene:
            return [{"text": choice.text, "consequences": choice.consequences} 
                   for choice in scene.choices]
        
        # Default exploration actions
        return [
            {"text": "Continue exploring", "consequences": {"experience": 25}},
            {"text": "Train your techniques", "consequences": {"traits": {"focused": 5}}},
            {"text": "Interact with NPCs", "consequences": {"npc_interaction": True}}
        ]
    
    def process_action(self, choice_index: int, game_state) -> Dict[str, Any]:
        """Process the selected action."""
        actions = self.get_available_actions(game_state)
        
        if choice_index >= len(actions):
            return {"error": "Invalid choice"}
        
        chosen_action = actions[choice_index]
        consequences = chosen_action["consequences"]
        
        # Use manga story manager to process consequences
        result = self.manga_story.process_choice_consequences(consequences, game_state)
        
        # Handle special consequence types
        if "npc_interaction" in consequences:
            result.update(self._handle_npc_interaction(game_state))
        
        if "combat" in consequences:
            result["combat"] = True
            result["enemy"] = self._create_enemy_from_type(consequences.get("enemy_type", "generic_curse"))
        
        if "next_scene" in consequences:
            self.current_scene = consequences["next_scene"]
        
        # Check for chapter progression
        if game_state.current_chapter < 20:  # Progress story
            if random.random() < 0.3:  # 30% chance to advance chapter
                game_state.current_chapter += 1
                result["effects"].append(f"Advanced to Chapter {game_state.current_chapter}")
        
        return result
    
    def _handle_npc_interaction(self, game_state) -> Dict[str, Any]:
        """Handle NPC interaction sequences."""
        available_npcs = ["yuji", "megumi", "nobara", "gojo"]
        
        if game_state.current_chapter >= 5:
            available_npcs.extend(["todo", "maki"])
        
        if game_state.current_chapter >= 10:
            available_npcs.append("sukuna")
        
        # Select random NPC for interaction
        npc_name = random.choice(available_npcs)
        
        # Determine interaction context
        context = "casual"
        if game_state.current_chapter >= 10:
            context = random.choice(["casual", "training", "personal"])
        
        # Process interaction
        interaction_result = self.npc_manager.interact_with_npc(npc_name, game_state.player, context)
        
        return {
            "npc_interaction": True,
            "npc_name": npc_name,
            "dialogue": interaction_result.get("dialogue", "..."),
            "relationship_change": interaction_result.get("relationship_change", 0),
            "new_abilities": interaction_result.get("new_abilities", [])
        }
    
    def _create_enemy_from_type(self, enemy_type: str) -> Enemy:
        """Create an enemy based on type."""
        enemy_configs = {
            "generic_curse": {
                "name": "Cursed Spirit",
                "hp": 80,
                "ce": 40,
                "difficulty": "normal"
            },
            "detention_center_curse": {
                "name": "Detention Center Curse",
                "hp": 120,
                "ce": 60,
                "difficulty": "hard"
            },
            "special_grade": {
                "name": "Special Grade Curse",
                "hp": 200,
                "ce": 100,
                "difficulty": "extreme"
            },
            "curse_user": {
                "name": "Curse User",
                "hp": 100,
                "ce": 80,
                "difficulty": "hard"
            }
        }
        
        config = enemy_configs.get(enemy_type, enemy_configs["generic_curse"])
        enemy = Enemy(config["name"], config["hp"], config["ce"], config["difficulty"])
        
        # Add appropriate techniques based on enemy type
        if enemy_type == "special_grade":
            enemy.max_phases = 3
            enemy.phase_transition_messages = [
                "The curse's true form begins to emerge!",
                "Overwhelming cursed energy floods the area!",
                "This is the curse's final, desperate form!"
            ]
        
        return enemy
    
    def _initialize_story(self):
        """Initialize backup story scenes for fallback."""
        # Keep original scenes as fallback when manga scenes aren't available
        intro_choices = [
            StoryChoice(
                "Help the injured student immediately",
                {
                    "traits": {"compassionate": 10, "protective": 5},
                    "next_scene": "first_mission_compassionate", 
                    "relationships": {"yuji": 10},
                    "story_flags": {"helped_student": True}
                }
            ),
            StoryChoice(
                "Assess the situation carefully first",
                {
                    "traits": {"analytical": 10, "cautious": 5},
                    "next_scene": "first_mission_analytical",
                    "relationships": {"megumi": 10},
                    "story_flags": {"assessed_situation": True}
                }
            ),
            StoryChoice(
                "Charge in to fight the curse immediately",
                {
                    "traits": {"aggressive": 10, "reckless": 5},
                    "next_scene": "first_mission_aggressive",
                    "relationships": {"nobara": 10},
                    "story_flags": {"fought_immediately": True}
                }
            )
        ]
        
        self.story_scenes["intro"] = StoryScene(
            "Arrival at Tokyo Jujutsu High",
            """You arrive at Tokyo Jujutsu High as a new first-year student. The imposing 
traditional buildings are surrounded by powerful barriers, and you can feel the cursed 
energy in the air. As you walk through the courtyard, you notice a commotion ahead.

A fellow student has been cornered by a Grade 3 cursed spirit near the training grounds. 
The curse spirit writhes with malevolent energy, and the student looks terrified and injured.

What do you do?""",
            intro_choices,
            "Tokyo Jujutsu High - Courtyard"
        )
    
    def _initialize_locations(self):
        """Initialize exploration locations."""
        self.exploration_locations = {
            "tokyo_jujutsu_high": {
                "name": "Tokyo Jujutsu High",
                "description": "The premier institution for training jujutsu sorcerers in Japan.",
                "available_actions": [
                    "Visit the training grounds",
                    "Explore the library", 
                    "Check the dormitories",
                    "Meet with Gojo-sensei"
                ],
                "encounters": ["training_dummy", "library_ghost", "senior_student"]
            },
            "shibuya_district": {
                "name": "Shibuya District", 
                "description": "A bustling commercial district that often attracts cursed spirits.",
                "available_actions": [
                    "Patrol for curses",
                    "Visit Shibuya Crossing",
                    "Investigate reports",
                    "Help civilians"
                ],
                "encounters": ["grade_3_curse", "curse_user", "trapped_civilian"]
            },
            "kyoto_jujutsu_high": {
                "name": "Kyoto Jujutsu High",
                "description": "The sister school known for its traditional approach to jujutsu.",
                "available_actions": [
                    "Meet Kyoto students",
                    "Observe training methods", 
                    "Challenge students",
                    "Learn techniques"
                ],
                "encounters": ["todo", "mai_zenin", "noritoshi_kamo"]
            }
        }