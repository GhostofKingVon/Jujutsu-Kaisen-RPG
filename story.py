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
        self._initialize_story()
        self._initialize_locations()
    
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
        
        # Enhanced exploration outcomes with character development
        outcomes = [
            "A hidden cursed tool",
            "An old scroll with technique hints", 
            "A peaceful meditation spot",
            "Traces of cursed energy",
            "A mysterious letter addressed to someone",
            "Personal belongings from a past student",
            "Ancient technique training notes",
            "A hidden shrine with spiritual energy",
            "Footprints leading to a secret area",
            "Nothing of interest"
        ]
        
        outcome = random.choice(outcomes)
        print(f"✨ {outcome}!")
        
        if "cursed tool" in outcome:
            game_state.add_to_inventory("Cursed Tool Fragment")
        elif "scroll" in outcome:
            game_state.player.gain_experience(25)
            # Chance to discover technique hints
            if random.random() < 0.3:
                game_state.player.gain_skill_point(1)
                print("📜 The scroll contains valuable technique insights!")
        elif "meditation" in outcome:
            restored = game_state.player.restore_cursed_energy(20)
            if restored > 0:
                print(f"Restored {restored} cursed energy from meditation.")
        elif "mysterious letter" in outcome:
            self._trigger_character_backstory_event(game_state)
        elif "personal belongings" in outcome:
            self._discover_student_history(game_state)
        elif "training notes" in outcome:
            self._find_technique_knowledge(game_state)
        elif "shrine" in outcome:
            self._spiritual_encounter(game_state)
        elif "secret area" in outcome:
            self._hidden_area_discovery(game_state)
        
        return {}
    
    def _trigger_character_backstory_event(self, game_state):
        """Trigger a character backstory exploration event."""
        print("\n📖 CHARACTER BACKSTORY EVENT")
        print("=" * 40)
        
        backstory_events = [
            {
                "title": "Family Legacy",
                "description": "You find records mentioning your family's connection to jujutsu sorcery...",
                "choices": [
                    ("Investigate further", {"traits": {"Analytical": 5}, "exp": 30}),
                    ("Keep it private", {"traits": {"Cautious": 5}, "energy": 15}),
                    ("Share with friends", {"traits": {"Compassionate": 5}, "relationships": {"yuji": 10}})
                ]
            },
            {
                "title": "Past Trauma",
                "description": "A memory surfaces of your first encounter with cursed spirits...",
                "choices": [
                    ("Face the memory", {"traits": {"Determined": 10}, "exp": 40}),
                    ("Suppress it", {"traits": {"Cautious": 5}, "hp": -10}),
                    ("Seek support", {"traits": {"Compassionate": 5}, "relationships": {"gojo": 15}})
                ]
            },
            {
                "title": "Hidden Talent",
                "description": "You discover evidence of an unusual ability you might possess...",
                "choices": [
                    ("Train intensively", {"traits": {"Focused": 10}, "skill_points": 2}),
                    ("Research carefully", {"traits": {"Analytical": 8}, "exp": 35}),
                    ("Ask for guidance", {"traits": {"Protective": 5}, "relationships": {"megumi": 12}})
                ]
            }
        ]
        
        event = random.choice(backstory_events)
        print(f"📚 {event['title']}")
        print(f"{event['description']}")
        print("\nHow do you respond?")
        
        for i, (choice_text, _) in enumerate(event['choices'], 1):
            print(f"{i}. {choice_text}")
        
        try:
            choice_idx = int(input("Enter your choice (1-3): ")) - 1
            if 0 <= choice_idx < len(event['choices']):
                choice_text, effects = event['choices'][choice_idx]
                print(f"\n🎭 You choose: {choice_text}")
                self._apply_backstory_effects(game_state, effects)
            else:
                print("Invalid choice, no effect.")
        except ValueError:
            print("Invalid input, no effect.")
    
    def _apply_backstory_effects(self, game_state, effects):
        """Apply effects from character backstory choices."""
        for effect_type, value in effects.items():
            if effect_type == "traits":
                for trait_name, amount in value.items():
                    from character import Trait
                    trait = next((t for t in Trait if t.value == trait_name), None)
                    if trait:
                        game_state.player.modify_trait(trait, amount)
                        print(f"🌟 {trait_name} increased by {amount}")
            elif effect_type == "exp":
                game_state.player.gain_experience(value)
                print(f"📈 Gained {value} experience!")
            elif effect_type == "energy":
                restored = game_state.player.restore_cursed_energy(value)
                print(f"⚡ Restored {restored} cursed energy")
            elif effect_type == "hp":
                if value < 0:
                    damage_taken = game_state.player.take_damage(-value)
                    print(f"💔 Lost {damage_taken} HP from emotional stress")
                else:
                    healed = game_state.player.heal(value)
                    print(f"❤️ Restored {healed} HP")
            elif effect_type == "skill_points":
                game_state.player.gain_skill_point(value)
            elif effect_type == "relationships":
                for npc, amount in value.items():
                    game_state.update_relationship(npc, amount)
                    print(f"💝 Relationship with {npc.title()} improved by {amount}")
    
    def _discover_student_history(self, game_state):
        """Discover history of past students."""
        histories = [
            "Records of a student who mastered unique shadow techniques...",
            "A diary describing the development of cursed speech abilities...",
            "Training logs of someone who overcame great personal loss...",
            "Notes about a student who created their own fighting style..."
        ]
        
        history = random.choice(histories)
        print(f"📖 {history}")
        
        # Gain insight and inspiration
        game_state.player.gain_experience(20)
        game_state.player.gain_skill_point(1)
        print("💡 You gain insight from their journey!")
    
    def _find_technique_knowledge(self, game_state):
        """Discover advanced technique knowledge."""
        knowledge_types = [
            ("Cursed Energy Flow Optimization", "All techniques cost 10% less energy for next 5 combats"),
            ("Combat Stance Analysis", "Next 3 attacks have increased accuracy"),
            ("Defensive Positioning", "Take 20% less damage for next 4 combats"),
            ("Power Focus Meditation", "Next technique deals 50% more damage")
        ]
        
        knowledge_name, effect = random.choice(knowledge_types)
        print(f"📚 Technique Knowledge: {knowledge_name}")
        print(f"✨ Effect: {effect}")
        
        # Add temporary enhancement flag
        game_state.add_story_flag(f"temp_enhancement_{knowledge_name.lower().replace(' ', '_')}", 
                                  {"effect": effect, "uses_remaining": 5})
        game_state.player.gain_skill_point(1)
    
    def _spiritual_encounter(self, game_state):
        """Encounter spiritual energy that affects character development."""
        encounters = [
            {
                "name": "Benevolent Spirit",
                "description": "A peaceful spirit offers wisdom about compassion",
                "effect": {"traits": {"Compassionate": 8}, "energy_restore": 30}
            },
            {
                "name": "Warrior Spirit", 
                "description": "An ancient warrior's spirit teaches about determination",
                "effect": {"traits": {"Determined": 8}, "hp_restore": 25}
            },
            {
                "name": "Scholar Spirit",
                "description": "A learned spirit shares knowledge about focus and analysis",
                "effect": {"traits": {"Focused": 5, "Analytical": 5}, "skill_points": 2}
            }
        ]
        
        encounter = random.choice(encounters)
        print(f"👻 Spiritual Encounter: {encounter['name']}")
        print(f"✨ {encounter['description']}")
        
        # Apply effects
        for effect_type, value in encounter["effect"].items():
            if effect_type == "traits":
                for trait_name, amount in value.items():
                    from character import Trait
                    trait = next((t for t in Trait if t.value == trait_name), None)
                    if trait:
                        game_state.player.modify_trait(trait, amount)
                        print(f"🌟 {trait_name} increased by {amount}")
            elif effect_type == "energy_restore":
                restored = game_state.player.restore_cursed_energy(value)
                print(f"⚡ Spiritual energy restores {restored} cursed energy")
            elif effect_type == "hp_restore":
                healed = game_state.player.heal(value)
                print(f"❤️ Spiritual blessing restores {healed} HP")
            elif effect_type == "skill_points":
                game_state.player.gain_skill_point(value)
    
    def _hidden_area_discovery(self, game_state):
        """Discover a hidden area with special properties."""
        areas = [
            {
                "name": "Secret Training Ground",
                "description": "An ancient training area with enhanced cursed energy",
                "reward": "Can train here for double experience gain (once per chapter)"
            },
            {
                "name": "Meditation Chamber",
                "description": "A peaceful room that enhances spiritual growth", 
                "reward": "Permanent +5 to maximum cursed energy"
            },
            {
                "name": "Technique Archive",
                "description": "Hidden scrolls containing lost knowledge",
                "reward": "Unlock special technique: Ancient Arts"
            },
            {
                "name": "Memorial Garden",
                "description": "A garden dedicated to fallen sorcerers",
                "reward": "Gain 'Memorial Blessing' - protection from critical hits"
            }
        ]
        
        area = random.choice(areas)
        print(f"🗝️ Hidden Discovery: {area['name']}")
        print(f"📍 {area['description']}")
        print(f"🎁 Reward: {area['reward']}")
        
        # Apply area-specific rewards
        area_name = area["name"]
        game_state.add_story_flag(f"discovered_{area_name.lower().replace(' ', '_')}", True)
        
        if "Training Ground" in area_name:
            game_state.add_story_flag("secret_training_available", True)
        elif "Meditation Chamber" in area_name:
            game_state.player.max_cursed_energy += 5
            game_state.player.cursed_energy += 5
            print("⚡ Maximum cursed energy permanently increased!")
        elif "Technique Archive" in area_name:
            # Add special technique
            if not any(t.name == "Ancient Arts" for t in game_state.player.techniques):
                ancient_arts = game_state.player._create_technique_from_name("Ancient Arts")
                if not ancient_arts:
                    from character import CursedTechnique
                    ancient_arts = CursedTechnique(
                        "Ancient Arts",
                        damage=55,
                        cost=30,
                        description="Lost technique with mystical properties",
                        technique_type="offensive",
                        cooldown=4
                    )
                game_state.player.add_technique(ancient_arts)
                print("📜 Learned Ancient Arts technique!")
        elif "Memorial Garden" in area_name:
            game_state.add_story_flag("memorial_blessing", True)
            print("🛡️ Gained Memorial Blessing protection!")
    
    def get_available_personal_missions(self, game_state) -> List[Dict[str, Any]]:
        """Get available personal missions based on character development."""
        missions = []
        player = game_state.player
        dominant_traits = player.get_dominant_traits()
        
        # Trait-based personal missions
        if any(trait.value == "Compassionate" for trait in dominant_traits):
            if not game_state.is_mission_completed("heal_the_wounded"):
                missions.append({
                    "id": "heal_the_wounded",
                    "title": "Heal the Wounded",
                    "description": "Use your compassionate nature to help injured students",
                    "requirements": ["Learn Healing Aura technique", "Relationship with Gojo 40+"],
                    "rewards": ["Experience: 100", "Skill Points: 3", "New technique: Greater Healing"],
                    "chapters": [5, 6, 7]  # Available in these chapters
                })
        
        if any(trait.value == "Determined" for trait in dominant_traits):
            if not game_state.is_mission_completed("overcome_limits"):
                missions.append({
                    "id": "overcome_limits",
                    "title": "Overcome Your Limits",
                    "description": "Push beyond your physical and mental boundaries",
                    "requirements": ["Level 10+", "Defeat 3 Grade 2 curses without assistance"],
                    "rewards": ["Max HP +30", "Max CE +20", "Ultimate technique: Limitless Determination"],
                    "chapters": [8, 9, 10]
                })
        
        if any(trait.value == "Protective" for trait in dominant_traits):
            if not game_state.is_mission_completed("guardian_oath"):
                missions.append({
                    "id": "guardian_oath",
                    "title": "Guardian's Oath",
                    "description": "Swear to protect those who cannot protect themselves",
                    "requirements": ["Save 5 civilians", "Relationship with all first years 50+"],
                    "rewards": ["Protective aura ability", "Team combo techniques", "Guardian title"],
                    "chapters": [6, 7, 8, 9]
                })
        
        # Level-based missions
        if player.level >= 8 and not game_state.is_mission_completed("technique_mastery"):
            missions.append({
                "id": "technique_mastery",
                "title": "Master of Techniques",
                "description": "Achieve mastery in multiple cursed techniques",
                "requirements": ["Master 3 techniques to level 4+", "Use 100 techniques in combat"],
                "rewards": ["Technique efficiency +25%", "New fusion abilities", "Master title"],
                "chapters": [7, 8, 9, 10, 11]
            })
        
        if player.level >= 12 and not game_state.is_mission_completed("inner_strength"):
            missions.append({
                "id": "inner_strength",
                "title": "Discover Inner Strength",
                "description": "Uncover the true source of your power",
                "requirements": ["Complete character backstory events", "Reach high bond with mentor"],
                "rewards": ["Unique personal technique", "Stat bonuses based on journey", "True potential unlocked"],
                "chapters": [10, 11, 12]
            })
        
        # Relationship-based missions
        if game_state.get_relationship("yuji") >= 60:
            if not game_state.is_mission_completed("brothers_in_arms"):
                missions.append({
                    "id": "brothers_in_arms", 
                    "title": "Brothers in Arms",
                    "description": "Forge an unbreakable bond with Yuji through shared trials",
                    "requirements": ["Fight alongside Yuji in 5 battles", "Share personal backstory"],
                    "rewards": ["Synchronized Black Flash technique", "Yuji's trust", "Brotherhood bonus"],
                    "chapters": [4, 5, 6, 7]
                })
        
        # Filter missions available in current chapter
        current_chapter = game_state.current_chapter
        available_missions = [m for m in missions if current_chapter in m.get("chapters", [current_chapter])]
        
        return available_missions
    
    def start_personal_mission(self, mission_id: str, game_state) -> Dict[str, Any]:
        """Start a personal mission."""
        missions = self.get_available_personal_missions(game_state)
        mission = next((m for m in missions if m["id"] == mission_id), None)
        
        if not mission:
            return {"success": False, "message": "Mission not available"}
        
        print(f"\n🎯 PERSONAL MISSION STARTED")
        print(f"📋 {mission['title']}")
        print(f"📖 {mission['description']}")
        print("\nRequirements:")
        for req in mission["requirements"]:
            print(f"  • {req}")
        print("\nRewards:")
        for reward in mission["rewards"]:
            print(f"  🎁 {reward}")
        
        # Add mission to active missions
        game_state.add_story_flag(f"active_mission_{mission_id}", {
            "started_chapter": game_state.current_chapter,
            "progress": {},
            "requirements_met": []
        })
        
        return {"success": True, "mission": mission}
    
    def check_personal_mission_progress(self, game_state):
        """Check and update progress on active personal missions."""
        active_missions = [flag for flag in game_state.story_flags.keys() 
                          if flag.startswith("active_mission_")]
        
        for mission_flag in active_missions:
            mission_id = mission_flag.replace("active_mission_", "")
            mission_data = game_state.get_story_flag(mission_flag)
            
            # Check specific mission progress
            progress_made = False
            
            if mission_id == "heal_the_wounded":
                progress_made = self._check_healing_mission_progress(game_state, mission_data)
            elif mission_id == "overcome_limits":
                progress_made = self._check_limits_mission_progress(game_state, mission_data)
            elif mission_id == "guardian_oath":
                progress_made = self._check_guardian_mission_progress(game_state, mission_data)
            elif mission_id == "technique_mastery":
                progress_made = self._check_mastery_mission_progress(game_state, mission_data)
            elif mission_id == "brothers_in_arms":
                progress_made = self._check_brotherhood_mission_progress(game_state, mission_data)
            
            # Check if mission is complete
            if self._is_mission_complete(mission_id, game_state, mission_data):
                self._complete_personal_mission(mission_id, game_state)
            elif progress_made:
                print(f"📈 Progress made on mission: {mission_id.replace('_', ' ').title()}")
    
    def _check_healing_mission_progress(self, game_state, mission_data) -> bool:
        """Check progress on healing mission."""
        # Implementation depends on tracking healing actions
        return False
    
    def _check_limits_mission_progress(self, game_state, mission_data) -> bool:
        """Check progress on limits mission."""
        # Track combat victories and conditions
        return False
    
    def _check_guardian_mission_progress(self, game_state, mission_data) -> bool:
        """Check progress on guardian mission."""
        # Track protective actions and relationship levels
        return False
    
    def _check_mastery_mission_progress(self, game_state, mission_data) -> bool:
        """Check progress on mastery mission."""
        player = game_state.player
        mastered_techniques = sum(1 for tech in player.techniques if tech.mastery_level >= 4)
        total_usage = sum(tech.usage_count for tech in player.techniques)
        
        progress = mission_data.get("progress", {})
        progress["mastered_techniques"] = mastered_techniques
        progress["total_usage"] = total_usage
        
        return mastered_techniques >= 3 and total_usage >= 100
    
    def _check_brotherhood_mission_progress(self, game_state, mission_data) -> bool:
        """Check progress on brotherhood mission."""
        yuji_relationship = game_state.get_relationship("yuji")
        return yuji_relationship >= 60
    
    def _is_mission_complete(self, mission_id: str, game_state, mission_data) -> bool:
        """Check if a mission is complete."""
        # Simplified completion check - in full game would be more detailed
        if mission_id == "technique_mastery":
            return self._check_mastery_mission_progress(game_state, mission_data)
        elif mission_id == "brothers_in_arms":
            return (game_state.get_relationship("yuji") >= 70 and 
                    game_state.get_story_flag("shared_backstory_yuji", False))
        
        return False
    
    def _complete_personal_mission(self, mission_id: str, game_state):
        """Complete a personal mission and award rewards."""
        print(f"\n🎉 PERSONAL MISSION COMPLETED!")
        print(f"✅ {mission_id.replace('_', ' ').title()}")
        
        # Mark as completed
        game_state.complete_mission(mission_id)
        game_state.story_flags.pop(f"active_mission_{mission_id}", None)
        
        # Award mission-specific rewards
        if mission_id == "technique_mastery":
            print("🌟 Technique efficiency increased by 25%!")
            game_state.add_story_flag("technique_efficiency_bonus", 0.25)
            game_state.player.gain_skill_point(5)
            
        elif mission_id == "brothers_in_arms":
            print("🤝 Unbreakable bond with Yuji formed!")
            game_state.update_relationship("yuji", 30)
            game_state.add_story_flag("yuji_brotherhood", True)
            
            # Unlock special technique
            from character import CursedTechnique
            sync_flash = CursedTechnique(
                "Synchronized Black Flash",
                damage=100,
                cost=45,
                description="Perfect synchronization with Yuji for massive damage",
                technique_type="offensive",
                cooldown=8
            )
            game_state.player.add_technique(sync_flash)
            print("🌟 Learned Synchronized Black Flash!")
        
        # Common rewards
        game_state.player.gain_experience(100)
        print("📈 Gained 100 experience from mission completion!")
    
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