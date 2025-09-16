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
                    "courtyard": "The main courtyard with cherry blossom trees and meditation stones.",
                    "training_grounds": "Where students practice combat techniques and spar with cursed spirits.",
                    "library": "Contains ancient texts about cursed spirits, forbidden techniques, and historical records.",
                    "dormitories": "Student living quarters with communal areas and private study rooms.",
                    "teacher_offices": "Faculty offices and meeting rooms where missions are planned.",
                    "underground_vault": "Hidden basement containing dangerous cursed objects and sealed artifacts.",
                    "rooftop_observatory": "High vantage point for observing cursed energy fluctuations across the city."
                },
                "npcs": ["gojo", "nanami", "yuji", "megumi", "nobara", "shoko"],
                "secrets": ["hidden_technique_scroll", "old_mission_records", "ancient_binding_contract", "master_key"]
            },
            
            "shibuya": {
                "name": "Shibuya District",
                "description": "A busy district transformed into a battleground against cursed spirits.",
                "areas": {
                    "shibuya_crossing": "The famous intersection, now a vortex of cursed energy.",
                    "shopping_district": "Abandoned shops harboring powerful curse nests and lost artifacts.",
                    "subway_station": "Underground tunnels with dangerous curses and hidden passages.",
                    "high_rise_buildings": "Tall buildings offering strategic advantages and aerial combat opportunities.",
                    "sewers": "Dark underground network crawling with evolved cursed spirits.",
                    "radio_tower": "Communication hub surrounded by electromagnetic cursed energy."
                },
                "npcs": ["injured_civilians", "cursed_spirit_users", "resistance_fighters"],
                "secrets": ["hidden_passage", "powerful_curse_tools", "emergency_cache", "dimensional_anchor"]
            },
            
            "kyoto_school": {
                "name": "Kyoto Jujutsu High",
                "description": "The traditional rival school with ancient philosophies and powerful techniques.",
                "areas": {
                    "main_hall": "Traditional Japanese architecture and ceremonial chambers.",
                    "zen_garden": "Peaceful area for meditation and cursed energy cultivation.",
                    "sparring_dojo": "Where Kyoto students train in traditional combat forms.",
                    "artifact_vault": "Ancient cursed tools and legendary relics from the Heian period.",
                    "tea_house": "Meeting place for formal discussions and political negotiations.",
                    "mountain_path": "Hiking trail leading to hermit caves and natural cursed energy springs."
                },
                "npcs": ["todo", "mai", "momo", "noritoshi", "yaga_kyoto", "elder_council"],
                "secrets": ["ancient_technique_manual", "forbidden_cursed_tool", "succession_scroll", "treaty_documents"]
            },
            
            "cursed_forest": {
                "name": "The Whispering Woods",
                "description": "An ancient forest where cursed energy has accumulated for centuries, creating twisted ecosystems.",
                "areas": {
                    "entrance_grove": "Seemingly normal trees that test visitors' resolve and cursed energy sensitivity.",
                    "thorn_maze": "Labyrinthine paths lined with cursed thorns that react to negative emotions.",
                    "spirit_sanctuary": "Sacred grove where benevolent nature spirits dwell and teach ancient wisdom.",
                    "cursed_lake": "Dark waters that reflect not your image, but your deepest fears and regrets.",
                    "elder_tree": "Massive ancient tree serving as a nexus for all cursed energy in the forest.",
                    "hunter_camps": "Abandoned camps of cursed spirit hunters with valuable equipment and journals.",
                    "void_clearing": "Unnatural clearing where reality seems thin and other dimensions bleed through."
                },
                "npcs": ["forest_guardian", "lost_hunter", "hermit_sage", "dryad_spirits"],
                "secrets": ["nature_technique_codex", "spirit_communication_ritual", "dimensional_compass", "life_essence_crystal"]
            },
            
            "underground_city": {
                "name": "The Forgotten Depths",
                "description": "Ancient underground civilization buried beneath modern Tokyo, filled with pre-modern cursed techniques.",
                "areas": {
                    "entrance_catacombs": "Bone-lined tunnels marking the boundary between the modern and ancient worlds.",
                    "crystal_caverns": "Glowing chambers where cursed energy crystallizes into physical form.",
                    "ruined_temples": "Sacred spaces dedicated to forgotten deities of cursed energy.",
                    "underground_market": "Hidden bazaar where rare cursed items and forbidden knowledge are traded.",
                    "throne_chamber": "Seat of the ancient rulers who first codified cursed energy manipulation.",
                    "training_amphitheater": "Circular arena where ancient sorcerers tested their most dangerous techniques.",
                    "library_ruins": "Collapsed archive containing pre-historic cursed technique research."
                },
                "npcs": ["ancient_keeper", "cursed_merchant", "underground_exile", "stone_guardian"],
                "secrets": ["primordial_technique_tablet", "ancient_crown", "binding_chains", "reality_anchor"]
            },
            
            "sky_fortress": {
                "name": "Celestial Observatory",
                "description": "A floating structure created by master sorcerers to study cursed energy from above the earthly realm.",
                "areas": {
                    "landing_platform": "Where aerial vehicles dock and visitors first experience the fortress's unique energy.",
                    "observation_deck": "Glass-enclosed area offering panoramic views and cursed energy monitoring equipment.",
                    "research_laboratories": "Advanced facilities for studying the interaction between cosmic and cursed energies.",
                    "meditation_spheres": "Floating chambers that amplify cursed energy and enable advanced training.",
                    "star_map_chamber": "Room containing detailed maps of cursed energy flows across the planet.",
                    "commander_quarters": "Living spaces for the elite sorcerers who maintain the fortress.",
                    "energy_core": "The powerful heart of the fortress that keeps it airborne through pure cursed energy."
                },
                "npcs": ["sky_commander", "stellar_researcher", "cloud_navigator", "wind_spirit"],
                "secrets": ["celestial_technique_manual", "star_compass", "gravity_defiance_core", "cosmic_resonator"]
            },
            
            "temporal_ruins": {
                "name": "Chronos Sanctum",
                "description": "Mysterious ruins where time flows differently, containing powerful temporal cursed techniques.",
                "areas": {
                    "time_gate_entrance": "Portal-like structure where visitors experience temporal displacement effects.",
                    "past_echoes_hall": "Chamber that shows glimpses of historical events and ancient battles.",
                    "future_glimpse_tower": "Tall spire from which possible futures can be observed and studied.",
                    "temporal_workshop": "Laboratory where time-based cursed tools and artifacts were created.",
                    "paradox_chamber": "Dangerous room where multiple timelines intersect and reality becomes unstable.",
                    "chrono_library": "Archive containing records of events across multiple timelines.",
                    "eternal_garden": "Outdoor space where plants exist in permanent temporal loops."
                },
                "npcs": ["time_keeper", "temporal_scholar", "chronos_guardian", "timeline_refugee"],
                "secrets": ["temporal_mastery_scroll", "paradox_stabilizer", "time_lock_mechanism", "causality_anchor"]
            },
            
            "void_nexus": {
                "name": "The Abyssal Gateway",
                "description": "A dangerous interdimensional hub where the barriers between realities are thinnest.",
                "areas": {
                    "stability_platform": "The only safe zone, reinforced with powerful barrier techniques.",
                    "dimensional_fissures": "Tears in reality leading to unknown realms and parallel dimensions.",
                    "void_research_station": "Abandoned facility where scientists studied interdimensional phenomena.",
                    "mirror_maze": "Labyrinth of reflective surfaces showing alternate versions of reality.",
                    "gravity_wells": "Areas where space-time is warped, creating unusual gravitational effects.",
                    "entity_containment": "Secure chambers once used to study beings from other dimensions.",
                    "nexus_core": "The central point where all dimensional pathways converge."
                },
                "npcs": ["void_researcher", "dimension_exile", "reality_anchor", "chaos_entity"],
                "secrets": ["dimensional_key", "reality_stabilizer", "void_protection_ward", "interdimensional_map"]
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
    
    def explore_location(self, game_state, location_key: str, area_key: str = None):
        """Handle location exploration with dynamic content generation."""
        if location_key not in self.exploration_locations:
            return {"error": "Location not found"}
        
        location = self.exploration_locations[location_key]
        
        # Update current location
        game_state.current_location = location["name"]
        if area_key and area_key in location["areas"]:
            game_state.current_area = area_key
        
        # Create exploration checkpoint
        checkpoint_desc = f"Exploring {location['name']}"
        if area_key:
            checkpoint_desc += f" - {area_key.replace('_', ' ').title()}"
        game_state.create_exploration_checkpoint(location["name"], area_key or "main", checkpoint_desc)
        
        # Generate exploration content
        exploration_result = {
            "location": location["name"],
            "description": location["description"],
            "current_area": area_key,
            "available_areas": list(location["areas"].keys()),
            "area_descriptions": location["areas"],
            "npcs": location.get("npcs", []),
            "actions": []
        }
        
        # Add area-specific content
        if area_key and area_key in location["areas"]:
            exploration_result["area_description"] = location["areas"][area_key]
            
            # Check for secrets in this area
            for secret in location.get("secrets", []):
                if not game_state.discovered_secrets or f"{location['name']}:{secret}" not in game_state.discovered_secrets:
                    if self._should_reveal_secret(game_state, secret):
                        exploration_result["actions"].append({
                            "text": f"Investigate {secret.replace('_', ' ')}",
                            "type": "discover_secret",
                            "secret": secret
                        })
        
        # Add movement actions
        for area, desc in location["areas"].items():
            if area != area_key:
                exploration_result["actions"].append({
                    "text": f"Go to {area.replace('_', ' ').title()}",
                    "type": "move_area",
                    "target_area": area
                })
        
        # Add technique training opportunities based on location
        training_techniques = self._get_location_techniques(location_key, game_state)
        if training_techniques:
            for technique in training_techniques:
                exploration_result["actions"].append({
                    "text": f"Train {technique} technique",
                    "type": "train_technique",
                    "technique": technique
                })
        
        return exploration_result
    
    def _should_reveal_secret(self, game_state, secret_name: str) -> bool:
        """Determine if a secret should be revealed based on player progress."""
        import random
        base_chance = 0.3
        
        # Increase chance based on player level
        if game_state.player:
            level_bonus = game_state.player.level * 0.02
            return random.random() < (base_chance + level_bonus)
        
        return random.random() < base_chance
    
    def _get_location_techniques(self, location_key: str, game_state) -> list:
        """Get techniques that can be learned at this location."""
        location_techniques = {
            "cursed_forest": ["thorn_guardians", "spirit_mirage", "harmonic_resonance"],
            "underground_city": ["soul_pierce", "entropy_manipulation", "dimensional_rift"],
            "sky_fortress": ["time_dilation", "astral_projection", "quantum_shift"],
            "temporal_ruins": ["time_dilation", "entropy_manipulation", "eternal_nexus"],
            "void_nexus": ["dimensional_rift", "void_grasp", "voidborne_cathedral"]
        }
        
        available = location_techniques.get(location_key, [])
        if not game_state.player:
            return []
        
        # Filter by player level and existing techniques
        player_techniques = [t.name.lower().replace(" ", "_").replace(":", "").replace("-", "_") for t in game_state.player.techniques]
        return [tech for tech in available if tech not in player_techniques and game_state.player.level >= 10]