"""
Enhanced Story System - Manga Alignment

Follows the Jujutsu Kaisen manga storyline with major arcs, character development
moments, and player choice integration.
"""

from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
from character import Player, Enemy, Trait
import random


class StoryArc(Enum):
    """Major story arcs from the Jujutsu Kaisen manga."""
    INTRODUCTION = "introduction"
    FEARSOME_WOMB = "fearsome_womb" 
    KYOTO_GOODWILL_EVENT = "kyoto_goodwill_event"
    DEATH_PAINTING_WOMBS = "death_painting_wombs"
    SHIBUYA_INCIDENT = "shibuya_incident"
    PERFECT_PREPARATION = "perfect_preparation"
    CULLING_GAME = "culling_game"


class MangaStoryManager:
    """Enhanced story manager following manga arcs with player choices."""
    
    def __init__(self):
        self.current_arc = StoryArc.INTRODUCTION
        self.arc_progress = 0
        self.manga_scenes = {}
        self.character_development_moments = {}
        self.major_battles = {}
        self._initialize_manga_story()
    
    def _initialize_manga_story(self):
        """Initialize all manga-based story content."""
        self._setup_introduction_arc()
        self._setup_fearsome_womb_arc()
        self._setup_kyoto_goodwill_arc()
        self._setup_shibuya_incident_arc()
        self._setup_character_moments()
        self._setup_major_battles()
    
    def _setup_introduction_arc(self):
        """Set up the introduction arc following manga events."""
        self.manga_scenes["intro_arrival"] = {
            "title": "Arrival at Tokyo Jujutsu High",
            "description": """You arrive at Tokyo Jujutsu High, the premier institution for training jujutsu sorcerers. 
The ancient buildings are protected by powerful barriers, and you can feel the dense cursed energy permeating the air.

As you walk through the main courtyard, you notice three first-year students:
- A pink-haired boy with incredible physical strength (Yuji Itadori)
- A serious black-haired boy with an air of nobility (Megumi Fushiguro)  
- A confident brown-haired girl with fierce eyes (Nobara Kugisaki)

They seem to be discussing their first mission assignment.""",
            "choices": [
                {
                    "text": "Approach and introduce yourself as a fellow first-year",
                    "consequences": {
                        "traits": {"compassionate": 10, "protective": 5},
                        "relationships": {"yuji": 10, "megumi": 5, "nobara": 8},
                        "story_flags": {"friendly_introduction": True},
                        "next_scene": "intro_friendly_meeting"
                    }
                },
                {
                    "text": "Observe them quietly to assess their abilities first",
                    "consequences": {
                        "traits": {"analytical": 15, "cautious": 10},
                        "relationships": {"yuji": 2, "megumi": 8, "nobara": -2},
                        "story_flags": {"analytical_introduction": True},
                        "next_scene": "intro_observant_meeting"
                    }
                },
                {
                    "text": "Challenge them to see their strength",
                    "consequences": {
                        "traits": {"aggressive": 15, "reckless": 10},
                        "relationships": {"yuji": 5, "megumi": -5, "nobara": 10},
                        "story_flags": {"challenging_introduction": True},
                        "next_scene": "intro_combat_meeting"
                    }
                }
            ]
        }
        
        self.manga_scenes["intro_gojo_meeting"] = {
            "title": "Meeting Satoru Gojo",
            "description": """\"Oh? Another first-year student?\"

A tall man with white hair and dark sunglasses approaches with a casual stride. 
Despite his relaxed demeanor, you immediately sense overwhelming cursed energy - 
this must be Satoru Gojo, the strongest jujutsu sorcerer.

\"I'm Gojo-sensei, your teacher. I hope you're ready for some interesting times ahead.\"
His smile is playful, but there's something unsettling about the way space seems to bend around him.

\"Before we begin your training, I want to see what you're made of. How do you view the world of curses?\" """,
            "choices": [
                {
                    "text": "\"I want to save people from the suffering curses cause.\"",
                    "consequences": {
                        "traits": {"compassionate": 20, "protective": 15},
                        "relationships": {"gojo": 15},
                        "morality": {"altruism": 15, "justice": 10},
                        "story_flags": {"heroic_motivation": True}
                    }
                },
                {
                    "text": "\"I need to understand the true nature of cursed energy.\"",
                    "consequences": {
                        "traits": {"analytical": 20, "focused": 15},
                        "relationships": {"gojo": 10},
                        "morality": {"pragmatism": 15},
                        "story_flags": {"scholar_motivation": True}
                    }
                },
                {
                    "text": "\"I want to become strong enough that no one can threaten what I care about.\"",
                    "consequences": {
                        "traits": {"determined": 20, "protective": 10},
                        "relationships": {"gojo": 12},
                        "morality": {"justice": 15},
                        "story_flags": {"strength_motivation": True}
                    }
                }
            ]
        }
    
    def _setup_fearsome_womb_arc(self):
        """Set up the Fearsome Womb arc - first major mission."""
        self.manga_scenes["fearsome_womb_mission"] = {
            "title": "Fearsome Womb: Eishu Detention Center",
            "description": """Gojo-sensei briefs you and the other first-years on your first real mission:

\"There's been a disturbance at the Eishu Juvenile Detention Center. A cursed womb appeared and 
has been growing rapidly. The entire facility is now covered by a veil, and five detainees 
are trapped inside along with the staff.\"

Yuji clenches his fists. \"We have to save them!\"
Megumi looks concerned. \"The cursed energy readings are abnormally high...\"
Nobara checks her tools. \"So what's the plan?\"

The mission briefing indicates this could be a Special Grade curse - far beyond what first-years 
should handle. But people's lives are at stake.""",
            "choices": [
                {
                    "text": "Volunteer to enter first and scout the situation",
                    "consequences": {
                        "traits": {"reckless": 10, "protective": 15},
                        "relationships": {"yuji": 10, "megumi": -5, "nobara": 5},
                        "story_flags": {"fearsome_womb_scout": True},
                        "combat": True,
                        "enemy_type": "detention_center_curse"
                    }
                },
                {
                    "text": "Suggest a coordinated team approach",
                    "consequences": {
                        "traits": {"analytical": 15, "focused": 10},
                        "relationships": {"yuji": 8, "megumi": 15, "nobara": 8},
                        "story_flags": {"fearsome_womb_team": True},
                        "team_combat": True
                    }
                },
                {
                    "text": "Propose evacuating civilians first",
                    "consequences": {
                        "traits": {"compassionate": 20, "cautious": 10},
                        "relationships": {"yuji": 15, "megumi": 10, "nobara": 5},
                        "story_flags": {"fearsome_womb_rescue": True},
                        "rescue_mission": True
                    }
                }
            ]
        }
        
        self.manga_scenes["sukuna_awakening"] = {
            "title": "The King of Curses Awakens",
            "description": """As the battle intensifies, Yuji is severely wounded protecting a civilian. 
In desperation, he allows Sukuna to take control of his body.

The air grows thick with malevolent energy as Sukuna's tattoos appear on Yuji's face and body. 
The King of Curses stretches languidly and grins with predatory satisfaction.

\"Finally... it's been far too long since I've had a proper body.\"

Sukuna's attention turns to you, his eyes gleaming with dangerous interest.

\"And what do we have here? Another little sorcerer playing hero? How... amusing.\"

The Special Grade curse that was dominating the fight moments ago now cowers in terror.""",
            "choices": [
                {
                    "text": "Stand your ground and try to reason with Sukuna",
                    "consequences": {
                        "traits": {"determined": 25, "reckless": 15},
                        "relationships": {"sukuna": 5, "yuji": 10},
                        "story_flags": {"confronted_sukuna": True},
                        "morality": {"justice": 10}
                    }
                },
                {
                    "text": "Focus on helping Yuji regain control",
                    "consequences": {
                        "traits": {"compassionate": 20, "focused": 15},
                        "relationships": {"yuji": 20, "sukuna": -5},
                        "story_flags": {"helped_yuji": True},
                        "technique_unlock": "supportive_energy"
                    }
                },
                {
                    "text": "Retreat and observe Sukuna's power",
                    "consequences": {
                        "traits": {"analytical": 20, "cautious": 15},
                        "relationships": {"sukuna": 8, "yuji": 5},
                        "story_flags": {"studied_sukuna": True},
                        "knowledge_gained": "sukuna_techniques"
                    }
                }
            ]
        }
    
    def _setup_kyoto_goodwill_arc(self):
        """Set up the Kyoto Goodwill Event arc."""
        self.manga_scenes["kyoto_arrival"] = {
            "title": "Kyoto Sister School Exchange Event",
            "description": """You arrive at Kyoto Jujutsu High for the annual Exchange Event. 
The atmosphere is tense - there's clearly rivalry between the schools.

You're greeted by the Kyoto students:
- Aoi Todo, a massive third-year with an intimidating presence
- Mai Zenin, Maki's twin sister with a cold demeanor  
- Noritoshi Kamo, the heir of the Kamo clan
- Kokichi Muta, operating through his Mechamaru puppet
- Kasumi Miwa, a nervous but determined second-year
- Momo Nishimiya, floating on her broomstick

Todo steps forward, cracking his knuckles. \"So you're the new Tokyo first-year? 
Tell me... what's your type in women?\"

The question catches you off guard. You sense this isn't just casual conversation - 
your answer could determine whether Todo sees you as a friend or enemy.""",
            "choices": [
                {
                    "text": "\"I value someone's strength and determination over appearance.\"",
                    "consequences": {
                        "traits": {"focused": 15, "analytical": 10},
                        "relationships": {"todo": 20, "maki": 15, "nobara": 10},
                        "story_flags": {"todo_approved": True},
                        "technique_unlock": "boogie_woogie_training"
                    }
                },
                {
                    "text": "\"I think personality matters most - kindness and compassion.\"",
                    "consequences": {
                        "traits": {"compassionate": 15, "protective": 10},
                        "relationships": {"todo": -10, "yuji": 15, "kasumi": 10},
                        "story_flags": {"todo_disapproved": True}
                    }
                },
                {
                    "text": "\"That's... not really something I think about much.\"",
                    "consequences": {
                        "traits": {"cautious": 10, "analytical": 5},
                        "relationships": {"todo": -15, "megumi": 10},
                        "story_flags": {"todo_confused": True}
                    }
                }
            ]
        }
    
    def _setup_shibuya_incident_arc(self):
        """Set up the climactic Shibuya Incident arc."""
        self.manga_scenes["shibuya_halloween"] = {
            "title": "Shibuya Incident - Halloween Night",
            "description": """Halloween night in Shibuya. The streets are packed with civilians in costumes, 
unaware of the danger lurking beneath the festivities.

Multiple veils suddenly drop across different areas of Shibuya, trapping thousands of people inside. 
This is no random curse attack - it's a coordinated assault by a group of special grade curses.

Gojo-sensei's voice comes through your communicator: \"This is bad. I'm being drawn into a trap, 
but I can't ignore the civilians. You need to evacuate as many people as possible and engage 
any curses you encounter.\"

The air thrums with malevolent energy. In the distance, you can see Hanami, Jogo, and other 
special grade curses coordinating their attack. This is war.""",
            "choices": [
                {
                    "text": "Focus on civilian evacuation",
                    "consequences": {
                        "traits": {"compassionate": 25, "protective": 20},
                        "story_flags": {"shibuya_evacuator": True},
                        "civilians_saved": 50,
                        "morality": {"altruism": 20}
                    }
                },
                {
                    "text": "Hunt down the curse users behind this",
                    "consequences": {
                        "traits": {"aggressive": 20, "determined": 15},
                        "story_flags": {"shibuya_hunter": True},
                        "combat": True,
                        "enemy_type": "curse_user",
                        "morality": {"justice": 15}
                    }
                },
                {
                    "text": "Try to support Gojo against the trap",
                    "consequences": {
                        "traits": {"reckless": 25, "determined": 20},
                        "relationships": {"gojo": 20},
                        "story_flags": {"tried_to_help_gojo": True},
                        "danger_level": "extreme"
                    }
                }
            ]
        }
    
    def _setup_character_moments(self):
        """Set up key character development moments from the manga."""
        self.character_development_moments = {
            "yuji_death_fear": {
                "trigger": "after_fearsome_womb",
                "description": "Yuji grapples with the fear of dying and leaving others behind",
                "player_impact": "relationship_deepening"
            },
            "megumi_self_worth": {
                "trigger": "kyoto_event",
                "description": "Megumi questions whether he's holding the team back",
                "player_impact": "technique_teaching_opportunity"
            },
            "nobara_country_past": {
                "trigger": "death_painting_arc",
                "description": "Nobara reveals her past in the countryside and why she came to Tokyo",
                "player_impact": "background_resonance"
            },
            "gojo_sealed": {
                "trigger": "shibuya_incident",
                "description": "Gojo is sealed in the Prison Realm, leaving students on their own",
                "player_impact": "leadership_opportunity"
            }
        }
    
    def _setup_major_battles(self):
        """Set up major battles from the manga with dramatic elements."""
        self.major_battles = {
            "vs_finger_bearer": {
                "arc": StoryArc.FEARSOME_WOMB,
                "enemy": "Special Grade Finger Bearer",
                "phases": [
                    {
                        "description": "The curse emerges from its cocoon, a grotesque mass of flesh and bone",
                        "special_mechanics": ["curse_domain", "regeneration"]
                    },
                    {
                        "description": "The finger bearer reveals its full power, domain begins manifesting", 
                        "special_mechanics": ["partial_domain", "enhanced_strength"]
                    }
                ],
                "victory_conditions": ["reduce_hp_to_25%", "team_combination_attack"],
                "dramatic_moments": [
                    "sukuna_finger_resonance",
                    "yuji_near_death",
                    "team_bond_awakening"
                ]
            },
            "vs_hanami": {
                "arc": StoryArc.KYOTO_GOODWILL_EVENT,
                "enemy": "Special Grade Curse Hanami",
                "phases": [
                    {
                        "description": "Hanami emerges to test the students' strength",
                        "special_mechanics": ["plant_manipulation", "cursed_buds"]
                    },
                    {
                        "description": "Hanami gets serious, revealing nature's wrath",
                        "special_mechanics": ["forest_domain", "massive_growth"]
                    },
                    {
                        "description": "Todo and Yuji's combination attack",
                        "special_mechanics": ["boogie_woogie_combos", "black_flash_chain"]
                    }
                ],
                "victory_conditions": ["force_retreat"],
                "dramatic_moments": [
                    "todo_yuji_friendship",
                    "black_flash_awakening", 
                    "gojo_arrival"
                ]
            },
            "shibuya_special_grades": {
                "arc": StoryArc.SHIBUYA_INCIDENT,
                "enemy": "Multiple Special Grade Curses",
                "phases": [
                    {
                        "description": "Coordinated assault by Jogo, Hanami, and Choso",
                        "special_mechanics": ["multiple_enemies", "environmental_destruction"]
                    },
                    {
                        "description": "Gojo enters the battle",
                        "special_mechanics": ["limitless_techniques", "domain_expansion"]
                    },
                    {
                        "description": "The trap is sprung - Prison Realm activation",
                        "special_mechanics": ["sealing_mechanics", "time_limit"]
                    }
                ],
                "victory_conditions": ["survive_until_gojo_sealed"],
                "dramatic_moments": [
                    "civilian_casualties",
                    "gojo_overwhelmed_by_memories",
                    "prison_realm_success"
                ]
            }
        }
    
    def get_current_scene(self, game_state) -> Dict[str, Any]:
        """Get the current scene based on story progress."""
        # Determine current scene based on arc and progress
        scene_key = self._determine_current_scene(game_state)
        return self.manga_scenes.get(scene_key, self._get_default_scene())
    
    def _determine_current_scene(self, game_state) -> str:
        """Determine which scene should be displayed based on game state."""
        chapter = game_state.current_chapter
        flags = game_state.story_flags
        
        if chapter <= 2:
            if "met_classmates" not in flags:
                return "intro_arrival"
            elif "met_gojo" not in flags:
                return "intro_gojo_meeting"
        elif chapter <= 5:
            if "fearsome_womb_started" not in flags:
                return "fearsome_womb_mission"
            elif "sukuna_encountered" not in flags:
                return "sukuna_awakening"
        elif chapter <= 10:
            if "kyoto_event_started" not in flags:
                return "kyoto_arrival"
        elif chapter <= 20:
            if "shibuya_incident_started" not in flags:
                return "shibuya_halloween"
        
        return "default_exploration"
    
    def _get_default_scene(self) -> Dict[str, Any]:
        """Return a default exploration scene."""
        return {
            "title": "Tokyo Jujutsu High - Daily Life",
            "description": "Continue your training and daily life at the school.",
            "choices": [
                {
                    "text": "Train with classmates",
                    "consequences": {"experience": 50, "relationships": {"yuji": 5, "megumi": 5, "nobara": 5}}
                },
                {
                    "text": "Study cursed techniques",
                    "consequences": {"traits": {"analytical": 10}, "technique_progress": True}
                },
                {
                    "text": "Explore Tokyo",
                    "consequences": {"experience": 25, "story_flags": {"explored_tokyo": True}}
                }
            ]
        }
    
    def process_choice_consequences(self, choice_consequences: Dict[str, Any], game_state) -> Dict[str, Any]:
        """Process the consequences of a player choice."""
        result = {"message": "", "effects": []}
        
        # Handle trait changes
        if "traits" in choice_consequences:
            for trait_name, change in choice_consequences["traits"].items():
                trait = next((t for t in Trait if t.value.lower() == trait_name.lower()), None)
                if trait and game_state.player:
                    game_state.player.modify_trait(trait, change)
                    result["effects"].append(f"Trait {trait.value} modified by {change}")
        
        # Handle relationship changes
        if "relationships" in choice_consequences:
            for npc, change in choice_consequences["relationships"].items():
                game_state.update_relationship(npc, change)
                result["effects"].append(f"Relationship with {npc.title()} changed by {change}")
        
        # Handle morality changes
        if "morality" in choice_consequences and game_state.player and game_state.player.morality:
            for aspect, change in choice_consequences["morality"].items():
                game_state.player.morality.modify_morality(aspect, change)
                result["effects"].append(f"Morality {aspect} changed by {change}")
        
        # Handle story flags
        if "story_flags" in choice_consequences:
            for flag, value in choice_consequences["story_flags"].items():
                game_state.add_story_flag(flag, value)
                result["effects"].append(f"Story flag set: {flag}")
        
        # Handle combat triggers
        if "combat" in choice_consequences:
            result["combat"] = True
            result["enemy_type"] = choice_consequences.get("enemy_type", "generic_curse")
        
        # Handle experience gain
        if "experience" in choice_consequences:
            if game_state.player:
                game_state.player.gain_experience(choice_consequences["experience"])
                result["effects"].append(f"Gained {choice_consequences['experience']} experience")
        
        # Handle technique unlocks
        if "technique_unlock" in choice_consequences:
            result["technique_unlock"] = choice_consequences["technique_unlock"]
            result["effects"].append(f"New technique available: {choice_consequences['technique_unlock']}")
        
        return result