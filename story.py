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
        self.current_scene = "character_background"
        self.story_scenes = {}
        self.exploration_locations = {}
        self._initialize_story()
        self._initialize_locations()
    
    def _initialize_story(self):
        """Initialize all story scenes."""
        
        # === ARC 1: TOKYO JUJUTSU HIGH INTRODUCTION ===
        
        # Character Background Selection
        background_choices = [
            StoryChoice(
                "You come from a long line of jujutsu sorcerers",
                {
                    "traits": {Trait.FOCUSED: 10, Trait.ANALYTICAL: 5},
                    "story_flags": {"sorcerer_heritage": True},
                    "relationships": {"megumi": 5},
                    "next_scene": "heritage_arrival"
                }
            ),
            StoryChoice(
                "You discovered your abilities recently after a traumatic curse encounter",
                {
                    "traits": {Trait.DETERMINED: 10, Trait.PROTECTIVE: 5},
                    "story_flags": {"recent_awakening": True},
                    "relationships": {"yuji": 5},
                    "next_scene": "awakened_arrival"
                }
            ),
            StoryChoice(
                "You've always been able to see curses but kept it secret",
                {
                    "traits": {Trait.CAUTIOUS: 10, Trait.COMPASSIONATE: 5},
                    "story_flags": {"hidden_sight": True},
                    "relationships": {"nobara": 5},
                    "next_scene": "secretive_arrival"
                }
            )
        ]
        
        self.story_scenes["character_background"] = StoryScene(
            "Your Journey to Jujutsu High",
            """Before you can understand where you're going, you must understand where you've been.
The path that led you to Tokyo Jujutsu High defines not just your past, but who you are as a 
person and as a potential jujutsu sorcerer.

The morning mist clings to the train windows as you travel toward your new life. In the 
reflection, you see not just your face, but the experiences that shaped you. The cursed world 
has always existed parallel to the normal one, but how did you first encounter it?

Your memories drift back to the moment that changed everything...""",
            background_choices,
            "Train to Tokyo"
        )
        
        # Heritage Path - Traditional Sorcerer Family
        self.story_scenes["heritage_arrival"] = StoryScene(
            "Legacy of Power",
            """The weight of generations rests on your shoulders as you approach Tokyo Jujutsu High.
Your family's reputation precedes you - a long line of distinguished sorcerers who have served
to protect humanity from cursed spirits for over three centuries.

Your grandmother's final words echo in your mind: "Power without wisdom is destruction, but 
wisdom without power is helplessness. Find the balance, child, as your ancestors have."

The imposing gates of the school bear familiar insignias - your great-grandfather helped 
establish this very institution. Students and faculty will have expectations, and your family
name carries both privilege and burden.

As you step through the barrier, you feel the ancient protective techniques woven into the 
very foundations - some of which bear your family's cursed energy signature. A few senior 
students notice your confident bearing and whisper among themselves.

Near the main courtyard, you see a commotion ahead where a fellow student has been cornered 
by a Grade 3 cursed spirit. Your family training kicks in immediately - assess, analyze, act.""",
            [
                StoryChoice(
                    "Use your family's traditional binding technique to immobilize the curse",
                    {
                        "traits": {Trait.FOCUSED: 15, Trait.ANALYTICAL: 5},
                        "next_scene": "heritage_technique_display",
                        "relationships": {"megumi": 15, "faculty": 10},
                        "story_flags": {"displayed_heritage_power": True}
                    }
                ),
                StoryChoice(
                    "Assist the student first, then deal with the curse",
                    {
                        "traits": {Trait.COMPASSIONATE: 10, Trait.PROTECTIVE: 10},
                        "next_scene": "heritage_compassionate_act",
                        "relationships": {"yuji": 10, "injured_student": 20},
                        "story_flags": {"prioritized_rescue": True}
                    }
                ),
                StoryChoice(
                    "Observe the situation to understand how the school handles such incidents",
                    {
                        "traits": {Trait.CAUTIOUS: 15, Trait.ANALYTICAL: 10},
                        "next_scene": "heritage_observation",
                        "relationships": {"faculty": 15},
                        "story_flags": {"strategic_patience": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Main Gate"
        )
        
        # Awakened Path - Recent Discovery
        self.story_scenes["awakened_arrival"] = StoryScene(
            "Baptism by Fire",
            """Just three months ago, you were living a normal life, completely oblivious to the 
world of cursed spirits and jujutsu sorcery. That changed in a single, terrifying night when 
your younger sibling was attacked by a curse that had been feeding off the negative emotions 
in your apartment building.

The memory still burns fresh in your mind - the moment when raw determination and desperate 
love manifested as cursed energy, allowing you to drive off the creature and save your sibling's
life. The Jujutsu High scouts found you three days later, sitting by your unconscious sibling's
hospital bed, still radiating unstable cursed energy.

"You have potential," the recruiter had said. "But potential without training is dangerous - 
to yourself and everyone around you."

Now, as you stand before the imposing buildings of Tokyo Jujutsu High, you feel both grateful
and overwhelmed. Unlike your classmates who may have grown up knowing about this world, 
everything is new and intimidating. The cursed energy barriers make your skin tingle, and you 
can sense the power radiating from every building.

Your phone buzzes - a text from your sibling: "Good luck, big brother/sister. I know you'll 
become the strongest and protect everyone like you protected me."

Suddenly, shouting erupts from the courtyard ahead. A student is cornered by what your crash-course
education tells you is a Grade 3 cursed spirit. Your body tenses - this is just like that night
three months ago.""",
            [
                StoryChoice(
                    "Rush in immediately - you can't let someone else get hurt like your sibling did",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.PROTECTIVE: 10},
                        "next_scene": "awakened_heroic_rush",
                        "relationships": {"yuji": 15, "injured_student": 15},
                        "story_flags": {"protective_instinct": True}
                    }
                ),
                StoryChoice(
                    "Try to remember your emergency training and approach strategically",
                    {
                        "traits": {Trait.FOCUSED: 10, Trait.DETERMINED: 10},
                        "next_scene": "awakened_trained_response",
                        "relationships": {"megumi": 10, "faculty": 10},
                        "story_flags": {"applied_training": True}
                    }
                ),
                StoryChoice(
                    "Call for help while moving to assist - you're still learning and backup is wise",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.COMPASSIONATE: 10},
                        "next_scene": "awakened_cautious_help",
                        "relationships": {"faculty": 15, "nobara": 5},
                        "story_flags": {"sought_guidance": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Entrance"
        )
        
        # Secretive Path - Hidden Abilities
        self.story_scenes["secretive_arrival"] = StoryScene(
            "A Life of Watching",
            """For as long as you can remember, you've seen things that others couldn't - shadowy 
figures lurking in corners, twisted shapes that seemed to feed on human misery, creatures that
existed just outside the normal world's perception. You learned early to keep quiet about it.

The first time you mentioned the "scary monsters" to your parents, the concerned looks and 
hushed conversations between adults taught you that this was something to hide. Throughout 
your childhood, you became an expert at pretending normalcy while navigating a world full of 
invisible threats.

You developed coping strategies: avoiding places where curses congregated, learning to control
your reactions when something particularly horrifying appeared, and most importantly, never 
letting anyone know what you could see. You became observant, empathetic, and careful - traits
that served you well in the normal world.

The invitation to Tokyo Jujutsu High came as both a relief and a terror. Relief, because finally
someone else could see what you saw and you weren't going insane. Terror, because it meant 
stepping out of the shadows and embracing a part of yourself you'd spent years hiding.

Now, walking through the school gates, you're overwhelmed by the sheer concentration of cursed
energy. It's like going from seeing the world in black and white to suddenly experiencing full
color. Every building, every barrier, every student radiates power that you can finally 
acknowledge.

The irony isn't lost on you when you see a cursed spirit cornering another student in the 
courtyard ahead. After years of avoiding such creatures, you're now expected to face them. 
Your instinct is to look away, pretend you don't see it, and walk past - but those days are over.""",
            [
                StoryChoice(
                    "Steel yourself and approach calmly - you've watched curses before, now learn from them",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10},
                        "next_scene": "secretive_analytical_approach",
                        "relationships": {"megumi": 15, "faculty": 5},
                        "story_flags": {"analytical_observer": True}
                    }
                ),
                StoryChoice(
                    "Feel empathy for the student's fear - you know exactly how terrifying this is",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 5},
                        "next_scene": "secretive_empathetic_rescue",
                        "relationships": {"yuji": 10, "injured_student": 20},
                        "story_flags": {"empathetic_connection": True}
                    }
                ),
                StoryChoice(
                    "Look for other students or faculty - surely they have protocols for this",
                    {
                        "traits": {Trait.CAUTIOUS: 15, Trait.FOCUSED: 5},
                        "next_scene": "secretive_protocol_seeking",
                        "relationships": {"nobara": 10, "faculty": 15},
                        "story_flags": {"protocol_conscious": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Student Path"
        )
        
        # Main Introduction Scene (after background selection)
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
        
        # Heritage Path Extended Scenes
        self.story_scenes["heritage_technique_display"] = StoryScene(
            "Family Techniques Revealed",
            """Your family's binding technique manifests with practiced precision - ethereal chains 
of cursed energy spiral around the Grade 3 curse, immobilizing it completely. The technique 
bears the distinctive golden glow that has been your family's signature for generations.

"Impressive," comes a voice from behind you. You turn to see Megumi Fushiguro, his divine dogs
flanking him. "That's the Celestial Binding technique, isn't it? I've read about your family's 
methods in the archives."

The other students watch in awe as you maintain perfect control of the binding while Megumi's
divine dogs dispatch the immobilized curse with clinical efficiency. A few senior students 
have gathered, whispering about bloodline techniques and family legacies.

"Clean technique, good control," Megumi continues, his tone neutral but respectful. "Though 
you held back quite a bit of power. Testing the school's response protocols?"

Your demonstration has clearly marked you as someone to watch. The injured student looks at 
you with gratitude and obvious intimidation - your family's reputation precedes you even here.""",
            [
                StoryChoice(
                    "Acknowledge Megumi's insight and offer to collaborate",
                    {
                        "traits": {Trait.FOCUSED: 10, Trait.ANALYTICAL: 5},
                        "relationships": {"megumi": 20, "faculty": 15},
                        "next_scene": "heritage_megumi_collaboration",
                        "story_flags": {"megumi_partnership": True}
                    }
                ),
                StoryChoice(
                    "Downplay your abilities and focus on the injured student",
                    {
                        "traits": {Trait.COMPASSIONATE: 10, Trait.PROTECTIVE: 5},
                        "relationships": {"injured_student": 25, "yuji": 10},
                        "next_scene": "heritage_humble_assistance",
                        "story_flags": {"humble_heritage": True}
                    }
                ),
                StoryChoice(
                    "Show confidence in your family's legacy while remaining approachable",
                    {
                        "traits": {Trait.FOCUSED: 10, Trait.DETERMINED: 5},
                        "relationships": {"megumi": 15, "nobara": 10, "faculty": 10},
                        "next_scene": "heritage_confident_introduction",
                        "story_flags": {"confident_heritage": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Courtyard"
        )
        
        # Awakened Path Extended Scenes  
        self.story_scenes["awakened_heroic_rush"] = StoryScene(
            "Instinct Over Training",
            """Without hesitation, you sprint toward the cornered student, raw determination flooding
your body with cursed energy. The memories of your sibling's attack fuel your movements - never 
again will you stand by while someone suffers.

Your cursed energy flares wildly, unrefined but powerful. The Grade 3 curse notices your 
approach and turns its attention to you, recognizing a threat. Its twisted form writhes with 
malevolent hunger, but you don't slow down.

"Hey, wait!" shouts a voice behind you. "You can't just charge in without—"

But you're already there, your fist connecting with the curse's form. Your untrained but 
emotionally-charged cursed energy tears into the spirit, dealing significant damage but leaving
you completely open to counterattack.

The curse's claws rake across your shoulder as Yuji Itadori appears beside you, his own fists
glowing with cursed energy. "That was reckless but brave!" he grins, even as he engages the 
curse. "Reminds me of my first day!"

Together, you overwhelm the curse through sheer determination rather than technique. The injured
student stares at both of you in amazement.""",
            [
                StoryChoice(
                    "Ask Yuji to teach you proper combat techniques",
                    {
                        "traits": {Trait.DETERMINED: 10, Trait.FOCUSED: 5},
                        "relationships": {"yuji": 25, "injured_student": 15},
                        "next_scene": "awakened_training_request",
                        "story_flags": {"yuji_mentorship": True}
                    }
                ),
                StoryChoice(
                    "Check on the injured student and apologize for the chaos",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 5},
                        "relationships": {"injured_student": 30, "yuji": 15},
                        "next_scene": "awakened_compassionate_followup",
                        "story_flags": {"student_focused": True}
                    }
                ),
                StoryChoice(
                    "Express concern about your wild cursed energy outburst",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.ANALYTICAL: 5},
                        "relationships": {"yuji": 15, "faculty": 10},
                        "next_scene": "awakened_energy_concern",
                        "story_flags": {"energy_awareness": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Courtyard"
        )
        
        # Secretive Path Extended Scenes
        self.story_scenes["secretive_analytical_approach"] = StoryScene(
            "The Observer Steps Forward",
            """Years of watching from the shadows have given you unique insights into cursed spirit
behavior. As you approach the scene calmly, you automatically catalog everything: the curse's
feeding pattern, its obvious blind spots, the optimal escape routes for the injured student.

Your measured approach catches the attention of Megumi Fushiguro, who was already moving to
intervene. He pauses, watching your careful analysis with growing interest.

"You're reading its behavior patterns," he observes quietly, positioning himself to support
your approach. "Most new students either run in blind or freeze up entirely."

The curse hasn't noticed you yet, focused as it is on terrorizing its current victim. Your
years of avoiding detection serve you well as you position yourself for maximum strategic
advantage. You can see exactly how this should unfold - not through overwhelming force, but
through understanding and precision.

"The way you move," Megumi continues, "you've been watching curses for a long time, haven't you?"

Your secret is becoming less secret by the moment, but perhaps that's not entirely a bad thing.""",
            [
                StoryChoice(
                    "Share your observations and coordinate a strategic approach with Megumi",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 10},
                        "relationships": {"megumi": 25, "faculty": 15},
                        "next_scene": "secretive_strategic_partnership",
                        "story_flags": {"megumi_strategist": True}
                    }
                ),
                StoryChoice(
                    "Use your knowledge to create a distraction while Megumi handles the curse",
                    {
                        "traits": {Trait.CAUTIOUS: 15, Trait.PROTECTIVE: 5},
                        "relationships": {"megumi": 15, "injured_student": 20},
                        "next_scene": "secretive_tactical_support",
                        "story_flags": {"tactical_support": True}
                    }
                ),
                StoryChoice(
                    "Reveal your lifetime of observation and ask for guidance on finally acting",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.COMPASSIONATE: 10},
                        "relationships": {"megumi": 20, "faculty": 10},
                        "next_scene": "secretive_revelation_moment",
                        "story_flags": {"observation_revelation": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Courtyard"
        )
        
        # === ARC 2: FIRST MISSION PATHS (EXPANDED) ===
        
        # Compassionate Path - Heavily Expanded
        self.story_scenes["first_mission_compassionate"] = StoryScene(
            "The Rescuer's Path",
            """You rush to help the injured student without hesitation. Your quick action 
surprises the cursed spirit, giving you the advantage. As you engage the curse, 
Yuji Itadori appears, impressed by your immediate response to help others.

"That was brave!" Yuji says with a grin. "You remind me of myself when I first got here."

The curse spirit snarls and prepares to attack both of you. The injured student, a second-year
named Takeshi, looks up at you with gratitude mixed with fear. Blood trickles from a gash on
his forehead, and his arm hangs at an awkward angle.

"I was just walking to the library," Takeshi gasps. "It came out of nowhere... I couldn't even
see it clearly until it grabbed me."

The curse spirit, resembling a twisted amalgamation of spider and human features, clicks its
mandibles menacingly. Its multiple eyes focus on you and Yuji, recognizing that its easy prey
has suddenly become protected.

"First rule of rescue," Yuji says, settling into a combat stance, "protect the victim first,
then deal with the threat. You've got good instincts."

The curse's cursed energy spikes, preparing for a desperate assault. You realize this moment
will define not just this encounter, but potentially your entire approach to being a jujutsu
sorcerer.""",
            [
                StoryChoice(
                    "Fight alongside Yuji while keeping yourself between the curse and Takeshi",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse",
                        "ally": "yuji",
                        "traits": {Trait.DETERMINED: 5, Trait.PROTECTIVE: 10},
                        "relationships": {"yuji": 15, "takeshi": 20},
                        "next_scene": "compassionate_protective_combat",
                        "story_flags": {"protective_fighter": True}
                    }
                ),
                StoryChoice(
                    "Focus entirely on getting Takeshi to safety while Yuji handles the curse",
                    {
                        "traits": {Trait.PROTECTIVE: 15, Trait.COMPASSIONATE: 10},
                        "relationships": {"takeshi": 30, "yuji": 10},
                        "next_scene": "compassionate_rescue_focus",
                        "story_flags": {"rescue_specialist": True}
                    }
                ),
                StoryChoice(
                    "Try to heal Takeshi's wounds while Yuji fights",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.FOCUSED: 5},
                        "relationships": {"takeshi": 25, "yuji": 10},
                        "next_scene": "compassionate_healing_attempt",
                        "story_flags": {"healing_instinct": True}
                    }
                ),
                StoryChoice(
                    "Coordinate with Yuji to end the fight quickly and minimize Takeshi's exposure",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse",
                        "ally": "yuji",
                        "traits": {Trait.ANALYTICAL: 10, Trait.PROTECTIVE: 5},
                        "relationships": {"yuji": 20, "takeshi": 15},
                        "next_scene": "compassionate_tactical_rescue",
                        "story_flags": {"tactical_rescuer": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # Compassionate Combat Resolution
        self.story_scenes["compassionate_protective_combat"] = StoryScene(
            "Shield of Determination",
            """You position yourself as a living barrier between the injured Takeshi and the 
advancing curse, your body radiating protective determination. Yuji nods approvingly as he 
flanks the creature from the opposite side.

"Nice positioning!" Yuji calls out as he delivers a powerful punch enhanced with cursed energy.
"You're thinking like a real sorcerer already!"

The curse spirit lashes out with spider-like appendages, but you deflect them away from Takeshi
with desperate precision. Your cursed energy, though untrained, responds to your protective 
instincts with surprising effectiveness. Each impact sends shockwaves through your body, but 
you hold your ground.

Takeshi watches in amazement as you weather the curse's assault. "I've never seen a first-year
fight so protectively," he whispers. "Most students focus on attacking or showing off their 
techniques."

Working in perfect synchronization with Yuji, you create openings for his more experienced 
attacks while ensuring no harm comes to the injured student. The curse spirit, frustrated by 
its inability to reach its original target, makes increasingly desperate attacks.

"Final push!" Yuji shouts. "Keep Takeshi covered, I'm going for the finishing blow!"

Your combined assault overwhelms the curse spirit, which dissolves into wisps of dark energy.
As the immediate danger passes, Takeshi looks at you with profound gratitude.""",
            [
                StoryChoice(
                    "Check on Takeshi's injuries immediately and help him to the infirmary",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 5},
                        "relationships": {"takeshi": 35, "medical_staff": 15},
                        "next_scene": "compassionate_medical_care",
                        "story_flags": {"medical_focus": True}
                    }
                ),
                StoryChoice(
                    "Ask Yuji about proper protective combat techniques",
                    {
                        "traits": {Trait.FOCUSED: 10, Trait.DETERMINED: 10},
                        "relationships": {"yuji": 25, "takeshi": 20},
                        "next_scene": "compassionate_training_discussion",
                        "story_flags": {"combat_improvement": True}
                    }
                ),
                StoryChoice(
                    "Thank Yuji for the teamwork and reflect on the importance of cooperation",
                    {
                        "traits": {Trait.COMPASSIONATE: 10, Trait.ANALYTICAL: 5},
                        "relationships": {"yuji": 25, "takeshi": 20},
                        "next_scene": "compassionate_teamwork_reflection",
                        "story_flags": {"cooperation_focused": True}
                    }
                ),
                StoryChoice(
                    "Express concern about your lack of proper training and ask for guidance",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.FOCUSED: 10},
                        "relationships": {"yuji": 20, "faculty": 15},
                        "next_scene": "compassionate_training_concern",
                        "story_flags": {"training_awareness": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # Rescue Focus Path
        self.story_scenes["compassionate_rescue_focus"] = StoryScene(
            "The Guardian's Priority",
            """While Yuji engages the curse spirit in direct combat, you immediately turn your full
attention to Takeshi's welfare. Your hands shake slightly as you assess his injuries, but your
voice remains calm and reassuring.

"Hey, Takeshi, right? I'm going to get you somewhere safe," you say, gently supporting his 
uninjured arm. "Can you walk if I help you?"

Behind you, the sounds of Yuji's battle with the curse echo through the training grounds - 
impacts, shouts, and the distinctive crack of cursed energy techniques. But your focus remains
entirely on the injured student.

Takeshi nods weakly. "I think so, but my arm... I think it might be broken."

"We'll get that looked at," you assure him, carefully helping him to his feet. "There's an 
infirmary in the main building, right?"

As you begin moving Takeshi toward safety, he looks back at the ongoing fight with worry. 
"Shouldn't we help him? That curse looked really strong..."

"Yuji can handle it," you reply with more confidence than you feel. "Right now, my job is 
making sure you're safe."

Your dedication to his welfare over the excitement of combat clearly moves Takeshi. Other 
students who have gathered to watch begin to take notice of your priorities.""",
            [
                StoryChoice(
                    "Stay with Takeshi at the infirmary and ensure he receives proper care",
                    {
                        "traits": {Trait.COMPASSIONATE: 20, Trait.PROTECTIVE: 10},
                        "relationships": {"takeshi": 40, "medical_staff": 20},
                        "next_scene": "compassionate_infirmary_dedication",
                        "story_flags": {"medical_dedication": True}
                    }
                ),
                StoryChoice(
                    "After getting Takeshi to safety, return to help Yuji if needed",
                    {
                        "traits": {Trait.PROTECTIVE: 15, Trait.DETERMINED: 5},
                        "relationships": {"takeshi": 25, "yuji": 15},
                        "next_scene": "compassionate_return_assistance",
                        "story_flags": {"balanced_protection": True}
                    }
                ),
                StoryChoice(
                    "Use this time to learn about campus safety protocols from medical staff",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.CAUTIOUS: 10},
                        "relationships": {"takeshi": 20, "medical_staff": 25, "faculty": 10},
                        "next_scene": "compassionate_protocol_learning",
                        "story_flags": {"safety_protocol_focus": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Path to Infirmary"
        )
        
        # Analytical Path - Heavily Expanded
        self.story_scenes["first_mission_analytical"] = StoryScene(
            "The Strategist's Path",
            """You take a measured approach, carefully observing the cursed spirit's behavior 
patterns and energy signature before acting. Your analytical mindset catches the attention 
of Megumi Fushiguro, who has been watching the situation develop from a strategic vantage point.

"Smart approach," Megumi says quietly, appearing beside you. "Most first-years either charge 
in blindly or freeze up completely. You're actually thinking."

The curse spirit - a grotesque amalgamation resembling a twisted librarian with multiple arms
and glowing red eyes - seems to be feeding off the injured student's fear and pain rather than
attempting to kill immediately. Its movements follow a predictable pattern: terrorize, feed,
pause, repeat.

"Grade 3, probably manifested from academic stress and fear of failure," Megumi observes, 
following your analytical gaze. "Notice how it's positioned near the library entrance? And 
see that weakness in its left side stance every third movement cycle?"

Your careful observation reveals multiple tactical advantages: the curse's predictable behavior,
its feeding-focused distraction, the injured student's position relative to escape routes, and
the environmental factors that could be used strategically.

"The question is," Megumi continues, "what do you do with that information?"

The injured student - you can see from his uniform it's a second-year named Takeshi - looks 
increasingly pale as the curse continues its psychological assault. Time is a factor, but 
rushing in without a plan could make things worse.""",
            [
                StoryChoice(
                    "Share your analysis with Megumi and coordinate a precise tactical assault",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse_weakened",
                        "ally": "megumi",
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 10},
                        "relationships": {"megumi": 20, "takeshi": 10},
                        "next_scene": "analytical_tactical_success",
                        "story_flags": {"megumi_coordination": True}
                    }
                ),
                StoryChoice(
                    "Use your analysis to create a distraction while Megumi rescues the student",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.PROTECTIVE: 10},
                        "relationships": {"megumi": 15, "takeshi": 25},
                        "next_scene": "analytical_distraction_tactic",
                        "story_flags": {"tactical_support": True}
                    }
                ),
                StoryChoice(
                    "Suggest exploiting the environmental advantages you've identified",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse_environmental",
                        "ally": "megumi",
                        "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 5},
                        "relationships": {"megumi": 25, "faculty": 15},
                        "next_scene": "analytical_environmental_victory",
                        "story_flags": {"environmental_tactician": True}
                    }
                ),
                StoryChoice(
                    "Propose a psychological approach to counter the curse's fear-feeding behavior",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 10},
                        "relationships": {"megumi": 15, "takeshi": 20},
                        "next_scene": "analytical_psychological_counter",
                        "story_flags": {"psychological_insight": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # Analytical Success Paths
        self.story_scenes["analytical_tactical_success"] = StoryScene(
            "Perfect Coordination",
            """Your shared analysis with Megumi results in a flawlessly executed tactical assault.
You position yourself to exploit the curse's predictable movement pattern while Megumi summons
his Divine Dogs to create a coordinated pincer attack.

"On my mark," Megumi says, his shadows beginning to writhe with cursed energy. "You take the
left flank during its third pause cycle, I'll hit it from the right with Nue."

The precision of your combined approach is a thing of beauty. As predicted, the curse enters
its vulnerability window, and your simultaneous assault catches it completely off-guard. Your
cursed energy, though less refined than Megumi's, strikes with perfect timing.

Takeshi watches in amazement as the two of you dismantle the curse with surgical precision.
"I've never seen first-years coordinate like that," he breathes. "It was like you could read
each other's minds."

"Good analysis leads to good tactics," Megumi replies, but there's clear approval in his voice.
"And good tactics executed properly save lives with minimal risk."

The curse dissolves under your combined assault, its feeding-based manifestation unable to
sustain itself against such coordinated opposition. Other students who witnessed the encounter
begin to gather, clearly impressed by the display of tactical thinking.""",
            [
                StoryChoice(
                    "Discuss advanced tactical theory with Megumi while helping Takeshi",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 10},
                        "relationships": {"megumi": 30, "takeshi": 15, "faculty": 20},
                        "next_scene": "analytical_advanced_discussion",
                        "story_flags": {"tactical_theorist": True}
                    }
                ),
                StoryChoice(
                    "Ask Megumi to help you understand how to improve your cursed energy control",
                    {
                        "traits": {Trait.FOCUSED: 15, Trait.DETERMINED: 5},
                        "relationships": {"megumi": 25, "takeshi": 10},
                        "next_scene": "analytical_energy_training",
                        "story_flags": {"technique_improvement": True}
                    }
                ),
                StoryChoice(
                    "Express interest in learning more about curse behavior analysis",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 5},
                        "relationships": {"megumi": 20, "faculty": 25},
                        "next_scene": "analytical_curse_study",
                        "story_flags": {"curse_researcher": True}
                    }
                ),
                StoryChoice(
                    "Focus on ensuring this tactical approach can be documented for other students",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.COMPASSIONATE: 10},
                        "relationships": {"megumi": 20, "takeshi": 20, "faculty": 15},
                        "next_scene": "analytical_knowledge_sharing",
                        "story_flags": {"educational_focus": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # Aggressive Path - Heavily Expanded
        self.story_scenes["first_mission_aggressive"] = StoryScene(
            "The Warrior's Path",
            """You charge directly at the cursed spirit with fierce determination, your instincts
screaming that action is better than hesitation. Your bold approach catches everyone off guard,
including Nobara Kugisaki who was approaching from the other side with her hammer and nails ready.

"Finally!" Nobara grins fiercely, her brown eyes lighting up with approval. "Someone who doesn't 
overthink everything! Let's crush this disgusting thing!"

The curse spirit - a writhing mass of academic anxiety given form, with too many eyes and grasping
hands clutching torn textbooks - seems surprised by your direct assault. It had been savoring the
fear from the injured student, but your aggressive cursed energy flare forces it to shift focus.

"You've got spirit, newbie!" Nobara calls out as she flanks the creature. "But raw aggression 
without technique will get you killed. Watch and learn!"

Her hammer glows with cursed energy as she readies her Straw Doll Technique. The injured student - 
Takeshi, you notice from his nameplate - looks between you and the curse with a mixture of hope 
and terror.

The curse, startled by your bold approach but now fully engaged, becomes more dangerous as its
panic makes it reckless. Its multiple arms lash out wildly, books and papers swirling around it
in a maelstrom of academic dread.

"First lesson in aggressive fighting," Nobara shouts over the chaos, "commit fully or don't 
commit at all! No half-measures!"

Your charge has created an opportunity, but it's also put you in immediate danger. The curse's
wild swings could connect at any moment.""",
            [
                StoryChoice(
                    "Continue your aggressive assault while coordinating with Nobara's technique",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse_enraged",
                        "ally": "nobara",
                        "traits": {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 10},
                        "relationships": {"nobara": 25, "takeshi": 15},
                        "next_scene": "aggressive_coordinated_assault",
                        "story_flags": {"nobara_partnership": True}
                    }
                ),
                StoryChoice(
                    "Use your aggressive momentum to draw the curse away from Takeshi",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse_focused",
                        "traits": {Trait.AGGRESSIVE: 10, Trait.PROTECTIVE: 15},
                        "relationships": {"nobara": 15, "takeshi": 25},
                        "next_scene": "aggressive_protective_diversion",
                        "story_flags": {"protective_aggression": True}
                    }
                ),
                StoryChoice(
                    "Channel your aggression into a powerful all-out attack",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse_enraged",
                        "traits": {Trait.AGGRESSIVE: 20, Trait.RECKLESS: 10},
                        "relationships": {"nobara": 20, "takeshi": 10},
                        "next_scene": "aggressive_overwhelming_force",
                        "story_flags": {"overwhelming_combatant": True}
                    }
                ),
                StoryChoice(
                    "Adapt your aggression into calculated strikes after watching Nobara's technique",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse_enraged",
                        "ally": "nobara",
                        "traits": {Trait.AGGRESSIVE: 10, Trait.FOCUSED: 10},
                        "relationships": {"nobara": 20, "takeshi": 15},
                        "next_scene": "aggressive_adaptive_combat",
                        "story_flags": {"adaptive_fighter": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # Aggressive Combat Resolutions
        self.story_scenes["aggressive_coordinated_assault"] = StoryScene(
            "Partnership in Battle",
            """Your continued aggressive assault creates perfect openings for Nobara's precision 
techniques. While you keep the curse's attention with your relentless forward pressure, she 
positions her straw doll with surgical accuracy.

"Nice work keeping it focused on you!" Nobara calls out as her cursed energy builds. "Now 
watch a real technique in action!"

Her Straw Doll Technique activates with devastating effect. The curse spirit writhes in agony
as Nobara's attack channels through the doll, causing massive internal damage. Your aggressive
energy and her technical precision prove to be a potent combination.

"Hairpin!" she shouts, following up with her signature finishing move. The curse spirit, 
already weakened by your assault and her initial technique, can't withstand the coordinated
attack.

Takeshi watches in amazement as the curse dissolves. "That was incredible! You two fought like 
you'd been partners for years!"

"Not bad for a first-timer," Nobara grins, giving you an appraising look. "Most people either
get in my way or try to show off. You actually made my job easier."

Your aggressive approach, tempered by tactical awareness, has clearly impressed both Nobara 
and the watching students. Several upperclassmen nod approvingly at the display of coordinated
combat.""",
            [
                StoryChoice(
                    "Ask Nobara to teach you more about precision techniques to complement your aggression",
                    {
                        "traits": {Trait.FOCUSED: 15, Trait.AGGRESSIVE: 5},
                        "relationships": {"nobara": 30, "takeshi": 15},
                        "next_scene": "aggressive_precision_training",
                        "story_flags": {"nobara_mentorship": True}
                    }
                ),
                StoryChoice(
                    "Express excitement about finding such effective combat partnerships",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.AGGRESSIVE: 5},
                        "relationships": {"nobara": 25, "takeshi": 20},
                        "next_scene": "aggressive_partnership_enthusiasm",
                        "story_flags": {"partnership_focused": True}
                    }
                ),
                StoryChoice(
                    "Check on Takeshi and make sure the aggressive approach didn't traumatize him further",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 5},
                        "relationships": {"takeshi": 30, "nobara": 20},
                        "next_scene": "aggressive_victim_care",
                        "story_flags": {"caring_warrior": True}
                    }
                ),
                StoryChoice(
                    "Analyze what made your aggressive approach work so well with Nobara's style",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 5},
                        "relationships": {"nobara": 20, "faculty": 15},
                        "next_scene": "aggressive_tactical_analysis",
                        "story_flags": {"tactical_aggression": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # === ARC 3: KYOTO EXCHANGE EVENT (MASSIVELY EXPANDED) ===
        
        # Pre-Exchange Preparation
        self.story_scenes["kyoto_exchange_announcement"] = StoryScene(
            "The Exchange Event Approaches",
            """Several weeks have passed since your first encounter with cursed spirits at Tokyo High.
Your reputation has grown based on your initial actions - whether as a tactical thinker, a 
protective rescuer, or an aggressive fighter. Now, the annual Exchange Event with Kyoto Jujutsu
High looms ahead.

Principal Yaga stands before the assembled first and second years in the main hall, his massive
frame casting an intimidating shadow. "The Exchange Event is not just a competition," he announces
in his gravelly voice. "It's a chance to test your growth, learn from your peers, and understand
the different philosophies that guide jujutsu sorcery."

Gojo-sensei lounges against the wall, his blindfold doing nothing to hide his amused expression.
"Plus, it's fun to show off how much better Tokyo students are," he adds cheerfully, earning 
glares from the faculty.

Yuji raises his hand excitedly. "What kind of events are there? Combat tournaments?"

"Team battles, individual matches, and cooperative exercises," Yaga explains. "But remember - 
this isn't just about winning. Kyoto school follows more traditional methods. Their students 
are disciplined, technically proficient, and..." he pauses meaningfully, "they have some very
strong personalities."

Megumi speaks up quietly. "I've heard about their star student, Aoi Todo. He's supposedly 
exceptionally powerful."

"Ah yes," Gojo grins. "Todo. He's... unique. You'll understand when you meet him."

The room buzzes with nervous excitement as students discuss strategies and worry about the 
upcoming competition.""",
            [
                StoryChoice(
                    "Focus on intensive training to prepare for powerful opponents",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.FOCUSED: 10},
                        "relationships": {"yuji": 10, "megumi": 10},
                        "next_scene": "kyoto_intensive_training",
                        "story_flags": {"training_focused_prep": True}
                    }
                ),
                StoryChoice(
                    "Research Kyoto school's fighting styles and student capabilities",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10},
                        "relationships": {"megumi": 15, "faculty": 10},
                        "next_scene": "kyoto_research_preparation",
                        "story_flags": {"intelligence_gathering": True}
                    }
                ),
                StoryChoice(
                    "Work on team coordination with your Tokyo classmates",
                    {
                        "traits": {Trait.COMPASSIONATE: 10, Trait.FOCUSED: 10},
                        "relationships": {"yuji": 15, "megumi": 10, "nobara": 15},
                        "next_scene": "kyoto_team_preparation",
                        "story_flags": {"teamwork_preparation": True}
                    }
                ),
                StoryChoice(
                    "Maintain confidence and prepare mentally for the psychological aspects",
                    {
                        "traits": {Trait.DETERMINED: 10, Trait.AGGRESSIVE: 10},
                        "relationships": {"nobara": 15, "gojo": 10},
                        "next_scene": "kyoto_mental_preparation",
                        "story_flags": {"psychological_readiness": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Main Hall"
        )
        
        # Intensive Training Path
        self.story_scenes["kyoto_intensive_training"] = StoryScene(
            "Forging Strength Through Effort",
            """You throw yourself into intense training regimens, determined to be as prepared as 
possible for whatever Kyoto's students might bring. The training grounds become your second home
as you push your cursed energy control and combat techniques to new levels.

Yuji joins you for morning conditioning, both of you running laps around the campus as the sun
rises. "You know," he pants between breaths, "I heard Todo can bench press a small car. Think
we should work on strength training too?"

Your dedication catches the attention of Nanami-sensei, who observes your solo practice sessions
with his characteristic stoic expression. "Consistency," he notes approvingly. "Many students
train intensely before events, then slack off afterward. True strength comes from sustained effort."

During one particularly grueling evening session, you're practicing cursed energy flow when
Maki appears. "Not bad form," she says, watching your technique. "But you're trying too hard.
Cursed energy responds to intent, not force. Here, watch."

Her demonstration is a masterclass in efficiency - every movement precise, every energy expenditure
calculated. "Kyoto students will be technically proficient," she explains. "You can't out-technique
them overnight, but you can out-smart them if you understand your own abilities better."

As the week progresses, your training becomes more sophisticated. You develop personal routines,
identify your strengths and weaknesses, and begin to understand how your unique approach to
jujutsu might surprise traditionally-trained opponents.""",
            [
                StoryChoice(
                    "Ask Maki to help you develop a signature fighting style",
                    {
                        "traits": {Trait.FOCUSED: 20, Trait.DETERMINED: 10},
                        "relationships": {"maki": 25, "yuji": 15},
                        "next_scene": "kyoto_signature_style_development",
                        "story_flags": {"maki_mentorship": True}
                    }
                ),
                StoryChoice(
                    "Continue solo training but incorporate Nanami's efficiency principles",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15},
                        "relationships": {"nanami": 20, "faculty": 15},
                        "next_scene": "kyoto_efficiency_mastery",
                        "story_flags": {"nanami_guidance": True}
                    }
                ),
                StoryChoice(
                    "Combine your training with Yuji to develop combination techniques",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.COMPASSIONATE: 10},
                        "relationships": {"yuji": 30, "maki": 10},
                        "next_scene": "kyoto_combination_training",
                        "story_flags": {"yuji_partnership": True}
                    }
                ),
                StoryChoice(
                    "Balance intense training with strategic thinking about match-ups",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.CAUTIOUS: 10, Trait.FOCUSED: 10},
                        "relationships": {"nanami": 15, "megumi": 15},
                        "next_scene": "kyoto_strategic_preparation",
                        "story_flags": {"balanced_preparation": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # The Todo Encounter - Massively Expanded
        self.story_scenes["meet_todo"] = StoryScene(
            "The Mountain That Walks",
            """The day of the Exchange Event arrives with crisp autumn air and electric tension. 
As the Tokyo students gather in the courtyard, a convoy of black vehicles approaches from the
distance - the Kyoto delegation has arrived.

The cars come to a stop with military precision, and Kyoto's students emerge like warriors
preparing for battle. Each carries themselves with rigid discipline and obvious confidence.
But all of that fades into background noise when the final figure steps out.

Aoi Todo.

Even at a distance, his presence is overwhelming. Standing well over six feet tall with a 
physique that suggests he could wrestle bears for fun, Todo surveys the Tokyo campus with 
the confidence of a conquering general. His school uniform strains against muscles that 
seem almost inhuman in their development.

"Is that really a high school student?" whispers one of the second-years.

"I heard he once punched a Special Grade curse so hard it apologized," another adds nervously.

Todo's gaze sweeps across the assembled Tokyo students, evaluating each one with the intensity
of a predator selecting prey. When his eyes land on you, they linger for a long moment, and
you feel like you're being measured for worthiness.

Then, without warning, Todo begins walking directly toward you. Each step seems to make the
ground vibrate slightly. Other students instinctively move out of his path.

"You," he says, his voice carrying the authority of someone accustomed to being obeyed. "New
first-year. You have potential - I can sense it in your cursed energy signature."

He stops just close enough that you have to crane your neck to meet his gaze, his presence 
both intimidating and oddly charismatic.

"But potential means nothing without proper understanding," Todo continues, his expression
completely serious. "Tell me, what is your type of woman?"

The question hangs in the air like a thunderclap. You can hear several students behind you
make confused noises, but Todo's expression indicates this is not a joke - this is somehow
a deeply important question to him.""",
            [
                StoryChoice(
                    "Give a thoughtful answer about personality traits you admire",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.FOCUSED: 5},
                        "relationships": {"todo": 30},
                        "story_flags": {"todo_respects_depth": True},
                        "next_scene": "todo_philosophical_approval"
                    }
                ),
                StoryChoice(
                    "Admit you haven't really thought about it seriously yet",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.ANALYTICAL: 5},
                        "relationships": {"todo": 5},
                        "story_flags": {"todo_neutral_response": True},
                        "next_scene": "todo_neutral_reaction"
                    }
                ),
                StoryChoice(
                    "Deflect with humor and ask about his fighting techniques instead",
                    {
                        "traits": {Trait.FOCUSED: 10, Trait.AGGRESSIVE: 5},
                        "relationships": {"todo": 10},
                        "story_flags": {"todo_combat_interest": True},
                        "next_scene": "todo_combat_redirect"
                    }
                ),
                StoryChoice(
                    "Challenge the relevance of the question to being a jujutsu sorcerer",
                    {
                        "traits": {Trait.AGGRESSIVE: 15, Trait.ANALYTICAL: 5},
                        "relationships": {"todo": 15},
                        "story_flags": {"todo_philosophical_challenge": True},
                        "next_scene": "todo_philosophical_debate"
                    }
                ),
                StoryChoice(
                    "Answer with complete honesty about what attracts you to people",
                    {
                        "traits": {Trait.COMPASSIONATE: 10, Trait.DETERMINED: 10},
                        "relationships": {"todo": 35},
                        "story_flags": {"todo_brotherhood": True},
                        "next_scene": "todo_brotherhood_moment"
                    }
                )
            ],
            "Tokyo Jujutsu High - Main Courtyard"
        )
        
        # Todo Brotherhood Path
        self.story_scenes["todo_brotherhood_moment"] = StoryScene(
            "A Bond Forged in Understanding",
            """Your honest, heartfelt response seems to strike something deep within Todo's soul.
His stern expression gradually transforms into one of genuine respect and warmth.

"Brother," he says quietly, and the single word carries more weight than any lengthy speech.
"You understand that the question is not about physical attraction - it's about the character
of your soul, the depth of your convictions, the sincerity of your heart."

Todo places a massive hand on your shoulder with surprising gentleness. "Most people give 
shallow answers, or try to impress me, or dismiss the question entirely. But you... you 
answered with truth. That tells me everything I need to know about who you are."

The other students watch in amazement as Todo's entire demeanor shifts from intimidating 
interrogator to older brother figure. "You have the spirit of a true warrior," he continues.
"Not because you seek conflict, but because you understand what's worth fighting for."

"But!" Todo's grin returns, fierce and competitive. "Understanding character is only the 
beginning. A true brother must also prove himself in combat! The Exchange Event will show
me if your fighting spirit matches your heart."

Megumi steps forward cautiously. "Todo, the formal events don't start for another hour..."

"Formal events?" Todo laughs, a sound like controlled thunder. "Brother, every moment is a
chance to grow stronger! Come, let me show you something about cursed energy that your 
Tokyo teachers haven't mentioned."

He begins to demonstrate an unusual energy manipulation technique, his massive frame moving
with surprising grace. "Cursed energy responds to emotion, yes? But most sorcerers use basic
emotions - anger, fear, determination. Watch what happens when you use more complex feelings..."

His demonstration reveals cursed energy patterns you've never seen before - flowing like 
music instead of burning like fire.""",
            [
                StoryChoice(
                    "Ask Todo to teach you these advanced emotional energy techniques",
                    {
                        "traits": {Trait.FOCUSED: 20, Trait.DETERMINED: 10},
                        "relationships": {"todo": 40, "faculty": 10},
                        "next_scene": "todo_advanced_energy_training",
                        "story_flags": {"todo_technique_student": True}
                    }
                ),
                StoryChoice(
                    "Express gratitude for his acceptance and ask about Kyoto's training methods",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.ANALYTICAL: 10},
                        "relationships": {"todo": 35, "kyoto_students": 15},
                        "next_scene": "todo_kyoto_insights",
                        "story_flags": {"kyoto_cultural_exchange": True}
                    }
                ),
                StoryChoice(
                    "Challenge Todo to a friendly sparring match before the formal events",
                    {
                        "traits": {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 15},
                        "relationships": {"todo": 30, "tokyo_students": 10},
                        "next_scene": "todo_brotherhood_spar",
                        "story_flags": {"todo_informal_combat": True}
                    }
                ),
                StoryChoice(
                    "Share your own insights about emotional cursed energy control",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 10},
                        "relationships": {"todo": 35, "faculty": 15},
                        "next_scene": "todo_mutual_learning",
                        "story_flags": {"mutual_teaching": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Main Courtyard"
        )
        
        # === ARC 3: KYOTO EXCHANGE EVENT (MASSIVELY EXPANDED) ===
        
        # Pre-Exchange Preparation
        self.story_scenes["kyoto_exchange_announcement"] = StoryScene(
            "The Exchange Event Approaches",
            """Several weeks have passed since your first encounter with cursed spirits at Tokyo High.
Your reputation has grown based on your initial actions - whether as a tactical thinker, a 
protective rescuer, or an aggressive fighter. Now, the annual Exchange Event with Kyoto Jujutsu
High looms ahead.

Principal Yaga stands before the assembled first and second years in the main hall, his massive
frame casting an intimidating shadow. "The Exchange Event is not just a competition," he announces
in his gravelly voice. "It's a chance to test your growth, learn from your peers, and understand
the different philosophies that guide jujutsu sorcery."

Gojo-sensei lounges against the wall, his blindfold doing nothing to hide his amused expression.
"Plus, it's fun to show off how much better Tokyo students are," he adds cheerfully, earning 
glares from the faculty.

Yuji raises his hand excitedly. "What kind of events are there? Combat tournaments?"

"Team battles, individual matches, and cooperative exercises," Yaga explains. "But remember - 
this isn't just about winning. Kyoto school follows more traditional methods. Their students 
are disciplined, technically proficient, and..." he pauses meaningfully, "they have some very
strong personalities."

Megumi speaks up quietly. "I've heard about their star student, Aoi Todo. He's supposedly 
exceptionally powerful."

"Ah yes," Gojo grins. "Todo. He's... unique. You'll understand when you meet him."

The room buzzes with nervous excitement as students discuss strategies and worry about the 
upcoming competition.""",
            [
                StoryChoice(
                    "Focus on intensive training to prepare for powerful opponents",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.FOCUSED: 10},
                        "relationships": {"yuji": 10, "megumi": 10},
                        "next_scene": "kyoto_intensive_training",
                        "story_flags": {"training_focused_prep": True}
                    }
                ),
                StoryChoice(
                    "Research Kyoto school's fighting styles and student capabilities",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10},
                        "relationships": {"megumi": 15, "faculty": 10},
                        "next_scene": "kyoto_research_preparation",
                        "story_flags": {"intelligence_gathering": True}
                    }
                ),
                StoryChoice(
                    "Work on team coordination with your Tokyo classmates",
                    {
                        "traits": {Trait.COMPASSIONATE: 10, Trait.FOCUSED: 10},
                        "relationships": {"yuji": 15, "megumi": 10, "nobara": 15},
                        "next_scene": "kyoto_team_preparation",
                        "story_flags": {"teamwork_preparation": True}
                    }
                ),
                StoryChoice(
                    "Maintain confidence and prepare mentally for the psychological aspects",
                    {
                        "traits": {Trait.DETERMINED: 10, Trait.AGGRESSIVE: 10},
                        "relationships": {"nobara": 15, "gojo": 10},
                        "next_scene": "kyoto_mental_preparation",
                        "story_flags": {"psychological_readiness": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Main Hall"
        )
        
        # Enhanced Todo Encounter
        self.story_scenes["enhanced_meet_todo"] = StoryScene(
            "The Mountain That Walks",
            """The day of the Exchange Event arrives with crisp autumn air and electric tension. 
As the Tokyo students gather in the courtyard, a convoy of black vehicles approaches from the
distance - the Kyoto delegation has arrived.

The cars come to a stop with military precision, and Kyoto's students emerge like warriors
preparing for battle. Each carries themselves with rigid discipline and obvious confidence.
But all of that fades into background noise when the final figure steps out.

Aoi Todo.

Even at a distance, his presence is overwhelming. Standing well over six feet tall with a 
physique that suggests he could wrestle bears for fun, Todo surveys the Tokyo campus with 
the confidence of a conquering general. His school uniform strains against muscles that 
seem almost inhuman in their development.

"Is that really a high school student?" whispers one of the second-years.

"I heard he once punched a Special Grade curse so hard it apologized," another adds nervously.

Todo's gaze sweeps across the assembled Tokyo students, evaluating each one with the intensity
of a predator selecting prey. When his eyes land on you, they linger for a long moment, and
you feel like you're being measured for worthiness.

Then, without warning, Todo begins walking directly toward you. Each step seems to make the
ground vibrate slightly. Other students instinctively move out of his path.

"You," he says, his voice carrying the authority of someone accustomed to being obeyed. "New
first-year. You have potential - I can sense it in your cursed energy signature."

He stops just close enough that you have to crane your neck to meet his gaze, his presence 
both intimidating and oddly charismatic.

"But potential means nothing without proper understanding," Todo continues, his expression
completely serious. "Tell me, what is your type of woman?"

The question hangs in the air like a thunderclap. You can hear several students behind you
make confused noises, but Todo's expression indicates this is not a joke - this is somehow
a deeply important question to him.""",
            [
                StoryChoice(
                    "Give a thoughtful answer about personality traits you admire",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.FOCUSED: 5},
                        "relationships": {"todo": 30},
                        "story_flags": {"todo_respects_depth": True},
                        "next_scene": "todo_philosophical_approval"
                    }
                ),
                StoryChoice(
                    "Answer with complete honesty about what attracts you to people",
                    {
                        "traits": {Trait.COMPASSIONATE: 10, Trait.DETERMINED: 10},
                        "relationships": {"todo": 35},
                        "story_flags": {"todo_brotherhood": True},
                        "next_scene": "todo_brotherhood_moment"
                    }
                ),
                StoryChoice(
                    "Challenge the relevance of the question to being a jujutsu sorcerer",
                    {
                        "traits": {Trait.AGGRESSIVE: 15, Trait.ANALYTICAL: 5},
                        "relationships": {"todo": 15},
                        "story_flags": {"todo_philosophical_challenge": True},
                        "next_scene": "todo_philosophical_debate"
                    }
                )
            ],
            "Tokyo Jujutsu High - Main Courtyard"
        )
        
        # Todo Brotherhood Moment - Enhanced
        self.story_scenes["todo_brotherhood_moment"] = StoryScene(
            "A Bond Forged in Understanding",
            """Your honest, heartfelt response seems to strike something deep within Todo's soul.
His stern expression gradually transforms into one of genuine respect and warmth.

"Brother," he says quietly, and the single word carries more weight than any lengthy speech.
"You understand that the question is not about physical attraction - it's about the character
of your soul, the depth of your convictions, the sincerity of your heart."

Todo places a massive hand on your shoulder with surprising gentleness. "Most people give 
shallow answers, or try to impress me, or dismiss the question entirely. But you... you 
answered with truth. That tells me everything I need to know about who you are."

The other students watch in amazement as Todo's entire demeanor shifts from intimidating 
interrogator to older brother figure. "You have the spirit of a true warrior," he continues.
"Not because you seek conflict, but because you understand what's worth fighting for."

"But!" Todo's grin returns, fierce and competitive. "Understanding character is only the 
beginning. A true brother must also prove himself in combat! The Exchange Event will show
me if your fighting spirit matches your heart."

Megumi steps forward cautiously. "Todo, the formal events don't start for another hour..."

"Formal events?" Todo laughs, a sound like controlled thunder. "Brother, every moment is a
chance to grow stronger! Come, let me show you something about cursed energy that your 
Tokyo teachers haven't mentioned."

He begins to demonstrate an unusual energy manipulation technique, his massive frame moving
with surprising grace. "Cursed energy responds to emotion, yes? But most sorcerers use basic
emotions - anger, fear, determination. Watch what happens when you use more complex feelings..."

His demonstration reveals cursed energy patterns you've never seen before - flowing like 
music instead of burning like fire.""",
            [
                StoryChoice(
                    "Ask Todo to teach you these advanced emotional energy techniques",
                    {
                        "traits": {Trait.FOCUSED: 20, Trait.DETERMINED: 10},
                        "relationships": {"todo": 40, "faculty": 10},
                        "next_scene": "todo_advanced_energy_training",
                        "story_flags": {"todo_technique_student": True}
                    }
                ),
                StoryChoice(
                    "Express gratitude for his acceptance and ask about Kyoto's training methods",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.ANALYTICAL: 10},
                        "relationships": {"todo": 35, "kyoto_students": 15},
                        "next_scene": "todo_kyoto_insights",
                        "story_flags": {"kyoto_cultural_exchange": True}
                    }
                ),
                StoryChoice(
                    "Challenge Todo to a friendly sparring match before the formal events",
                    {
                        "traits": {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 15},
                        "relationships": {"todo": 30, "tokyo_students": 10},
                        "next_scene": "todo_brotherhood_spar",
                        "story_flags": {"todo_informal_combat": True}
                    }
                ),
                StoryChoice(
                    "Share your own insights about emotional cursed energy control",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 10},
                        "relationships": {"todo": 35, "faculty": 15},
                        "next_scene": "todo_mutual_learning",
                        "story_flags": {"mutual_teaching": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Main Courtyard"
        )
        
        # === ARC 4: SHIBUYA INCIDENT (MASSIVELY EXPANDED) ===
        
        # Pre-Shibuya Intelligence Gathering
        self.story_scenes["shibuya_intelligence_briefing"] = StoryScene(
            "Shadows Over Shibuya",
            """The atmosphere at Tokyo Jujutsu High has grown increasingly tense over the past week.
Reports from the intelligence division paint a troubling picture: unusual cursed energy spikes
in Shibuya district, civilian disappearances, and sightings of powerful unregistered cursed spirits.

You sit in the emergency briefing room alongside your classmates, watching as Nanami-sensei 
points to various locations on a detailed map of Shibuya. His usually calm demeanor carries
an edge of concern that puts everyone on high alert.

"The pattern suggests coordination," Nanami explains, his voice grave. "This isn't random 
curse manifestation. Someone - or something - is orchestrating events in Shibuya district."

Ijichi adjusts his glasses nervously as he presents surveillance photos. "We've confirmed
at least three Grade 1 equivalent cursed spirits, with possibility of Special Grade presence.
The barrier techniques being used are... sophisticated."

Gojo-sensei is notably absent from the briefing, which only adds to the general unease. 
Principal Yaga's expression is grimmer than you've ever seen it.

"This could be the largest coordinated curse incident in decades," Yaga announces. "We're
calling in sorcerers from across the country, but..." he pauses, looking directly at the
first-years, "we may need every capable sorcerer we can muster."

Yuji raises his hand tensely. "Are you saying first-years might be deployed to Shibuya?"

"We're saying," Nanami responds carefully, "that you should be prepared for anything. This
situation is evolving rapidly."

The weight of potential real combat - not training exercises or Grade 3 encounters, but 
life-or-death battles against powerful enemies - settles over the room like a heavy blanket.""",
            [
                StoryChoice(
                    "Volunteer immediately for any mission to Shibuya",
                    {
                        "traits": {Trait.DETERMINED: 20, Trait.PROTECTIVE: 10},
                        "relationships": {"faculty": 20, "yuji": 15},
                        "next_scene": "shibuya_volunteer_immediate",
                        "story_flags": {"shibuya_volunteer": True}
                    }
                ),
                StoryChoice(
                    "Request additional training before any deployment",
                    {
                        "traits": {Trait.CAUTIOUS: 15, Trait.FOCUSED: 15},
                        "relationships": {"nanami": 20, "megumi": 15},
                        "next_scene": "shibuya_training_request",
                        "story_flags": {"preparation_focused": True}
                    }
                ),
                StoryChoice(
                    "Ask about civilian evacuation and rescue operations",
                    {
                        "traits": {Trait.COMPASSIONATE: 20, Trait.PROTECTIVE: 10},
                        "relationships": {"nanami": 15, "faculty": 15},
                        "next_scene": "shibuya_civilian_focus",
                        "story_flags": {"civilian_priority": True}
                    }
                ),
                StoryChoice(
                    "Inquire about the intelligence gaps and offer analytical support",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 10},
                        "relationships": {"ijichi": 20, "faculty": 20},
                        "next_scene": "shibuya_intelligence_support",
                        "story_flags": {"intelligence_specialist": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Emergency Briefing Room"
        )
        
        # Shibuya Preparation Expanded
        self.story_scenes["shibuya_preparation"] = StoryScene(
            "Before the Storm",
            """Halloween night approaches, and the intelligence gathered paints an even grimmer 
picture than initially suspected. What seemed like isolated incidents are clearly part of 
a massive, coordinated assault on Shibuya district. The scale and sophistication suggest
involvement of Special Grade cursed spirits - possibly even curse users.

You stand in the strategy room, watching as senior sorcerers debate deployment plans. The
atmosphere is tense with the knowledge that this could be the most dangerous operation any
of you have ever faced. Maps cover every surface, marked with enemy positions, civilian
evacuation routes, and tactical objectives.

Gojo-sensei has finally returned, but his usual jovial demeanor is replaced by a focused
intensity that makes everyone nervous. "The enemy knows our capabilities," he explains to
the assembled sorcerers. "This is a trap designed specifically for us."

"Which means," Principal Yaga adds grimly, "we have no choice but to spring it. The civilian
casualty potential is too high to ignore."

Nanami approaches your group with a serious expression. "First-years, I want you to understand
something. What we're about to face isn't like anything you've encountered. The enemies in
Shibuya won't hold back because you're students. They'll try to kill you with everything
they have."

The weight of his words settles over you. This isn't training anymore - this is war.

"That said," Nanami continues, "we believe your unique perspectives and abilities could be
valuable assets. The enemy has planned for traditional sorcerer responses. Your unconventional
approaches might provide the tactical advantage we need."

The decision looms before you: how will you contribute to the most dangerous mission of your life?""",
            [
                StoryChoice(
                    "Volunteer for the front-line assault team to face the strongest enemies",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.AGGRESSIVE: 10},
                        "relationships": {"gojo": 20, "yuji": 20},
                        "story_flags": {"frontline_volunteer": True},
                        "next_scene": "shibuya_frontline_deployment"
                    }
                ),
                StoryChoice(
                    "Request assignment to civilian rescue and evacuation operations",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 15},
                        "relationships": {"nanami": 25, "ijichi": 15},
                        "story_flags": {"rescue_volunteer": True},
                        "next_scene": "shibuya_rescue_operations"
                    }
                ),
                StoryChoice(
                    "Offer to work with intelligence gathering and tactical coordination",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 15},
                        "relationships": {"megumi": 20, "faculty": 20},
                        "story_flags": {"intelligence_focused": True},
                        "next_scene": "shibuya_tactical_coordination"
                    }
                ),
                StoryChoice(
                    "Propose a flexible support role that can adapt to changing conditions",
                    {
                        "traits": {Trait.FOCUSED: 15, Trait.ANALYTICAL: 10},
                        "relationships": {"nanami": 20, "gojo": 15},
                        "story_flags": {"adaptive_support": True},
                        "next_scene": "shibuya_adaptive_deployment"
                    }
                )
            ],
            "Tokyo Jujutsu High - Strategy Room"
        )
        
        # Shibuya Frontline Deployment
        self.story_scenes["shibuya_frontline_deployment"] = StoryScene(
            "Into the Heart of Darkness",
            """Your assignment to the frontline assault team places you at the epicenter of the
Shibuya incident. As your team approaches the district, the oppressive weight of multiple
powerful cursed auras makes the air itself feel thick and hostile.

The normally bustling streets of Shibuya are eerily empty, civilian evacuation having begun
hours ago. However, the barriers erected by the enemy prevent complete evacuation - thousands
of people remain trapped within the district, used as both shields and bait.

Gojo-sensei leads your assault group, his Six Eyes constantly scanning for threats. "Remember,"
he says, his voice carrying unusual gravity, "our primary objective is neutralizing the Special
Grade threats. Everything else is secondary."

As you move deeper into the district, the cursed energy becomes so intense it's physically
uncomfortable. Buildings show signs of structural damage from cursed spirit activity, and
the very air seems to writhe with malevolent intent.

"Contact ahead," Megumi reports, his divine dogs having detected movement. "Multiple Grade 1
equivalents, approximately three hundred meters."

Through the shadows between buildings, you catch glimpses of the enemy: cursed spirits unlike
anything in your textbooks, their forms suggesting intelligence and coordination far beyond
typical manifestations.

"This is it," Gojo announces. "Your first real combat as jujutsu sorcerers. Show me what
Tokyo High has taught you."

The battle for Shibuya begins now.""",
            [
                StoryChoice(
                    "Take point and engage the first wave of enemies directly",
                    {
                        "combat": True,
                        "enemy": "shibuya_grade_1_squad",
                        "ally": "gojo",
                        "traits": {Trait.AGGRESSIVE: 20, Trait.DETERMINED: 15},
                        "relationships": {"gojo": 25, "yuji": 20},
                        "next_scene": "shibuya_frontline_combat",
                        "story_flags": {"shibuya_vanguard": True}
                    }
                ),
                StoryChoice(
                    "Support Gojo while protecting the team's flanks",
                    {
                        "combat": True,
                        "enemy": "shibuya_grade_1_ambush",
                        "ally": "gojo",
                        "traits": {Trait.PROTECTIVE: 20, Trait.FOCUSED: 10},
                        "relationships": {"gojo": 20, "team_members": 25},
                        "next_scene": "shibuya_tactical_support",
                        "story_flags": {"shibuya_guardian": True}
                    }
                ),
                StoryChoice(
                    "Use your unique abilities to disrupt enemy coordination",
                    {
                        "combat": True,
                        "enemy": "shibuya_coordinated_spirits",
                        "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15},
                        "relationships": {"gojo": 20, "megumi": 20},
                        "next_scene": "shibuya_disruption_tactics",
                        "story_flags": {"shibuya_disruptor": True}
                    }
                ),
                StoryChoice(
                    "Focus on identifying and tracking the enemy's strategic objectives",
                    {
                        "traits": {Trait.ANALYTICAL: 25, Trait.CAUTIOUS: 10},
                        "relationships": {"gojo": 15, "faculty": 25},
                        "next_scene": "shibuya_strategic_analysis",
                        "story_flags": {"shibuya_analyst": True}
                    }
                )
            ],
            "Shibuya District - Front Lines"
        )
        
        # Shibuya Rescue Operations
        self.story_scenes["shibuya_rescue_operations"] = StoryScene(
            "Angels in Hell",
            """Your assignment to the rescue operations team leads you through the terrifying
maze of Shibuya's civilian shelters and trapped populations. Working alongside Nanami-sensei
and a team of support sorcerers, you navigate the district's underground areas where thousands
of civilians cower in fear.

The barriers erected by the enemies have created a nightmarish environment where normal
evacuation routes are blocked, and cursed spirits hunt civilians like predators. Your job
is to clear safe passages and escort groups to evacuation points while avoiding the major
combat zones.

"Remember," Nanami instructs as you approach your first shelter, "these people have been
trapped for hours. They're terrified, potentially injured, and may panic when they see us.
Your demeanor and approach will determine whether we can save them."

The first shelter you reach contains nearly fifty people huddled in a subway station. The
cursed energy in the area is oppressive, and several Grade 2 cursed spirits patrol the
tunnels between you and the evacuation routes.

A small girl, maybe eight years old, looks up at you with tears in her eyes. "Are you here
to save us?" she whispers.

The weight of responsibility settles on your shoulders like a mountain. These people are
depending on you not just for rescue, but for hope itself.

"We're getting you out of here," you promise, and you mean it with every fiber of your being.""",
            [
                StoryChoice(
                    "Focus on clearing the safest route and moving large groups quickly",
                    {
                        "combat": True,
                        "enemy": "shibuya_tunnel_patrol",
                        "ally": "nanami",
                        "traits": {Trait.PROTECTIVE: 20, Trait.FOCUSED: 15},
                        "relationships": {"nanami": 30, "civilians": 40},
                        "next_scene": "shibuya_mass_evacuation",
                        "story_flags": {"mass_rescuer": True}
                    }
                ),
                StoryChoice(
                    "Take personal responsibility for the most vulnerable civilians",
                    {
                        "traits": {Trait.COMPASSIONATE: 25, Trait.PROTECTIVE: 20},
                        "relationships": {"civilians": 50, "nanami": 20},
                        "next_scene": "shibuya_vulnerable_protection",
                        "story_flags": {"guardian_angel": True}
                    }
                ),
                StoryChoice(
                    "Coordinate with other rescue teams to maximize coverage",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15},
                        "relationships": {"nanami": 25, "rescue_teams": 30},
                        "next_scene": "shibuya_rescue_coordination",
                        "story_flags": {"rescue_coordinator": True}
                    }
                ),
                StoryChoice(
                    "Hunt down the cursed spirits threatening civilians in this sector",
                    {
                        "combat": True,
                        "enemy": "shibuya_civilian_hunters",
                        "traits": {Trait.AGGRESSIVE: 15, Trait.PROTECTIVE: 20},
                        "relationships": {"nanami": 20, "civilians": 35},
                        "next_scene": "shibuya_predator_elimination",
                        "story_flags": {"civilian_avenger": True}
                    }
                )
            ],
            "Shibuya District - Underground Shelters"
        )
        
        # === ARC 5: ADVANCED TRAINING & DOMAIN EXPANSION ===
        
        # Post-Shibuya Recovery and Growth
        self.story_scenes["post_shibuya_reflection"] = StoryScene(
            "After the Storm",
            """Weeks have passed since the Shibuya Incident, and the jujutsu world has been forever
changed. The events of that night tested every sorcerer involved, and you've emerged from the
experience fundamentally different - stronger, more experienced, but also bearing the weight
of what you've witnessed.

You sit in the peaceful gardens of Tokyo Jujutsu High, watching cherry blossoms fall while
processing everything that happened. The contrast between this serene moment and the chaos
of Shibuya feels almost surreal.

Gojo-sensei approaches, his blindfold unable to hide the fact that he's studying you carefully.
"You did well in Shibuya," he says, settling down on the bench beside you. "Better than well,
actually. You showed real growth under pressure."

"But," he continues, and you can hear the shift in his tone, "Shibuya was just the beginning.
The enemies we face are getting stronger, more coordinated. If we're going to protect people,
we need to push our abilities to new heights."

He turns to face you directly. "I'm talking about advanced techniques. Domain Expansion.
The kind of power that can turn the tide of battle against Special Grade threats."

The weight of his words settles over you. Domain Expansion - the pinnacle of jujutsu sorcery,
a technique that only the most skilled sorcerers can master. The idea that you might be ready
to begin that training is both thrilling and terrifying.

"Your performance in Shibuya convinced me that you have the potential," Gojo explains. "But
potential isn't enough. Are you ready to push yourself harder than you ever have before?"

The question hangs in the air. This is a crossroads moment - the difference between remaining
a promising student and becoming a true jujutsu sorcerer capable of facing the greatest threats.""",
            [
                StoryChoice(
                    "Accept the advanced training immediately - you're ready for anything",
                    {
                        "traits": {Trait.DETERMINED: 25, Trait.AGGRESSIVE: 10},
                        "relationships": {"gojo": 30, "faculty": 20},
                        "next_scene": "domain_training_immediate",
                        "story_flags": {"domain_candidate": True}
                    }
                ),
                StoryChoice(
                    "Ask to train with your classmates for mutual support and growth",
                    {
                        "traits": {Trait.COMPASSIONATE: 20, Trait.FOCUSED: 15},
                        "relationships": {"yuji": 25, "megumi": 25, "nobara": 25},
                        "next_scene": "domain_group_training",
                        "story_flags": {"team_advancement": True}
                    }
                ),
                StoryChoice(
                    "Request time to master your current abilities before advancing further",
                    {
                        "traits": {Trait.CAUTIOUS: 20, Trait.ANALYTICAL: 15},
                        "relationships": {"gojo": 20, "nanami": 25},
                        "next_scene": "foundation_mastery_focus",
                        "story_flags": {"foundation_perfectionist": True}
                    }
                ),
                StoryChoice(
                    "Express interest but ask about the mental and physical costs",
                    {
                        "traits": {Trait.ANALYTICAL: 25, Trait.CAUTIOUS: 10},
                        "relationships": {"gojo": 25, "faculty": 20},
                        "next_scene": "domain_training_analysis",
                        "story_flags": {"informed_advancement": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Memorial Garden"
        )
        
        # Domain Expansion Training Path
        self.story_scenes["domain_training_immediate"] = StoryScene(
            "The Path to Absolute Power",
            """Your immediate acceptance of Gojo's offer leads to the most intensive training
regimen you've ever experienced. Domain Expansion isn't just about raw power - it's about
understanding the very nature of your cursed technique and extending it into reality itself.

"Domain Expansion," Gojo explains as he leads you to a specially prepared training chamber,
"is the manifestation of your innate technique combined with your deepest understanding of
yourself. It's not something you can force or fake."

The training chamber is unlike anything you've seen before - walls covered in protective
barriers, sensors monitoring cursed energy fluctuations, and emergency protocols in case
something goes wrong. The very air hums with contained power.

"First," Gojo continues, "you need to understand what your technique truly is at its core.
Not just how you use it, but why it exists, what it represents about your soul."

Over the following weeks, you dive deeper into your cursed technique than ever before.
Every aspect is analyzed, deconstructed, and rebuilt from first principles. The process
is mentally exhausting but reveals layers of your ability you never knew existed.

"Good," Gojo observes as you demonstrate a new application of your technique. "You're
beginning to understand. But understanding isn't enough - you need to project that
understanding into physical space."

The moment arrives when you attempt your first Domain Expansion. The sensation is unlike
anything you've ever experienced - your cursed energy doesn't just flow outward, it
reshapes the very fabric of local reality according to your will and technique.""",
            [
                StoryChoice(
                    "Focus on creating a domain that enhances your protective abilities",
                    {
                        "traits": {Trait.PROTECTIVE: 30, Trait.FOCUSED: 20},
                        "relationships": {"gojo": 35, "civilians": 30},
                        "next_scene": "domain_sanctuary_creation",
                        "story_flags": {"sanctuary_domain": True}
                    }
                ),
                StoryChoice(
                    "Develop a domain that maximizes your analytical and strategic capabilities",
                    {
                        "traits": {Trait.ANALYTICAL: 30, Trait.FOCUSED: 25},
                        "relationships": {"gojo": 30, "megumi": 30},
                        "next_scene": "domain_analysis_field",
                        "story_flags": {"analysis_domain": True}
                    }
                ),
                StoryChoice(
                    "Create a domain focused on overwhelming offensive power",
                    {
                        "traits": {Trait.AGGRESSIVE: 30, Trait.DETERMINED: 20},
                        "relationships": {"gojo": 30, "todo": 25},
                        "next_scene": "domain_devastation_zone",
                        "story_flags": {"combat_domain": True}
                    }
                ),
                StoryChoice(
                    "Attempt to balance all aspects of your abilities in the domain",
                    {
                        "traits": {Trait.FOCUSED: 25, Trait.ANALYTICAL: 15, Trait.DETERMINED: 15},
                        "relationships": {"gojo": 40, "faculty": 30},
                        "next_scene": "domain_perfect_balance",
                        "story_flags": {"balanced_domain": True}
                    }
                )
            ],
            "Tokyo Jujutsu High - Domain Training Chamber"
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