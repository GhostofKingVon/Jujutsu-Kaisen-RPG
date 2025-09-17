"""
Arc 3: Kyoto Exchange Event Arc - Rivalry and Growth

This arc covers the competition between Tokyo and Kyoto Jujutsu High Schools,
featuring tournament battles, political intrigue, and character development
through rivalry and teamwork.
"""

from typing import Dict, List, Any
from character import Trait
from story import StoryChoice, StoryScene


def get_arc3_scenes() -> Dict[str, StoryScene]:
    """Return all scenes for Arc 3: Kyoto Exchange Event Arc."""
    scenes = {}
    
    # ============================================================================
    # ARC 3 INTRODUCTION - The Exchange Event Announcement
    # ============================================================================
    
    scenes["arc3_intro"] = StoryScene(
        "The Challenge from Kyoto",
        """The announcement comes during what should have been a normal morning training session. 
Gojo-sensei strolls into the practice area with his characteristic casual confidence, but there's 
something different in his demeanor - an anticipation that immediately puts everyone on alert.

"Gather around, my dear students," he calls out cheerfully, though his tone carries undertones 
that suggest this isn't just another routine lesson. "We've received some interesting news from 
our colleagues at Kyoto Jujutsu High."

Yuji, Megumi, and Nobara stop their individual training exercises and move closer, their 
expressions ranging from curious to wary. You join them, noting the way Gojo's usual playful 
energy seems more focused than usual.

"Every year," Gojo begins, settling against a training post with theatrical casualness, "the 
two premier jujutsu education institutions hold an exchange event. It's officially described 
as 'fostering cooperation and mutual understanding between future sorcerers,' but let's be 
honest - it's a competition to see which school produces superior fighters."

Nobara's eyes light up with competitive fire. "Are you saying we get to show those Kyoto 
snobs who's really the best?"

"Now, now," Gojo chuckles, "let's not be too hasty to dismiss our competitors. Kyoto has 
produced some remarkable sorcerers over the years. Their current students include some truly 
formidable individuals who would love nothing more than to humiliate Tokyo's 'inferior' approach 
to jujutsu education."

The challenge is clear in his words, and you can feel the competitive tension building among 
your classmates. This isn't just about individual pride - it's about representing your school, 
your teachers, and your philosophy of what it means to be a jujutsu sorcerer.

"The event consists of multiple competitions," Gojo continues. "Individual duels, team battles, 
cursed spirit exorcism challenges, and various tests of skill, strategy, and adaptability. 
The winner isn't just determined by combat prowess, but by overall demonstration of what it 
means to be a complete sorcerer."

Megumi speaks up, his analytical mind already working on the implications. "What's the real 
stakes here? This sounds like more than just friendly competition."

Gojo's expression becomes slightly more serious behind his blindfold. "Perceptive as always, 
Megumi. The exchange event serves multiple purposes. It's a way for the higher-ups to evaluate 
upcoming talent, for schools to demonstrate their teaching methods, and for students to learn 
from different approaches to jujutsu. But it's also... political."

The word hangs in the air with weight that suggests complications beyond simple rivalry.

How do you respond to this opportunity?""",
        [
            StoryChoice(
                "Express enthusiasm for the challenge and competitive opportunity",
                {
                    "traits": {Trait.AGGRESSIVE: 20, Trait.DETERMINED: 15, Trait.DETERMINED: 15},
                    "relationships": {"nobara": 15, "gojo": 10},
                    "next_scene": "competitive_preparation",
                    "story_flags": {"attitude": "competitive", "exchange_mindset": "victory_focused"}
                }
            ),
            StoryChoice(
                "Ask about the political implications and what they mean for students",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 15, Trait.ANALYTICAL: 15},
                    "relationships": {"megumi": 15, "gojo": 15},
                    "next_scene": "political_discussion",
                    "story_flags": {"attitude": "analytical", "exchange_mindset": "politically_aware"}
                }
            ),
            StoryChoice(
                "Focus on the learning opportunity and what you can gain from other students",
                {
                    "traits": {Trait.FOCUSED: 20, Trait.FOCUSED: 15, Trait.FOCUSED: 15},
                    "relationships": {"yuji": 15, "faculty": 10},
                    "next_scene": "learning_focus",
                    "story_flags": {"attitude": "educational", "exchange_mindset": "growth_oriented"}
                }
            ),
            StoryChoice(
                "Inquire about team composition and how you can best support your classmates",
                {
                    "traits": {Trait.PROTECTIVE: 20, Trait.PROTECTIVE: 15, Trait.ANALYTICAL: 15},
                    "relationships": {"team": 15},
                    "next_scene": "team_strategy",
                    "story_flags": {"attitude": "team_focused", "exchange_mindset": "collaborative"}
                }
            )
        ],
        "Tokyo Jujutsu High - Training Grounds"
    )
    
    # ============================================================================
    # PREPARATION PHASE - Training and Strategy
    # ============================================================================
    
    scenes["competitive_preparation"] = StoryScene(
        "The Fire of Competition",
        """Your enthusiastic response to the challenge seems to energize the entire group. Nobara 
grins fiercely and cracks her knuckles, while even the usually reserved Megumi shows a hint 
of competitive spark in his eyes. Gojo's approval is evident in his widening smile.

"That's the spirit I like to see!" he exclaims. "Confidence without preparation is just 
arrogance, but confidence WITH preparation? That's how legends are made."

Over the following weeks, the training intensifies dramatically. What were once routine 
practice sessions become grueling marathons of technique refinement, strategic planning, 
and physical conditioning. The school brings in additional instructors, sets up advanced 
training scenarios, and even arranges sparring sessions with older students and alumni.

Your competitive drive pushes you to excel in every aspect of preparation. During technique 
training, you focus on perfecting your most reliable abilities while also developing new 
applications. In physical conditioning, you push your limits until exhaustion becomes just 
another obstacle to overcome. During strategic planning sessions, you study videos of past 
exchange events and analyze the fighting styles of known Kyoto students.

The atmosphere at the school shifts as word spreads about the upcoming competition. Other 
students watch your training with mixtures of respect, envy, and anticipation. Faculty 
members offer advice and additional resources. Even the usually aloof upperclassmen begin 
treating you and your classmates with new levels of seriousness.

"Tokyo's reputation rests on our shoulders," Nobara declares during one particularly intense 
training session, sweat dripping from her forehead as she practices precision strikes against 
moving targets. "No pressure, right?"

"Pressure makes diamonds," you reply, channeling your competitive energy into focus. "Let 
them bring their best - we'll be ready for anything they can throw at us."

As the weeks pass, you notice changes not just in your own abilities, but in how the team 
functions together. The competitive atmosphere has forged stronger bonds between you and your 
classmates, built on mutual respect for each other's dedication and improvement.

Three days before the exchange event, Gojo calls a final strategy meeting.

"You've all improved remarkably," he says, genuine pride evident in his voice. "But remember - 
this isn't just about individual strength. Kyoto students are taught to value tradition, 
discipline, and coordinated tactics. They'll likely try to expose any weaknesses in our 
teamwork or unconventional approaches."

How do you want to focus your final preparations?""",
        [
            StoryChoice(
                "Perfect your signature techniques to ensure maximum impact",
                {
                    "traits": {Trait.FOCUSED: 15, Trait.FOCUSED: 20, Trait.DETERMINED: 15},
                    "next_scene": "technique_mastery",
                    "story_flags": {"preparation_focus": "technique", "specialization": True}
                }
            ),
            StoryChoice(
                "Practice team combinations and coordinated attacks",
                {
                    "traits": {Trait.PROTECTIVE: 20, Trait.FOCUSED: 15, Trait.ANALYTICAL: 15},
                    "next_scene": "team_synergy",
                    "story_flags": {"preparation_focus": "teamwork", "coordination_emphasis": True}
                }
            ),
            StoryChoice(
                "Study Kyoto students' known weaknesses and develop counter-strategies",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 15, Trait.FOCUSED: 15},
                    "next_scene": "counter_strategy",
                    "story_flags": {"preparation_focus": "analysis", "counter_planning": True}
                }
            ),
            StoryChoice(
                "Focus on mental preparation and psychological readiness",
                {
                    "traits": {Trait.DETERMINED: 20, Trait.FOCUSED: 15, Trait.DETERMINED: 15},
                    "next_scene": "mental_preparation",
                    "story_flags": {"preparation_focus": "mental", "psychological_training": True}
                }
            )
        ],
        "Tokyo Jujutsu High - Strategy Room"
    )
    
    # ============================================================================
    # KYOTO STUDENTS INTRODUCTION - Meeting the Competition
    # ============================================================================
    
    scenes["kyoto_arrival"] = StoryScene(
        "The Rival School Arrives",
        """The morning of the exchange event dawns crisp and clear, with an electric tension in 
the air that seems to charge every breath you take. Tokyo Jujutsu High has been transformed 
for the occasion - training grounds expanded, spectator areas constructed, and barrier 
techniques deployed to contain the powerful cursed energy that will soon be unleashed.

You and your classmates wait in the main courtyard as the Kyoto delegation arrives. Their 
approach is formal and coordinated, a stark contrast to Tokyo's more casual atmosphere. They 
move with military precision, each student perfectly positioned relative to the others, their 
uniforms immaculate and their expressions serious.

Leading the group is a tall, imposing figure with traditional hakama and an aura of absolute 
authority - Principal Yoshinobu Gakuganji of Kyoto Jujutsu High. Behind him walk the students 
who will be your competition, each one radiating confidence and barely contained power.

"So these are Tokyo's representatives," says a voice filled with barely concealed disdain. 
You turn to see a young man with pale hair and sharp features, his eyes scanning your group 
with calculating assessment. "They look... informal."

Another Kyoto student, a girl with elegant twin tails and an expensive-looking uniform, 
nods in agreement. "I expected more discipline from the school that claims to produce the 
strongest sorcerers. Their posture alone suggests inadequate training."

But it's the third member of their group that immediately draws your attention - a massive 
figure with wild hair and scars across his knuckles, grinning with undisguised excitement 
for violence. This can only be Todo Aoi, whose reputation for both strength and eccentricity 
has reached even Tokyo.

"My brother!" Todo suddenly shouts, his booming voice carrying across the courtyard as his 
eyes fix on Yuji. "I can smell the potential for greatness on you! Tell me - what type of 
woman is your ideal?"

The unexpected question catches everyone off guard, and you can see Yuji's confusion as he 
tries to process both the inquiry and the intense scrutiny he's receiving.

"This is exactly the kind of unpredictable behavior we expected from Tokyo students," the 
pale-haired boy comments. "No discipline, no focus, no respect for proper conduct."

Nobara steps forward, her temper already flaring. "And I suppose Kyoto's idea of proper 
conduct includes insulting your hosts before the competition even begins?"

The tension in the courtyard ratchets up several levels as the two groups face each other. 
You can feel cursed energy beginning to build on both sides, students unconsciously preparing 
for confrontation even though the formal events haven't started yet.

Gojo appears between the groups with his characteristic casual timing, his presence immediately 
diffusing some of the tension while somehow making it clear that any premature violence would 
be... inadvisable.

"Now, now," he says cheerfully, "save that energy for the actual competition. We have a full 
day of events planned, and I'd hate for anyone to exhaust themselves on mere posturing."

How do you handle this first encounter with your rivals?""",
        [
            StoryChoice(
                "Introduce yourself politely and try to establish mutual respect",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.COMPASSIONATE: 15, Trait.FOCUSED: 15},
                    "relationships": {"kyoto_students": 10},
                    "next_scene": "diplomatic_introduction",
                    "story_flags": {"first_impression": "diplomatic", "kyoto_respect": True}
                }
            ),
            StoryChoice(
                "Match their competitive energy and make it clear Tokyo won't be intimidated",
                {
                    "traits": {Trait.DETERMINED: 20, Trait.AGGRESSIVE: 15, Trait.AGGRESSIVE: 15},
                    "relationships": {"kyoto_students": -5, "tokyo_team": 15},
                    "next_scene": "confident_response",
                    "story_flags": {"first_impression": "confident", "showed_strength": True}
                }
            ),
            StoryChoice(
                "Observe and analyze each Kyoto student to gather intelligence",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 15, Trait.FOCUSED: 15},
                    "next_scene": "tactical_observation",
                    "story_flags": {"first_impression": "analytical", "gathered_intelligence": True}
                }
            ),
            StoryChoice(
                "Support your teammates and let them take the lead in interactions",
                {
                    "traits": {Trait.PROTECTIVE: 20, Trait.FOCUSED: 15, Trait.COMPASSIONATE: 10},
                    "relationships": {"tokyo_team": 20},
                    "next_scene": "supportive_stance",
                    "story_flags": {"first_impression": "supportive", "team_unity": True}
                }
            )
        ],
        "Tokyo Jujutsu High - Main Courtyard"
    )
    
    # ============================================================================
    # INDIVIDUAL TOURNAMENT BATTLES
    # ============================================================================
    
    scenes["tournament_first_match"] = StoryScene(
        "The Arena Awaits",
        """The first official event of the exchange is individual combat tournaments, designed 
to showcase personal skill and technique mastery. The arena has been specially prepared with 
reinforced barriers and elevated viewing platforms for spectators and judges.

As you enter the designated waiting area, you can feel the weight of expectation from faculty, 
fellow students, and the political undercurrents that Gojo mentioned. This isn't just about 
personal victory - every match represents the philosophy and training methods of your respective 
schools.

The tournament bracket has been announced, and you learn that your first opponent will be 
Noritoshi Kamo, the pale-haired young man who made dismissive comments about Tokyo's discipline. 
He comes from a prestigious sorcerer family with a long history of traditional jujutsu practices, 
and his technique involves blood manipulation with deadly precision.

"Kamo, huh?" Nobara comments, studying the bracket. "I've heard about his family. Old money, 
old techniques, and old attitudes about how jujutsu should be practiced. He's going to try 
to prove that traditional methods are superior to our 'unorthodox' approaches."

Megumi nods thoughtfully. "His blood manipulation technique is extremely versatile - offense, 
defense, binding, and tracking. But it requires him to injure himself to access his own blood, 
or to draw blood from enemies. That could be a weakness if you can control the pace of combat."

As you prepare for the match, you consider your strategy. Kamo will likely expect you to rely 
on raw power or unconventional tactics, as that fits Kyoto's stereotypes about Tokyo students. 
But you have the advantage of knowing his preconceptions while he knows little about your 
specific capabilities.

The arena announcer calls your name, and the moment of truth arrives. You walk onto the combat 
floor to find Kamo already in position, his posture perfect and his expression coldly confident. 
The referee explains the rules - victory by knockout, surrender, or judge's decision if the 
match exceeds the time limit.

"I hope you'll provide more challenge than your school's reputation suggests," Kamo says formally, 
drawing a small blade across his palm to access his blood technique. "It would be disappointing 
if this ended too quickly."

The crowd falls silent as the referee raises his hand. This is your moment to represent 
everything Tokyo Jujutsu High has taught you about being a sorcerer.

What's your opening strategy against Kamo?""",
        [
            StoryChoice(
                "Open with aggressive close-range attacks to prevent him from setting up blood techniques",
                {
                    "combat": True,
                    "enemy": "noritoshi_kamo_pressured",
                    "traits": {Trait.AGGRESSIVE: 15, Trait.FOCUSED: 15, Trait.FOCUSED: 20},
                    "next_scene": "aggressive_opening",
                    "story_flags": {"opening_strategy": "aggressive", "pressure_tactics": True}
                }
            ),
            StoryChoice(
                "Maintain distance and study his techniques before committing to an approach",
                {
                    "traits": {Trait.CAUTIOUS: 20, Trait.ANALYTICAL: 15, Trait.FOCUSED: 15},
                    "next_scene": "analytical_opening",
                    "story_flags": {"opening_strategy": "analytical", "defensive_study": True}
                }
            ),
            StoryChoice(
                "Use unpredictable movement patterns to confuse his targeting",
                {
                    "traits": {Trait.RECKLESS: 20, Trait.FOCUSED: 15, Trait.ANALYTICAL: 15},
                    "next_scene": "unpredictable_opening",
                    "story_flags": {"opening_strategy": "unpredictable", "mobility_focus": True}
                }
            ),
            StoryChoice(
                "Attempt to bait him into overextending with false openings",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15, Trait.FOCUSED: 15},
                    "next_scene": "baiting_strategy",
                    "story_flags": {"opening_strategy": "tactical", "deception_tactics": True}
                }
            )
        ],
        "Exchange Event Arena - Individual Tournament"
    )
    
    # ============================================================================
    # TEAM BATTLE SCENARIOS
    # ============================================================================
    
    scenes["team_battle_preparation"] = StoryScene(
        "United We Stand",
        """Following the individual tournaments, the exchange event moves to its centerpiece - 
team battles that test coordination, strategy, and the ability to work together under pressure. 
The arena has been reconfigured into a complex environment with multiple levels, obstacles, 
and strategic positions.

You gather with Yuji, Megumi, and Nobara in the team preparation area, the bonds forged through 
weeks of training now put to the ultimate test. Each of you has shown your individual capabilities, 
but this is where Tokyo's philosophy of adaptation and mutual support will either prove its 
worth or reveal its weaknesses.

"Kyoto's team strategy will be built around traditional formations and predetermined roles," 
Megumi observes, studying diagrams of the arena layout. "They train to function as a coordinated 
unit with each member fulfilling a specific tactical purpose."

Nobara grins confidently while checking her equipment. "Good for them. Too bad we're not 
traditional enough to be predictable. By the time they figure out our approach, we'll have 
already adapted three different strategies."

Yuji, surprisingly, seems the most focused of the group. "We've gotten really good at 
supporting each other's strengths and covering each other's weaknesses. That's something 
you can't just teach in a classroom - it comes from actually trusting your teammates."

The team battle format involves multiple scenarios: capture the flag with cursed spirit 
obstacles, escort missions with simulated civilian protection, and direct team-versus-team 
combat. Points are awarded for completion speed, efficiency, and demonstration of tactical 
flexibility.

As you discuss strategy, you realize this is your chance to showcase not just individual 
power, but the unique Tokyo approach to jujutsu sorcery - the ability to think outside 
traditional constraints and adapt to unexpected challenges.

"The question is," you say, looking at your teammates, "do we play to our individual strengths 
and support each other's specialties, or do we try to function as a more integrated unit?"

Gojo appears at the entrance to your preparation area, his timing as impeccable as always. 
"Interesting question," he comments. "Kyoto will expect you to be disorganized and overly 
individualistic. They've prepared counters for uncoordinated attacks and chaos tactics. 
But what they haven't prepared for..."

He pauses dramatically, letting the implications sink in.

"Is the possibility that Tokyo students might be BOTH individually exceptional AND perfectly 
coordinated when it matters most."

How do you approach the team battle strategy?""",
        [
            StoryChoice(
                "Focus on seamless combination attacks that play to everyone's strengths",
                {
                    "traits": {Trait.FOCUSED: 25, Trait.FOCUSED: 20, Trait.COMPASSIONATE: 15},
                    "relationships": {"tokyo_team": 25},
                    "next_scene": "combination_strategy",
                    "story_flags": {"team_strategy": "combination", "synergy_focus": True}
                }
            ),
            StoryChoice(
                "Develop multiple backup plans for different scenarios",
                {
                    "traits": {Trait.FOCUSED: 25, Trait.CAUTIOUS: 20, Trait.FOCUSED: 15},
                    "next_scene": "adaptive_strategy",
                    "story_flags": {"team_strategy": "adaptive", "multiple_plans": True}
                }
            ),
            StoryChoice(
                "Create unpredictable role rotations that confuse enemy expectations",
                {
                    "traits": {Trait.RECKLESS: 25, Trait.ANALYTICAL: 20, Trait.AGGRESSIVE: 15},
                    "next_scene": "rotation_strategy", 
                    "story_flags": {"team_strategy": "rotation", "role_flexibility": True}
                }
            ),
            StoryChoice(
                "Plan psychological warfare to disrupt Kyoto's disciplined approach",
                {
                    "traits": {Trait.ANALYTICAL: 25, Trait.AGGRESSIVE: 20, Trait.ANALYTICAL: 15},
                    "next_scene": "psychological_strategy",
                    "story_flags": {"team_strategy": "psychological", "mental_warfare": True}
                }
            )
        ],
        "Exchange Event Arena - Team Preparation Area"
    )
    
    # ============================================================================
    # CLIMACTIC CONFRONTATIONS - Todo Fight and Resolution
    # ============================================================================
    
    scenes["todo_confrontation"] = StoryScene(
        "The Beast of Kyoto",
        """The final individual match of the day pits you against Todo Aoi, and the anticipation 
in the arena is palpable. Todo's reputation precedes him - a sorcerer of immense physical 
power whose unconventional personality masks tactical brilliance and fighting instincts 
that border on supernatural.

As you enter the arena, Todo is already waiting, his massive frame relaxed but ready for 
explosive action. His presence alone seems to change the atmosphere, making the air feel 
heavier and charged with potential violence.

"My friend!" he calls out with genuine enthusiasm, though you're not sure you qualify as 
friends having barely spoken before. "I've been looking forward to this match more than 
any other. Do you know why?"

Before you can answer, he continues with the rapid-fire intensity that characterizes all 
his interactions. "Because I can sense something in you - a potential for growth, for 
understanding what it truly means to fight with everything on the line. Today, you will 
discover things about yourself that you never knew existed!"

The referee begins explaining the rules, but Todo waves him off impatiently. "The only 
rule that matters is giving everything you have. Anything less is an insult to both of 
us and to the art of combat itself."

As the match begins, Todo doesn't immediately attack. Instead, he studies you with the 
intensity of a predator evaluating prey, his eyes taking in your stance, your breathing, 
the way you hold your cursed energy in reserve.

"Show me your resolve!" he demands, his voice echoing off the arena walls. "Show me the 
fire that burns in your soul when everything you believe in is put to the test!"

This isn't just a fight - it's Todo's way of pushing you to transcend your current limitations. 
He wants to see not just your technique or your power, but your character under ultimate 
pressure.

The crowd holds its breath as you prepare to face one of the most formidable opponents 
you've ever encountered. Todo's technique allows him to swap the positions of any two 
objects by clapping his hands, making conventional strategy nearly useless against him.

But perhaps that's exactly what he wants you to realize - that true growth comes from 
abandoning conventional approaches and discovering new possibilities in the heat of combat.

How do you approach this ultimate test?""",
        [
            StoryChoice(
                "Accept his challenge and fight with complete emotional commitment",
                {
                    "combat": True,
                    "enemy": "todo_aoi_full_power",
                    "traits": {Trait.AGGRESSIVE: 25, Trait.AGGRESSIVE: 25, Trait.RECKLESS: 20},
                    "relationships": {"todo": 30},
                    "next_scene": "passionate_battle",
                    "story_flags": {"todo_approach": "passionate", "emotional_breakthrough": True}
                }
            ),
            StoryChoice(
                "Try to outthink his position-swapping technique with complex strategies",
                {
                    "combat": True,
                    "enemy": "todo_aoi_tactical",
                    "traits": {Trait.ANALYTICAL: 25, Trait.CAUTIOUS: 25, Trait.FOCUSED: 20},
                    "relationships": {"todo": 20},
                    "next_scene": "tactical_battle",
                    "story_flags": {"todo_approach": "tactical", "strategic_thinking": True}
                }
            ),
            StoryChoice(
                "Focus on pure speed and overwhelming offense to prevent his technique use",
                {
                    "combat": True,
                    "enemy": "todo_aoi_pressured",
                    "traits": {Trait.AGGRESSIVE: 25, Trait.AGGRESSIVE: 25, Trait.AGGRESSIVE: 20},
                    "relationships": {"todo": 25},
                    "next_scene": "speed_battle",
                    "story_flags": {"todo_approach": "speed", "overwhelming_offense": True}
                }
            ),
            StoryChoice(
                "Embrace unpredictability and let instinct guide your fighting",
                {
                    "combat": True,
                    "enemy": "todo_aoi_chaotic",
                    "traits": {Trait.RECKLESS: 25, Trait.RECKLESS: 25, Trait.FOCUSED: 20},
                    "relationships": {"todo": 35},
                    "next_scene": "instinctive_battle",
                    "story_flags": {"todo_approach": "instinctive", "transcendent_fight": True}
                }
            )
        ],
        "Exchange Event Arena - Final Individual Match"
    )
    
    # ============================================================================
    # MULTIPLE ENDINGS BASED ON PERFORMANCE
    # ============================================================================
    
    scenes["exchange_victory_ending"] = StoryScene(
        "Tokyo's Triumph",
        """The final scores are announced as the sun sets over the exchange event arena, and 
the results send waves of celebration through the Tokyo delegation. Through a combination 
of individual excellence, innovative teamwork, and strategic adaptability, Tokyo Jujutsu 
High has achieved a decisive victory over their Kyoto rivals.

You stand with your teammates on the victor's platform, exhausted but exhilarated. The 
battles throughout the day pushed each of you beyond your previous limits, forging new 
levels of skill and understanding that will serve you throughout your careers as sorcerers.

"I have to admit," says Noritoshi Kamo, approaching your group with surprising grace in 
defeat, "your unorthodox methods proved more effective than I anticipated. Perhaps there's 
wisdom in Tokyo's approach that Kyoto has been too proud to acknowledge."

Todo Aoi slaps you on the back with enough force to stagger most people, his face beaming 
with approval. "Outstanding! You fought with the kind of passion and growth that makes 
victories meaningful! I look forward to our next encounter, my friend!"

Even the usually stern Principal Gakuganji offers grudging respect. "Tokyo's students 
showed remarkable development throughout the competition. Your school's emphasis on 
individual growth within team frameworks has produced... unexpected results."

Gojo appears beside your group with his characteristic satisfied grin. "Not bad for a 
bunch of 'undisciplined' students, wouldn't you say? Sometimes the best way to honor 
tradition is to transcend it."

As the formal ceremonies conclude and both schools prepare to return to their regular 
routines, you realize that this victory represents more than just competitive success. 
It validates Tokyo's philosophy of encouraging individual expression within collaborative 
frameworks, of adapting traditional techniques to modern challenges, and of growing 
stronger through diversity rather than conformity.

The relationships forged through competition - both with teammates and former rivals - 
will continue to shape your development as a sorcerer. The exchange event has proven 
that strength comes not from rigid adherence to tradition, but from the wisdom to 
combine the best of old and new approaches.

How do you want to build on this victory going forward?""",
        [
            StoryChoice(
                "Focus on refining the new techniques and insights gained during competition",
                {
                    "traits": {Trait.FOCUSED: 25, Trait.FOCUSED: 20, Trait.FOCUSED: 20},
                    "next_scene": "post_victory_training",
                    "story_flags": {"exchange_outcome": "victory", "focus": "technique_development"},
                    "experience": 200
                }
            ),
            StoryChoice(
                "Work on building ongoing relationships with Kyoto students for mutual growth",
                {
                    "traits": {Trait.COMPASSIONATE: 25, Trait.FOCUSED: 20, Trait.PROTECTIVE: 20},
                    "relationships": {"kyoto_students": 25},
                    "next_scene": "inter_school_cooperation",
                    "story_flags": {"exchange_outcome": "victory", "focus": "relationship_building"},
                    "experience": 150
                }
            ),
            StoryChoice(
                "Help train younger students using lessons learned from the exchange",
                {
                    "traits": {Trait.FOCUSED: 25, Trait.DETERMINED: 20, Trait.PROTECTIVE: 20},
                    "relationships": {"junior_students": 30},
                    "next_scene": "mentoring_role", 
                    "story_flags": {"exchange_outcome": "victory", "focus": "mentoring"},
                    "experience": 175
                }
            )
        ],
        "Exchange Event Arena - Victory Ceremony"
    )
    
    # Continue with additional scenes covering:
    # - Detailed individual matches with each Kyoto student
    # - Complex team battle scenarios with multiple objectives
    # - Political intrigue and faculty discussions
    # - Character development through rivalry and respect
    # - Alternative endings based on different outcomes
    # - Side quests involving inter-school relationships
    # - Exploration of different jujutsu philosophies
    
    return scenes