"""
Story and Exploration System

Manages story progression, character choices, exploration, and narrative branching
following the Jujutsu Kaisen manga with player-driven deviations.

Now supports dynamic loading of expanded story arcs for richer storytelling.
"""

from typing import Dict, List, Any, Optional
import random
import importlib
from character import Player, Enemy, Trait


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
    """Manages the overall story progression and exploration."""
    
    def __init__(self):
        self.current_scene = "intro"
        self.current_arc = 1
        self.story_scenes = {}
        self.exploration_locations = {}
        self.loaded_arcs = {}
        self._load_story_arcs()
        self._initialize_locations()
    
    def _load_story_arcs(self):
        """Load all available story arc modules."""
        arc_modules = {
            1: "story1",  # Introduction Arc
            2: "story2",  # Vs. Mahito/Junpei Arc  
            3: "story3",  # Kyoto Exchange Event Arc
        }
        
        for arc_num, module_name in arc_modules.items():
            try:
                # Import the arc module
                arc_module = importlib.import_module(module_name)
                
                # Get the scenes from the arc
                if hasattr(arc_module, f'get_arc{arc_num}_scenes'):
                    arc_scenes = getattr(arc_module, f'get_arc{arc_num}_scenes')()
                    self.loaded_arcs[arc_num] = arc_scenes
                    
                    # Add scenes to main story scenes dict with arc prefix
                    for scene_key, scene in arc_scenes.items():
                        prefixed_key = f"arc{arc_num}_{scene_key}" if not scene_key.startswith("arc") else scene_key
                        self.story_scenes[prefixed_key] = scene
                        
                    print(f"✅ Loaded Arc {arc_num}: {len(arc_scenes)} scenes")
                else:
                    print(f"⚠️  Arc {arc_num} module missing get_arc{arc_num}_scenes function")
                    
            except ImportError as e:
                print(f"⚠️  Could not load Arc {arc_num} ({module_name}): {e}")
                # Fall back to basic story for missing arcs
                if arc_num == 1:
                    self._initialize_basic_story()
        
        # If no arcs loaded successfully, ensure we have basic content
        if not self.story_scenes:
            print("🔄 No story arcs loaded, falling back to basic story")
            self._initialize_basic_story()
    
    def _initialize_basic_story(self):
        """Initialize basic story scenes as fallback."""
        
        # Introduction Scene
        intro_choices = [
            StoryChoice(
                "Help the injured student immediately",
                {
                    "traits": {Trait.COMPASSIONATE: 10, Trait.PROTECTIVE: 5},
                    "next_scene": "first_mission_compassionate",
                    "relationships": {"yuji": 10},
                    "story_flags": {"helped_student": True}
                }
            ),
            StoryChoice(
                "Assess the situation carefully first",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.CAUTIOUS: 5},
                    "next_scene": "first_mission_analytical",
                    "relationships": {"megumi": 10},
                    "story_flags": {"assessed_situation": True}
                }
            ),
            StoryChoice(
                "Charge in to fight the curse immediately",
                {
                    "traits": {Trait.AGGRESSIVE: 10, Trait.RECKLESS: 5},
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
        
        # Compassionate Path
        self.story_scenes["first_mission_compassionate"] = StoryScene(
            "The Rescuer's Path",
            """You rush to help the injured student without hesitation. Your quick action 
surprises the cursed spirit, giving you the advantage. As you engage the curse, 
Yuji Itadori appears, impressed by your immediate response to help others.

"That was brave!" Yuji says with a grin. "You remind me of myself when I first got here."

The curse spirit snarls and prepares to attack both of you.""",
            [
                StoryChoice(
                    "Fight alongside Yuji",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse",
                        "ally": "yuji",
                        "traits": {Trait.DETERMINED: 5},
                        "next_scene": "post_first_battle"
                    }
                ),
                StoryChoice(
                    "Protect the injured student while Yuji fights",
                    {
                        "traits": {Trait.PROTECTIVE: 10},
                        "relationships": {"yuji": 5, "injured_student": 15},
                        "next_scene": "protective_outcome"
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # Analytical Path
        self.story_scenes["first_mission_analytical"] = StoryScene(
            "The Strategist's Path",
            """You carefully observe the cursed spirit, noting its movement patterns and energy 
signature. Your analytical approach catches the attention of Megumi Fushiguro, who nods 
approvingly from nearby.

"Smart. Understanding your enemy before acting is crucial," Megumi says quietly. 
"That curse has a weakness on its left side."

Your careful observation reveals the optimal strategy for defeating this spirit.""",
            [
                StoryChoice(
                    "Use Megumi's advice to exploit the weakness",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse_weakened",
                        "traits": {Trait.FOCUSED: 10},
                        "relationships": {"megumi": 10},
                        "next_scene": "strategic_victory"
                    }
                ),
                StoryChoice(
                    "Share your own analysis with Megumi",
                    {
                        "traits": {Trait.ANALYTICAL: 5, Trait.FOCUSED: 5},
                        "relationships": {"megumi": 15},
                        "story_flags": {"impressed_megumi": True},
                        "next_scene": "analytical_bond"
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # Aggressive Path
        self.story_scenes["first_mission_aggressive"] = StoryScene(
            "The Warrior's Path",
            """You charge directly at the cursed spirit with fierce determination. Your bold 
approach catches everyone off guard, including Nobara Kugisaki who was approaching 
from the other side.

"Finally, someone who doesn't overthink everything!" Nobara grins, readying her hammer 
and nails. "Let's crush this thing!"

The curse spirit, startled by your aggressive approach, becomes more dangerous but 
also more reckless.""",
            [
                StoryChoice(
                    "Coordinate with Nobara for a combined assault",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse_enraged",
                        "ally": "nobara",
                        "traits": {Trait.AGGRESSIVE: 5},
                        "relationships": {"nobara": 15},
                        "next_scene": "aggressive_victory"
                    }
                ),
                StoryChoice(
                    "Go all-out on your own",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse_enraged",
                        "traits": {Trait.RECKLESS: 10, Trait.DETERMINED: 5},
                        "next_scene": "solo_battle"
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # Meeting Todo Scene
        self.story_scenes["meet_todo"] = StoryScene(
            "Encounter with Todo",
            """During a joint training exercise with Kyoto School, you encounter the imposing 
figure of Aoi Todo. His massive frame and confident stance make it clear he's evaluating 
you as a potential sparring partner.

"What's your type of woman?" Todo asks with complete seriousness.

The question catches you off guard, but you realize this might be Todo's way of 
understanding your character.""",
            [
                StoryChoice(
                    "Give a thoughtful, honest answer",
                    {
                        "traits": {Trait.COMPASSIONATE: 5},
                        "relationships": {"todo": 20},
                        "story_flags": {"todo_approves": True},
                        "next_scene": "todo_training"
                    }
                ),
                StoryChoice(
                    "Deflect with humor",
                    {
                        "traits": {Trait.FOCUSED: 5},
                        "relationships": {"todo": 5},
                        "next_scene": "todo_neutral"
                    }
                ),
                StoryChoice(
                    "Challenge him to a fight instead",
                    {
                        "traits": {Trait.AGGRESSIVE: 10},
                        "combat": True,
                        "enemy": "todo_sparring",
                        "next_scene": "todo_fight"
                    }
                )
            ],
            "Kyoto Jujutsu High - Training Grounds"
        )
        
        # Shibuya Incident preparation
        self.story_scenes["shibuya_preparation"] = StoryScene(
            "Before the Shibuya Incident",
            """Halloween night approaches, and intelligence suggests a major cursed spirit 
incident will occur in Shibuya. You've grown stronger, but this will be your biggest 
challenge yet. The atmosphere is tense as everyone prepares.

Gojo-sensei is nowhere to be found, and there's a sense of unease among the students 
and faculty.""",
            [
                StoryChoice(
                    "Volunteer for the front-line assault team",
                    {
                        "traits": {Trait.DETERMINED: 10, Trait.PROTECTIVE: 5},
                        "story_flags": {"frontline_volunteer": True},
                        "next_scene": "shibuya_frontline"
                    }
                ),
                StoryChoice(
                    "Request to support rescue operations",
                    {
                        "traits": {Trait.COMPASSIONATE: 10, Trait.ANALYTICAL: 5},
                        "story_flags": {"rescue_volunteer": True},
                        "next_scene": "shibuya_rescue"
                    }
                ),
                StoryChoice(
                    "Suggest gathering more intelligence first",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.ANALYTICAL: 5},
                        "story_flags": {"intelligence_focused": True},
                        "next_scene": "shibuya_intel"
                    }
                )
            ],
            "Tokyo Jujutsu High - Meeting Room"
        )
    
    def advance_to_arc(self, arc_number: int, starting_scene: str = None):
        """Advance to a specific story arc."""
        if arc_number in self.loaded_arcs:
            self.current_arc = arc_number
            if starting_scene:
                self.current_scene = starting_scene
            else:
                # Default to arc intro scene
                self.current_scene = f"arc{arc_number}_intro"
            return True
        return False
    
    def get_current_arc_info(self) -> Dict[str, Any]:
        """Get information about the current arc."""
        arc_info = {
            1: {"name": "Introduction Arc", "description": "Arrival at Tokyo Jujutsu High"},
            2: {"name": "Vs. Mahito/Junpei Arc", "description": "The Nature of Humanity"},
            3: {"name": "Kyoto Exchange Event Arc", "description": "Rivalry and Growth"}
        }
        return arc_info.get(self.current_arc, {"name": "Unknown Arc", "description": "Continuing the story..."})
    
    def get_available_arcs(self) -> List[Dict[str, Any]]:
        """Get list of available story arcs."""
        available = []
        arc_names = {
            1: {"name": "Introduction Arc", "description": "Arrival at Tokyo Jujutsu High"},
            2: {"name": "Vs. Mahito/Junpei Arc", "description": "The Nature of Humanity"}, 
            3: {"name": "Kyoto Exchange Event Arc", "description": "Rivalry and Growth"}
        }
        
        for arc_num in self.loaded_arcs.keys():
            arc_info = arc_names.get(arc_num, {"name": f"Arc {arc_num}", "description": "Story content"})
            available.append({
                "arc": arc_num,
                "name": arc_info["name"],
                "description": arc_info["description"],
                "current": arc_num == self.current_arc
            })
        return sorted(available, key=lambda x: x["arc"])
    
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
            next_scene = consequences["next_scene"]
            
            # Check if this is an arc transition
            if "next_arc" in consequences:
                next_arc = consequences["next_arc"]
                if self.advance_to_arc(next_arc, next_scene):
                    print(f"🌟 Advancing to {self.get_current_arc_info()['name']}!")
                else:
                    print(f"⚠️  Could not advance to Arc {next_arc}")
            else:
                self.current_scene = next_scene
            
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