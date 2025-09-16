"""
Story and Exploration System

Manages story progression, character choices, exploration, and narrative branching
following the Jujutsu Kaisen manga with player-driven deviations.
"""

from typing import Dict, List, Any, Optional
import random
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
        self.story_scenes = {}
        self.exploration_locations = {}
        self.downtime_activities = {}
        self.in_downtime = False
        self._initialize_story()
        self._initialize_locations()
        self._initialize_downtime_activities()
    
    def _initialize_story(self):
        """Initialize all story scenes."""
        
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
    
    def _initialize_downtime_activities(self):
        """Initialize downtime activities for between-mission periods."""
        self.downtime_activities = {
            "training": {
                "name": "Train Your Abilities",
                "description": "Focus on improving your cursed techniques and physical conditioning.",
                "effects": {
                    "experience": lambda level: 20 + (level * 2),
                    "cursed_energy": lambda player: min(10, player.max_cursed_energy - player.cursed_energy),
                    "trait_bonus": "focused"
                },
                "flavor_text": [
                    "You spend hours perfecting your cursed energy control.",
                    "Your technique precision improves through dedicated practice.",
                    "The training grounds echo with your determined efforts."
                ]
            },
            
            "socialize": {
                "name": "Spend Time with Classmates",
                "description": "Build relationships and learn from your fellow sorcerers.",
                "effects": {
                    "relationships": {"yuji": 5, "megumi": 5, "nobara": 5},
                    "trait_bonus": "compassionate",
                    "technique_hint": True
                },
                "flavor_text": [
                    "You share stories and bond with your classmates over meals.",
                    "Yuji shows you a new way to apply cursed energy.",
                    "The shared experiences strengthen your bonds."
                ]
            },
            
            "study": {
                "name": "Research Cursed Spirits",
                "description": "Study ancient texts and curse documentation in the library.",
                "effects": {
                    "experience": lambda level: 15 + level,
                    "trait_bonus": "analytical",
                    "knowledge": True
                },
                "flavor_text": [
                    "You discover fascinating historical accounts of powerful curses.",
                    "The ancient texts reveal patterns in cursed spirit behavior.",
                    "Your understanding of jujutsu theory deepens significantly."
                ]
            },
            
            "explore": {
                "name": "Explore the Campus",
                "description": "Search for hidden areas and secrets around the school.",
                "effects": {
                    "discovery_chance": 0.3,
                    "trait_bonus": "reckless",
                    "cursed_energy": lambda player: 5
                },
                "flavor_text": [
                    "You find a hidden meditation spot with strong spiritual energy.",
                    "The old buildings hold many secrets waiting to be discovered.",
                    "Your curiosity leads you to unexpected places."
                ]
            },
            
            "rest": {
                "name": "Rest and Recover",
                "description": "Take time to relax and restore your energy.",
                "effects": {
                    "hp_restore": lambda player: min(20, player.max_hp - player.hp),
                    "cursed_energy": lambda player: min(15, player.max_cursed_energy - player.cursed_energy),
                    "trait_bonus": "cautious"
                },
                "flavor_text": [
                    "You feel refreshed and ready for new challenges.",
                    "The peaceful rest restores both body and spirit.",
                    "Sometimes the best action is knowing when to rest."
                ]
            },
            
            "mentor_session": {
                "name": "Seek Guidance from Teachers",
                "description": "Learn from experienced sorcerers and gain wisdom.",
                "effects": {
                    "experience": lambda level: 25 + level,
                    "relationships": {"gojo": 3, "nanami": 3},
                    "trait_bonus": "determined",
                    "technique_progress": True
                },
                "flavor_text": [
                    "Gojo-sensei shares insights that change your perspective.",
                    "Nanami's practical advice helps you see techniques differently.", 
                    "The wisdom of experienced sorcerers guides your growth."
                ]
            }
        }
    
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
        if self.in_downtime:
            self._display_downtime_scene(game_state)
            return
        
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
    
    def _display_downtime_scene(self, game_state):
        """Display downtime scene information."""
        print(f"\n🏫 Downtime at {game_state.current_location}")
        print("=" * 50)
        print("You have some free time to focus on personal development.")
        print("What would you like to do?")
        
        # Show character status
        player = game_state.player
        print(f"\n📊 Character Status:")
        print(f"   HP: {player.hp}/{player.max_hp}")
        print(f"   Cursed Energy: {player.cursed_energy}/{player.max_cursed_energy}")
        print(f"   Level: {player.level} (EXP: {player.experience})")
        
        # Show dominant traits
        dominant_traits = player.get_dominant_traits()
        if dominant_traits:
            trait_names = [trait.value for trait in dominant_traits]
            print(f"   Dominant Traits: {', '.join(trait_names)}")
        
        # Show relationships
        if game_state.relationships:
            print(f"\n💭 Key Relationships:")
            for npc, level in game_state.relationships.items():
                if level > 0:
                    relationship_status = self._get_relationship_status(level)
                    print(f"   {npc.title()}: {level} ({relationship_status})")
    
    def _get_relationship_status(self, level: int) -> str:
        """Get relationship status description."""
        if level >= 80:
            return "Unbreakable Bond"
        elif level >= 60:
            return "Close Friend"
        elif level >= 40:
            return "Good Friend"
        elif level >= 20:
            return "Friend"
        elif level >= 10:
            return "Acquaintance"
        else:
            return "Distant"
    
    def get_available_actions(self, game_state) -> List[Dict[str, Any]]:
        """Get available actions for the current scene."""
        if self.in_downtime:
            return self._get_downtime_actions(game_state)
        
        if self.current_scene not in self.story_scenes:
            # Default exploration actions
            return [
                {"text": "Explore the area", "type": "explore"},
                {"text": "Talk to NPCs", "type": "social"},
                {"text": "Train your abilities", "type": "training"},
                {"text": "Enter downtime period", "type": "enter_downtime"}
            ]
        
        scene = self.story_scenes[self.current_scene]
        actions = []
        
        for choice in scene.choices:
            # Check if choice is available based on requirements
            if self._check_requirements(choice.consequences, game_state):
                actions.append({"text": choice.text, "choice": choice})
        
        # Add downtime option after major story beats
        if game_state.current_chapter > 2:
            actions.append({"text": "Take some downtime before continuing", "type": "enter_downtime"})
        
        return actions
    
    def _get_downtime_actions(self, game_state) -> List[Dict[str, Any]]:
        """Get available actions during downtime."""
        actions = []
        
        # Add downtime activities
        for activity_key, activity in self.downtime_activities.items():
            actions.append({
                "text": activity["name"],
                "description": activity["description"],
                "type": "downtime_activity",
                "activity": activity_key
            })
        
        # Add option to continue main story
        actions.append({
            "text": "Continue the main story",
            "description": "Resume your mission and advance the plot.",
            "type": "continue_story"
        })
        
        return actions
    
    def enter_downtime(self, game_state):
        """Enter downtime mode."""
        self.in_downtime = True
        print("\n" + "=" * 60)
        print("               DOWNTIME PERIOD")
        print("=" * 60)
        print("You have some free time between missions. This is a chance to")
        print("develop your character, build relationships, and prepare for")
        print("upcoming challenges.")
        print("\nChoose how you'd like to spend your time, or continue with")
        print("the main story when you're ready.")
        print("=" * 60)
    
    def exit_downtime(self, game_state):
        """Exit downtime mode and continue story."""
        self.in_downtime = False
        print("\n📖 Returning to the main story...")
        print("Your downtime has prepared you for what lies ahead.")
    
    def process_downtime_activity(self, activity_key: str, game_state) -> Dict[str, Any]:
        """Process a downtime activity and apply its effects."""
        if activity_key not in self.downtime_activities:
            return {"error": "Invalid activity"}
        
        activity = self.downtime_activities[activity_key]
        effects = activity["effects"]
        
        print(f"\n🎯 {activity['name']}")
        print("-" * 40)
        print(activity["description"])
        print()
        
        # Apply effects
        result = {"activity_completed": True}
        
        # Experience gain
        if "experience" in effects:
            if callable(effects["experience"]):
                exp_gain = effects["experience"](game_state.player.level)
            else:
                exp_gain = effects["experience"]
            game_state.player.gain_experience(exp_gain)
            print(f"📈 Gained {exp_gain} experience!")
        
        # HP restoration
        if "hp_restore" in effects:
            if callable(effects["hp_restore"]):
                hp_gain = effects["hp_restore"](game_state.player)
            else:
                hp_gain = effects["hp_restore"]
            if hp_gain > 0:
                actual_heal = game_state.player.heal(hp_gain)
                print(f"💚 Restored {actual_heal} HP!")
        
        # Cursed energy restoration
        if "cursed_energy" in effects:
            if callable(effects["cursed_energy"]):
                ce_gain = effects["cursed_energy"](game_state.player)
            else:
                ce_gain = effects["cursed_energy"]
            if ce_gain > 0:
                actual_restore = game_state.player.restore_cursed_energy(ce_gain)
                print(f"⚡ Restored {actual_restore} cursed energy!")
        
        # Relationship changes
        if "relationships" in effects:
            for npc, change in effects["relationships"].items():
                game_state.update_relationship(npc, change)
                print(f"💭 Relationship with {npc.title()} improved by {change}!")
        
        # Trait bonuses
        if "trait_bonus" in effects:
            from character import Trait
            trait_name = effects["trait_bonus"]
            for trait in Trait:
                if trait.value.lower() == trait_name.lower():
                    game_state.player.modify_trait(trait, 5)
                    print(f"🌟 {trait.value} trait increased!")
                    break
        
        # Special effects
        if effects.get("discovery_chance", 0) > 0:
            if random.random() < effects["discovery_chance"]:
                discoveries = [
                    "a hidden cursed tool fragment",
                    "an ancient training manual",
                    "a secret meditation spot",
                    "a rare cursed energy crystal"
                ]
                discovery = random.choice(discoveries)
                print(f"✨ You discovered {discovery}!")
                game_state.add_to_inventory(discovery)
        
        if effects.get("technique_hint"):
            print("💡 You gained insight into advanced cursed techniques!")
        
        if effects.get("knowledge"):
            print("📚 Your understanding of jujutsu theory has deepened!")
        
        if effects.get("technique_progress"):
            print("🎓 Your technical skills have improved significantly!")
        
        # Display flavor text
        flavor_text = random.choice(activity["flavor_text"])
        print(f"\n✨ {flavor_text}")
        
        return result
    
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
        
        # Handle downtime-related actions
        if action.get("type") == "enter_downtime":
            self.enter_downtime(game_state)
            return {}
        elif action.get("type") == "continue_story":
            self.exit_downtime(game_state)
            return {}
        elif action.get("type") == "downtime_activity":
            return self.process_downtime_activity(action["activity"], game_state)
        
        # Handle regular actions
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