"""
Arc 2: Vs. Mahito/Junpei Arc - The Nature of Humanity

This arc explores the complex themes of humanity, cursed spirits, and moral choices
through the tragic story of Junpei Yoshino and his manipulation by Mahito.
Expanded to provide deep character development and multiple branching outcomes.
"""

from typing import Dict, List, Any
from character import Trait
from story import StoryChoice, StoryScene


def get_arc2_scenes() -> Dict[str, StoryScene]:
    """Return all scenes for Arc 2: Vs. Mahito/Junpei Arc."""
    scenes = {}
    
    # ============================================================================
    # ARC 2 INTRODUCTION - Setting the Stage
    # ============================================================================
    
    scenes["arc2_intro"] = StoryScene(
        "Shadows Gathering",
        """Several weeks have passed since your arrival at Tokyo Jujutsu High, and you've begun 
to settle into the rhythm of training, missions, and the constant threat of cursed spirits. 
The autumn leaves are falling when Gojo-sensei calls you into his office for what he describes 
as "a delicate situation that requires a particular kind of sensitivity."

The office is surprisingly normal for someone of Gojo's reputation - a desk covered in papers, 
books on jujutsu theory, and a half-eaten bag of kikufuku mochi. What's not normal is the 
serious expression on his face, visible even through his blindfold.

"We've been monitoring some unusual cursed spirit activity in the city," he begins, pulling 
out a file thick with reports and photographs. "Multiple incidents involving curse-related 
deaths, but not random attacks. These are targeted, methodical, and show signs of 
intelligence far beyond typical cursed spirits."

He slides a photograph across the desk. It shows a gruesome scene - bodies twisted in 
impossible ways, faces frozen in expressions of terror and confusion. But what catches your 
attention is the precision of it all. This isn't the chaotic destruction usually left by 
cursed spirits.

"More concerning," Gojo continues, "is that we've identified a potential human ally to 
whatever is causing this. A high school student named Junpei Yoshino. His school has reported 
him as a truant, and he was last seen near several of the incident sites."

The weight of implications settles on you. A human working with cursed spirits is almost 
unheard of, and the reasons someone might make such a choice are usually tragic.

"This mission requires more than just combat skills," Gojo says, studying your reaction. 
"It requires understanding, empathy, and the ability to see beyond the surface of things. 
Are you ready for something like this?"

The question hangs in the air, heavy with unspoken complexities. This isn't just about 
defeating enemies - it's about understanding them, and potentially saving someone who might 
not want to be saved.

How do you respond to this assignment?""",
        [
            StoryChoice(
                "I want to understand why a human would ally with cursed spirits",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.ANALYTICAL: 15, Trait.ANALYTICAL: 15},
                    "relationships": {"gojo": 15},
                    "next_scene": "investigation_empathy",
                    "story_flags": {"approach": "understanding", "mission_mindset": "empathetic"}
                }
            ),
            StoryChoice(
                "What's our strategy for stopping these targeted killings?",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15, Trait.FOCUSED: 15},
                    "relationships": {"gojo": 10},
                    "next_scene": "investigation_tactical",
                    "story_flags": {"approach": "strategic", "mission_mindset": "tactical"}
                }
            ),
            StoryChoice(
                "Someone manipulating a student... that's unforgivable",
                {
                    "traits": {Trait.PROTECTIVE: 20, Trait.PROTECTIVE: 15, Trait.RECKLESS: 10},
                    "relationships": {"gojo": 12},
                    "next_scene": "investigation_protective",
                    "story_flags": {"approach": "protective", "mission_mindset": "righteous"}
                }
            ),
            StoryChoice(
                "I need all available information before making any judgments",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 15, Trait.ANALYTICAL: 15},
                    "relationships": {"gojo": 18},
                    "next_scene": "investigation_analytical",
                    "story_flags": {"approach": "analytical", "mission_mindset": "methodical"}
                }
            )
        ],
        "Tokyo Jujutsu High - Gojo's Office"
    )
    
    # ============================================================================
    # INVESTIGATION PHASE - Different Approaches
    # ============================================================================
    
    scenes["investigation_empathy"] = StoryScene(
        "Walking in Another's Shoes",
        """Your response seems to please Gojo, who leans back in his chair with something 
approaching approval. "That's exactly the kind of thinking this situation needs. Too many 
sorcerers see the world in black and white - cursed spirits are evil, humans are good, 
end of story. But reality is much more complicated."

He opens the file further, revealing more detailed information about Junpei Yoshino. 
School records show a pattern of bullying, social isolation, and declining grades. 
Teacher reports describe him as "withdrawn" and "concerning," but nobody seemed to 
have tried to actually help.

"Junpei is seventeen years old," Gojo explains, his voice taking on a more serious tone. 
"His father died two years ago in what was officially ruled an accident, but the timing 
coincides with increased cursed spirit activity in his neighborhood. His mother works 
double shifts to keep them afloat, so he's essentially raising himself."

The photographs show a thin, pale teenager with dark circles under his eyes and an 
expression of someone who's given up on finding kindness in the world. It's the face 
of someone who's been disappointed too many times to hope for better.

"The bullying at his school is severe," Gojo continues. "Physical violence, social 
ostracism, teachers who look the other way. From what we can determine, Junpei has 
been living in a world where cruelty is the norm and kindness is the exception."

You study the information, trying to imagine what it would be like to live with that 
level of constant fear and isolation. The idea of someone offering power and revenge 
to a person in that situation becomes frighteningly understandable.

"So when something - or someone - offered him a way to fight back..." you begin.

"Exactly," Gojo nods. "The question is whether we can reach him before it's too late, 
and whether we can offer him something better than what he's already found."

The complexity of the situation is daunting. This isn't just about stopping a threat - 
it's about understanding pain deep enough to drive someone to desperate choices.

What's your first step in trying to understand Junpei?""",
        [
            StoryChoice(
                "Visit his school to understand the bullying situation firsthand",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 15, Trait.ANALYTICAL: 10},
                    "next_scene": "school_investigation",
                    "story_flags": {"investigation_method": "school", "understanding_bullying": True}
                }
            ),
            StoryChoice(
                "Research his father's death and the circumstances around it",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10, Trait.FOCUSED: 5},
                    "next_scene": "father_investigation",
                    "story_flags": {"investigation_method": "family", "father_mystery": True}
                }
            ),
            StoryChoice(
                "Try to find and observe Junpei directly",
                {
                    "traits": {Trait.AGGRESSIVE: 15, Trait.ANALYTICAL: 15, Trait.RECKLESS: 10},
                    "next_scene": "direct_observation",
                    "story_flags": {"investigation_method": "direct", "personal_approach": True}
                }
            ),
            StoryChoice(
                "Study the curse-related incidents to understand the pattern",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.ANALYTICAL: 15, Trait.ANALYTICAL: 10},
                    "next_scene": "incident_analysis",
                    "story_flags": {"investigation_method": "incidents", "pattern_focus": True}
                }
            )
        ],
        "Tokyo Jujutsu High - Gojo's Office"
    )
    
    # ============================================================================
    # SCHOOL INVESTIGATION - Understanding the Bullying
    # ============================================================================
    
    scenes["school_investigation"] = StoryScene(
        "The Halls of Cruelty",
        """Satozakura High School looks like any other public school in Japan - concrete 
buildings, small windows, and the familiar sounds of teenagers going about their daily 
routines. But as you walk through the halls disguised as a transfer student, you quickly 
sense the undercurrents of tension and fear that permeate the environment.

It doesn't take long to identify the social dynamics at play. There's a clear hierarchy 
of power, with certain students wielding influence through intimidation and others 
cowering in corners, trying to become invisible. The teachers you observe seem either 
oblivious to the bullying or actively ignoring it.

During lunch, you find yourself in the cafeteria when the daily ritual begins. A group 
of three students approaches a table where a lone figure sits - not Junpei, but clearly 
another victim of the same system. You watch as they "accidentally" knock over his lunch, 
then laugh as he scrambles to clean up the mess.

"Every day, same thing," whispers a girl sitting near you. She's speaking to her friend, 
but loud enough for you to hear. "They used to do it to Yoshino too, before he stopped 
coming to school. Poor guy just... disappeared one day. Can't say I blame him."

"Yoshino was weird though," her friend replies. "Always talking about movies and stuff 
nobody cared about. Made himself a target, you know?"

The casual way they discuss systematic cruelty as if it's natural law makes your stomach 
turn. This is the environment that shaped Junpei's worldview - a place where victims are 
blamed for their victimization and kindness is seen as weakness.

After school, you follow the main group of bullies to see how far their cruelty extends. 
What you discover is worse than you imagined - they don't just target fellow students, 
but younger kids walking home, store clerks who can't fight back, and anyone they perceive 
as vulnerable.

One of them, a boy with bleached hair and cruel eyes, seems to take particular pleasure 
in causing pain. "This is boring," he complains to his friends. "I wish something exciting 
would happen. Like that Yoshino freak finally snapping and doing something crazy."

The others laugh, but there's something in the way he says it that suggests this isn't 
just idle talk. There's anticipation there, as if he's waiting for violence to escalate.

As you observe this toxic ecosystem, you begin to understand how someone like Junpei 
might come to see cursed spirits as preferable to humans. At least cursed spirits are 
honest about their malice.

What's your next move?""",
        [
            StoryChoice(
                "Confront the bullies directly about their behavior",
                {
                    "traits": {Trait.AGGRESSIVE: 15, Trait.PROTECTIVE: 20, Trait.AGGRESSIVE: 10},
                    "next_scene": "bully_confrontation",
                    "story_flags": {"confronted_bullies": True, "direct_action": True}
                }
            ),
            StoryChoice(
                "Try to befriend some of the victims to understand their perspective",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 10},
                    "next_scene": "victim_befriending",
                    "story_flags": {"befriended_victims": True, "gentle_approach": True}
                }
            ),
            StoryChoice(
                "Investigate the teachers' role in allowing this to continue",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.ANALYTICAL: 15, Trait.ANALYTICAL: 15},
                    "next_scene": "teacher_investigation",
                    "story_flags": {"investigated_faculty": True, "systematic_approach": True}
                }
            ),
            StoryChoice(
                "Focus on gathering more information about Junpei specifically",
                {
                    "traits": {Trait.FOCUSED: 20, Trait.FOCUSED: 15, Trait.ANALYTICAL: 10},
                    "next_scene": "junpei_specific_search",
                    "story_flags": {"junpei_focused": True, "mission_priority": True}
                }
            )
        ],
        "Satozakura High School - Cafeteria"
    )
    
    # ============================================================================
    # FIRST ENCOUNTER WITH JUNPEI
    # ============================================================================
    
    scenes["junpei_first_meeting"] = StoryScene(
        "The Boy Who Talks to Monsters",
        """You find Junpei exactly where Gojo's intelligence suggested you might - sitting alone 
on a bench in Kasumigaoka Park, feeding bread to pigeons while rain begins to fall. He doesn't 
seem to notice or care about getting wet, lost in his own thoughts as he mechanically breaks 
pieces of bread and scatters them for the increasingly excited birds.

Up close, he's even thinner than his photographs suggested, with the hollow-cheeked look of 
someone who doesn't eat regularly. His school uniform is clean but worn, and there's a careful 
distance he maintains between himself and the world around him - the body language of someone 
who's learned to expect pain.

What strikes you most is his gentleness with the pigeons. Despite everything he's been through, 
despite whatever dark path he's walking now, there's still kindness in the way he makes sure 
each bird gets fed, how he speaks softly to them in a voice that suggests he finds more 
understanding from animals than he does from people.

"They don't judge, you know," he says suddenly, not looking up at you but clearly aware of 
your presence. "Pigeons. They don't care if you're popular or smart or if you fit in. They 
just want food and warmth and to be left alone. Seems like a pretty reasonable way to live."

You realize this is your chance to make a first impression that could determine everything 
that follows. Junpei is clearly expecting another disappointment from human contact, another 
reason to confirm his belief that people are fundamentally cruel and selfish.

But there's also something in his voice - a tiny note of hope that maybe, just maybe, this 
time might be different. It's the voice of someone who desperately wants to be proven wrong 
about humanity, even though experience has taught him to expect the worst.

The rain is getting heavier, and you can see him getting soaked through his uniform. He doesn't 
seem to care, or perhaps he's so used to discomfort that he no longer notices it.

"Mind if I sit?" you ask, gesturing to the other end of the bench.

He looks up at you for the first time, and you see eyes that are older than his seventeen years - 
eyes that have seen too much cruelty and not enough kindness. "Free country," he says with a 
shrug, but he doesn't move away.

This is the moment that will define your relationship with Junpei. How do you proceed?""",
        [
            StoryChoice(
                "Start by talking about the pigeons and his obvious care for them",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 15},
                    "relationships": {"junpei": 15},
                    "next_scene": "pigeon_conversation",
                    "story_flags": {"first_topic": "pigeons", "gentle_approach": True, "noticed_kindness": True}
                }
            ),
            StoryChoice(
                "Ask if he's okay and if he needs any help",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.AGGRESSIVE: 10, Trait.FOCUSED: 15},
                    "relationships": {"junpei": 10},
                    "next_scene": "direct_concern",
                    "story_flags": {"first_topic": "concern", "direct_care": True, "offered_help": True}
                }
            ),
            StoryChoice(
                "Comment on the rain and suggest finding shelter together",
                {
                    "traits": {Trait.CAUTIOUS: 15, Trait.FOCUSED: 10, Trait.PROTECTIVE: 10},
                    "relationships": {"junpei": 8},
                    "next_scene": "shelter_suggestion",
                    "story_flags": {"first_topic": "practical", "shelter_offer": True, "social_approach": True}
                }
            ),
            StoryChoice(
                "Sit quietly for a while and let him make the first move",
                {
                    "traits": {Trait.CAUTIOUS: 25, Trait.COMPASSIONATE: 20, Trait.COMPASSIONATE: 15},
                    "relationships": {"junpei": 20},
                    "next_scene": "patient_silence",
                    "story_flags": {"first_topic": "silence", "patient_approach": True, "respected_space": True}
                }
            )
        ],
        "Kasumigaoka Park - Rainy Afternoon"
    )
    
    # ============================================================================
    # BUILDING RELATIONSHIP WITH JUNPEI
    # ============================================================================
    
    scenes["pigeon_conversation"] = StoryScene(
        "Small Kindnesses",
        """You settle onto the bench and watch the pigeons for a moment, noting how they seem 
to trust Junpei completely. Some even perch on his knees and shoulders, treating him like 
a living tree rather than a potential threat.

"You're right about them not judging," you say softly, keeping your voice at the same gentle 
level he used. "There's something peaceful about creatures that just... exist without all 
the complicated social games humans play."

Junpei glances at you sideways, clearly surprised that someone would engage with his comment 
rather than dismissing it as weird. "Most people think it's stupid," he says, breaking off 
another piece of bread. "Feeding pigeons. They say they're just flying rats, disease carriers, 
nuisances that should be exterminated."

"Those people probably haven't sat quietly with them like this," you observe. "It's different 
when you actually pay attention to individual personalities. That one there," you point to 
a particularly bold pigeon, "definitely has more confidence than the others. And that little 
gray one waits until everyone else has eaten before approaching."

For the first time, Junpei's expression shifts slightly toward something that might be surprise 
or even the beginning of interest. "You... you actually looked at them. Like, really looked."

"Hard not to when someone cares about them the way you do," you reply. "Says something about 
a person, how they treat creatures that can't give them anything back except maybe a moment 
of peace."

The rain continues to fall, but neither of you moves to leave. Junpei seems to be processing 
the fact that someone noticed his kindness rather than his isolation, that someone saw 
gentleness where others saw only strangeness.

"I come here every day after school," he says after a long pause. "Well, when I went to school, 
anyway. It's... quiet. Nobody bothers me here. Nobody expects anything from me except maybe 
some bread crumbs."

There's an opening here - a chance to learn more about why he stopped going to school, about 
what's been happening in his life. But you sense that pushing too hard too fast could shatter 
this fragile moment of connection.

How do you continue building this relationship?""",
        [
            StoryChoice(
                "Share a story about your own experience with bullying or isolation",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.COMPASSIONATE: 15, Trait.DETERMINED: 15},
                    "relationships": {"junpei": 25},
                    "next_scene": "shared_vulnerability",
                    "story_flags": {"shared_pain": True, "vulnerability_shown": True, "personal_connection": True}
                }
            ),
            StoryChoice(
                "Ask about his interests and hobbies outside of school",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 15, Trait.FOCUSED: 10},
                    "relationships": {"junpei": 18},
                    "next_scene": "hobby_discussion",
                    "story_flags": {"learned_interests": True, "positive_focus": True, "avoided_school_topic": True}
                }
            ),
            StoryChoice(
                "Gently ask why he stopped going to school",
                {
                    "traits": {Trait.AGGRESSIVE: 10, Trait.PROTECTIVE: 20, Trait.DETERMINED: 15},
                    "relationships": {"junpei": 12},
                    "next_scene": "school_discussion",
                    "story_flags": {"addressed_school": True, "direct_concern": True, "potential_trigger": True}
                }
            ),
            StoryChoice(
                "Suggest meeting again tomorrow to feed the pigeons together",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 20, Trait.DETERMINED: 15},
                    "relationships": {"junpei": 22},
                    "next_scene": "friendship_invitation",
                    "story_flags": {"friendship_offered": True, "future_meetings": True, "included_junpei": True}
                }
            )
        ],
        "Kasumigaoka Park - Under the Rain"
    )
    
    # ============================================================================
    # THE MAHITO ENCOUNTER
    # ============================================================================
    
    scenes["mahito_revelation"] = StoryScene(
        "The Monster's Face",
        """The atmosphere in the park shifts suddenly, like the moment before lightning strikes. 
The pigeons around Junpei become agitated, taking flight in a panicked swirl of wings and 
startled cries. Even the rain seems to fall differently, heavier and somehow more oppressive.

"Oh, Junpei," a voice calls out with sickening cheerfulness, "you didn't tell me you'd made 
a new friend!"

You turn to see a figure approaching through the rain - tall, pale, with mismatched eyes and 
an expression of constant, unsettling amusement. But what makes your blood run cold is the 
wrongness of him, the way reality seems to bend slightly around his presence. This isn't human, 
despite the almost-human appearance.

Junpei's entire demeanor changes instantly. The tentative warmth that had been growing between 
you evaporates, replaced by a mixture of eagerness and fear that makes your heart sink. This 
is clearly someone who has significant influence over him.

"Mahito," Junpei says, and there's something in his voice - relief, gratitude, and a desperate 
kind of attachment that speaks to deep manipulation. "I wasn't expecting you today."

"I was in the neighborhood and thought I'd check on my favorite human," the creature - Mahito - 
says with a grin that reveals too many teeth. His eyes fix on you with predatory interest. 
"And look what I find! A little sorcerer, trying to play friend with our Junpei."

The casual way he says 'sorcerer' makes it clear that your disguise has been useless from the 
start. Worse, the way Junpei's face changes - shock, betrayal, and growing anger replacing the 
fragile trust you'd been building - tells you that everything you've worked for is crumbling.

"You're... you're one of them," Junpei says, his voice hollow with disappointment. "A jujutsu 
sorcerer. Just like the ones who ignored what was happening to me. Just like the ones who let 
my father die."

Mahito's grin widens impossibly. "Humans are so predictable, aren't they, Junpei? They always 
disappoint in the end. But that's what makes them so much fun to play with."

The cursed spirit's presence is overwhelming this close, and you can feel the malevolent energy 
radiating from him like heat from a furnace. But what's worse is seeing how completely he's 
twisted Junpei's perception of reality, how skillfully he's used the boy's pain to create 
loyalty built on shared hatred.

This is the moment everything has been building toward. How do you handle this crucial encounter?""",
        [
            StoryChoice(
                "Try to explain that you genuinely care about Junpei, not just the mission",
                {
                    "traits": {Trait.DETERMINED: 25, Trait.AGGRESSIVE: 20, Trait.DETERMINED: 15},
                    "relationships": {"junpei": -5, "mahito": -10},
                    "next_scene": "honest_explanation",
                    "story_flags": {"honest_approach": True, "exposed_feelings": True, "defied_mahito": True}
                }
            ),
            StoryChoice(
                "Challenge Mahito directly and call out his manipulation",
                {
                    "traits": {Trait.AGGRESSIVE: 25, Trait.PROTECTIVE: 20, Trait.FOCUSED: 15},
                    "relationships": {"junpei": 5, "mahito": -25},
                    "next_scene": "mahito_confrontation",
                    "story_flags": {"confronted_mahito": True, "exposed_manipulation": True, "protective_of_junpei": True}
                }
            ),
            StoryChoice(
                "Focus on Junpei and ask him what he really wants",
                {
                    "traits": {Trait.COMPASSIONATE: 25, Trait.FOCUSED: 20, Trait.COMPASSIONATE: 15},
                    "relationships": {"junpei": 10, "mahito": -5},
                    "next_scene": "junpei_choice_focus",
                    "story_flags": {"junpei_autonomy": True, "ignored_mahito": True, "personal_focus": True}
                }
            ),
            StoryChoice(
                "Prepare for combat while trying to position yourself between them",
                {
                    "traits": {Trait.PROTECTIVE: 25, Trait.ANALYTICAL: 20, Trait.FOCUSED: 15},
                    "relationships": {"junpei": 8, "mahito": -15},
                    "next_scene": "combat_preparation",
                    "story_flags": {"combat_ready": True, "protective_stance": True, "tactical_positioning": True}
                }
            )
        ],
        "Kasumigaoka Park - The Confrontation"
    )
    
    # ============================================================================
    # MULTIPLE ENDINGS BASED ON PLAYER CHOICES
    # ============================================================================
    
    scenes["junpei_saved_ending"] = StoryScene(
        "The Light in the Darkness",
        """The final confrontation with Mahito has ended, but not in the way anyone expected. 
Through persistence, genuine care, and the gradual building of trust, you managed to reach 
Junpei at the crucial moment when Mahito's influence was strongest. The cursed spirit's 
manipulation crumbled when faced with authentic human connection.

Junpei sits on a hospital bed, his physical wounds healing but his emotional scars still 
visible. He's alive, he's safe, and most importantly, he's beginning to believe that not 
all humans are cruel. It's a fragile belief, carefully nurtured through weeks of patient 
friendship and proven through actions rather than words.

"I almost killed innocent people," he says quietly, staring at his hands. "I was so angry, 
so hurt, that I believed him when he said humans deserved to suffer. How do I live with 
knowing I was capable of that?"

The question hangs heavy in the air between you. This isn't a simple victory - it's the 
beginning of a long journey of healing and redemption, complicated by the knowledge of 
what almost happened and the genuine damage that was done.

"You stopped," you reply. "When it mattered most, when you had the power to hurt people 
the way you'd been hurt, you chose not to. That's what defines you, not the darkness 
you considered but the light you chose instead."

Through the window, you can see Tokyo spread out in the afternoon sun. The city continues 
its daily rhythm, unaware of how close it came to tragedy, unaware of the quiet victory 
that happened in choosing compassion over revenge.

Gojo appears in the doorway, his usual playful demeanor replaced by something more serious. 
"The higher-ups want to classify Junpei as a potential threat," he says. "They think anyone 
who was influenced by a special grade curse is too dangerous to leave unwatched."

"And what do you think?" Junpei asks, his voice small but determined to face whatever 
judgment comes.

"I think," Gojo says with a slight smile, "that someone who chose to save others when he 
could have destroyed them is exactly the kind of person we need at this school. If he's 
interested in learning how to use his abilities to protect instead of harm."

The offer hangs in the air - a chance at redemption, at belonging, at finding purpose 
in protection rather than destruction. But it's also a massive responsibility and a 
lifetime of proving that this choice was real.

How do you support Junpei in this decision?""",
        [
            StoryChoice(
                "Encourage him to accept and offer to help him adjust to school life",
                {
                    "traits": {Trait.PROTECTIVE: 25, Trait.FOCUSED: 20, Trait.FOCUSED: 20},
                    "relationships": {"junpei": 40, "gojo": 20},
                    "next_scene": "junpei_enrollment",
                    "story_flags": {"junpei_saved": True, "became_student": True, "friendship_continued": True},
                    "experience": 100
                }
            ),
            StoryChoice(
                "Suggest he take time to heal before making any major decisions",
                {
                    "traits": {Trait.FOCUSED: 25, Trait.CAUTIOUS: 20, Trait.COMPASSIONATE: 20},
                    "relationships": {"junpei": 35, "gojo": 15},
                    "next_scene": "healing_time",
                    "story_flags": {"junpei_saved": True, "gradual_recovery": True, "wisdom_shown": True},
                    "experience": 80
                }
            ),
            StoryChoice(
                "Tell him the choice is entirely his and you'll support whatever he decides",
                {
                    "traits": {Trait.COMPASSIONATE: 25, Trait.FOCUSED: 20, Trait.DETERMINED: 20},
                    "relationships": {"junpei": 30, "gojo": 10},
                    "next_scene": "independent_choice",
                    "story_flags": {"junpei_saved": True, "respected_autonomy": True, "unconditional_support": True},
                    "experience": 90
                }
            )
        ],
        "Tokyo General Hospital - Recovery Room"
    )
    
    scenes["junpei_lost_ending"] = StoryScene(
        "The Price of Hatred",
        """The confrontation with Mahito has ended in tragedy. Despite your efforts, despite the 
genuine connection you tried to build, Junpei's pain ran too deep and Mahito's manipulation 
proved too strong. The boy who fed pigeons in the rain, who showed kindness to creatures 
that couldn't repay him, made choices that can't be undone.

You stand in the ruins of what was once Satozakura High School, surrounded by the aftermath 
of cursed energy unleashed in rage and despair. The building is partially collapsed, windows 
blown out, walls twisted by forces that shouldn't exist in the normal world. Emergency 
vehicles circle the perimeter, their lights painting everything in harsh reds and blues.

The casualties could have been much worse - your intervention and that of other sorcerers 
prevented a complete massacre. But the cost was still too high, and among the wounded is 
the knowledge that this tragedy might have been prevented with different choices, different 
timing, different words at crucial moments.

Gojo stands beside you, his usual cheerfulness completely absent. "We lost him," he says 
simply. "Not just to death, but to the hatred that consumed everything good in him. In the 
end, Mahito didn't even need to force him - Junpei chose revenge over redemption."

The most haunting part is that you can understand why. Every conversation, every moment of 
connection you shared, showed you glimpses of the pain that drove him to this point. The 
bullying, the isolation, the systematic cruelty of a world that taught him that kindness 
was weakness and that humans were fundamentally selfish.

"Could we have done something different?" you ask, though you're not sure you want to hear 
the answer.

"Maybe," Gojo replies. "Or maybe some wounds go too deep for healing, some anger burns too 
hot for cooling. The tragedy isn't that Junpei was evil - it's that he was human, and 
humans can break in ways that can't be fixed."

As you leave the scene, you carry with you the weight of failure, but also hard-won wisdom 
about the complexity of human nature and the responsibility that comes with power.

This ending will shape how you approach future encounters with those walking the line 
between light and darkness.

How do you process this tragic outcome?""",
        [
            StoryChoice(
                "Vow to become stronger so you can save the next person like Junpei",
                {
                    "traits": {Trait.DETERMINED: 30, Trait.FOCUSED: 25, Trait.FOCUSED: 20},
                    "next_scene": "strength_vow",
                    "story_flags": {"junpei_lost": True, "strength_focused": True, "future_oriented": True},
                    "experience": 150
                }
            ),
            StoryChoice(
                "Dedicate yourself to understanding and preventing the conditions that create such despair",
                {
                    "traits": {Trait.ANALYTICAL: 25, Trait.ANALYTICAL: 25, Trait.FOCUSED: 25},
                    "next_scene": "systematic_change",
                    "story_flags": {"junpei_lost": True, "systematic_approach": True, "prevention_focused": True},
                    "experience": 120
                }
            ),
            StoryChoice(
                "Accept that some people can't be saved and focus on protecting those who can be",
                {
                    "traits": {Trait.FOCUSED: 25, Trait.CAUTIOUS: 25, Trait.PROTECTIVE: 20},
                    "next_scene": "pragmatic_acceptance",
                    "story_flags": {"junpei_lost": True, "pragmatic_wisdom": True, "protective_focus": True},
                    "experience": 100
                }
            )
        ],
        "Satozakura High School - Aftermath"
    )
    
    # Continue expanding the arc with more scenes covering:
    # - Multiple meeting scenarios with Junpei
    # - Various ways the relationship can develop
    # - Different approaches to handling Mahito
    # - Multiple possible endings based on player choices
    # - Character development and growth opportunities
    # - Side quests involving other victims of bullying
    # - Exploration of the philosophical themes
    
    return scenes