"""
Vs. Mahito/Junpei Arc - The Weight of Human Souls

This module contains the expanded Vs. Mahito/Junpei Arc story content with deep character 
development, moral dilemmas, complex combat scenarios, and emotional storytelling.
Minimum 800 lines of detailed story content focusing on humanity, friendship, and loss.
"""

from typing import Dict, List, Any, Optional
from character import Trait
from story import StoryChoice, StoryScene


class MahitoJunpeiArc:
    """Manages the Vs. Mahito/Junpei Arc story scenes and progression."""
    
    def __init__(self):
        self.scenes = {}
        self._initialize_mahito_arc()
    
    def _initialize_mahito_arc(self):
        """Initialize all Vs. Mahito/Junpei Arc story scenes."""
        
        # =================================================================
        # SCENE 1: STRANGE INCIDENTS IN THE CITY
        # =================================================================
        
        strange_incidents_description = """Several weeks have passed since your arrival at Tokyo Jujutsu High, and you've settled into a routine of training, study, and small-scale missions. However, recent reports have been troubling the faculty. A series of bizarre incidents across Tokyo has caught the attention of the jujutsu world - incidents that seem to involve cursed spirits with unusual abilities.

You're sitting in the briefing room with your fellow first-years, listening as Nanami-sensei explains the situation with his characteristic precision. "The pattern is disturbing," he says, adjusting his glasses as he reviews the case files. "Multiple victims found in public places, apparently killed instantly, but with their bodies... altered in ways that suggest something beyond typical cursed spirit behavior."

The photographs he shows are difficult to look at. Bodies twisted into impossible shapes, faces frozen in expressions of absolute terror, some victims appearing to have been turned inside-out while somehow still maintaining their basic human form. It's unlike anything you've seen in your textbooks or training scenarios.

"The curse responsible appears to be intelligent and methodical," Nanami continues. "It's not simply killing for sustenance or out of mindless aggression. There's purpose behind these attacks, though we haven't determined what that purpose might be."

Yuji raises his hand, his usually cheerful demeanor subdued by the grim subject matter. "Are there any witnesses? Anyone who's seen this curse and survived?"

"That's where things become more complicated," Nanami replies. "There have been sightings of a young man, approximately high school age, present at several of the incident locations. However, he doesn't appear to be a victim. Security footage suggests he may be... involved somehow."

Megumi leans forward in his chair, his analytical mind clearly working through the implications. "Involved how? As an accomplice? A controller? Or is he another cursed spirit disguised as human?"

"Unknown," Nanami admits. "What we do know is that this individual appears to be a student at Satozakura High School. Intelligence suggests his name is Junpei Yoshino, and according to school records, he's been frequently absent and has a history of bullying incidents."

Nobara crosses her arms, her expression skeptical. "So we're looking for a high school kid who might be working with a curse that's killing people? That's... disturbing on multiple levels."

The weight of the situation settles over the room. This isn't a simple cursed spirit elimination mission - there are human elements involved, moral complexities that your training hasn't fully prepared you for. The possibility that a human might be willingly collaborating with a murderous curse raises questions about the nature of evil that go beyond the usual clear-cut conflicts with mindless monsters.

"Your assignment," Nanami says, looking at each of you in turn, "is to investigate Satozakura High School and the surrounding area. Locate this Junpei Yoshino, determine his connection to the incidents, and gather intelligence on the cursed spirit responsible. But remember - if he is involved, he's still a human being. That makes this situation infinitely more delicate than our usual operations."

The implications of the mission weigh heavily on your mind. How do you want to approach this investigation?"""

        strange_incidents_choices = [
            StoryChoice(
                "Suggest investigating Junpei's background and motivations first",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 10},
                    "story_flags": {"investigation_focused": True, "human_priority": True},
                    "next_scene": "junpei_background_investigation",
                    "experience": 40,
                    "relationships": {"nanami": 10}
                }
            ),
            StoryChoice(
                "Propose going directly to Satozakura High to observe Junpei",
                {
                    "traits": {Trait.DETERMINED: 10, Trait.CAUTIOUS: 5, Trait.ANALYTICAL: 5},
                    "story_flags": {"direct_observation": True, "school_infiltration": True},
                    "next_scene": "satozakura_infiltration",
                    "experience": 35,
                    "relationships": {"megumi": 5}
                }
            ),
            StoryChoice(
                "Focus on tracking the cursed spirit responsible for the murders",
                {
                    "traits": {Trait.AGGRESSIVE: 10, Trait.DETERMINED: 10, Trait.PROTECTIVE: 5},
                    "story_flags": {"curse_focused": True, "protection_priority": True},
                    "next_scene": "mahito_tracking_mission",
                    "experience": 45,
                    "relationships": {"nobara": 10}
                }
            ),
            StoryChoice(
                "Suggest a multi-pronged approach covering all angles",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 10, Trait.CAUTIOUS: 5},
                    "story_flags": {"comprehensive_strategy": True, "team_coordination": True},
                    "next_scene": "comprehensive_investigation_plan",
                    "experience": 50,
                    "relationships": {"nanami": 15, "team": 10}
                }
            )
        ]
        
        self.scenes["strange_incidents_briefing"] = StoryScene(
            "Strange Incidents in the City",
            strange_incidents_description,
            strange_incidents_choices,
            "Tokyo Jujutsu High - Briefing Room"
        )
        
        # =================================================================
        # SCENE 2A: JUNPEI BACKGROUND INVESTIGATION
        # =================================================================
        
        investigation_description = """Your decision to investigate Junpei's background first proves insightful. Spending the afternoon in the school's research archives and coordinating with intelligence contacts, you begin to piece together a troubling picture of Junpei Yoshino's life.

The official records tell one story: a quiet, academically average student with increasing absences and declining grades over the past year. But deeper investigation reveals a much darker reality. Incident reports from Satozakura High School paint a picture of systematic bullying that the administration has consistently failed to address adequately.

"Look at this," Megumi says, showing you a particularly disturbing report. "Three separate incidents in the past six months where Junpei was hospitalized due to 'accidents' during school activities. Each time, the same group of students was involved, and each time, the incidents were ruled accidental or Junpei was blamed for provoking the situation."

The files contain photographs that make your stomach turn. Junpei with a black eye and split lip, explained away as "falling down stairs." Burns on his arms that were supposedly from "accidentally" touching hot equipment in science class. Most recently, a severe injury to his head that required stitches, officially recorded as the result of "horsing around" during physical education.

Yuji's hands clench into fists as he reads through the reports. "How is this possible? How can a school just... ignore this kind of treatment?"

"It's more common than you might think," Nanami says grimly. "Institutional failure to protect vulnerable students creates environments where this kind of systematic abuse can flourish. And in Junpei's case, it appears his home situation offers little refuge."

The family records reveal additional challenges. Junpei's mother works multiple jobs to support them both after his father's death three years ago. She's rarely home, and when she is, she's often too exhausted to provide the emotional support her son desperately needs. Social services has been called twice, but with no evidence of parental abuse and Junpei consistently covering for his school tormentors, no action was taken.

"There's something else," you say, pointing to a recent psychological evaluation tucked into his file. "A school counselor noted that Junpei has been expressing increasingly dark thoughts about humanity and justice. He's been asking questions about whether people who cause suffering deserve to suffer themselves."

The psychological profile becomes more disturbing as you read deeper. Junpei has been obsessing over philosophy and concepts of justice, particularly focusing on the idea that most humans are fundamentally selfish and cruel. His recent essays for literature class have contained disturbing themes about the worthlessness of human life and the appeal of power that could "correct" human nature.

"This is textbook radicalization," Nanami observes. "A vulnerable individual, systematically abused and isolated, begins to develop ideologies that justify extreme actions. If a cursed spirit with the right kind of influence encountered him in this state..."

The implications are chilling. Junpei isn't just a random victim or accomplice - he's been psychologically groomed for exactly the kind of partnership that a manipulative cursed spirit could exploit. His pain, anger, and growing misanthropy would make him an ideal tool for a creature that feeds on human suffering.

"We need to approach this very carefully," you realize aloud. "If we're right about his mental state, then confronting him directly could push him further toward whatever influence is controlling him. But if we wait too long..."

The weight of responsibility settles on your shoulders. Junpei Yoshino is both a potential threat and a victim in desperate need of help. The choices you make in approaching him could determine whether he can be saved or whether he's lost forever to whatever darkness has already begun consuming him.

How do you want to proceed with this delicate situation?"""

        investigation_choices = [
            StoryChoice(
                "Attempt to approach Junpei at school as a concerned peer",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.CAUTIOUS: 10},
                    "story_flags": {"peer_approach": True, "empathy_focused": True},
                    "next_scene": "junpei_peer_contact",
                    "experience": 45,
                    "relationships": {"junpei": 15}
                }
            ),
            StoryChoice(
                "Investigate his bullies to understand the full scope of his trauma",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.PROTECTIVE: 10, Trait.AGGRESSIVE: 5},
                    "story_flags": {"bully_investigation": True, "justice_focused": True},
                    "next_scene": "bully_confrontation_investigation",
                    "experience": 40,
                    "relationships": {"yuji": 10}
                }
            ),
            StoryChoice(
                "Try to contact his mother to warn her about the danger",
                {
                    "traits": {Trait.PROTECTIVE: 15, Trait.CAUTIOUS: 10},
                    "story_flags": {"family_contact": True, "protection_priority": True},
                    "next_scene": "mother_contact_attempt",
                    "experience": 35,
                    "relationships": {"nanami": 10}
                }
            ),
            StoryChoice(
                "Set up surveillance to observe Junpei and identify the cursed spirit",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 15},
                    "story_flags": {"surveillance_strategy": True, "intelligence_gathering": True},
                    "next_scene": "junpei_surveillance_operation",
                    "experience": 50,
                    "relationships": {"megumi": 15}
                }
            )
        ]
        
        self.scenes["junpei_background_investigation"] = StoryScene(
            "Uncovering Junpei's Tragedy",
            investigation_description,
            investigation_choices,
            "Tokyo Jujutsu High - Research Archives"
        )
        
        # =================================================================
        # SCENE 3: FIRST CONTACT WITH JUNPEI
        # =================================================================
        
        first_contact_description = """Your surveillance of Satozakura High School has finally paid off. After three days of careful observation, you've identified Junpei Yoshino and confirmed that he is indeed involved with something supernatural. The cursed energy signature around him is unmistakable, though it's unlike anything you've encountered before - twisted, artificial, and somehow fundamentally wrong.

You watch from a concealed position as Junpei sits alone on the school's rooftop during lunch period, a place where he clearly feels safe from his tormentors. He's thin, pale, with dark hair that falls across his face as if he's trying to hide from the world. Even from a distance, you can see the barely healed bruises on his arms and the way he unconsciously touches a bandage on the back of his neck.

But what truly catches your attention is what he's talking to.

At first glance, it appears to be empty air. But with your cursed energy sight active, you can see the monstrous form hovering near Junpei - a pale, humanoid figure with patched skin and mismatched features, like a doll sewn together from different people. This must be the cursed spirit responsible for the recent murders, and it's speaking to Junpei with an familiarity that suggests a well-established relationship.

"The world is full of suffering because humans choose to make it so," the curse is saying, its voice carrying clearly across the rooftop despite the distance. "But what if someone had the power to reshape human nature itself? To eliminate the cruelty and selfishness that causes so much pain?"

Junpei nods slowly, hanging on every word. "Sometimes I wonder if people like my bullies even deserve to be called human. They cause so much suffering without any remorse."

"Exactly!" the curse responds with apparent enthusiasm. "You understand what so many fail to grasp. Humans are flawed creatures, but those flaws can be... corrected. I can show you techniques that would allow you to reshape not just their bodies, but their very souls."

The conversation continues, and you realize you're witnessing a masterful manipulation. The curse - who introduces himself as Mahito - is systematically reinforcing Junpei's trauma-induced misanthropy while positioning himself as both a friend and a solution to Junpei's pain. Every word is carefully chosen to deepen Junpei's isolation from normal human connection while strengthening his bond with this monster.

"The people who hurt you," Mahito continues, "they chose to cause you pain because they could. But what if you had the power to show them exactly how their victims feel? What if you could make them understand suffering from the other perspective?"

Junpei's expression grows more conflicted. "I... I don't want to become like them. I don't want to be someone who hurts people just because I can."

"Of course not," Mahito says smoothly. "That's exactly why you're different. You've experienced suffering, so you understand its true weight. When you have power, you'll use it justly - to protect the innocent and educate the cruel. You won't be like your bullies because your motivations are pure."

The manipulation is so skillful it's almost artistic in its horror. Mahito is taking Junpei's genuine desire not to become a bully himself and twisting it into justification for much worse actions. By framing potential violence as justice and education rather than revenge, he's giving Junpei a moral framework that could rationalize almost any atrocity.

Your position is becoming precarious. You need to act soon, but the wrong approach could drive Junpei deeper into Mahito's influence or trigger a violent confrontation that could endanger innocent students throughout the school. The curse clearly has significant power, and Junpei's emotional state makes him unpredictable.

From your concealed position, you also notice something troubling. Other students occasionally glance up at the rooftop, but their eyes seem to slide away from Junpei's location as if they can't quite focus on it. Mahito appears to be using some kind of perception-blocking technique to keep their conversations private, which means he's both more powerful and more careful than initial reports suggested.

The weight of the decision before you is enormous. Junpei is still saveable - you can see the conflict in his expression, the part of him that still rejects the path Mahito is offering. But that window is closing rapidly, and once he fully commits to Mahito's ideology, bringing him back may become impossible.

How do you choose to make contact?"""

        first_contact_choices = [
            StoryChoice(
                "Approach openly and try to start a genuine conversation with Junpei",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.DETERMINED: 10, Trait.RECKLESS: 5},
                    "story_flags": {"direct_approach": True, "honest_contact": True},
                    "next_scene": "direct_junpei_conversation",
                    "experience": 55,
                    "relationships": {"junpei": 20},
                    "combat_risk": True
                }
            ),
            StoryChoice(
                "Confront Mahito directly and expose his manipulation",
                {
                    "traits": {Trait.AGGRESSIVE: 15, Trait.PROTECTIVE: 15, Trait.DETERMINED: 10},
                    "story_flags": {"mahito_confrontation": True, "protection_focused": True},
                    "next_scene": "rooftop_mahito_confrontation",
                    "experience": 60,
                    "combat": True,
                    "enemy": "mahito_first_encounter"
                }
            ),
            StoryChoice(
                "Wait and follow them to gather more intelligence about their relationship",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 15, Trait.FOCUSED: 5},
                    "story_flags": {"continued_surveillance": True, "intelligence_priority": True},
                    "next_scene": "extended_surveillance_sequence",
                    "experience": 45,
                    "relationships": {"megumi": 10}
                }
            ),
            StoryChoice(
                "Create a distraction to separate Junpei from Mahito temporarily",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 10, Trait.CAUTIOUS: 10},
                    "story_flags": {"separation_strategy": True, "tactical_approach": True},
                    "next_scene": "separation_distraction_plan",
                    "experience": 50
                }
            )
        ]
        
        self.scenes["first_contact_with_junpei"] = StoryScene(
            "The Rooftop Revelation",
            first_contact_description,
            first_contact_choices,
            "Satozakura High School - Rooftop"
        )
        
        # =================================================================
        # SCENE 4: MAHITO'S TRUE NATURE REVEALED
        # =================================================================
        
        mahito_revelation_description = """Your confrontation with Mahito has revealed the true horror of what Junpei has been drawn into. The cursed spirit's casual attitude toward human suffering is beyond anything you could have imagined, and his power - the ability to reshape human souls and bodies at will - represents a threat unlike any you've trained to face.

"You're just like all the other sorcerers," Mahito says with a twisted smile as he demonstrates his technique on a nearby pigeon, transforming it into a grotesque mockery of its former self before allowing it to revert. "So focused on maintaining the status quo that you can't see the beauty in transformation. Junpei understands - don't you, Junpei?"

Junpei stands frozen between you and Mahito, his face a mask of confusion and growing horror. The demonstrations of Mahito's power have clearly shaken him, but the psychological manipulation runs so deep that he's struggling to process what he's really seeing.

"This is what you wanted to show me?" Junpei asks, his voice barely above a whisper. "The power to... to change people like this?"

"Power to reshape reality itself," Mahito corrects enthusiastically. "Think about it, Junpei. Your bullies, the teachers who ignored your suffering, the system that failed you - all of them could be improved. Made to truly understand the pain they've caused others."

You step forward, trying to reach Junpei before Mahito's words can sink in further. "Junpei, listen to me. What he's showing you isn't justice - it's torture. The power to reshape someone's soul isn't meant to punish or educate. It's meant to destroy what makes them human."

"But they destroyed what made me human first!" Junpei suddenly explodes, tears streaming down his face. "Day after day, week after week, they ground me down until I started to believe that maybe I deserved it! Maybe I was as worthless as they said!"

The pain in his voice is raw and real, and you can see how Mahito has weaponized that trauma. Every genuine hurt Junpei has experienced has been twisted into justification for embracing monstrous power. The curse has taken a victim and convinced him that becoming a victimizer is the only path to healing.

"Your pain is real," you say, trying to project sincerity and understanding. "What they did to you was wrong, and the adults who should have protected you failed. But becoming like Mahito won't heal that pain - it will only create more of it."

Mahito laughs, a sound like glass breaking. "Such naive idealism! Tell me, little sorcerer, what would you do with bullies? Talk to them? Report them to the same authorities who've already failed Junpei? Your solutions are as weak as your convictions."

The challenge hits uncomfortably close to home because you don't have a simple answer. The system did fail Junpei catastrophically, and traditional solutions have already proven inadequate. But that doesn't make Mahito's path of transformation and torture the right alternative.

"I don't know what the perfect solution is," you admit. "But I know it's not this. Junpei, you said yourself that you don't want to become someone who hurts people just because you can. This power that Mahito is offering - it's exactly that. It's the power to hurt people because you can, just dressed up as justice."

Junpei wavers, clearly torn between the pain that drove him to Mahito and the part of him that still rejects cruelty. "But what's the alternative? Go back to being powerless? Go back to being a victim?"

"The alternative is becoming someone who protects other people from going through what you went through," you say. "Using your understanding of suffering to prevent it, not to cause more of it."

Mahito's expression darkens as he realizes his psychological hold on Junpei is being challenged. "Enough philosophy," he says, his casual demeanor shifting to something more predatory. "Junpei, you've already accepted my gift. Use it. Show this meddling sorcerer what real power looks like."

You see the moment of decision in Junpei's eyes - and realize with growing horror that Mahito is right. Junpei has already been marked with cursed energy, already given access to a twisted version of Mahito's soul-shaping technique. The choice isn't whether to give him power anymore; it's whether he'll use the power he already has.

The air around Junpei begins to distort as cursed energy builds around his hands. His technique is crude compared to Mahito's mastery, but the fundamental horror is the same - the ability to reach into someone's soul and reshape it according to his will.

What's your approach to this critical moment?"""

        mahito_revelation_choices = [
            StoryChoice(
                "Try to reach Junpei emotionally before he uses his new power",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.DETERMINED: 10},
                    "story_flags": {"emotional_appeal": True, "save_junpei_attempt": True},
                    "next_scene": "emotional_breakthrough_attempt",
                    "experience": 60,
                    "relationships": {"junpei": 25},
                    "risk": "high_emotional_stakes"
                }
            ),
            StoryChoice(
                "Focus on fighting Mahito to protect Junpei from further manipulation",
                {
                    "traits": {Trait.AGGRESSIVE: 15, Trait.PROTECTIVE: 15, Trait.DETERMINED: 15},
                    "story_flags": {"mahito_battle_priority": True, "protection_focused": True},
                    "next_scene": "mahito_protection_battle",
                    "experience": 70,
                    "combat": True,
                    "enemy": "mahito_serious_fight"
                }
            ),
            StoryChoice(
                "Attempt to disable Junpei's technique before he can use it",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15, Trait.CAUTIOUS: 5},
                    "story_flags": {"technique_disruption": True, "tactical_intervention": True},
                    "next_scene": "technique_disruption_attempt",
                    "experience": 65,
                    "relationships": {"junpei": -10},
                    "risk": "technique_backlash"
                }
            ),
            StoryChoice(
                "Challenge Mahito's philosophy directly to expose his lies to Junpei",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.DETERMINED: 10, Trait.FOCUSED: 10},
                    "story_flags": {"philosophical_challenge": True, "expose_manipulation": True},
                    "next_scene": "mahito_philosophy_confrontation",
                    "experience": 55,
                    "relationships": {"junpei": 15}
                }
            )
        ]
        
        self.scenes["mahito_true_nature_revealed"] = StoryScene(
            "The Horror of Soul Manipulation",
            mahito_revelation_description,
            mahito_revelation_choices,
            "Satozakura High School - Rooftop"
        )
        
        # =================================================================
        # SCENE 5: THE WEIGHT OF HUMAN SOULS
        # =================================================================
        
        weight_of_souls_description = """The confrontation has reached its climax, and the outcome will determine not just Junpei's fate, but potentially the futures of countless other vulnerable people that Mahito might target. Your emotional appeal has created a crack in the psychological manipulation, but Mahito isn't giving up easily.

"Don't listen to them, Junpei," Mahito says urgently, his casual demeanor completely dropped now. "They're trying to drag you back into a world that will never accept you. You've seen what humans really are - cruel, selfish, destructive. Why would you want to protect creatures like that?"

But your words have planted a seed of doubt. Junpei's hands shake as the cursed energy continues to build around them, and you can see the internal war playing out across his face. The part of him that Mahito has corrupted wars with the part that still remembers what it means to care about others.

"I... I don't know anymore," Junpei whispers. "I'm so tired of being in pain. I'm so tired of feeling helpless. But if I use this power... if I become like the people who hurt me..."

"You won't become like them," you say firmly. "Because you're asking that question. Because you're fighting against it even now. The people who hurt you never asked themselves if what they were doing was wrong. You're different because you care about the answer."

Mahito's expression becomes truly malevolent as he realizes he's losing control of the situation. "Enough!" he snarls. "If Junpei won't use his gift willingly, then I'll demonstrate its proper application myself!"

Before you can react, Mahito reaches out toward a group of students visible through the rooftop access door. His technique activates, and you watch in horror as three innocent teenagers begin to convulse, their bodies starting to twist and change under the influence of his soul manipulation.

"Stop!" Junpei screams, the emotional pain in his voice like a physical blow. "They didn't do anything! They're not the ones who hurt me!"

"All humans are the same," Mahito replies coldly, continuing his technique. "These ones, your bullies, your teachers, your mother - they're all capable of the same cruelty given the right circumstances. I'm simply revealing their true nature."

The students' screams echo across the rooftop as their transformations continue. You're faced with an impossible choice - engage Mahito directly to stop the transformations, potentially leaving Junpei vulnerable to further manipulation, or try to save the students while Mahito escapes with his psychological hold on Junpei intact.

But Junpei makes the choice for you.

"I said STOP!" he roars, and his own technique activates - not against you or the innocent students, but against Mahito himself. The cursed spirit staggers as Junpei's crude soul manipulation clashes with his own, creating a feedback loop that forces him to release his hold on the transforming students.

"You lied to me," Junpei says, tears streaming down his face but his voice growing stronger. "You said this power was about justice, about protecting people from suffering. But you just hurt innocent people to make a point. You're exactly like my bullies - you cause pain because you can."

Mahito's shocked expression quickly shifts to rage. "Ungrateful child! I gave you power! I gave you purpose! And you use it against me for the sake of these worthless humans?"

"They're not worthless," Junpei says, his technique growing more stable as his resolve hardens. "Some humans are cruel, yes. Some cause suffering. But that doesn't mean all of them deserve to be transformed into monsters. And it doesn't mean I should become a monster to punish them."

The philosophical breakthrough represents a crucial victory, but the immediate situation remains dangerous. Mahito is now openly hostile, his manipulative facade completely abandoned in favor of pure malevolence. The innocent students are still recovering from their partial transformations, and Junpei - despite his moment of moral clarity - is still inexperienced with his dangerous new abilities.

"You think you've won something?" Mahito laughs bitterly. "Junpei may have rejected me, but the seed is planted. Every time he suffers, every time humans disappoint him, he'll remember the power I gave him. And eventually, he'll use it."

The curse spirit begins to retreat, but not before fixing his gaze on you specifically. "And you, little sorcerer - you think you've saved him? You've only delayed the inevitable. Humans will disappoint him again, and when they do, he'll remember that there's another way. A way to make them understand."

With that ominous promise, Mahito vanishes, leaving you alone on the rooftop with Junpei and the traumatized students. The immediate threat is over, but the larger implications of this encounter are just beginning to sink in.

Junpei collapses to his knees, the emotional and physical strain of opposing Mahito finally overwhelming him. "What have I done?" he whispers. "I almost... I could have hurt them. I could have become exactly what I always hated."

The weight of the moment settles on everyone present. Junpei has rejected Mahito's manipulation and chosen to protect innocent people, but he's still marked with cursed energy, still has access to that terrible power. The question now becomes what happens next - how do you help someone who's been given the ability to reshape souls find a way to live with that responsibility?

How do you want to help Junpei moving forward?"""

        weight_of_souls_choices = [
            StoryChoice(
                "Offer to help Junpei learn to control his technique safely",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 10, Trait.FOCUSED: 10},
                    "story_flags": {"junpei_training_offer": True, "technique_control": True},
                    "next_scene": "junpei_technique_training",
                    "experience": 70,
                    "relationships": {"junpei": 30}
                }
            ),
            StoryChoice(
                "Suggest bringing Junpei to Tokyo Jujutsu High for proper guidance",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.PROTECTIVE: 15, Trait.CAUTIOUS: 10},
                    "story_flags": {"school_integration": True, "official_support": True},
                    "next_scene": "junpei_school_integration",
                    "experience": 65,
                    "relationships": {"junpei": 25, "gojo": 10}
                }
            ),
            StoryChoice(
                "Focus on helping Junpei find healing from his trauma first",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.ANALYTICAL: 5, Trait.PROTECTIVE: 5},
                    "story_flags": {"trauma_healing_priority": True, "emotional_support": True},
                    "next_scene": "junpei_trauma_healing",
                    "experience": 60,
                    "relationships": {"junpei": 35}
                }
            ),
            StoryChoice(
                "Work with Junpei to understand and counter Mahito's influence",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.DETERMINED: 15, Trait.FOCUSED: 10},
                    "story_flags": {"mahito_counter_strategy": True, "intelligence_gathering": True},
                    "next_scene": "anti_mahito_partnership",
                    "experience": 75,
                    "relationships": {"junpei": 25}
                }
            )
        ]
        
        self.scenes["weight_of_human_souls"] = StoryScene(
            "The Weight of Human Souls",
            weight_of_souls_description,
            weight_of_souls_choices,
            "Satozakura High School - Rooftop"
        )
        
        # =================================================================
        # ADDITIONAL SCENES: CHARACTER DEVELOPMENT AND RESOLUTION
        # =================================================================
        
        self._add_junpei_development_scenes()
        self._add_mahito_aftermath_scenes()
        self._add_moral_reflection_scenes()
        self._add_team_bonding_scenes()
        
    def _add_junpei_development_scenes(self):
        """Add scenes focusing on Junpei's character development and integration."""
        
        junpei_training_description = """The training room at Tokyo Jujutsu High feels like a sanctuary compared to the chaos of recent events. Junpei sits across from you, his hands resting carefully in his lap as if he's afraid they might act on their own. The technique Mahito gave him is still there, dormant but ever-present, like a loaded weapon he's forced to carry.

"I can feel it," he says quietly, staring at his hands. "This... thing inside me. It's like having someone else's thoughts mixed with my own. Sometimes I'll look at a person and for just a second, I'll think about how I could change them. How I could make them... better."

The admission hangs in the air between you, heavy with implication. Junpei's honesty is both brave and terrifying - he's acknowledging the corruption that Mahito's influence has left behind while actively fighting against it.

"The important thing is that you recognize those thoughts as foreign," you tell him. "They're not really yours - they're echoes of Mahito's manipulation. The fact that you can identify them and resist them shows that you're still in control."

Gojo-sensei enters the training room, his usual carefree demeanor replaced by something more serious. "How are we doing today?" he asks, though his question is clearly directed at both of you.

"He's making progress," you report. "The cursed energy fluctuations around his technique are becoming more stable. He's learning to contain it without suppressing it completely."

Junpei looks up at Gojo with a mixture of gratitude and apprehension. "Are you sure it's safe for me to be here? What if I lose control? What if I hurt someone?"

Gojo's expression softens slightly. "Junpei, the fact that you're asking that question is exactly why you belong here. Students who don't worry about hurting others are the ones we need to watch carefully. Students who are terrified of their own power... well, they usually turn out to be our best protectors."

The training session that follows is unlike anything in the standard curriculum. Instead of learning to maximize destructive potential, Junpei is learning restraint, precision, and most importantly, consent. His technique touches the very essence of what makes someone human, so every application must be approached with the utmost care and ethical consideration.

"The key is understanding the difference between healing and changing," you explain as you guide him through a basic exercise with a cursed dummy. "Healing restores someone to what they were meant to be. Changing imposes your will on what they should become. Mahito taught you changing. We're teaching you healing."

The distinction proves crucial as Junpei begins to understand how his technique could be used constructively. Instead of reshaping souls according to his judgment of what's better, he can learn to repair damage caused by curses, trauma, or negative emotions. It's still incredibly powerful and potentially dangerous, but the philosophical framework transforms it from a weapon into a tool of genuine healing.

What aspect of Junpei's training do you want to focus on next?"""

        junpei_training_choices = [
            StoryChoice(
                "Work on emotional control and trauma processing",
                {
                    "traits": {Trait.COMPASSIONATE: 10, Trait.FOCUSED: 10},
                    "relationships": {"junpei": 20},
                    "story_flags": {"emotional_training": True},
                    "next_scene": "junpei_emotional_healing",
                    "experience": 45
                }
            ),
            StoryChoice(
                "Focus on technical mastery of his healing applications",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15},
                    "relationships": {"junpei": 15, "gojo": 10},
                    "story_flags": {"technical_mastery": True},
                    "next_scene": "advanced_technique_training",
                    "experience": 50
                }
            ),
            StoryChoice(
                "Help him develop defenses against Mahito's potential return",
                {
                    "traits": {Trait.PROTECTIVE: 15, Trait.ANALYTICAL: 10, Trait.DETERMINED: 10},
                    "relationships": {"junpei": 25},
                    "story_flags": {"anti_mahito_defenses": True},
                    "next_scene": "mahito_defense_training",
                    "experience": 55
                }
            )
        ]
        
        self.scenes["junpei_technique_training"] = StoryScene(
            "Learning to Heal Instead of Harm",
            junpei_training_description,
            junpei_training_choices,
            "Tokyo Jujutsu High - Special Training Room"
        )
        
    def _add_mahito_aftermath_scenes(self):
        """Add scenes dealing with the aftermath of the Mahito encounter."""
        
        aftermath_description = """The debriefing session following the Mahito incident brings together the full faculty and your fellow students. The gravity of what occurred - a human being granted cursed spirit abilities and nearly turned into a weapon - has shaken everyone involved in jujutsu education.

"This represents a new type of threat," Nanami says, his usual composed demeanor showing cracks of concern. "Mahito's ability to corrupt humans at the soul level creates potential enemies who were once innocent victims. Our response protocols are inadequate for this scenario."

Principal Yaga nods grimly. "The psychological manipulation aspect is particularly troubling. Traditional curse elimination techniques are useless if the real weapon is a human being who genuinely believes they're doing the right thing."

You find yourself at the center of the discussion, as your direct involvement in Junpei's rescue has made you something of an expert on the situation. "The key insight," you explain, "is that Mahito doesn't just corrupt people randomly. He specifically targets individuals who are already suffering, already isolated, already questioning the value of human connection. He takes their legitimate pain and weaponizes it."

Megumi raises his hand. "So the best defense would be identifying and helping vulnerable individuals before Mahito can reach them?"

"Exactly," Gojo confirms. "This incident has highlighted gaps in our approach to protecting potential victims. We've focused so heavily on hunting cursed spirits that we've neglected the human factors that make people susceptible to corruption in the first place."

The discussion turns to practical applications - how to identify at-risk individuals, how to provide support that actually addresses root causes rather than just symptoms, and how to counter the specific type of psychological manipulation that Mahito employs.

"There's another concern," Nobara points out. "What happens to people like Junpei who've already been corrupted but fought their way back? Are they permanently changed? Could they relapse?"

The question hangs heavy in the air because nobody has a definitive answer. Junpei's case is unprecedented, and while his rejection of Mahito's influence was genuine, the long-term effects of soul-level manipulation are unknown.

"That's why ongoing support and monitoring are essential," you say. "Not surveillance like he's a threat, but genuine relationship and community that makes it impossible for him to feel isolated enough for Mahito's message to seem appealing again."

The meeting concludes with new protocols for identifying and supporting vulnerable individuals, expanded psychological support resources, and a specialized task force dedicated to understanding and countering Mahito's specific abilities.

But as everyone files out, you can't shake the feeling that this is just the beginning. Mahito is still out there, and his final words on the rooftop suggested that his interest in corrupting humans is far from over.

How do you want to contribute to the ongoing anti-Mahito efforts?"""

        aftermath_choices = [
            StoryChoice(
                "Volunteer for the specialized anti-Mahito task force",
                {
                    "traits": {Trait.DETERMINED: 15, Trait.ANALYTICAL: 10, Trait.PROTECTIVE: 10},
                    "story_flags": {"task_force_member": True, "mahito_specialist": True},
                    "next_scene": "task_force_assignment",
                    "experience": 60,
                    "relationships": {"nanami": 15}
                }
            ),
            StoryChoice(
                "Focus on developing support systems for vulnerable individuals",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.PROTECTIVE: 10},
                    "story_flags": {"support_system_developer": True, "prevention_focused": True},
                    "next_scene": "support_system_development",
                    "experience": 55,
                    "relationships": {"gojo": 10}
                }
            ),
            StoryChoice(
                "Work with Junpei to understand soul manipulation defenses",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15, Trait.COMPASSIONATE: 5},
                    "story_flags": {"soul_defense_research": True, "junpei_partnership": True},
                    "next_scene": "soul_manipulation_research",
                    "experience": 65,
                    "relationships": {"junpei": 20}
                }
            )
        ]
        
        self.scenes["mahito_incident_aftermath"] = StoryScene(
            "Lessons from the Mahito Incident",
            aftermath_description,
            aftermath_choices,
            "Tokyo Jujutsu High - Faculty Conference Room"
        )
        
    def _add_moral_reflection_scenes(self):
        """Add scenes for moral reflection and philosophical development."""
        
        moral_reflection_description = """Late at night, you find yourself on the school grounds, staring up at the stars and thinking about everything that's happened with Junpei and Mahito. The encounter has raised questions that go far beyond typical cursed spirit elimination - questions about justice, human nature, and the responsibility that comes with power.

Yuji joins you on the bench, his usually cheerful demeanor subdued. "Can't sleep either?" he asks.

You shake your head. "I keep thinking about what Mahito said - about humans being fundamentally flawed, capable of great cruelty. The bullying that Junpei experienced, the institutional failures that enabled it... it's hard to argue that he was completely wrong about human nature."

"But he was wrong about the solution," Yuji says firmly. "Even if humans are flawed, that doesn't mean we should give up on them. It means we should work harder to help them be better."

The conversation is interrupted by the arrival of Megumi, who's carrying a thermos of tea. "Couldn't sleep either," he explains. "I've been thinking about the same things."

As the three of you sit together in the quiet night, the conversation deepens into philosophical territory that your formal education barely touched on. What does it mean to protect people who might not deserve protection? How do you maintain faith in humanity when confronted with evidence of systematic cruelty? When is intervention justified, and when does it become control?

"The thing that bothers me most," Megumi says, "is how close Junpei came to accepting Mahito's worldview. And honestly... if I'd gone through what he went through, would I have been strong enough to resist?"

It's a sobering question because none of you can answer it with certainty. Junpei's strength in rejecting Mahito's influence was remarkable, but it came at enormous personal cost and only after he'd already been marked with dangerous power. How many others might not be strong enough or lucky enough to escape similar manipulation?

"Maybe that's the point," you realize aloud. "It's not about being strong enough to resist corruption. It's about building a world where people don't have to resist it alone. Junpei was vulnerable because he was isolated. Mahito's manipulation worked because Junpei had no one else offering him support or hope."

The insight feels important, but it also raises new questions about your role as jujutsu sorcerers. Is it enough to simply eliminate curses after they've caused damage? Or do you have a responsibility to address the human conditions that make corruption possible in the first place?

What philosophical approach do you want to embrace moving forward?"""

        moral_reflection_choices = [
            StoryChoice(
                "Commit to a preventive approach focused on addressing root causes",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.ANALYTICAL: 10, Trait.PROTECTIVE: 10},
                    "story_flags": {"preventive_philosophy": True, "root_cause_focus": True},
                    "next_scene": "preventive_sorcery_path",
                    "experience": 50,
                    "relationships": {"yuji": 15, "megumi": 10}
                }
            ),
            StoryChoice(
                "Focus on being prepared to help people who are already suffering",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.PROTECTIVE: 15},
                    "story_flags": {"rescue_philosophy": True, "healing_focus": True},
                    "next_scene": "healing_sorcery_path",
                    "experience": 45,
                    "relationships": {"yuji": 20}
                }
            ),
            StoryChoice(
                "Emphasize the importance of community and connection in resistance",
                {
                    "traits": {Trait.COMPASSIONATE: 10, Trait.ANALYTICAL: 5, Trait.FOCUSED: 10},
                    "story_flags": {"community_philosophy": True, "connection_focus": True},
                    "next_scene": "community_building_path",
                    "experience": 55,
                    "relationships": {"yuji": 15, "megumi": 15, "junpei": 10}
                }
            )
        ]
        
        self.scenes["moral_philosophical_reflection"] = StoryScene(
            "Questions in the Starlight",
            moral_reflection_description,
            moral_reflection_choices,
            "Tokyo Jujutsu High - Courtyard Gardens"
        )
        
    def _add_team_bonding_scenes(self):
        """Add scenes for team bonding and relationship development after the crisis."""
        
        team_bonding_description = """The week following the Mahito incident has brought your group closer together in ways that normal training never could. Facing a crisis that challenged not just your abilities but your fundamental beliefs about humanity and justice has created bonds that feel deeper than mere friendship.

Junpei has been gradually integrating into your circle, though the process isn't without challenges. His experiences have left him with perspectives that sometimes clash with the more optimistic worldviews of your classmates, but those differences have led to conversations that have enriched everyone's understanding.

"I still have trouble trusting adults," Junpei admits during a group lunch. "When I needed help most, every adult who was supposed to protect me either failed or actively made things worse. It's hard to shake that feeling that institutions will always prioritize convenience over doing what's right."

Nobara nods thoughtfully. "I get that. I grew up in a small town where everyone knew everyone, and there were definitely adults who chose to look the other way when convenient. But there are also adults like Gojo-sensei and Nanami-sensei who go out of their way to do right by us."

"Maybe the key is not blind trust in institutions, but careful evaluation of individuals," Megumi suggests. "Some adults deserve trust, others don't. Some systems work, others fail. The trick is learning to tell the difference."

The conversation represents progress for everyone involved. Junpei is learning to distinguish between justified caution and cynical withdrawal, while the rest of you are gaining appreciation for perspectives shaped by different experiences of trauma and recovery.

Your training sessions have also evolved to incorporate lessons learned from the Mahito encounter. Instead of focusing solely on individual technique development, there's new emphasis on psychological resilience, ethical decision-making under pressure, and recognizing signs of manipulation or corruption.

"The most dangerous curses," Gojo explained during a recent lecture, "aren't necessarily the strongest ones. They're the ones that convince you they're not really enemies at all. Mahito's true power wasn't soul manipulation - it was the ability to make victims feel like willing participants in their own destruction."

These insights have practical applications that extend far beyond curse elimination. Learning to recognize and counter manipulation makes you better equipped to help people in various forms of distress, whether supernatural or entirely mundane.

As the group dynamic continues to evolve, you find yourself in a unique position - having been central to Junpei's rescue, you've become something of a bridge between his traumatic past and his hopeful future with the group.

How do you want to continue supporting both Junpei's integration and the group's overall development?"""

        team_bonding_choices = [
            StoryChoice(
                "Organize group activities that help Junpei build positive social experiences",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.FOCUSED: 10},
                    "story_flags": {"social_integration_leader": True, "positive_experiences": True},
                    "next_scene": "group_activity_planning",
                    "experience": 40,
                    "relationships": {"junpei": 20, "group": 15}
                }
            ),
            StoryChoice(
                "Focus on developing the group's collective understanding of trauma and recovery",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 10, Trait.FOCUSED: 10},
                    "story_flags": {"trauma_education": True, "group_wisdom": True},
                    "next_scene": "trauma_understanding_development",
                    "experience": 50,
                    "relationships": {"group": 20}
                }
            ),
            StoryChoice(
                "Work on building the group's resistance to manipulation and corruption",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.PROTECTIVE: 10, Trait.CAUTIOUS: 5},
                    "story_flags": {"corruption_resistance": True, "group_protection": True},
                    "next_scene": "manipulation_resistance_training",
                    "experience": 55,
                    "relationships": {"group": 15}
                }
            )
        ]
        
        self.scenes["team_bonding_after_crisis"] = StoryScene(
            "Stronger Together",
            team_bonding_description,
            team_bonding_choices,
            "Tokyo Jujutsu High - Student Common Room"
        )
        
    def get_all_scenes(self):
        """Return all scenes in the Vs. Mahito/Junpei Arc."""
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