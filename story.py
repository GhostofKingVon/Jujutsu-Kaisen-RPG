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
        self.recent_events = []  # Track recent events for emotional triggers
        self._initialize_story()
        self._initialize_locations()
    
    def add_recent_event(self, event: str):
        """Add a recent event for emotional moment tracking."""
        self.recent_events.append(event)
        # Keep only the last 10 events
        if len(self.recent_events) > 10:
            self.recent_events = self.recent_events[-10:]
    
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
        
        # New expanded story scenes
        
        # Post first battle scenes
        self.story_scenes["post_first_battle"] = StoryScene(
            "After the First Victory",
            """The cursed spirit dissolves into nothingness, leaving only the fading echoes 
of its malevolent energy. You and Yuji stand victorious, but the injured student lies 
unconscious nearby. This was your first real taste of what it means to be a sorcerer.

"That was incredible!" Yuji exclaims, his eyes bright with excitement. "The way we 
worked together... it felt natural, like we've been partners for years!"

But beneath the adrenaline, you feel the weight of responsibility settling on your 
shoulders. Every victory comes with the knowledge that somewhere else, another curse 
might be threatening innocent lives.""",
            [
                StoryChoice(
                    "Focus on helping the injured student",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 10},
                        "relationships": {"injured_student": 20, "yuji": 5},
                        "next_scene": "medical_training",
                        "story_flags": {"prioritized_healing": True}
                    }
                ),
                StoryChoice(
                    "Discuss the battle strategy with Yuji",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 5},
                        "relationships": {"yuji": 15},
                        "next_scene": "tactical_discussion",
                        "story_flags": {"analytical_approach": True}
                    }
                ),
                StoryChoice(
                    "Reflect on the responsibility of being a sorcerer",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.CAUTIOUS: 5},
                        "next_scene": "responsibility_reflection",
                        "story_flags": {"deep_reflection": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # Emotional breakthrough scene
        self.story_scenes["first_loss_recovery"] = StoryScene(
            "Rising from Defeat",
            """Days have passed since your crushing defeat. Your physical wounds have healed, 
but the emotional scars run deeper. You sit alone in the school's meditation garden, 
questioning everything you thought you knew about strength and purpose.

Megumi approaches quietly, his footsteps soft on the gravel path.

"Defeat isn't the end," he says, settling beside you. "It's information. Every loss 
teaches us something about ourselves, about our limits, and about how to grow beyond them."

His words carry the weight of personal experience. You realize that every sorcerer 
here has faced their own moments of crushing defeat.""",
            [
                StoryChoice(
                    "Ask Megumi about his own failures",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.COMPASSIONATE: 5},
                        "relationships": {"megumi": 20},
                        "next_scene": "megumi_backstory",
                        "story_flags": {"learned_from_megumi": True}
                    }
                ),
                StoryChoice(
                    "Share your fears about not being strong enough",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.DETERMINED: 10},
                        "relationships": {"megumi": 15},
                        "next_scene": "vulnerability_moment",
                        "story_flags": {"opened_up_to_megumi": True}
                    }
                ),
                StoryChoice(
                    "Vow to become stronger no matter what it takes",
                    {
                        "traits": {Trait.DETERMINED: 20, Trait.RECKLESS: 5},
                        "next_scene": "determination_training",
                        "story_flags": {"intense_training_vow": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Meditation Garden"
        )
        
        # Special training arc
        self.story_scenes["special_training_offer"] = StoryScene(
            "An Unusual Opportunity",
            """Gojo-sensei appears with his characteristic casual smile, but there's something 
different in his expression - a seriousness that makes you pay attention.

"I've been watching your progress," he says, hands in his pockets. "You have potential 
that goes beyond the ordinary. I'm offering you special training, but I need to warn you - 
this isn't going to be easy. We'll be pushing your limits in ways that might fundamentally 
change who you are as a sorcerer."

He removes his blindfold, and his Six Eyes seem to peer directly into your soul.

"The question is: are you ready to discover what you're truly capable of?"

The weight of this opportunity settles on your shoulders. Special training with the 
strongest sorcerer alive - but at what cost?""",
            [
                StoryChoice(
                    "Accept immediately - you need to become stronger",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.RECKLESS: 10},
                        "relationships": {"gojo": 15},
                        "next_scene": "intensive_training_arc",
                        "story_flags": {"gojo_special_training": True}
                    }
                ),
                StoryChoice(
                    "Ask about the risks before deciding",
                    {
                        "traits": {Trait.CAUTIOUS: 15, Trait.ANALYTICAL: 10},
                        "relationships": {"gojo": 10},
                        "next_scene": "training_explanation",
                        "story_flags": {"cautious_about_training": True}
                    }
                ),
                StoryChoice(
                    "Request time to think about it",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.FOCUSED: 5},
                        "next_scene": "contemplation_period",
                        "story_flags": {"delayed_training_decision": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Gojo's Office"
        )
        
        # Shibuya incident scenes
        self.story_scenes["shibuya_frontline"] = StoryScene(
            "Into the Heart of Darkness",
            """Shibuya burns. Not with ordinary fire, but with the malevolent energy of 
countless cursed spirits. The famous crossing that once pulsed with human life now 
writhes with supernatural malice.

You stand with the assault team at the perimeter, knowing that once you cross this line, 
nothing will ever be the same. The mission briefing was clear: locate and neutralize 
the Special Grade curse orchestrating this chaos.

Yuji grips your shoulder. "Whatever happens in there," he says quietly, "we watch each 
other's backs. Some of us might not make it out, but we make sure our sacrifice means 
something."

The weight of those words settles over the team like a shroud.""",
            [
                StoryChoice(
                    "Lead the charge into the district",
                    {
                        "traits": {Trait.DETERMINED: 20, Trait.PROTECTIVE: 10},
                        "combat": True,
                        "enemy": "shibuya_curse_horde",
                        "next_scene": "shibuya_first_battle"
                    }
                ),
                StoryChoice(
                    "Suggest a coordinated strategic advance",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10},
                        "next_scene": "shibuya_tactical_approach",
                        "story_flags": {"strategic_shibuya_entry": True}
                    }
                ),
                StoryChoice(
                    "Focus on protecting civilians first",
                    {
                        "traits": {Trait.COMPASSIONATE: 20, Trait.PROTECTIVE: 15},
                        "next_scene": "shibuya_rescue_priority",
                        "story_flags": {"civilian_priority": True}
                    }
                )
            ],
            "Shibuya District - Perimeter"
        )
        
        # CT Awakening scene
        self.story_scenes["first_ct_awakening"] = StoryScene(
            "Awakening of Power",
            """In the depths of despair, as your friends lie wounded and the enemy prepares 
their final attack, something deep within you stirs. Memories flash before your eyes - 
every moment of training, every person you've sworn to protect, every dream of becoming 
stronger.

"I won't let this end here," you whisper, and suddenly your cursed energy feels different. 
It flows with a purpose and clarity you've never experienced before.

The very air around you begins to shimmer with power as something awakens within your soul. 
This isn't just a new technique - it's the manifestation of everything you've learned, 
everything you've felt, everything you are.

Your enemies step back, sensing that something fundamental has changed.""",
            [
                StoryChoice(
                    "Channel the awakening into a devastating attack",
                    {
                        "traits": {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 20},
                        "combat": True,
                        "enemy": "awakening_test_enemy",
                        "special_effect": "ct_awakening_power",
                        "next_scene": "post_awakening_reflection"
                    }
                ),
                StoryChoice(
                    "Use the new power to protect your friends",
                    {
                        "traits": {Trait.PROTECTIVE: 25, Trait.COMPASSIONATE: 15},
                        "next_scene": "protective_awakening",
                        "story_flags": {"protective_awakening": True}
                    }
                ),
                StoryChoice(
                    "Try to understand this new power before using it",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 10},
                        "next_scene": "awakening_analysis",
                        "story_flags": {"studied_awakening": True}
                    }
                )
            ],
            "Unknown Location - Moment of Crisis"
        )
        
        # Final arc preparation
        self.story_scenes["final_arc_preparation"] = StoryScene(
            "The Gathering Storm",
            """The pieces are finally coming together. Everything you've learned, everyone 
you've grown close to, all the trials you've endured - they've all led to this moment.

Intelligence reports indicate that the source of the cursed spirit crisis has been 
identified. It's not just a powerful curse - it's something that threatens the very 
balance between the human and cursed spirit worlds.

Gojo-sensei stands before the assembled students and faculty, his usual playful demeanor 
replaced by grim determination.

"This is it," he says simply. "Everything we've trained for comes down to this final 
confrontation. Some of us might not return, but we go forward anyway. Because that's 
what it means to be a Jujutsu Sorcerer."

Your friends look to you. In their eyes, you see the same determination that burns in 
your own heart.""",
            [
                StoryChoice(
                    "Give an inspiring speech to rally everyone",
                    {
                        "traits": {Trait.DETERMINED: 25, Trait.PROTECTIVE: 15},
                        "relationships": {"yuji": 10, "megumi": 10, "nobara": 10},
                        "next_scene": "inspirational_leader_path",
                        "story_flags": {"became_inspirational_leader": True}
                    }
                ),
                StoryChoice(
                    "Focus on the tactical aspects of the mission",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15},
                        "next_scene": "tactical_leader_path",
                        "story_flags": {"became_tactical_leader": True}
                    }
                ),
                StoryChoice(
                    "Quietly prepare yourself and support others",
                    {
                        "traits": {Trait.COMPASSIONATE: 20, Trait.CAUTIOUS: 10},
                        "next_scene": "supportive_role_path",
                        "story_flags": {"became_supportive_leader": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Assembly Hall"
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
        
        # Check for emotional moments and CT awakenings
        try:
            from emotional_moments import get_emotional_moment_manager
            from cutscenes import get_cutscene_manager
            
            emotion_manager = get_emotional_moment_manager()
            cutscene_manager = get_cutscene_manager()
            
            # Check for emotional moments
            emotional_moment = emotion_manager.check_emotional_triggers(game_state, self.recent_events)
            if emotional_moment:
                emotion_manager.apply_emotional_moment(emotional_moment, game_state.player, game_state)
            
            # Check for CT awakenings
            emotional_state = emotion_manager.get_emotional_state(game_state.player, self.recent_events)
            ct_awakening = emotion_manager.check_ct_awakening_triggers(game_state.player, game_state, emotional_state)
            if ct_awakening:
                emotion_manager.apply_ct_awakening(ct_awakening, game_state.player, game_state)
            
            # Play relevant cutscenes
            if scene.title == "Arrival at Tokyo Jujutsu High" and not game_state.get_story_flag("intro_cutscene_played", False):
                cutscene_manager.play_cutscene("opening")
                game_state.add_story_flag("intro_cutscene_played", True)
            
        except ImportError:
            # Fallback if emotional moments system isn't available
            pass
        
        print(f"\n📖 {scene.title}")
        print("=" * 50)
        print(scene.description)
        
        # Show relevant character status
        if game_state.player:
            dominant_traits = game_state.player.get_dominant_traits()
            if dominant_traits:
                trait_names = [trait.value for trait in dominant_traits]
                print(f"\n🌟 Your dominant traits: {', '.join(trait_names)}")
        
        # Show emotional flags if any major ones are set
        emotional_flags = [flag for flag in game_state.story_flags.keys() 
                          if any(keyword in flag for keyword in ["emotional", "awakening", "brotherhood"])]
        if emotional_flags:
            print(f"\n💫 Emotional milestones: {len(emotional_flags)} achieved")
    
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