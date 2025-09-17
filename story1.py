"""
Introduction Arc - First Days at Tokyo Jujutsu High

This module contains the expanded Introduction Arc story content with rich dialogue,
branching paths, character development, combat scenarios, and exploration elements.
Minimum 800 lines of detailed story content.
"""

from typing import Dict, List, Any, Optional
from character import Trait
from story_base import StoryChoice, StoryScene


class IntroductionArc:
    """Manages the Introduction Arc story scenes and progression."""
    
    def __init__(self):
        self.scenes = {}
        self._initialize_introduction_arc()
    
    def _initialize_introduction_arc(self):
        """Initialize all Introduction Arc story scenes."""
        
        # =================================================================
        # SCENE 1: ARRIVAL AT TOKYO JUJUTSU HIGH
        # =================================================================
        
        intro_description = """You step off the train at the nearest station to Tokyo Jujutsu High, your heart pounding with a mixture of excitement and nervousness. The weight of your acceptance letter feels heavy in your pocket as you navigate through the busy Tokyo streets.
        
As you approach the school grounds, you're struck by the traditional Japanese architecture mixed with modern security measures. The air itself feels different here - charged with an energy you can't quite identify. Other students walk past, some carrying what look like weapon cases, others moving with a confidence that speaks of hidden power.

You pause at the main gate, taking in the sight of the imposing buildings surrounded by towering trees. A security guard nods at you knowingly - clearly, you're expected. As you walk through the courtyard, you notice the way shadows seem deeper here, and the sound of training echoes from various buildings.

Suddenly, commotion erupts near the training grounds. You see a fellow first-year student backed against a wall, terror written across their face. Looming over them is something that makes your blood run cold - a grotesque, writhing mass of dark energy with too many eyes and limbs that bend in impossible directions. A Grade 3 cursed spirit, and it's focused entirely on the helpless student.

The student, a girl with short black hair, clutches what appears to be a wooden training sword, but her hands are shaking too badly to be of any use. Blood trickles from a cut on her forehead, and her school uniform is torn. She's clearly a non-combatant who was in the wrong place at the wrong time.

Around the courtyard, you notice other figures watching - some students, some faculty - but they seem to be observing rather than intervening. Is this... a test? A learning opportunity? Or are they simply confident that the situation will resolve itself?

Your cursed energy stirs within you, responding to the presence of the malevolent spirit. This is your first real encounter with a cursed spirit, and how you handle it will set the tone for your entire time at this school. The choices you make here will not only affect the outcome of this immediate situation but will also influence how your fellow students and teachers perceive you.

The cursed spirit's attention is completely focused on the trapped student, giving you a moment to assess your options. You can feel the weight of multiple gazes upon you - this is clearly a defining moment.

What do you choose to do?"""

        intro_choices = [
            StoryChoice(
                "Rush in immediately to help the injured student",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 10, Trait.RECKLESS: 5},
                    "next_scene": "intro_compassionate_path",
                    "relationships": {"yuji": 15, "injured_student": 20},
                    "story_flags": {"helped_immediately": True, "first_impression": "heroic"},
                    "experience": 50
                }
            ),
            StoryChoice(
                "Carefully assess the cursed spirit's weaknesses before acting",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10, Trait.FOCUSED: 5},
                    "next_scene": "intro_analytical_path",
                    "relationships": {"megumi": 15, "nanami": 10},
                    "story_flags": {"assessed_first": True, "first_impression": "strategic"},
                    "experience": 40
                }
            ),
            StoryChoice(
                "Charge directly at the cursed spirit with full aggression",
                {
                    "traits": {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 10, Trait.RECKLESS: 10},
                    "next_scene": "intro_aggressive_path",
                    "relationships": {"nobara": 15, "todo": 5},
                    "story_flags": {"fought_aggressively": True, "first_impression": "fierce"},
                    "experience": 45
                }
            ),
            StoryChoice(
                "Look for other students or teachers to coordinate with",
                {
                    "traits": {Trait.CAUTIOUS: 10, Trait.ANALYTICAL: 5, Trait.PROTECTIVE: 5},
                    "next_scene": "intro_coordination_path",
                    "relationships": {"group": 10},
                    "story_flags": {"sought_help": True, "first_impression": "teamwork"},
                    "experience": 35
                }
            )
        ]
        
        self.scenes["intro"] = StoryScene(
            "Arrival at Tokyo Jujutsu High",
            intro_description,
            intro_choices,
            "Tokyo Jujutsu High - Main Courtyard"
        )
        
        # =================================================================
        # SCENE 2A: COMPASSIONATE PATH - THE RESCUER'S JOURNEY
        # =================================================================
        
        compassionate_description = """Without a moment's hesitation, you sprint toward the cursed spirit and the trapped student. Your feet pound against the courtyard's stone pavement as adrenaline surges through your veins. The cursed spirit's many eyes swivel toward you with predatory interest, but you don't slow down.

"Get away from her!" you shout, your voice carrying across the courtyard with surprising authority.

The injured student - you can see now that her name tag reads "Akiko Tanaka" - looks up at you with a mixture of relief and horror. "No! Stay back! It's too dangerous!" she calls out, but her voice is weak from fear and exhaustion.

As you close the distance, you get a better look at the cursed spirit. It's roughly humanoid but wrong in every conceivable way. Its limbs are too long and bend at joints that shouldn't exist. Multiple mouths line its torso, each filled with needle-sharp teeth, and those eyes - dozens of them - track your movement with malevolent intelligence. This is definitely a Grade 3, powerful enough to seriously injure or kill an unprepared sorcerer.

Your sudden intervention catches the attention of several observers. From the corner of your eye, you spot a pink-haired boy about your age watching with intense interest. His posture suggests he was about to intervene himself, but your quick action has given him pause. There's something familiar about his energy signature - warm, bright, and incredibly powerful.

"Interesting approach," comes a voice from behind you. You risk a quick glance and see a tall man with white hair and a blindfold, clearly a teacher. Despite the dangerous situation, he seems remarkably calm. "Let's see how this plays out."

The cursed spirit lets out a sound that's part roar, part screech, and entirely inhuman. It abandons its focus on Akiko and turns its full attention to you. Several of its mouths begin to speak in unison, their voices creating a discordant chorus: "Fresh... meat... new... sorcerer... weak... will... feast..."

Your cursed energy responds to the threat, coursing through your body like liquid fire. You've trained for this moment, but facing a real cursed spirit is vastly different from any simulation or training exercise. The malevolent energy radiating from the creature is almost overwhelming, pressing against your consciousness like a physical weight.

Akiko struggles to her feet behind you, still clutching her wooden sword. "I can help!" she says, though her legs are clearly shaking. "I may not be strong, but I won't just hide while someone risks their life for me!"

The pink-haired student steps forward, his friendly demeanor shifting to something more serious. "That was brave," he calls out with genuine admiration in his voice. "I'm Yuji Itadori. Mind if I lend a hand? This thing looks like it could use a good beating!"

From another direction, you hear footsteps approaching. A dark-haired boy with an serious expression emerges from behind one of the training buildings. "The logical approach would be to attack it from multiple angles simultaneously," he says calmly. "Its attention is divided now, which gives us an advantage."

The situation has evolved rapidly. What started as a rescue mission has become a multi-person encounter. Your quick action to help has clearly impressed your fellow students and gained you potential allies. How you proceed from here will further define your relationships and reputation.

What's your next move?"""

        compassionate_choices = [
            StoryChoice(
                "Accept Yuji's help and fight together",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_standard",
                    "ally": "yuji",
                    "traits": {Trait.DETERMINED: 10, Trait.PROTECTIVE: 5},
                    "relationships": {"yuji": 20, "akiko": 15},
                    "story_flags": {"yuji_first_ally": True, "team_fighter": True},
                    "next_scene": "post_yuji_team_battle",
                    "experience": 75
                }
            ),
            StoryChoice(
                "Coordinate with both Yuji and the analytical student",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_weakened",
                    "ally": "yuji_and_megumi",
                    "traits": {Trait.ANALYTICAL: 5, Trait.PROTECTIVE: 5, Trait.FOCUSED: 5},
                    "relationships": {"yuji": 15, "megumi": 15, "akiko": 15},
                    "story_flags": {"team_coordination": True, "strategic_teamwork": True},
                    "next_scene": "post_team_coordination_battle",
                    "experience": 80
                }
            ),
            StoryChoice(
                "Tell everyone to stay back while you handle it alone",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_focused",
                    "traits": {Trait.DETERMINED: 15, Trait.PROTECTIVE: 10, Trait.RECKLESS: 5},
                    "relationships": {"akiko": 25, "yuji": 5, "megumi": -5},
                    "story_flags": {"solo_hero": True, "overprotective": True},
                    "next_scene": "post_solo_protection_battle",
                    "experience": 60
                }
            ),
            StoryChoice(
                "Focus on getting Akiko to safety first",
                {
                    "traits": {Trait.PROTECTIVE: 15, Trait.CAUTIOUS: 10},
                    "relationships": {"akiko": 30},
                    "story_flags": {"prioritized_safety": True, "rescue_focused": True},
                    "next_scene": "akiko_rescue_sequence",
                    "experience": 45
                }
            )
        ]
        
        self.scenes["intro_compassionate_path"] = StoryScene(
            "The Rescuer's Path",
            compassionate_description,
            compassionate_choices,
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # =================================================================
        # SCENE 2B: ANALYTICAL PATH - THE STRATEGIST'S APPROACH
        # =================================================================
        
        analytical_description = """You force yourself to stop and observe, despite every instinct screaming at you to act immediately. Your analytical mind takes over, cataloging details about the cursed spirit that could prove crucial in the coming confrontation.

The creature is approximately eight feet tall, with a lean but muscular build that suggests speed over brute strength. Its multiple limbs move in a coordinated pattern - not random flailing, but purposeful, practiced movements. This isn't a newly formed curse; it has experience with combat. Most telling are the scars across its torso, evidence of previous battles with sorcerers.

Its positioning is deliberately chosen. The cursed spirit has backed the student against the training building's wall, limiting her escape routes while positioning itself with multiple exit strategies. This level of tactical thinking is unusual for a Grade 3 curse - they're typically more driven by instinct than strategy.

You notice something else: the way it holds its left arm slightly closer to its body, favoring its right side. An old injury, perhaps, or a natural weakness. The multiple eyes seem to track movement differently too - the ones on the right side appear more alert and responsive.

"Impressive," comes a quiet voice from beside you. You turn to see a dark-haired student with intense green eyes watching both you and the cursed spirit with equal interest. "Most people would have charged in by now. I'm Megumi Fushiguro."

The student - Megumi - continues his own assessment. "Grade 3, probably been around for a while based on those scars. It's definitely intelligent enough to choose its battlefield. But did you notice the way it's favoring its right side?"

You nod, pleased that someone else caught the same detail. "Weakness on the left, possibly an old injury. And its eye placement suggests limited peripheral vision on that side."

"Exactly," Megumi says, a hint of approval in his voice. "Most first-years would miss those details. You might actually survive your first week here."

From across the courtyard, a pink-haired student is watching the situation with growing agitation. His body language suggests he's moments away from charging in regardless of strategy. Meanwhile, the trapped student - her nameplate reads "Akiko" - is trying to edge along the wall toward what she clearly hopes is an escape route.

A new voice joins the conversation - authoritative but relaxed. "Well, well. Looks like we have some natural tacticians in this year's class." You turn to see a tall man with distinctive white hair and a blindfold. Despite the unusual appearance, his presence immediately commands respect. This is clearly faculty - and high-ranking faculty at that.

"Gojo-sensei," Megumi acknowledges with a slight bow.

"Don't mind me," Gojo says with what you can hear is a grin in his voice. "I'm just here to make sure nobody gets permanently damaged on their first day. Though I have to say, your analytical approach is refreshing. Most students would have rushed in by now."

The cursed spirit, perhaps sensing the growing number of sorcerers in the area, becomes more agitated. Its multiple mouths begin speaking in an overlapping chorus: "Too... many... witnesses... must... eliminate... quickly... before... reinforcements..."

Akiko makes her move, trying to dart along the wall toward what she hopes is safety. The cursed spirit's attention snaps to her immediately, and it begins to move with alarming speed.

Your analytical observation has given you valuable tactical information, but now the situation is escalating rapidly. The knowledge you've gained about the creature's weaknesses could be the key to defeating it efficiently, but timing is now critical.

What's your tactical decision?"""

        analytical_choices = [
            StoryChoice(
                "Share tactical information with Megumi and coordinate an attack",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_tactical",
                    "ally": "megumi",
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 10},
                    "relationships": {"megumi": 25, "gojo": 10},
                    "story_flags": {"tactical_coordination": True, "megumi_partnership": True},
                    "next_scene": "post_tactical_battle",
                    "experience": 85
                }
            ),
            StoryChoice(
                "Use your analysis to execute a precise solo strike",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_analyzed",
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 15, Trait.DETERMINED: 5},
                    "relationships": {"megumi": 15, "gojo": 15},
                    "story_flags": {"tactical_solo": True, "precision_striker": True},
                    "next_scene": "post_precision_battle",
                    "experience": 70
                }
            ),
            StoryChoice(
                "Direct the pink-haired student's obvious eagerness strategically",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_distracted",
                    "ally": "yuji_directed",
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 5, Trait.DETERMINED: 5},
                    "relationships": {"yuji": 20, "megumi": 15},
                    "story_flags": {"tactical_leadership": True, "yuji_coordination": True},
                    "next_scene": "post_directed_battle",
                    "experience": 75
                }
            ),
            StoryChoice(
                "Create a diversion to help Akiko escape while others prepare",
                {
                    "traits": {Trait.ANALYTICAL: 5, Trait.PROTECTIVE: 10, Trait.CAUTIOUS: 10},
                    "relationships": {"akiko": 20, "megumi": 10},
                    "story_flags": {"diversion_tactician": True, "escape_facilitator": True},
                    "next_scene": "tactical_diversion_sequence",
                    "experience": 55
                }
            )
        ]
        
        self.scenes["intro_analytical_path"] = StoryScene(
            "The Strategist's Approach",
            analytical_description,
            analytical_choices,
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # =================================================================
        # SCENE 2C: AGGRESSIVE PATH - THE WARRIOR'S CHARGE
        # =================================================================
        
        aggressive_description = """Raw instinct takes over as you launch yourself toward the cursed spirit with a battle cry that echoes across the courtyard. Your cursed energy surges through your body like wildfire, heightening your senses and flooding your muscles with supernatural strength. This is what you came here for - this is what being a jujutsu sorcerer means!

The cursed spirit's multiple eyes widen in surprise at your direct approach. Clearly, it expected hesitation or fear from a first-year student. Instead, you're bearing down on it with the fury of someone who's been waiting their entire life for this moment.

"Finally!" comes an enthusiastic shout from nearby. You catch a glimpse of a girl with short brown hair and an enormous grin as she raises what appears to be a hammer. "Someone who doesn't overthink everything!"

The student by the wall - Akiko - stares at you with a mixture of awe and terror. "You're insane!" she calls out, but there's admiration in her voice. "It could kill you!"

Your aggressive charge has completely shifted the dynamic of the situation. The cursed spirit, caught off guard by your directness, rears back and lets out a sound that's part roar, part shriek. Its multiple limbs spread wide in a threatening display, but you can see uncertainty in its movements. It was prepared for a cowering victim, not a fierce opponent.

"That's the spirit!" The brown-haired girl is now running parallel to your charge, her hammer gleaming with cursed energy. "I'm Nobara Kugisaki, and I like your style! Let's crush this thing!"

From the sidelines, you're vaguely aware of other students watching. A pink-haired boy looks excited and is bouncing on his feet as if he wants to join in. A dark-haired student is shaking his head but reaching for what looks like a small pouch - preparing to support despite his apparent disapproval of your direct approach.

"Interesting," comes a calm voice that somehow carries clearly over the chaos. You risk a quick glance and see a tall man with white hair and a blindfold. A teacher, clearly, and one who seems completely unconcerned about the violence about to erupt. "Aggressive approach, but there's calculation behind it. Let's see if passion can overcome tactical disadvantage."

The cursed spirit makes its move, lunging forward with surprising speed. Its elongated limbs stretch toward you like twisted rubber, and multiple mouths along its torso open to reveal rows of needle-sharp teeth. This is it - your first real combat as a jujutsu sorcerer.

But your aggressive approach has done more than surprise the curse. You've inspired others to action, changed the entire dynamic of the encounter, and demonstrated a fearless spirit that marks you as someone to watch. The way you handle the next few moments will cement your reputation among your peers.

The spirit's attack comes in fast - a sweeping strike from its primary limbs intended to knock you off balance and leave you vulnerable to its follow-up bite attacks. Your aggressive momentum gives you options, but you need to decide quickly how to proceed.

What's your combat strategy?"""

        aggressive_choices = [
            StoryChoice(
                "Meet its attack head-on with pure aggression",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_aggressive_clash",
                    "traits": {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 10, Trait.RECKLESS: 10},
                    "relationships": {"nobara": 25},
                    "story_flags": {"pure_aggression": True, "fearless_fighter": True},
                    "next_scene": "post_aggressive_clash",
                    "experience": 65
                }
            ),
            StoryChoice(
                "Coordinate your aggression with Nobara's attack",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_dual_assault",
                    "ally": "nobara",
                    "traits": {Trait.AGGRESSIVE: 10, Trait.DETERMINED: 10, Trait.FOCUSED: 5},
                    "relationships": {"nobara": 30},
                    "story_flags": {"aggressive_teamwork": True, "nobara_partnership": True},
                    "next_scene": "post_nobara_team_battle",
                    "experience": 80
                }
            ),
            StoryChoice(
                "Use your momentum to get past it and protect Akiko",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_defensive",
                    "traits": {Trait.AGGRESSIVE: 10, Trait.PROTECTIVE: 15, Trait.DETERMINED: 5},
                    "relationships": {"akiko": 25, "nobara": 15},
                    "story_flags": {"aggressive_protection": True, "heroic_charge": True},
                    "next_scene": "post_protective_charge",
                    "experience": 70
                }
            ),
            StoryChoice(
                "Channel your aggression into a devastating first strike",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_surprised",
                    "traits": {Trait.AGGRESSIVE: 12, Trait.FOCUSED: 8, Trait.DETERMINED: 10},
                    "relationships": {"nobara": 20, "yuji": 10},
                    "story_flags": {"devastating_opener": True, "first_strike_master": True},
                    "next_scene": "post_devastating_strike",
                    "experience": 75
                }
            )
        ]
        
        self.scenes["intro_aggressive_path"] = StoryScene(
            "The Warrior's Charge",
            aggressive_description,
            aggressive_choices,
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # =================================================================
        # SCENE 2D: COORDINATION PATH - THE TEAM BUILDER
        # =================================================================
        
        coordination_description = """Rather than rushing in alone, you quickly scan the area for potential allies and support. Your instincts tell you that coordination and teamwork will be far more effective than any solo heroics, especially against a cursed spirit that clearly has combat experience.

"Hey!" you call out to the other students you've spotted around the courtyard. "This is a Grade 3 - we should work together!"

Your call for coordination immediately catches the attention of several nearby students. A pink-haired boy with an eager expression jogs over, his energy signature radiating warmth and incredible power. "Great idea! I'm Yuji Itadori. I was just thinking the same thing!"

From another direction, a dark-haired student approaches with measured steps, his green eyes already analyzing the situation. "Megumi Fushiguro," he introduces himself briefly. "Coordination is wise. That curse has been around long enough to develop tactical awareness."

A third student joins your impromptu group - a girl with short brown hair and confident posture. "Nobara Kugisaki," she says with a grin. "I like someone who thinks before they act. Though I also like smashing curses, so this works out perfectly."

The trapped student - Akiko - calls out from her position against the wall. "There are more of you! Thank goodness. I'm sorry I got caught like this - I'm still learning and I wandered into the wrong area during training."

Your coordination approach has immediately created a team dynamic that transforms the encounter from a chaotic scramble into an organized operation. The cursed spirit seems to sense this shift, its multiple eyes tracking between the four of you as it tries to assess this new threat level.

"Smart thinking," comes an approving voice from the sidelines. You turn to see a tall man with distinctive white hair and a blindfold. His relaxed posture suggests someone in authority who's confident in his students' abilities. "Teamwork is the foundation of effective sorcery. Individual strength means nothing if you can't work with others."

Megumi nods toward the curse. "Based on its positioning and behavior, it's been planning this encounter. See how it chose that corner? Multiple escape routes for itself, limited options for the victim. It's not just hunting - it's tactical."

Yuji cracks his knuckles with enthusiasm. "Tactical or not, it picked the wrong students to mess with today!"

Nobara hefts her hammer, cursed energy already beginning to flow around it. "So what's the plan, team leader?" she asks you with an expectant look.

The cursed spirit, perhaps realizing that the situation has shifted dramatically against its favor, begins to move more aggressively. Its multiple limbs spread wide in a threatening display, and the mouths along its torso begin speaking in an overlapping chorus: "Too... many... sorcerers... must... eliminate... quickly... before... more... arrive..."

Your coordination approach has given you the luxury of planning, but it's also given the curse time to prepare its own strategy. You can see it positioning itself for what will likely be a multi-target attack, trying to use its superior reach to engage all of you simultaneously.

Akiko presses herself further against the wall, clearly trying to stay out of the way while still providing what support she can. "I may not be much help in a fight, but I can create a distraction if you need one!"

The team looks to you expectantly. Your coordination approach has earned you a de facto leadership position, and how you direct this engagement will set the tone for future relationships with these talented sorcerers.

What's your tactical plan?"""

        coordination_choices = [
            StoryChoice(
                "Assign roles based on each person's strengths and coordinate a multi-angle attack",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_coordinated",
                    "ally": "full_team",
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 10, Trait.PROTECTIVE: 5},
                    "relationships": {"yuji": 20, "megumi": 20, "nobara": 20, "akiko": 15},
                    "story_flags": {"team_leader": True, "coordination_master": True, "tactical_genius": True},
                    "next_scene": "post_coordinated_victory",
                    "experience": 90
                }
            ),
            StoryChoice(
                "Focus on protecting Akiko while the others engage the curse",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_distracted",
                    "ally": "protection_team",
                    "traits": {Trait.PROTECTIVE: 15, Trait.CAUTIOUS: 10, Trait.ANALYTICAL: 5},
                    "relationships": {"akiko": 30, "yuji": 15, "megumi": 15, "nobara": 15},
                    "story_flags": {"protection_leader": True, "defensive_coordinator": True},
                    "next_scene": "post_protection_coordination",
                    "experience": 75
                }
            ),
            StoryChoice(
                "Create a pincer movement to limit the curse's escape options",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_trapped",
                    "ally": "tactical_team",
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 10, Trait.DETERMINED: 5},
                    "relationships": {"megumi": 25, "yuji": 15, "nobara": 15},
                    "story_flags": {"tactical_leader": True, "pincer_master": True, "strategic_mind": True},
                    "next_scene": "post_pincer_victory",
                    "experience": 85
                }
            ),
            StoryChoice(
                "Suggest everyone attack together in a overwhelming assault",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_overwhelmed",
                    "ally": "assault_team",
                    "traits": {Trait.DETERMINED: 15, Trait.AGGRESSIVE: 5, Trait.FOCUSED: 5},
                    "relationships": {"yuji": 25, "nobara": 20, "megumi": 10},
                    "story_flags": {"assault_coordinator": True, "overwhelming_force": True},
                    "next_scene": "post_coordinated_assault",
                    "experience": 80
                }
            )
        ]
        
        self.scenes["intro_coordination_path"] = StoryScene(
            "The Team Builder",
            coordination_description,
            coordination_choices,
            "Tokyo Jujutsu High - Training Grounds"
        )
        
        # =================================================================
        # FOLLOW-UP SCENES: POST-BATTLE OUTCOMES
        # =================================================================
        
        # These scenes show the consequences of the player's choices
        # and continue building relationships and story progression
        
        self._add_post_battle_scenes()
        self._add_character_development_scenes()
        self._add_exploration_sequences()
        self._add_training_scenarios()
        
    def _add_post_battle_scenes(self):
        """Add post-battle outcome scenes based on different approaches."""
        
        # Post-Yuji Team Battle
        post_yuji_description = """The dust settles around the defeated cursed spirit, its form already beginning to dissipate into wisps of malevolent energy. You and Yuji stand side by side, both breathing heavily but victorious. Your combined assault proved devastating - Yuji's incredible physical strength complemented your technique perfectly.

"That was amazing!" Yuji grins, his enthusiasm infectious despite the serious situation you just faced. "Your cursed energy has this really interesting flow to it. I've never seen anything quite like it!"

Akiko approaches cautiously, still shaken but clearly grateful. "Thank you both so much. I know I shouldn't have been out here alone, but I got lost after training and then that thing just appeared..." She bows deeply. "I'm Akiko Tanaka. I'll never forget what you did for me today."

From across the courtyard, the white-haired teacher approaches with an amused expression. "Well, that was entertaining! I'm Gojo Satoru, by the way. Your teacher for advanced combat techniques." He turns to you specifically. "Quick thinking, immediate action, and excellent teamwork instincts. Plus you managed to bring out Yuji's cooperative side right off the bat. That's no small feat."

Yuji scratches the back of his head sheepishly. "I guess I do get a little carried away sometimes. But working together felt natural! Like we were meant to be a team."

"Speaking of teams," Gojo continues, "you'll be assigned to a three-person squad for missions and advanced training. Based on what I just saw, I have some ideas about optimal configurations." His blindfolded gaze seems to focus on you intently. "Your instinct to protect others while maintaining tactical awareness is exactly what I look for in squad leaders."

The dark-haired student you noticed earlier - Megumi - approaches the group. "That was well executed," he says simply. "Most first-years would have either hesitated too long or rushed in without backup. You found the right balance."

Nobara joins the growing group, her hammer still crackling with residual cursed energy. "Not bad for a first day! Though next time, save some of the fun for the rest of us," she says with a competitive grin.

As the adrenaline fades, you begin to notice the aches and pains from your first real combat. But more than that, you feel a sense of accomplishment and belonging. These people - Yuji's enthusiasm, Akiko's gratitude, even Megumi's measured approval - they're going to be your companions in this dangerous but incredible world.

Gojo claps his hands together. "Alright, everyone! Excitement's over for now. Time for the boring stuff - paperwork, medical checks, and orientation schedules. But first..." He turns to you again. "Excellent work today. Your actions here will definitely be noted in your file."

What do you want to focus on next?"""

        post_yuji_choices = [
            StoryChoice(
                "Ask Yuji about his technique and try to build a stronger partnership",
                {
                    "traits": {Trait.FOCUSED: 10, Trait.ANALYTICAL: 5},
                    "relationships": {"yuji": 15},
                    "story_flags": {"yuji_technique_interest": True, "partnership_building": True},
                    "next_scene": "yuji_technique_discussion",
                    "experience": 30
                }
            ),
            StoryChoice(
                "Check on Akiko and make sure she's really okay",
                {
                    "traits": {Trait.COMPASSIONATE: 10, Trait.PROTECTIVE: 5},
                    "relationships": {"akiko": 20},
                    "story_flags": {"akiko_care": True, "protective_instincts": True},
                    "next_scene": "akiko_care_sequence",
                    "experience": 25
                }
            ),
            StoryChoice(
                "Talk to Gojo about squad assignments and training",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.DETERMINED: 5},
                    "relationships": {"gojo": 15},
                    "story_flags": {"gojo_mentorship": True, "training_focused": True},
                    "next_scene": "gojo_mentorship_start",
                    "experience": 35
                }
            ),
            StoryChoice(
                "Introduce yourself properly to Megumi and Nobara",
                {
                    "traits": {Trait.FOCUSED: 5, Trait.ANALYTICAL: 5},
                    "relationships": {"megumi": 10, "nobara": 10},
                    "story_flags": {"social_building": True, "group_integration": True},
                    "next_scene": "peer_introduction_sequence",
                    "experience": 20
                }
            )
        ]
        
        self.scenes["post_yuji_team_battle"] = StoryScene(
            "Victory Through Partnership",
            post_yuji_description,
            post_yuji_choices,
            "Tokyo Jujutsu High - Training Grounds"
        )
        
    def _add_character_development_scenes(self):
        """Add scenes focused on character development and relationship building."""
        
        # Character interaction scenes that develop based on previous choices
        # These scenes are shorter but crucial for relationship progression
        
        yuji_discussion_description = """You and Yuji find a quiet spot under one of the large trees in the courtyard. The excitement of your first battle is still fresh, but now you have a chance to really talk with your new teammate.

"So," Yuji begins, settling down on the grass, "that was your first cursed spirit fight too, right? You handled it like you'd been doing this for years!" His genuine admiration is clear in his voice.

You find yourself relaxing in his presence. There's something refreshing about Yuji's straightforward, honest personality. No hidden agendas or complex political maneuvering - just sincere appreciation for good teamwork.

"Your cursed energy is really interesting," you tell him. "It felt incredibly powerful, but there was something else... something almost familiar about it."

Yuji's expression grows slightly more serious. "Yeah, there's... something special about my situation. I can't really go into all the details yet, but let's just say I'm carrying more than just my own power." He looks at his hands thoughtfully. "Sometimes that makes things complicated."

The weight of unspoken secrets hangs in the air, but Yuji brightens quickly. "But that's exactly why teamwork is so important! When we fought together back there, I felt like I could focus all my power without worrying about... other things. Does that make sense?"

You nod, sensing that there's much more to Yuji's story than he can share right now. But his trust in you, even this early in your relationship, feels significant.

"I hope we end up on the same squad," Yuji continues. "I have a feeling we could become really strong together. And honestly, it's nice to have someone who gets the whole 'protect people first, ask questions later' approach."

What do you want to discuss with Yuji?"""

        yuji_discussion_choices = [
            StoryChoice(
                "Ask about the 'something special' in his situation",
                {
                    "traits": {Trait.ANALYTICAL: 5},
                    "relationships": {"yuji": 10},
                    "story_flags": {"yuji_secret_interest": True},
                    "next_scene": "yuji_reveals_sukuna",
                    "experience": 15
                }
            ),
            StoryChoice(
                "Share your own background and motivations for becoming a sorcerer",
                {
                    "traits": {Trait.COMPASSIONATE: 5, Trait.FOCUSED: 5},
                    "relationships": {"yuji": 15},
                    "story_flags": {"personal_sharing": True},
                    "next_scene": "personal_backstory_share",
                    "experience": 20
                }
            ),
            StoryChoice(
                "Suggest training together to improve your teamwork",
                {
                    "traits": {Trait.DETERMINED: 10, Trait.FOCUSED: 5},
                    "relationships": {"yuji": 12},
                    "story_flags": {"training_partnership": True},
                    "next_scene": "yuji_training_partnership",
                    "experience": 25
                }
            )
        ]
        
        self.scenes["yuji_technique_discussion"] = StoryScene(
            "Getting to Know Yuji",
            yuji_discussion_description,
            yuji_discussion_choices,
            "Tokyo Jujutsu High - Courtyard"
        )
        
    def _add_exploration_sequences(self):
        """Add exploration scenes that expand the world and provide discovery opportunities."""
        
        # Campus exploration scene
        campus_exploration_description = """With the immediate excitement of your first cursed spirit encounter behind you, you decide to explore the Tokyo Jujutsu High campus more thoroughly. The grounds are larger than you initially realized, with multiple buildings connected by covered walkways and hidden courtyards.

Your footsteps echo against the traditional wooden floors as you walk through one of the main buildings. The architecture is a fascinating blend of classical Japanese design and modern security features. You notice subtle barrier inscriptions carved into doorframes and window sills - protection spells that create a nearly impenetrable fortress around the school.

In one corridor, you discover a wall lined with portraits of former students and faculty. Some of the faces look young - too young - with dates that suggest they died in service far too early. The weight of what you've chosen to pursue settles on you more heavily as you realize these were real people who paid the ultimate price in the fight against cursed spirits.

"Sobering, isn't it?" comes a voice from behind you. You turn to see a man in a business suit with distinctively parted blonde hair and small round glasses. His presence emanates the calm authority of someone accustomed to life-or-death situations. "I'm Nanami Kento. I teach practical combat applications and mission strategy."

You introduce yourself, and Nanami nods approvingly. "I heard about your performance in the courtyard earlier. Gojo mentioned you showed both tactical awareness and protective instincts - a rare combination in first-year students."

As you continue your exploration with Nanami as an impromptu guide, he points out various important locations: the medical wing where injured sorcerers are treated, the equipment vault where cursed tools are stored and maintained, and the mission briefing rooms where assignments are planned and debriefed.

"Understanding the infrastructure is crucial," Nanami explains. "Jujutsu sorcery isn't just about individual power - it's about being part of a larger system dedicated to protecting innocent people from threats they can't even perceive."

You pause at a large window overlooking the training grounds where you can see other students practicing various techniques. Some are working on basic cursed energy manipulation, while others are engaged in complex combat scenarios against training dummies designed to mimic cursed spirit behavior.

"The most important thing to remember," Nanami continues, "is that every technique you learn, every relationship you build, every mission you complete - they all serve the same fundamental purpose. Protection of those who cannot protect themselves."

What aspect of the school would you like to explore further?"""

        exploration_choices = [
            StoryChoice(
                "Visit the library to research cursed techniques and history",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 5},
                    "story_flags": {"library_access": True, "research_focused": True},
                    "next_scene": "library_research_sequence",
                    "experience": 30,
                    "items": ["Research Notes"]
                }
            ),
            StoryChoice(
                "Check out the training facilities to understand available resources",
                {
                    "traits": {Trait.DETERMINED: 10, Trait.FOCUSED: 5},
                    "story_flags": {"training_facility_access": True, "equipment_knowledge": True},
                    "next_scene": "training_facility_tour",
                    "experience": 25
                }
            ),
            StoryChoice(
                "Ask Nanami about practical mission experience and real-world applications",
                {
                    "traits": {Trait.ANALYTICAL: 5, Trait.CAUTIOUS: 5, Trait.FOCUSED: 5},
                    "relationships": {"nanami": 15},
                    "story_flags": {"nanami_mentorship": True, "mission_insight": True},
                    "next_scene": "nanami_mission_discussion",
                    "experience": 35
                }
            ),
            StoryChoice(
                "Explore the student dormitories and social areas",
                {
                    "traits": {Trait.COMPASSIONATE: 5, Trait.FOCUSED: 5},
                    "story_flags": {"social_exploration": True, "dormitory_knowledge": True},
                    "next_scene": "dormitory_social_sequence",
                    "experience": 20
                }
            )
        ]
        
        self.scenes["campus_exploration"] = StoryScene(
            "Discovering Tokyo Jujutsu High",
            campus_exploration_description,
            exploration_choices,
            "Tokyo Jujutsu High - Main Building"
        )
        
    def _add_training_scenarios(self):
        """Add training scenarios that develop combat skills and relationships."""
        
        # First formal training session
        training_description = """The next morning, you find yourself in one of the school's specialized training rooms alongside your fellow first-years. The space is larger than it appeared from outside, with reinforced walls covered in barrier inscriptions and a floor designed to withstand the impact of cursed energy techniques.

Gojo-sensei stands at the center of the room, his relaxed posture contrasting with the serious nature of what you're about to undertake. "Welcome to your first formal training session! Today we're going to assess your current abilities and begin developing your individual fighting styles."

Yuji bounces excitedly beside you, clearly eager to get started. "This is going to be great! I can't wait to see what everyone can really do!"

Megumi maintains his typically serious expression, but you can sense an undercurrent of anticipation. "Proper training is essential. Self-taught techniques often develop bad habits that become harder to correct later."

Nobara cracks her knuckles with a confident grin. "Finally! I've been waiting to show off what I can really do. Hope everyone's ready to be impressed!"

"Alright, settle down," Gojo says with amusement. "Before we begin, I want to explain the philosophy behind our training methods. Unlike other schools that focus primarily on rigid technique memorization, we believe in developing each sorcerer's natural instincts and personal style."

He gestures to the various training equipment around the room - practice dummies, target arrays, obstacle courses, and meditation platforms. "Today's session will help me understand how each of you naturally approaches combat, problem-solving, and cursed energy manipulation. Based on what I observe, we'll design personalized training regimens."

"But first," Gojo continues with what you're beginning to recognize as his characteristic mischievous tone, "let's start with something fun. Everyone pair up for some light sparring. No techniques that could cause permanent damage, but don't hold back on creativity!"

The room buzzes with excitement as students begin pairing off. You notice that your choice of sparring partner will likely influence both your training experience and your relationships with your classmates.

Who do you want to spar with for your first training session?"""

        training_choices = [
            StoryChoice(
                "Partner with Yuji to build on your previous teamwork",
                {
                    "combat": True,
                    "enemy": "yuji_sparring",
                    "traits": {Trait.DETERMINED: 10, Trait.FOCUSED: 5},
                    "relationships": {"yuji": 15},
                    "story_flags": {"yuji_sparring_partner": True, "teamwork_training": True},
                    "next_scene": "yuji_sparring_session",
                    "experience": 40
                }
            ),
            StoryChoice(
                "Challenge Megumi to test your tactical abilities",
                {
                    "combat": True,
                    "enemy": "megumi_sparring",
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 10},
                    "relationships": {"megumi": 15},
                    "story_flags": {"megumi_sparring_partner": True, "tactical_training": True},
                    "next_scene": "megumi_sparring_session",
                    "experience": 45
                }
            ),
            StoryChoice(
                "Face off against Nobara to experience her aggressive style",
                {
                    "combat": True,
                    "enemy": "nobara_sparring",
                    "traits": {Trait.AGGRESSIVE: 10, Trait.DETERMINED: 5},
                    "relationships": {"nobara": 15},
                    "story_flags": {"nobara_sparring_partner": True, "aggressive_training": True},
                    "next_scene": "nobara_sparring_session",
                    "experience": 42
                }
            ),
            StoryChoice(
                "Ask to spar with multiple opponents to test your limits",
                {
                    "combat": True,
                    "enemy": "multiple_sparring",
                    "traits": {Trait.DETERMINED: 15, Trait.RECKLESS: 5},
                    "relationships": {"gojo": 10},
                    "story_flags": {"ambitious_training": True, "multi_opponent_experience": True},
                    "next_scene": "multiple_opponent_sparring",
                    "experience": 55
                }
            )
        ]
        
        self.scenes["first_training_session"] = StoryScene(
            "First Day of Training",
            training_description,
            training_choices,
            "Tokyo Jujutsu High - Training Room A"
        )
        
    def get_all_scenes(self):
        """Return all scenes in the Introduction Arc."""
        return self.scenes

    def get_scene_count(self):
        """Return the total number of scenes in this arc."""
        return len(self.scenes)
        
    def get_total_content_lines(self):
        """Calculate approximate line count of all story content."""
        total_lines = 0
        for scene in self.scenes.values():
            # Count description lines (rough estimate)
            total_lines += len(scene.description.split('\n'))
            # Count choice text lines
            for choice in scene.choices:
                total_lines += len(choice.text.split('\n'))
        return total_lines