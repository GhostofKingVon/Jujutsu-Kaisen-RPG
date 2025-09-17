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
        
        # Post-Shibuya Aftermath
        self.story_scenes["post_shibuya"] = StoryScene(
            "After the Shibuya Incident",
            """The Shibuya Incident is over, but the cost has been devastating. Gojo Satoru 
has been sealed away, countless civilians are dead, and the jujutsu world is in chaos. 
You survived the nightmare, but the scars run deep.

As you return to Tokyo Jujutsu High, the weight of what happened presses down on you. 
The other survivors look as haunted as you feel. The world has changed forever, and 
there's a sense that worse things are coming.

Principal Yaga calls for an emergency meeting of all surviving sorcerers.""",
            [
                StoryChoice(
                    "Focus on helping other survivors cope",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 10},
                        "relationships": {"yuji": 10, "megumi": 10, "nobara": 10},
                        "story_flags": {"survivor_support": True},
                        "next_scene": "post_shibuya_support"
                    }
                ),
                StoryChoice(
                    "Demand to know the plan for rescuing Gojo",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.AGGRESSIVE: 10},
                        "story_flags": {"rescue_gojo_priority": True},
                        "next_scene": "post_shibuya_rescue_planning"
                    }
                ),
                StoryChoice(
                    "Analyze what went wrong and how to prevent it",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10},
                        "story_flags": {"incident_analysis": True},
                        "next_scene": "post_shibuya_analysis"
                    }
                )
            ],
            "Tokyo Jujutsu High - Main Hall"
        )
        
        # Post-Shibuya Support Path
        self.story_scenes["post_shibuya_support"] = StoryScene(
            "Supporting Fellow Survivors",
            """You spend your time helping your fellow survivors process the trauma of 
Shibuya. Yuji struggles with the guilt over Sukuna's rampage, Megumi has withdrawn 
into himself, and others deal with their own wounds.

Your compassionate approach helps create bonds that will be crucial in the 
difficult times ahead. But even as you help others heal, you know that this 
is only the beginning of a much larger conflict.""",
            [
                StoryChoice(
                    "Continue building these relationships",
                    {
                        "traits": {Trait.COMPASSIONATE: 10},
                        "relationships": {"yuji": 15, "megumi": 15, "nobara": 15},
                        "next_scene": "culling_games_introduction"
                    }
                ),
                StoryChoice(
                    "Suggest group training to stay prepared",
                    {
                        "traits": {Trait.PROTECTIVE: 10, Trait.FOCUSED: 5},
                        "story_flags": {"group_training_leader": True},
                        "next_scene": "culling_games_introduction"
                    }
                )
            ],
            "Tokyo Jujutsu High - Student Lounge"
        )
        
        # Post-Shibuya Rescue Planning Path
        self.story_scenes["post_shibuya_rescue_planning"] = StoryScene(
            "Planning Gojo's Rescue",
            """Your determination to rescue Gojo catches the attention of the higher-ups. 
Principal Yaga explains that the Prison Realm is nearly impossible to open, and 
they're exploring every option.

However, your insistence on action over mourning marks you as someone willing to 
take risks for the greater good. This reputation will follow you into the trials ahead.""",
            [
                StoryChoice(
                    "Volunteer for the most dangerous missions",
                    {
                        "traits": {Trait.DETERMINED: 10, Trait.RECKLESS: 5},
                        "story_flags": {"high_risk_volunteer": True},
                        "next_scene": "culling_games_introduction"
                    }
                ),
                StoryChoice(
                    "Offer to research Prison Realm weaknesses",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 5},
                        "story_flags": {"prison_realm_researcher": True},
                        "next_scene": "culling_games_introduction"
                    }
                )
            ],
            "Tokyo Jujutsu High - Principal's Office"
        )
        
        # Post-Shibuya Analysis Path
        self.story_scenes["post_shibuya_analysis"] = StoryScene(
            "Analyzing the Shibuya Incident",
            """Your analytical approach to understanding what went wrong impresses the 
faculty. You spend hours reviewing footage, survivor testimonies, and cursed spirit 
behavior patterns from the incident.

Your insights reveal important tactical information that could prove crucial in 
future encounters. The higher-ups take note of your strategic mind, marking you 
as someone they can rely on for planning.""",
            [
                StoryChoice(
                    "Share your findings with other students",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.PROTECTIVE: 5},
                        "story_flags": {"tactical_teacher": True},
                        "next_scene": "culling_games_introduction"
                    }
                ),
                StoryChoice(
                    "Keep researching enemy weaknesses",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 10},
                        "story_flags": {"enemy_researcher": True},
                        "next_scene": "culling_games_introduction"
                    }
                )
            ],
            "Tokyo Jujutsu High - Research Library"
        )
        
        # Culling Games Introduction
        self.story_scenes["culling_games_introduction"] = StoryScene(
            "The Culling Games Begin",
            """Two months have passed since Shibuya, and the jujutsu world remains in chaos. 
Today, something unprecedented happens: barriers begin forming across Japan, trapping 
millions of people inside designated colonies.

Kenjaku's voice echoes across the nation through cursed energy, announcing the 
Culling Games. The rules are simple but terrifying:

1. Players must kill other players within 19 days of entering a colony
2. Players who break this rule will have their cursed technique removed
3. Players can add new rules by spending 100 points
4. Killing a player grants 5 points; killing a non-player grants 1 point

You and your fellow sorcerers realize this is Kenjaku's true plan - a death game 
designed to optimize cursed energy and push evolution of cursed techniques. 

As emergency meetings are called, you know your next decision will determine your 
role in this apocalyptic scenario.""",
            [
                StoryChoice(
                    "Volunteer to enter a colony immediately",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.RECKLESS: 10},
                        "story_flags": {"early_entry": True, "volunteer_scout": True},
                        "next_scene": "culling_games_colony_choice"
                    }
                ),
                StoryChoice(
                    "Suggest gathering intelligence on the colonies first",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10},
                        "story_flags": {"intelligence_priority": True},
                        "next_scene": "culling_games_intelligence"
                    }
                ),
                StoryChoice(
                    "Focus on protecting civilians still outside the barriers",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 10},
                        "story_flags": {"civilian_protector": True},
                        "next_scene": "culling_games_civilian_protection"
                    }
                ),
                StoryChoice(
                    "Propose finding a way to add favorable rules",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 10},
                        "story_flags": {"rule_strategist": True},
                        "next_scene": "culling_games_rule_strategy"
                    }
                )
            ],
            "Tokyo Jujutsu High - Emergency Command Center"
        )
        
        # Colony Choice Path
        self.story_scenes["culling_games_colony_choice"] = StoryScene(
            "Choosing Your Colony",
            """Your decision to enter the Culling Games early is met with both admiration 
and concern. The higher-ups present you with three colony options, each with 
different strategic importance:

**Tokyo Colony No. 1**: The most dangerous, containing ancient sorcerers and the 
highest concentration of players. High risk, high reward.

**Sendai Colony**: Home to several powerful modern sorcerers, including rumors of 
someone called the 'Disaster Flames.' Moderate risk with key strategic value.

**Tokyo Colony No. 2**: Less populated but containing several non-player cursed 
spirits. Lower immediate risk but unknown long-term threats.

Your choice will determine which powerful players you encounter and which 
strategic objectives you can pursue.""",
            [
                StoryChoice(
                    "Enter Tokyo Colony No. 1 - Face the strongest players",
                    {
                        "traits": {Trait.DETERMINED: 10, Trait.RECKLESS: 15},
                        "story_flags": {"tokyo_1_entry": True},
                        "next_scene": "tokyo_colony_1_entry"
                    }
                ),
                StoryChoice(
                    "Enter Sendai Colony - Pursue strategic objectives",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 10},
                        "story_flags": {"sendai_entry": True},
                        "next_scene": "sendai_colony_entry"
                    }
                ),
                StoryChoice(
                    "Enter Tokyo Colony No. 2 - Start with reconnaissance",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.ANALYTICAL: 5},
                        "story_flags": {"tokyo_2_entry": True},
                        "next_scene": "tokyo_colony_2_entry"
                    }
                )
            ],
            "Tokyo Jujutsu High - Strategy Room"
        )
        
        # Intelligence Gathering Path
        self.story_scenes["culling_games_intelligence"] = StoryScene(
            "Gathering Intelligence on the Colonies",
            """Your analytical approach proves invaluable as the team works to understand 
the Culling Games' true scope. Using drones, remote cursed energy sensing, and 
survivor testimonies, you help map out the colonies' layouts and identify key players.

Your intelligence reveals that several ancient sorcerers from the past have been 
awakened as players, their techniques evolved over centuries of existence. You also 
discover that some colonies have natural advantages or disadvantages based on their 
geographic locations.

Most importantly, you identify several high-value targets: players who might be 
reasoned with instead of fought, and strategic locations that could serve as 
safe zones or meeting points.""",
            [
                StoryChoice(
                    "Focus intelligence on ancient sorcerer patterns",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 10},
                        "story_flags": {"ancient_sorcerer_specialist": True},
                        "next_scene": "ancient_sorcerer_intelligence"
                    }
                ),
                StoryChoice(
                    "Map colony barrier weaknesses",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.CAUTIOUS: 10},
                        "story_flags": {"barrier_specialist": True},
                        "next_scene": "barrier_analysis"
                    }
                ),
                StoryChoice(
                    "Identify potential allied players",
                    {
                        "traits": {Trait.COMPASSIONATE: 10, Trait.ANALYTICAL: 10},
                        "story_flags": {"diplomacy_specialist": True},
                        "next_scene": "player_diplomacy_prep"
                    }
                )
            ],
            "Tokyo Jujutsu High - Intelligence Center"
        )
        
        # Tokyo Colony No. 1 Entry - The Most Dangerous Path
        self.story_scenes["tokyo_colony_1_entry"] = StoryScene(
            "Entering Tokyo Colony No. 1",
            """The barrier closes behind you with a finality that makes your skin crawl. 
Tokyo Colony No. 1 is a twisted version of downtown Tokyo, where familiar buildings 
stand but the atmosphere thrums with deadly cursed energy.

Almost immediately, you sense multiple powerful presences. This colony houses the 
strongest and most dangerous players, including ancient sorcerers who have survived 
for centuries.

As you navigate the eerily quiet streets, you encounter your first challenge: a 
player stands in your path. They wear traditional clothing that seems centuries old, 
and their cursed energy signature is unlike anything you've felt before.

"Another modern sorcerer," they say with ancient authority. "You children know 
nothing of true jujutsu. I am Hajime Kashimo, and I have waited four hundred years 
for a fight worthy of my time."

The legendary sorcerer's lightning crackles around his body, and you realize this 
isn't just your first encounter in the Culling Games - it might be your last.""",
            [
                StoryChoice(
                    "Accept his challenge head-on",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.AGGRESSIVE: 10},
                        "combat": True,
                        "enemy": "hajime_kashimo",
                        "story_flags": {"kashimo_direct_fight": True},
                        "next_scene": "kashimo_battle_outcome"
                    }
                ),
                StoryChoice(
                    "Try to reason with him about the true enemy",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.COMPASSIONATE: 10},
                        "story_flags": {"kashimo_diplomacy": True},
                        "next_scene": "kashimo_conversation"
                    }
                ),
                StoryChoice(
                    "Attempt to avoid the fight and escape",
                    {
                        "traits": {Trait.CAUTIOUS: 15, Trait.FOCUSED: 5},
                        "story_flags": {"kashimo_avoided": True},
                        "next_scene": "colony_exploration"
                    }
                ),
                StoryChoice(
                    "Challenge him to test your skills without killing intent",
                    {
                        "traits": {Trait.DETERMINED: 10, Trait.CAUTIOUS: 5},
                        "story_flags": {"kashimo_sparring": True},
                        "next_scene": "kashimo_sparring_match"
                    }
                )
            ],
            "Tokyo Colony No. 1 - Downtown District"
        )
        
        # Kashimo Battle Outcome
        self.story_scenes["kashimo_battle_outcome"] = StoryScene(
            "Aftermath of the Kashimo Battle",
            """The battle with Hajime Kashimo pushes you to your absolute limits. His 
lightning-based cursed technique is unlike anything you've faced - precise, 
devastating, and refined by four centuries of experience.

Whether you won or barely survived, the encounter teaches you something crucial 
about the Culling Games: the ancient sorcerers aren't just stronger, they're 
fundamentally different. Their techniques have evolved beyond modern understanding.

As you catch your breath, you notice someone watching from a nearby building. 
Another player, but their cursed energy signature suggests they might be more 
reasonable than Kashimo.

Your reputation in the colony has already begun to spread. How you handle your 
next encounters will determine whether you're seen as a threat to be eliminated 
or a force to be respected.""",
            [
                StoryChoice(
                    "Approach the watching player diplomatically",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.COMPASSIONATE: 5},
                        "story_flags": {"diplomatic_approach": True},
                        "next_scene": "player_diplomacy"
                    }
                ),
                StoryChoice(
                    "Use your victory reputation to your advantage",
                    {
                        "traits": {Trait.AGGRESSIVE: 10, Trait.FOCUSED: 5},
                        "story_flags": {"intimidation_reputation": True},
                        "next_scene": "reputation_advantage"
                    }
                ),
                StoryChoice(
                    "Find a place to recover and plan your next move",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.ANALYTICAL: 5},
                        "story_flags": {"strategic_retreat": True},
                        "next_scene": "tactical_planning"
                    }
                )
            ],
            "Tokyo Colony No. 1 - Aftermath Zone"
        )
        
        # Sendai Colony Entry
        self.story_scenes["sendai_colony_entry"] = StoryScene(
            "Entering Sendai Colony",
            """Sendai Colony feels different from what you expected. The barriers have 
transformed the city into a maze of twisted architecture and dangerous terrain. 
You can sense several powerful cursed energy signatures spread throughout the area.

Your intelligence suggested this colony contains both ancient sorcerers and modern 
players, creating a unique dynamic where old and new jujutsu clash constantly.

As you explore, you encounter signs of recent battles: destroyed buildings, scorch 
marks, and the lingering traces of powerful cursed techniques. This colony is 
active, with players already engaging in the deadly game.

Suddenly, you hear the sound of combat nearby. Through the debris, you see two 
players locked in an intense battle. One wields what appears to be cursed tools 
with incredible skill, while the other manipulates gravity itself.

You recognize one of them from the intelligence reports: Ryu Ishigori, a modern 
sorcerer with an immense cursed energy output. This could be your chance to 
observe high-level technique usage or potentially intervene to make an ally.""",
            [
                StoryChoice(
                    "Intervene to stop the fight and propose an alliance",
                    {
                        "traits": {Trait.COMPASSIONATE: 10, Trait.DETERMINED: 10},
                        "story_flags": {"intervention_attempt": True},
                        "next_scene": "sendai_intervention"
                    }
                ),
                StoryChoice(
                    "Observe the battle to learn their techniques",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10},
                        "story_flags": {"technique_analysis": True},
                        "next_scene": "sendai_observation"
                    }
                ),
                StoryChoice(
                    "Wait for the battle to end and approach the winner",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.FOCUSED: 10},
                        "story_flags": {"winner_approach": True},
                        "next_scene": "sendai_post_battle"
                    }
                ),
                StoryChoice(
                    "Use the distraction to explore other areas",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.CAUTIOUS: 5},
                        "story_flags": {"exploration_priority": True},
                        "next_scene": "sendai_exploration"
                    }
                )
            ],
            "Sendai Colony - Industrial District"
        )
        
        # Sukuna's Awakening - Major Plot Point
        self.story_scenes["sukuna_awakening"] = StoryScene(
            "The King of Curses Awakens",
            """The ground trembles beneath your feet as an overwhelming presence fills 
the colony. The air itself seems to thicken with malevolent cursed energy, and 
you feel a primal fear that reaches into your very soul.

Sukuna has taken control of Yuji's body.

From your position, you can see the King of Curses standing amid the destruction 
he's already caused. His presence warps reality itself, and every curse spirit 
in the area has either fled or been utterly destroyed by his mere existence.

"How boring," Sukuna's voice carries across the colony with casual cruelty. "These 
modern sorcerers are weak. Perhaps the ancient ones will provide better entertainment."

You realize you're witnessing a pivotal moment in the Culling Games. Sukuna's 
participation changes everything - not just the balance of power, but the very 
nature of the game itself. Players who were confident in their strength now face 
an opponent beyond their comprehension.

Your next decision could determine whether you survive this encounter and how the 
story of the Culling Games unfolds.""",
            [
                StoryChoice(
                    "Try to reach Yuji's consciousness within Sukuna",
                    {
                        "traits": {Trait.COMPASSIONATE: 20, Trait.DETERMINED: 15},
                        "story_flags": {"sukuna_yuji_attempt": True},
                        "next_scene": "sukuna_yuji_consciousness"
                    }
                ),
                StoryChoice(
                    "Observe Sukuna's techniques from a safe distance",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 15},
                        "story_flags": {"sukuna_observation": True},
                        "next_scene": "sukuna_technique_analysis"
                    }
                ),
                StoryChoice(
                    "Attempt to challenge Sukuna directly",
                    {
                        "traits": {Trait.RECKLESS: 25, Trait.DETERMINED: 15},
                        "story_flags": {"sukuna_direct_challenge": True},
                        "combat": True,
                        "enemy": "sukuna_avatar",
                        "next_scene": "sukuna_battle_outcome"
                    }
                ),
                StoryChoice(
                    "Rally other players to coordinate against Sukuna",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.PROTECTIVE: 10},
                        "story_flags": {"sukuna_coordination": True},
                        "next_scene": "sukuna_alliance_building"
                    }
                ),
                StoryChoice(
                    "Use the chaos to escape and warn others",
                    {
                        "traits": {Trait.CAUTIOUS: 20, Trait.PROTECTIVE: 10},
                        "story_flags": {"sukuna_escape_warn": True},
                        "next_scene": "sukuna_warning_mission"
                    }
                )
            ],
            "Colony Central Zone - Sukuna's Domain"
        )
        
        # Yuji Consciousness Scene
        self.story_scenes["sukuna_yuji_consciousness"] = StoryScene(
            "Reaching for Yuji's Soul",
            """Against all rational thought, you step forward and call out to Yuji's 
consciousness. Sukuna's four eyes turn toward you with amusement rather than anger.

"Interesting," the King of Curses muses. "You think you can reach the brat while 
I'm in control? Your courage borders on stupidity."

For a moment, you feel a flicker of something else - Yuji's presence, fighting 
desperately against Sukuna's control. The vessel's soul hasn't been completely 
suppressed, but the battle within is intense.

"He can hear you," Sukuna grins with cruel delight. "But he cannot respond. 
Shall I relay a message? Or would you prefer to join him in powerlessness?"

Your attempt to reach Yuji has caught Sukuna's attention, but whether this is 
a blessing or a curse remains to be seen. The King of Curses seems more 
interested in psychological torment than immediate violence.""",
            [
                StoryChoice(
                    "Continue trying to strengthen Yuji's will",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.DETERMINED: 10},
                        "story_flags": {"yuji_support_continued": True},
                        "next_scene": "yuji_soul_battle"
                    }
                ),
                StoryChoice(
                    "Challenge Sukuna's view of strength",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.ANALYTICAL: 5},
                        "story_flags": {"sukuna_philosophy_challenge": True},
                        "next_scene": "sukuna_philosophical_debate"
                    }
                ),
                StoryChoice(
                    "Ask Sukuna about his true goals in the Culling Games",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 5},
                        "story_flags": {"sukuna_goals_inquiry": True},
                        "next_scene": "sukuna_reveals_motives"
                    }
                ),
                StoryChoice(
                    "Withdraw respectfully to avoid further provocation",
                    {
                        "traits": {Trait.CAUTIOUS: 15, Trait.FOCUSED: 5},
                        "story_flags": {"sukuna_tactical_withdrawal": True},
                        "next_scene": "post_sukuna_planning"
                    }
                )
            ],
            "Colony Central Zone - Within Sukuna's Presence"
        )
        
        # Sukuna Technique Analysis
        self.story_scenes["sukuna_technique_analysis"] = StoryScene(
            "Analyzing the King of Curses",
            """From your concealed position, you observe Sukuna's casual demonstration of 
power. His cursed techniques are beyond anything in recorded history - spatial 
manipulation that cleaves through reality itself, fire techniques that burn with 
the heat of stars, and domain expansion that rewrites the laws of existence.

What strikes you most is the efficiency. Sukuna wastes no movement, no cursed 
energy. Every technique is perfectly calculated for maximum effect with minimal 
effort. This isn't just raw power - it's technique refined to absolute perfection.

You also notice something else: Sukuna seems to be testing the limits of Yuji's 
body. Despite his overwhelming power, he's constrained by his vessel's physical 
capabilities. This observation could be crucial intelligence.

As you watch, another player attempts to engage Sukuna. The ancient sorcerer's 
confidence evaporates in seconds as Sukuna's "Dismantle" technique reduces them 
to nothing without apparent effort.

Your analysis is interrupted when Sukuna's gaze turns in your direction. He knows 
you're watching, and his smile suggests he's aware of your analytical approach.""",
            [
                StoryChoice(
                    "Continue observing to gather more intelligence",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.RECKLESS: 5},
                        "story_flags": {"sukuna_extended_analysis": True},
                        "next_scene": "sukuna_advanced_techniques"
                    }
                ),
                StoryChoice(
                    "Retreat and document your findings",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10},
                        "story_flags": {"sukuna_intelligence_gathered": True},
                        "next_scene": "sukuna_intelligence_report"
                    }
                ),
                StoryChoice(
                    "Reveal yourself and ask to observe his techniques openly",
                    {
                        "traits": {Trait.DETERMINED: 10, Trait.ANALYTICAL: 10},
                        "story_flags": {"sukuna_open_observation": True},
                        "next_scene": "sukuna_teaching_moment"
                    }
                )
            ],
            "Colony Observation Point - Hidden Position"
        )
        
        # Ancient Sorcerer Encounter - Yorozu
        self.story_scenes["yorozu_encounter"] = StoryScene(
            "The Angel's Curse - Yorozu",
            """Deep within the colony, you encounter a presence that feels both ancient 
and fundamentally wrong. The woman before you appears young, but her cursed energy 
signature is impossibly old and complex.

"Another modern sorcerer," she says with a voice that carries the weight of 
centuries. "I am Yorozu, and I have waited a thousand years to create the perfect 
weapon for my beloved Sukuna."

Her cursed technique manifests as insect-like constructs that seem to shift between 
organic and mechanical forms. Each creation is perfectly adapted for its purpose, 
demonstrating a mastery of cursed technique construction that rivals domain expansion.

"I will test my latest creation on you," Yorozu continues with disturbing affection. 
"If you survive, perhaps you can deliver a message to Sukuna about my eternal love."

The air around you fills with her cursed constructs, each one analyzing your 
movements and adapting in real-time. This isn't just a battle - it's a laboratory 
experiment where you're the test subject.""",
            [
                StoryChoice(
                    "Focus on destroying her constructs methodically",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 10},
                        "combat": True,
                        "enemy": "yorozu_constructs",
                        "story_flags": {"yorozu_methodical_approach": True},
                        "next_scene": "yorozu_battle_analysis"
                    }
                ),
                StoryChoice(
                    "Try to disrupt her technique at its source",
                    {
                        "traits": {Trait.AGGRESSIVE: 15, Trait.FOCUSED: 10},
                        "combat": True,
                        "enemy": "yorozu_direct",
                        "story_flags": {"yorozu_direct_assault": True},
                        "next_scene": "yorozu_technique_disruption"
                    }
                ),
                StoryChoice(
                    "Attempt to reason with her about Sukuna's true nature",
                    {
                        "traits": {Trait.COMPASSIONATE: 10, Trait.ANALYTICAL: 10},
                        "story_flags": {"yorozu_sukuna_truth": True},
                        "next_scene": "yorozu_sukuna_revelation"
                    }
                ),
                StoryChoice(
                    "Use mobility to avoid her constructs and escape",
                    {
                        "traits": {Trait.CAUTIOUS: 15, Trait.FOCUSED: 5},
                        "story_flags": {"yorozu_escape": True},
                        "next_scene": "yorozu_pursuit"
                    }
                )
            ],
            "Colony Depths - Yorozu's Laboratory"
        )
        
        # Megumi's Dark Turn
        self.story_scenes["megumi_dark_turn"] = StoryScene(
            "Megumi's Descent",
            """You encounter Megumi in the colony, but something is terribly wrong. His 
cursed energy feels different - darker, more desperate. The trauma of Shibuya and 
the pressure of the Culling Games have pushed him toward a dangerous edge.

"I'm tired of being weak," Megumi says, his voice hollow. "Tired of watching 
people die because I hold back. Maybe it's time to stop restraining myself."

You can see the shadows around him writhing with unusual intensity. His Ten Shadows 
technique seems more aggressive, less controlled. He's walking the path toward 
unleashing his full potential, but at what cost?

"Sukuna said something to me once," Megumi continues. "About having the potential 
to surpass even Gojo-sensei. Maybe it's time to find out what that means."

This is a crucial moment. How you respond could determine whether Megumi finds 
the strength to continue fighting while remaining himself, or whether he crosses 
a line that transforms him into something else entirely.""",
            [
                StoryChoice(
                    "Remind him of what he's fighting to protect",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 10},
                        "relationships": {"megumi": 20},
                        "story_flags": {"megumi_protection_reminder": True},
                        "next_scene": "megumi_redemption_path"
                    }
                ),
                StoryChoice(
                    "Support his decision to become stronger",
                    {
                        "traits": {Trait.DETERMINED: 10, Trait.AGGRESSIVE: 5},
                        "relationships": {"megumi": 10},
                        "story_flags": {"megumi_power_support": True},
                        "next_scene": "megumi_power_embrace"
                    }
                ),
                StoryChoice(
                    "Challenge him to a fight to snap him out of it",
                    {
                        "traits": {Trait.AGGRESSIVE: 15, Trait.PROTECTIVE: 10},
                        "combat": True,
                        "enemy": "megumi_shadows",
                        "story_flags": {"megumi_shock_treatment": True},
                        "next_scene": "megumi_battle_revelation"
                    }
                ),
                StoryChoice(
                    "Analyze what's really driving his desperation",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 10},
                        "story_flags": {"megumi_analysis": True},
                        "next_scene": "megumi_psychological_insight"
                    }
                )
            ],
            "Colony - Abandoned Shopping District"
        )
        
        # Yuta's Return
        self.story_scenes["yuta_return"] = StoryScene(
            "The Return of Yuta Okkotsu",
            """A familiar cursed energy signature approaches through the colony - one that 
brings both relief and concern. Yuta Okkotsu has returned from his overseas training, 
but the young man who emerges from the shadows carries himself differently.

His cursed energy has grown exponentially, and there's a confidence in his movements 
that wasn't there before. More concerning is the way other cursed spirits in the 
area have simply... disappeared. Not destroyed, but fled from his presence.

"I heard about Gojo-sensei," Yuta says, his voice carrying a weight that wasn't 
there before. "And about what happened to everyone during Shibuya. I should have 
been here."

Rika's presence feels different too - more integrated, more terrifying. Yuta has 
clearly mastered aspects of his technique that were previously beyond his reach.

"I've learned things overseas," he continues. "Techniques, perspectives... methods 
that the higher-ups might not approve of. But if it means protecting everyone, 
I'll use whatever power is necessary."

The question becomes: how has Yuta's time away changed him, and what role will 
he play in the Culling Games?""",
            [
                StoryChoice(
                    "Ask about his overseas training experiences",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.COMPASSIONATE: 5},
                        "relationships": {"yuta": 15},
                        "story_flags": {"yuta_training_inquiry": True},
                        "next_scene": "yuta_training_revelation"
                    }
                ),
                StoryChoice(
                    "Suggest coordinating your efforts in the games",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.PROTECTIVE: 10},
                        "relationships": {"yuta": 10},
                        "story_flags": {"yuta_coordination": True},
                        "next_scene": "yuta_strategic_alliance"
                    }
                ),
                StoryChoice(
                    "Express concern about his changed demeanor",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.CAUTIOUS: 5},
                        "relationships": {"yuta": 20},
                        "story_flags": {"yuta_concern": True},
                        "next_scene": "yuta_emotional_check"
                    }
                ),
                StoryChoice(
                    "Challenge him to test his new abilities",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.AGGRESSIVE: 5},
                        "combat": True,
                        "enemy": "yuta_sparring",
                        "story_flags": {"yuta_power_test": True},
                        "next_scene": "yuta_abilities_demonstration"
                    }
                )
            ],
            "Colony - Meeting Point"
        )
        
        # Ancient Sorcerer - Uro Takako
        self.story_scenes["uro_takako_encounter"] = StoryScene(
            "The Sky Manipulator - Uro Takako",
            """The air itself becomes your enemy as you face Uro Takako, an ancient 
sorcerer whose mastery over spatial manipulation defies comprehension. Her cursed 
technique allows her to treat the sky itself as a tangible surface, bending and 
folding space with casual gestures.

"You modern sorcerers lack refinement," Uro declares as she literally peels back 
a section of air like fabric. "Your techniques are crude, your understanding 
shallow. Allow me to demonstrate what a thousand years of experience can achieve."

Her attacks come from impossible angles as she reshapes the battlefield itself. 
Traditional dodging becomes meaningless when your opponent can fold space to make 
distance irrelevant. Worse, her technique seems to have evolved beyond its original 
form - she's not just manipulating sky, but manipulating the concept of 'surface' 
itself.

"I was the captain of the Sun, Moon, and Stars Squad in the Heian era," she 
continues while casually deflecting your attacks by treating them as surfaces 
to be redirected. "We served the very same Sukuna you modern fools fear. Tell me, 
child, what have you learned in your brief years that could match centuries of 
warfare?"

This battle will test not just your power, but your ability to adapt to techniques 
that operate on fundamentally different principles than modern jujutsu.""",
            [
                StoryChoice(
                    "Study her technique to find spatial weaknesses",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15},
                        "story_flags": {"uro_technique_analysis": True},
                        "next_scene": "uro_spatial_weakness"
                    }
                ),
                StoryChoice(
                    "Overwhelm her with rapid-fire attacks",
                    {
                        "traits": {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 10},
                        "combat": True,
                        "enemy": "uro_takako",
                        "story_flags": {"uro_aggressive_assault": True},
                        "next_scene": "uro_overwhelming_offense"
                    }
                ),
                StoryChoice(
                    "Ask her about serving Sukuna in the Heian era",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 5},
                        "story_flags": {"uro_sukuna_history": True},
                        "next_scene": "uro_heian_revelations"
                    }
                ),
                StoryChoice(
                    "Attempt to turn her technique against itself",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.AGGRESSIVE: 10},
                        "story_flags": {"uro_technique_reversal": True},
                        "next_scene": "uro_spatial_reversal"
                    }
                )
            ],
            "Colony - Spatial Battlefield"
        )
        
        # Kenjaku's Revelation
        self.story_scenes["kenjaku_revelation"] = StoryScene(
            "The Mastermind's True Plan",
            """Your journey through the Culling Games has led you to this moment: a 
direct confrontation with Kenjaku, the ancient curse user whose plans have shaped 
the modern world's destruction.

"Impressive," Kenjaku says, his stolen face wearing an expression of genuine 
interest. "You've survived encounters with ancient sorcerers, witnessed Sukuna's 
awakening, and yet here you stand. You represent exactly what I hoped the Culling 
Games would produce."

The mastermind explains his true purpose: the games aren't just about evolution 
or entertainment. They're a massive ritual designed to merge humanity with cursed 
energy itself, creating a new form of existence where the boundary between human 
and curse dissolves entirely.

"You see," he continues, "Tengen's barriers have been collecting cursed energy 
for over a thousand years. The Culling Games are the key to releasing that power 
and integrating it with humanity's collective unconscious. Those who survive will 
become something beyond current understanding."

As he speaks, you realize the scope of his plan extends far beyond Japan. The 
Culling Games are a prototype for a global transformation that would fundamentally 
alter what it means to be human.

"The question becomes," Kenjaku concludes, "will you stand with evolution, or 
cling to humanity's current limitations?""",
            [
                StoryChoice(
                    "Reject his vision and fight for humanity's current form",
                    {
                        "traits": {Trait.DETERMINED: 20, Trait.PROTECTIVE: 15},
                        "combat": True,
                        "enemy": "kenjaku_avatar",
                        "story_flags": {"kenjaku_opposition": True},
                        "next_scene": "kenjaku_battle_humanity"
                    }
                ),
                StoryChoice(
                    "Question the ethics of forced evolution",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 15},
                        "story_flags": {"kenjaku_ethics_debate": True},
                        "next_scene": "kenjaku_philosophical_conflict"
                    }
                ),
                StoryChoice(
                    "Ask about alternatives that preserve choice",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 10},
                        "story_flags": {"kenjaku_alternative_inquiry": True},
                        "next_scene": "kenjaku_negotiation_attempt"
                    }
                ),
                StoryChoice(
                    "Demand to know what happens to those who can't adapt",
                    {
                        "traits": {Trait.COMPASSIONATE: 20, Trait.PROTECTIVE: 10},
                        "story_flags": {"kenjaku_casualty_concern": True},
                        "next_scene": "kenjaku_human_cost"
                    }
                )
            ],
            "Colony Central Core - Kenjaku's Domain"
        )
        
        # Sukuna's True Power Revealed
        self.story_scenes["sukuna_true_power"] = StoryScene(
            "The King's Domain",
            """The moment you've dreaded and anticipated arrives: Sukuna decides to reveal 
his true power. His Domain Expansion, "Malevolent Shrine," transforms the entire 
area into his personal killing field.

The shrine manifests as a grotesque structure of bones and cursed energy, with 
Sukuna seated at its center like a demon king holding court. Within this domain, 
his techniques are absolute - "Dismantle" and "Cleave" strike without the need 
for physical contact, cutting through anything that displeases him.

"This is what true power looks like," Sukuna declares, his voice echoing with 
the authority of centuries. "Not the desperate flailing of modern sorcerers, not 
the rigid traditions of ancient fools, but perfection refined through endless 
conflict."

You watch as other players who dared enter his domain are systematically 
dismantled. Their techniques, no matter how sophisticated, prove utterly 
inadequate against Sukuna's overwhelming superiority.

But something else becomes clear as you observe: Sukuna is enjoying this. The 
Culling Games aren't just a means to an end for him - they're entertainment, a 
chance to remind the world why he was feared as the King of Curses.

"Tell me, modern child," Sukuna addresses you directly, "do you still believe your 
era has produced anything worthy of my attention? Or shall I demonstrate why I 
remain unchallenged after a thousand years?""",
            [
                StoryChoice(
                    "Challenge his view that strength is the only measure of worth",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.COMPASSIONATE: 15},
                        "story_flags": {"sukuna_strength_philosophy": True},
                        "next_scene": "sukuna_strength_debate"
                    }
                ),
                StoryChoice(
                    "Ask about his relationship with the ancient sorcerers",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 10},
                        "story_flags": {"sukuna_ancient_history": True},
                        "next_scene": "sukuna_heian_era_stories"
                    }
                ),
                StoryChoice(
                    "Attempt to survive his domain through pure will",
                    {
                        "traits": {Trait.DETERMINED: 25, Trait.RECKLESS: 15},
                        "story_flags": {"sukuna_survival_attempt": True},
                        "next_scene": "sukuna_domain_survival"
                    }
                ),
                StoryChoice(
                    "Focus on protecting other players in the domain",
                    {
                        "traits": {Trait.PROTECTIVE: 20, Trait.COMPASSIONATE: 15},
                        "story_flags": {"sukuna_protection_focus": True},
                        "next_scene": "sukuna_protection_attempt"
                    }
                )
            ],
            "Sukuna's Domain - Malevolent Shrine"
        )
        
        # Culling Games Conclusion
        self.story_scenes["culling_games_conclusion"] = StoryScene(
            "The Games' End and New Beginnings",
            """The Culling Games reach their climax as the surviving players converge 
for the final confrontations. Your choices throughout the games have shaped not 
only your own development but the relationships and alliances that will determine 
the outcome.

Whether through combat, diplomacy, or strategic maneuvering, you've played a 
crucial role in how the games concluded. Ancient sorcerers have been defeated 
or reasoned with, Sukuna's rampage has been witnessed or survived, and Kenjaku's 
true plans have been exposed.

As the barriers finally begin to dissolve, the survivors emerge into a world 
forever changed. The Culling Games have demonstrated that the age of hidden 
jujutsu sorcery is over - cursed energy and its wielders are now part of the 
public consciousness.

Looking back on your experiences, you realize this was more than just a death 
game. It was a crucible that tested not just power, but character, adaptability, 
and the fundamental question of what it means to be human in a world where 
supernatural power exists.

The games may be over, but their consequences will ripple through society for 
generations. How you choose to use the strength, knowledge, and relationships 
you've gained will determine your role in the world that emerges from this chaos.""",
            [
                StoryChoice(
                    "Focus on helping rebuild jujutsu society",
                    {
                        "traits": {Trait.PROTECTIVE: 15, Trait.ANALYTICAL: 10},
                        "story_flags": {"rebuilding_focus": True},
                        "next_scene": "post_games_rebuilding"
                    }
                ),
                StoryChoice(
                    "Pursue the remaining threats from Kenjaku's plans",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.AGGRESSIVE: 10},
                        "story_flags": {"threat_pursuit": True},
                        "next_scene": "post_games_threat_hunting"
                    }
                ),
                StoryChoice(
                    "Work to integrate cursed energy knowledge with the public",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 10},
                        "story_flags": {"public_integration": True},
                        "next_scene": "post_games_integration"
                    }
                ),
                StoryChoice(
                    "Take time to process everything that happened",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.COMPASSIONATE: 10},
                        "story_flags": {"reflection_period": True},
                        "next_scene": "post_games_reflection"
                    }
                )
            ],
            "Post-Culling Games World"
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
        
        # Culling Games Ancient Sorcerers
        elif enemy_type == "hajime_kashimo":
            enemy = Enemy("Hajime Kashimo - The Lightning God", 300, 200, "legendary")
            enemy.ai_pattern = "aggressive"
            enemy.max_phases = 3
            enemy.phase_transition_messages = [
                "Kashimo's lightning intensifies! \"Finally, a worthy opponent!\"",
                "\"Let me show you four centuries of refined technique!\"",
                "\"This is what true lightning mastery looks like!\""
            ]
        
        elif enemy_type == "yorozu_constructs":
            enemy = Enemy("Yorozu's Cursed Constructs", 250, 180, "legendary")
            enemy.ai_pattern = "defensive"
            enemy.max_phases = 2
            enemy.phase_transition_messages = [
                "The constructs adapt and evolve!",
                "\"My perfect creations will not be defeated!\""
            ]
        
        elif enemy_type == "yorozu_direct":
            enemy = Enemy("Yorozu - The Angel's Curse", 280, 190, "legendary")
            enemy.ai_pattern = "mixed"
            enemy.max_phases = 3
            enemy.phase_transition_messages = [
                "Yorozu's technique becomes more sophisticated!",
                "\"I'll create the perfect weapon from this battle!\"",
                "\"For Sukuna's love, I'll surpass all limits!\""
            ]
        
        elif enemy_type == "uro_takako":
            enemy = Enemy("Uro Takako - Sky Manipulator", 320, 210, "legendary")
            enemy.ai_pattern = "defensive"
            enemy.max_phases = 2
            enemy.phase_transition_messages = [
                "Uro bends space itself to her will!",
                "\"The sky is my domain, child!\""
            ]
        
        elif enemy_type == "sukuna_avatar":
            enemy = Enemy("Sukuna - King of Curses (Suppressed)", 500, 300, "mythical")
            enemy.ai_pattern = "aggressive"
            enemy.max_phases = 4
            enemy.phase_transition_messages = [
                "Sukuna's true power begins to show...",
                "\"Boring. Let me try something more interesting.\"",
                "\"Domain Expansion: Malevolent Shrine!\"",
                "\"You've entertained me enough. Time to end this.\""
            ]
        
        elif enemy_type == "kenjaku_avatar":
            enemy = Enemy("Kenjaku - The Mastermind", 400, 250, "mythical")
            enemy.ai_pattern = "mixed"
            enemy.max_phases = 3
            enemy.phase_transition_messages = [
                "Kenjaku reveals more of his ancient techniques!",
                "\"Centuries of knowledge cannot be overcome so easily!\"",
                "\"I am evolution itself!\""
            ]
        
        # Modern Sorcerer Encounters
        elif enemy_type == "megumi_shadows":
            enemy = Enemy("Megumi Fushiguro (Ten Shadows)", 200, 150, "hard")
            enemy.ai_pattern = "defensive"
            enemy.max_phases = 2
            enemy.phase_transition_messages = [
                "Megumi's shadows grow more aggressive!",
                "\"I won't hold back anymore!\""
            ]
        
        elif enemy_type == "yuta_sparring":
            enemy = Enemy("Yuta Okkotsu (Returned)", 350, 220, "legendary")
            enemy.ai_pattern = "mixed"
            enemy.max_phases = 2
            enemy.phase_transition_messages = [
                "Yuta's overseas training shows!",
                "\"Rika, let's show them what we've learned!\""
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