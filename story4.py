"""
Shibuya Incident Arc - The Point of No Return

This module contains the expanded Shibuya Incident Arc story content featuring
high-stakes battles, moral complexity, character sacrifice, and world-changing events.
Minimum 800 lines of detailed story content focusing on loss, growth, and consequences.
"""

from typing import Dict, List, Any, Optional
from character import Trait
from story import StoryChoice, StoryScene


class ShibuyaIncidentArc:
    """Manages the Shibuya Incident Arc story scenes and progression."""
    
    def __init__(self):
        self.scenes = {}
        self._initialize_shibuya_arc()
    
    def _initialize_shibuya_arc(self):
        """Initialize all Shibuya Incident Arc story scenes."""
        
        # =================================================================
        # SCENE 1: THE NIGHT EVERYTHING CHANGED
        # =================================================================
        
        shibuya_setup_description = """Halloween night in Shibuya should be a celebration - thousands of costumed revelers crowding the famous crossing, enjoying the festive atmosphere of Tokyo's most vibrant district. Instead, the air thrums with malevolent energy as cursed spirits converge on the area in unprecedented numbers. This isn't a random occurrence; intelligence suggests a coordinated operation designed to trap and eliminate jujutsu sorcerers.

You stand with your team on a rooftop overlooking the chaos, watching as crowds of civilians flee from monstrous apparitions that have materialized throughout the district. The scale of the incident is unlike anything in recent jujutsu history - multiple Grade 1 spirits operating simultaneously, with what appears to be strategic coordination between different cursed entities.

"The barrier encompassing the area is preventing civilians from leaving while keeping law enforcement out," Megumi reports, his divine dogs having completed reconnaissance of the perimeter. "Whatever this is, it's been planned to create maximum chaos while isolating the area from outside intervention."

Yuji's expression is grim as he surveys the destruction below. "There are still thousands of people trapped down there. We can't just focus on the cursed spirits - we need to prioritize civilian evacuation."

"But that's exactly what they want," Nobara points out, her tactical instincts sharp despite the emotional weight of the situation. "Force us to divide our attention between combat and rescue operations. Classic strategy for overwhelming superior opponents."

Junpei, who has been unusually quiet since arriving at the scene, finally speaks up. "There's something else. The cursed energy signatures down there... some of them feel familiar. Like the energy that Mahito used to mark me."

His observation sends a chill through the group. If Mahito is involved in this operation, then the psychological and spiritual threats go far beyond simple combat challenges. His ability to corrupt and manipulate humans could turn civilian rescue operations into encounters with transformed monsters.

"Gojo-sensei should be handling the major threats," you note, looking for any sign of your teacher's distinctive energy signature. "But I'm not sensing him anywhere in the area. Either he's being blocked by the barrier, or..."

The implication hangs unspoken in the air. If Gojo has been neutralized or prevented from responding, then the responsibility for handling this crisis falls to students who, despite their training and recent experiences, are not prepared for an operation of this magnitude.

"We need to make a decision," Megumi says pragmatically. "Wait for adult sorcerer support that may not come, or begin operations with the understanding that we're potentially on our own."

The weight of command falls heavily on your shoulders as your teammates look to you for guidance. The mission parameters are unclear, the threat level is beyond your usual assignments, and the stakes - both for trapped civilians and for the jujutsu world's response to this crisis - could hardly be higher.

From the streets below, screams echo as civilians encounter horrors that their minds struggle to process. Every moment of hesitation means more innocent lives at risk, but reckless action could lead to catastrophic failure that makes the situation even worse.

"Whatever we decide," Yuji says firmly, "we do it together. No one gets left behind, and we don't abandon civilians to save ourselves."

His words crystallize the moral framework that will guide your decisions throughout the crisis. This isn't just about surviving or completing a mission - it's about upholding the fundamental principles that define what it means to be a jujutsu sorcerer.

What's your approach to this unprecedented crisis?"""

        shibuya_setup_choices = [
            StoryChoice(
                "Prioritize civilian evacuation while fighting defensively against cursed spirits",
                {
                    "traits": {Trait.PROTECTIVE: 20, Trait.COMPASSIONATE: 15, Trait.CAUTIOUS: 10},
                    "story_flags": {"civilian_priority": True, "defensive_approach": True, "evacuation_focus": True},
                    "next_scene": "civilian_evacuation_mission",
                    "experience": 70,
                    "relationships": {"civilians": 25, "team": 15}
                }
            ),
            StoryChoice(
                "Focus on eliminating the strongest cursed spirits to reduce overall threat level",
                {
                    "traits": {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 20, Trait.PROTECTIVE: 10},
                    "story_flags": {"combat_priority": True, "threat_elimination": True, "aggressive_approach": True},
                    "next_scene": "major_threat_engagement",
                    "experience": 80,
                    "combat": True,
                    "enemy": "grade_1_curse_coordinated"
                }
            ),
            StoryChoice(
                "Investigate the source of coordination to disrupt the operation",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15, Trait.CAUTIOUS: 10},
                    "story_flags": {"investigation_priority": True, "strategic_approach": True, "coordination_disruption": True},
                    "next_scene": "coordination_source_investigation",
                    "experience": 75,
                    "relationships": {"megumi": 15}
                }
            ),
            StoryChoice(
                "Split the team to handle multiple priorities simultaneously",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.PROTECTIVE: 15, Trait.DETERMINED: 15},
                    "story_flags": {"divided_approach": True, "multi_priority": True, "team_coordination": True},
                    "next_scene": "divided_operations_plan",
                    "experience": 85,
                    "relationships": {"team": 20},
                    "risk": "team_separation"
                }
            )
        ]
        
        self.scenes["shibuya_incident_begins"] = StoryScene(
            "The Night Everything Changed",
            shibuya_setup_description,
            shibuya_setup_choices,
            "Shibuya District - Rooftop Overlook"
        )
        
        # =================================================================
        # SCENE 2: INTO THE HEART OF DARKNESS
        # =================================================================
        
        heart_of_darkness_description = """Descending into the chaos of Shibuya's streets feels like entering a war zone designed by nightmares. The familiar landmarks of Tokyo's most famous district have been transformed into a hellscape where reality itself seems unstable. Buildings twist at impossible angles, shadows move independently of their sources, and the very air shimmers with malevolent cursed energy.

Your team moves in formation through streets that should be crowded with Halloween revelers but are instead littered with the evidence of panic and supernatural violence. Abandoned costumes, overturned vehicles, and scattered personal belongings tell the story of a civilian population that encountered horrors beyond their comprehension.

"The cursed energy concentration is getting stronger as we move toward the center," Junpei reports, his unique sensitivity to soul manipulation allowing him to detect patterns that others might miss. "But there's something else - the energy isn't just from cursed spirits. There are humans down here who've been... changed somehow."

His observation proves prophetic as you encounter your first group of affected civilians. They're still recognizably human, but their behavior is wrong in fundamental ways. They move with predatory coordination, their eyes reflect light like animals, and when they speak, their voices carry harmonics that suggest vocal cords reshaped for different purposes.

"Transfigured humans," Megumi identifies grimly. "Mahito's technique. He's been using the chaos to experiment on civilians, turning them into weapons while maintaining enough of their original form to cause psychological trauma for anyone trying to fight them."

The moral complexity of the situation immediately becomes apparent. These creatures were innocent people hours ago, transformed against their will into something monstrous. Fighting them feels like perpetuating the very victimization that Mahito feeds on, but allowing them to continue their attacks endangers other civilians who might still be saved.

"There has to be a way to reverse the transformation," Yuji says desperately, his characteristic empathy struggling with the tactical necessities of the situation. "We can't just treat them as enemies when they're really victims."

"Mahito's soul manipulation is theoretically reversible," Junpei says quietly, "but only if the transformation is very recent and the person's original soul shape is still accessible. After a certain point, the changes become permanent."

The time pressure adds another layer of urgency to an already overwhelming situation. Every moment spent in moral deliberation is time that allows more civilians to be transformed beyond the point of recovery.

As you advance deeper into the district, the encounters become more frequent and more disturbing. The transformed humans show increasing degrees of modification - some still clearly recognizable as former people, others so altered that their humanity is barely detectable. The progression suggests that Mahito is using this crisis as an opportunity for large-scale experimentation.

"Movement ahead," Nobara calls out, pointing toward the Shibuya Crossing intersection. "Multiple contacts, but the energy signatures are... wrong. Not fully human, not fully cursed spirit."

The observation proves accurate as you approach what was once Tokyo's most famous intersection. The area is now dominated by a massive cursed spirit that appears to be composed of dozens of transformed humans, their bodies and souls fused into a collective entity that retains the memories and personalities of its component parts while serving a single malevolent will.

"My family," one section of the creature speaks in a voice that was once human. "I was looking for my family. Have you seen them? Please, I need to find them."

The psychological warfare is as devastating as any physical attack. Mahito has created an enemy that weaponizes compassion, turning the very empathy that motivates sorcerers to protect people into a vulnerability that can be exploited.

"This is what he wants," you realize aloud. "He's not just creating monsters - he's forcing us to choose between our humanity and our effectiveness. Every choice that preserves our compassion weakens our tactical position, and every tactical decision that prioritizes effectiveness requires us to abandon our principles."

The philosophical challenge represents the true test of the Shibuya incident. It's not enough to be strong enough to defeat the threats - you must find ways to do so while maintaining the moral foundation that justifies being a jujutsu sorcerer in the first place.

How do you approach this impossible moral dilemma?"""

        heart_of_darkness_choices = [
            StoryChoice(
                "Try to separate the transformed humans from the collective entity to attempt reversal",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.DETERMINED: 15, Trait.ANALYTICAL: 10},
                    "story_flags": {"separation_attempt": True, "reversal_priority": True, "compassionate_approach": True},
                    "next_scene": "transformation_reversal_attempt",
                    "experience": 80,
                    "relationships": {"junpei": 20},
                    "risk": "compassion_exploitation"
                }
            ),
            StoryChoice(
                "Focus on defeating the collective entity quickly to prevent further transformations",
                {
                    "traits": {Trait.DETERMINED: 20, Trait.PROTECTIVE: 15, Trait.AGGRESSIVE: 10},
                    "story_flags": {"quick_elimination": True, "utilitarian_choice": True, "future_protection": True},
                    "next_scene": "collective_entity_battle",
                    "experience": 85,
                    "combat": True,
                    "enemy": "mahito_collective_entity",
                    "moral_cost": True
                }
            ),
            StoryChoice(
                "Attempt to communicate with the retained human consciousness",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.ANALYTICAL: 15, Trait.FOCUSED: 10},
                    "story_flags": {"communication_attempt": True, "consciousness_contact": True, "understanding_priority": True},
                    "next_scene": "consciousness_communication",
                    "experience": 75,
                    "relationships": {"civilians": 20},
                    "risk": "psychological_trauma"
                }
            ),
            StoryChoice(
                "Look for Mahito himself to stop the transformations at their source",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.DETERMINED: 15, Trait.AGGRESSIVE: 10},
                    "story_flags": {"source_priority": True, "mahito_tracking": True, "strategic_thinking": True},
                    "next_scene": "mahito_source_tracking",
                    "experience": 90,
                    "relationships": {"team": 15}
                }
            )
        ]
        
        self.scenes["heart_of_shibuya_darkness"] = StoryScene(
            "Into the Heart of Darkness",
            heart_of_darkness_description,
            heart_of_darkness_choices,
            "Shibuya District - Crossing Intersection"
        )
        
        # =================================================================
        # SCENE 3: THE WEIGHT OF IMPOSSIBLE CHOICES
        # =================================================================
        
        impossible_choices_description = """The deeper you penetrate into Shibuya's transformed landscape, the more apparent it becomes that this crisis was designed specifically to break the moral framework that guides jujutsu sorcerers. Every scenario presents choices where the right decision by traditional ethical standards leads to worse outcomes for everyone involved.

You've encountered three groups of civilians trapped in different locations, each requiring immediate assistance but in ways that prevent you from helping the others. A family barricaded in a convenience store, slowly being stalked by transformed humans who were once their neighbors. A group of teenagers trapped on a subway platform as cursed spirits systematically hunt them through the tunnels. An elderly man protecting a injured child in an alley while a Grade 1 spirit tears through the surrounding buildings, getting closer with each passing moment.

"We can't save all of them," Megumi states the horrible truth that everyone is thinking. "Our resources are finite, and the threats are designed to force us into triage decisions that compromise our principles."

The tactical reality is undeniable, but accepting it feels like a fundamental betrayal of everything you've trained to become. Jujutsu sorcerers exist to protect people - all people, not just the ones that tactical considerations deem most strategically valuable.

"There has to be another way," Yuji insists, though his voice carries the strain of someone who's beginning to doubt his own words. "We're supposed to be the ones who don't accept that people have to die just because someone else decides they're expendable."

Junpei, whose experience with systematic victimization gives him a different perspective on moral compromises, offers a darker insight. "Sometimes the only choices available are different types of failure. The question becomes which failure you can live with, not which success you can achieve."

His words hit uncomfortably close to the truth. This isn't a situation where clever tactics or superior power can create perfect outcomes. Someone is going to suffer regardless of your decisions, and the enemy has specifically structured things to ensure that your moral principles become liabilities rather than strengths.

"The family in the store has the best defensive position but the least time," Nobara analyzes coldly. "The teenagers have more time but no defenses. The elderly man and child are most vulnerable but closest to our current position."

The utilitarian calculus is clear - save the maximum number of people with the minimum expenditure of resources. But reducing human lives to tactical equations feels like exactly the kind of dehumanization that creates the conditions for Mahito's corruption in the first place.

From the streets around you, the sounds of suffering continue - screams, crashes, and the inhuman vocalizations of creatures that were once people. Each sound represents someone who needed help that didn't come in time, someone whose life was ended or transformed because the tactical situation didn't permit their rescue.

"Listen," you say to your team, the weight of command heavy on your shoulders. "We've trained for combat, we've trained for rescue operations, but we've never trained for this - systematic moral warfare designed to corrupt our fundamental principles. We need to acknowledge that we're facing something new."

The admission is both necessary and terrifying. If traditional jujutsu training hasn't prepared you for this type of crisis, then you're essentially improvising responses to threats that could determine the future direction of jujutsu society.

"Maybe that's the point," Megumi observes grimly. "Force us to make choices that contradict our principles, then use those compromises to justify further moral degradation. Turn us into the kind of people who can rationalize abandoning civilians for tactical advantage."

The insight reveals the deeper strategy behind the Shibuya incident. It's not just about causing damage or eliminating sorcerers - it's about forcing fundamental changes in how jujutsu society operates, creating precedents for moral compromise that can be exploited in future conflicts.

As the weight of these realizations settles on the team, you hear a new sound echoing through the district - laughter. Mahito's distinctive, chilling amusement carries clearly through the chaos, suggesting that your moral struggles are being observed and evaluated.

"He's watching," Junpei says quietly. "This is all entertainment for him. Our suffering, the civilians' terror, the impossible choices - it's exactly what he wanted to create."

The knowledge that your anguish is part of the enemy's plan adds another layer of complexity to an already overwhelming situation. Do you make decisions based on what you believe is right, knowing that those decisions are part of a larger manipulation? Or do you try to confound the manipulation by acting against your principles, potentially becoming exactly what the enemy wants you to become?

What approach do you take to these impossible moral choices?"""

        impossible_choices_choices = [
            StoryChoice(
                "Maintain your principles regardless of tactical consequences",
                {
                    "traits": {Trait.COMPASSIONATE: 25, Trait.DETERMINED: 20, Trait.PROTECTIVE: 15},
                    "story_flags": {"principled_stance": True, "moral_integrity": True, "tactical_disadvantage_accepted": True},
                    "next_scene": "principled_decision_consequences",
                    "experience": 70,
                    "relationships": {"yuji": 25, "civilians": 30},
                    "moral_cost": "tactical_weakness"
                }
            ),
            StoryChoice(
                "Make tactical decisions and deal with the moral consequences later",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15, Trait.CAUTIOUS: 10},
                    "story_flags": {"utilitarian_approach": True, "tactical_priority": True, "delayed_moral_processing": True},
                    "next_scene": "utilitarian_decision_path",
                    "experience": 85,
                    "relationships": {"megumi": 15},
                    "moral_cost": "principle_compromise"
                }
            ),
            StoryChoice(
                "Try to find creative solutions that transcend the false dilemmas",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.DETERMINED: 20, Trait.FOCUSED: 15},
                    "story_flags": {"creative_solutions": True, "transcendent_thinking": True, "dilemma_rejection": True},
                    "next_scene": "creative_solution_attempt",
                    "experience": 95,
                    "relationships": {"team": 20},
                    "risk": "resource_overextension"
                }
            ),
            StoryChoice(
                "Acknowledge the manipulation and choose actions that deny Mahito satisfaction",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.DETERMINED: 15, Trait.FOCUSED: 15},
                    "story_flags": {"meta_awareness": True, "manipulation_denial": True, "strategic_psychology": True},
                    "next_scene": "anti_manipulation_strategy",
                    "experience": 80,
                    "relationships": {"junpei": 20}
                }
            )
        ]
        
        self.scenes["impossible_moral_choices"] = StoryScene(
            "The Weight of Impossible Choices",
            impossible_choices_description,
            impossible_choices_choices,
            "Shibuya District - Multiple Crisis Points"
        )
        
        # =================================================================
        # SCENE 4: CONFRONTING MAHITO
        # =================================================================
        
        mahito_confrontation_description = """The moment you've been dreading and anticipating finally arrives as you track Mahito to his chosen battlefield - the ruins of what was once Shibuya's central shopping district. The area has been transformed into an amphitheater of suffering, with transformed humans arranged as both audience and potential weapons. Mahito stands at the center, his patchwork form radiating satisfaction as he surveys the chaos he's orchestrated.

"Welcome to my laboratory!" he calls out with genuine enthusiasm as your team approaches. "I've been so looking forward to seeing how you've developed since our last encounter. Especially you, Junpei - I'm curious to see if your little moral awakening has made you stronger or just more conflicted."

The psychological warfare begins immediately, with Mahito's words designed to undermine team cohesion and individual confidence. His technique for reading and manipulating souls gives him insights into psychological vulnerabilities that he exploits with surgical precision.

"Tell me," he continues, addressing the group but keeping his primary focus on you, "how many civilians did you save tonight? How many did you abandon? I've been keeping count, and the ratios are... illuminating."

The cruelty of the question lies not in its content but in its accuracy. Every member of your team is carrying the weight of people they couldn't help, decisions that prioritized some lives over others, moral compromises that felt necessary in the moment but seem increasingly questionable in retrospect.

"You're enjoying this," Yuji says, his voice tight with controlled anger. "All the suffering, all the impossible choices - it's entertainment for you."

"Not entertainment," Mahito corrects with mock seriousness. "Education! You see, I'm teaching the jujutsu world a valuable lesson about the true nature of human morality. When pushed to their limits, even the most principled people will abandon their convictions for tactical advantage."

His words carry the weight of observed truth because they're based on systematic study of exactly the scenarios you've been facing all night. Every moral compromise, every utilitarian calculation, every decision to prioritize some lives over others has been carefully documented and analyzed.

"But you, Junpei," Mahito continues, his attention shifting to your teammate whose relationship with the cursed spirit represents the most complex dynamic present. "You've been particularly interesting to observe. How does it feel to use the power I gave you to fight against me? The irony is delicious."

Junpei's response reveals the psychological growth he's achieved since your first encounter with Mahito. "The power was never yours," he says steadily. "You gave me access to it, but what it becomes depends on how it's used. Tonight I've used it to heal people you transformed, to undo damage you caused. That's not irony - that's justice."

The philosophical exchange represents more than mere dialogue - it's a battle for the ideological framework that will determine how this conflict is understood and remembered. Mahito's goal isn't just to win the immediate fight, but to establish a worldview where his approach to human nature is validated by the evidence of how heroes behave under pressure.

"Ah, but you've had to make choices tonight that contradict your precious principles," Mahito counters. "You've abandoned people to save others, used tactical deception that relied on civilian suffering, prioritized strategic objectives over individual lives. How are you different from me, really?"

The question strikes at the heart of the moral crisis that has defined the entire Shibuya incident. In the face of systematic manipulation designed to force moral compromises, how do you maintain the distinction between necessary tactical decisions and the casual cruelty that defines true evil?

"The difference," you say, finding your voice as the weight of leadership crystallizes into clear purpose, "is that our choices cause us pain. We don't enjoy making decisions that compromise our principles - we do it because the alternatives are worse. You've structured this entire situation to force us into those choices specifically so you can point to them as evidence that we're the same. But the fact that we struggle with these decisions is exactly what makes us different."

Mahito's expression shifts slightly, his amusement giving way to something approaching genuine interest. "Fascinating perspective! So you're arguing that moral anguish itself is what defines virtue? That suffering over your choices somehow purifies them?"

The philosophical challenge forces you to articulate the deeper principles that have guided your development as a sorcerer, the fundamental beliefs that distinguish protection from control, justice from revenge, necessary violence from cruelty for its own sake.

How do you choose to confront Mahito and the ideology he represents?"""

        mahito_confrontation_choices = [
            StoryChoice(
                "Engage in philosophical debate to expose the flaws in his worldview",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15, Trait.DETERMINED: 10},
                    "story_flags": {"philosophical_engagement": True, "ideological_combat": True, "worldview_challenge": True},
                    "next_scene": "philosophical_battle_with_mahito",
                    "experience": 85,
                    "relationships": {"junpei": 20}
                }
            ),
            StoryChoice(
                "Focus on physical combat to end his ability to cause more suffering",
                {
                    "traits": {Trait.AGGRESSIVE: 20, Trait.DETERMINED: 20, Trait.PROTECTIVE: 15},
                    "story_flags": {"combat_priority": True, "suffering_prevention": True, "direct_approach": True},
                    "next_scene": "direct_mahito_combat",
                    "experience": 90,
                    "combat": True,
                    "enemy": "mahito_final_form"
                }
            ),
            StoryChoice(
                "Demonstrate the strength that comes from moral principles under pressure",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.DETERMINED: 20, Trait.PROTECTIVE: 15},
                    "story_flags": {"moral_demonstration": True, "principle_strength": True, "virtue_power": True},
                    "next_scene": "moral_strength_demonstration",
                    "experience": 95,
                    "relationships": {"team": 25, "civilians": 20}
                }
            ),
            StoryChoice(
                "Work with Junpei to turn Mahito's own technique against him",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15, Trait.PROTECTIVE: 15},
                    "story_flags": {"junpei_partnership": True, "technique_reversal": True, "poetic_justice": True},
                    "next_scene": "junpei_mahito_reversal",
                    "experience": 100,
                    "relationships": {"junpei": 30},
                    "combat": True,
                    "enemy": "mahito_soul_battle"
                }
            )
        ]
        
        self.scenes["final_mahito_confrontation"] = StoryScene(
            "Confronting the Monster's Philosophy",
            mahito_confrontation_description,
            mahito_confrontation_choices,
            "Shibuya District - Mahito's Laboratory"
        )
        
        # =================================================================
        # SCENE 5: THE COST OF VICTORY
        # =================================================================
        
        cost_of_victory_description = """The battle with Mahito has ended, but victory feels hollow when measured against the devastation surrounding you. Shibuya District lies in ruins, its famous streets scarred by supernatural violence and littered with the evidence of lives that couldn't be saved. The civilian casualties are staggering - not just those killed outright, but those transformed into something inhuman and left to struggle with identities that no longer feel like their own.

You sit on the steps of what was once a busy department store, your team gathered around you in exhausted silence. The physical injuries from the night's battles are significant but treatable - it's the psychological and moral wounds that will take much longer to heal. Each member of your group is processing their own version of the trauma that defines the Shibuya incident.

"We won," Yuji says quietly, though his tone suggests someone trying to convince himself of a fact that doesn't feel true. "Mahito is defeated, the cursed spirits are eliminated, the immediate threat is over. So why does it feel like we lost?"

The question captures the complex reality of this kind of victory. Success in terms of mission objectives achieved doesn't necessarily translate to success in terms of values preserved or people protected. The enemy has been defeated, but at costs that challenge fundamental assumptions about what it means to be a jujutsu sorcerer.

"Because we had to become people we didn't want to be in order to win," Megumi answers with characteristic bluntness. "Every tactical decision that prioritized mission success over individual lives, every moral compromise that we justified as necessary - those changes in us are part of the victory's price."

Nobara nods slowly, examining her hands as if seeing them for the first time. "I keep thinking about the people we couldn't save. Not because we weren't strong enough or fast enough, but because saving them would have meant failing to save others. Having to choose who lives and who dies... that's going to stay with me."

Junpei's perspective, shaped by his unique relationship with both Mahito and the consequences of soul manipulation, offers a different angle on the night's events. "Maybe that's what growth looks like at this level," he suggests hesitantly. "Not becoming stronger or more skilled, but learning to carry the weight of impossible decisions without letting them break you."

The insight is profound and disturbing because it suggests that advancement in jujutsu sorcery involves not just developing power, but developing the psychological resilience to make morally complex choices under extreme pressure. The kind of choices that would destroy someone who hadn't been prepared for them.

From the streets around you, the sounds of cleanup and recovery begin as reinforcements finally arrive. Medical teams, curse specialists, and officials from various jujutsu institutions converge on Shibuya to begin the complex process of dealing with the aftermath. Their efficiency is impressive, but it also highlights how much of the crisis you were forced to handle alone.

"Where was everyone?" Nobara asks with an edge of bitterness in her voice. "We're students. We shouldn't have been handling something like this without adult support."

The question touches on larger issues within jujutsu society - resource allocation, emergency response protocols, and the tendency to rely on exceptional individuals rather than systemic solutions. The fact that first-year students were left to handle a Grade 1 threat scenario suggests problems that go beyond simple bad luck or poor planning.

"Gojo-sensei was detained by a special-grade situation across the city," a familiar voice explains as Nanami approaches your group. His appearance is disheveled and he's clearly been in his own battles throughout the night. "Multiple coordinated attacks designed to stretch our response capabilities beyond their limits. You handled an impossible situation with remarkable skill and character."

His assessment provides some validation, but it also confirms that the night's events were part of a larger strategy designed to exploit weaknesses in jujutsu society's defensive capabilities. The enemy didn't just want to cause damage - they wanted to demonstrate the inadequacy of current protection systems.

"The official reports will focus on mission success and threat elimination," Nanami continues, "but I want you to know that your performance tonight represents something more significant. You've demonstrated that the next generation of sorcerers can maintain their principles even under extreme pressure. That's... rarer than it should be."

The praise is meaningful but also carries implications about previous generations and the moral compromises that may have become normalized in jujutsu society. Your team's struggle to maintain ethical standards might be unusual precisely because those standards have been eroded by repeated exposure to impossible choices.

"What happens now?" you ask, looking out over the destruction that represents both your failure to prevent all suffering and your success in preventing much worse outcomes.

The question encompasses both immediate practical concerns and longer-term philosophical implications. How do you move forward as individuals who have been fundamentally changed by this experience? How does jujutsu society adapt to threats that target moral foundations rather than just physical capabilities?

How do you want to process and move forward from this experience?"""

        cost_of_victory_choices = [
            StoryChoice(
                "Focus on helping your team process the moral complexity of what you experienced",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.PROTECTIVE: 15, Trait.ANALYTICAL: 10},
                    "story_flags": {"team_support_priority": True, "moral_processing": True, "psychological_healing": True},
                    "next_scene": "team_trauma_processing",
                    "experience": 75,
                    "relationships": {"team": 30}
                }
            ),
            StoryChoice(
                "Work on developing better protocols for future crisis situations",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15, Trait.DETERMINED: 10},
                    "story_flags": {"protocol_development": True, "systemic_improvement": True, "future_preparation": True},
                    "next_scene": "crisis_protocol_development",
                    "experience": 80,
                    "relationships": {"nanami": 20, "faculty": 15}
                }
            ),
            StoryChoice(
                "Advocate for changes in how jujutsu society trains and prepares students",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.PROTECTIVE: 20, Trait.DETERMINED: 15},
                    "story_flags": {"educational_reform": True, "student_protection": True, "systemic_change": True},
                    "next_scene": "educational_system_reform",
                    "experience": 85,
                    "relationships": {"faculty": 20}
                }
            ),
            StoryChoice(
                "Reflect on personal growth and what this experience has taught you about being a sorcerer",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15, Trait.COMPASSIONATE: 15},
                    "story_flags": {"personal_reflection": True, "philosophical_growth": True, "identity_development": True},
                    "next_scene": "personal_philosophical_reflection",
                    "experience": 70,
                    "relationships": {"self": 25}
                }
            )
        ]
        
        self.scenes["shibuya_victory_cost"] = StoryScene(
            "The Cost of Victory",
            cost_of_victory_description,
            cost_of_victory_choices,
            "Shibuya District - Aftermath"
        )
        
        # =================================================================
        # ADDITIONAL SCENES: CHARACTER DEVELOPMENT AND LONG-TERM CONSEQUENCES
        # =================================================================
        
        self._add_aftermath_scenes()
        self._add_character_resolution_scenes()
        self._add_long_term_consequence_scenes()
        self._add_growth_integration_scenes()
        
    def _add_aftermath_scenes(self):
        """Add scenes dealing with the immediate aftermath of the Shibuya incident."""
        
        aftermath_processing_description = """The weeks following the Shibuya incident have been a blur of debriefings, medical evaluations, and psychological assessments. The jujutsu community is struggling to process not just the immediate damage, but the larger implications of what the crisis revealed about their preparedness and defensive capabilities.

You find yourself in the school's counseling center, a facility that had been underutilized before Shibuya but is now operating at capacity as students and faculty work through trauma that goes beyond anything their training prepared them for. The counselor across from you is someone specifically brought in to deal with the unique psychological challenges that arise from supernatural combat.

"The recurring nightmares are normal," she explains with professional compassion. "When you're forced to make life-or-death decisions under extreme stress, your mind continues processing those scenarios long after the immediate danger has passed. The important thing is learning to distinguish between useful analysis and destructive rumination."

The distinction is more difficult than it sounds because the decisions you made during the crisis require ongoing evaluation. Were they the right choices? Could different approaches have achieved better outcomes? How do you prevent similar moral dilemmas in future situations?

"What troubles me most," you admit, "is how natural some of those tactical decisions felt in the moment. Prioritizing strategic objectives over individual lives, using deception and misdirection... it felt like I was becoming someone I didn't want to be, but it also felt necessary."

The counselor nods with understanding. "That's actually a sign of healthy moral development. The fact that you can recognize when your actions diverge from your principles while still being able to take necessary action shows psychological resilience. The people we worry about are those who either can't make difficult decisions or those who can make them without any moral conflict."

The framework is helpful, but it doesn't resolve the fundamental tension between being effective as a sorcerer and maintaining the moral foundations that justify that effectiveness. The more capable you become at handling crisis situations, the more you're likely to be placed in scenarios that require morally complex decisions.

"Have you talked with your teammates about their experiences?" the counselor asks. "Shared processing can be more effective than individual reflection for this type of trauma."

The suggestion has merit, but it also raises concerns about how to support teammates who may be processing their experiences differently. Yuji's optimistic worldview has been shaken but not broken. Megumi's analytical approach helps him compartmentalize but may be preventing full emotional processing. Nobara's competitive nature has been redirected toward self-improvement but might be masking deeper struggles. And Junpei's unique relationship with the enemy adds layers of complexity that none of the others share.

"Group dynamics are important to consider," you say. "We all experienced the same events, but from different perspectives and with different psychological frameworks. I'm not sure how to support them without projecting my own processing needs onto their situations."

The conversation continues as you work through the individual and collective challenges of integrating the Shibuya experience into your ongoing development as a sorcerer.

How do you want to approach supporting your team through their recovery?"""

        aftermath_processing_choices = [
            StoryChoice(
                "Organize group discussion sessions focused on shared experiences and mutual support",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.FOCUSED: 10, Trait.PROTECTIVE: 10},
                    "story_flags": {"group_therapy_initiative": True, "mutual_support": True, "shared_processing": True},
                    "next_scene": "team_group_therapy",
                    "experience": 60,
                    "relationships": {"team": 25}
                }
            ),
            StoryChoice(
                "Work with each teammate individually to address their specific needs",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.ANALYTICAL: 10, Trait.PROTECTIVE: 15},
                    "story_flags": {"individual_support": True, "personalized_approach": True, "targeted_help": True},
                    "next_scene": "individual_teammate_support",
                    "experience": 65,
                    "relationships": {"individual_teammates": 20}
                }
            ),
            StoryChoice(
                "Focus on developing team resilience for future crisis situations",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15, Trait.DETERMINED: 10},
                    "story_flags": {"resilience_building": True, "future_preparation": True, "team_strengthening": True},
                    "next_scene": "resilience_training_development",
                    "experience": 70,
                    "relationships": {"team": 20}
                }
            )
        ]
        
        self.scenes["trauma_aftermath_processing"] = StoryScene(
            "Processing the Unthinkable",
            aftermath_processing_description,
            aftermath_processing_choices,
            "Tokyo Jujutsu High - Counseling Center"
        )
        
    def _add_character_resolution_scenes(self):
        """Add scenes focusing on individual character resolution and growth."""
        
        character_resolution_description = """Three months after Shibuya, the changes in your team are subtle but profound. Each member has found their own way of integrating the experience into their ongoing development, but those adaptations have also changed the group dynamic in ways that require ongoing attention and adjustment.

Yuji has retained his fundamental optimism but added layers of complexity that make his worldview more nuanced and, arguably, more realistic. He still believes in protecting people and doing the right thing, but he now understands that "the right thing" isn't always clear and sometimes requires accepting painful trade-offs.

"I used to think that if I just tried hard enough and stayed true to my principles, I could find solutions that saved everyone," he admits during a team training session. "Shibuya taught me that sometimes the best you can do is minimize harm while maximizing protection for the greatest number of people. That's... harder to live with than I expected."

Megumi's analytical nature has been both an asset and a liability in processing the crisis. His ability to compartmentalize traumatic experiences helps him function effectively, but it also creates emotional distance that sometimes prevents full integration of lessons learned.

"The tactical analysis is straightforward," he says with characteristic precision. "We identified threats, prioritized objectives, allocated resources, and achieved mission success with acceptable losses. But the emotional processing... that's more complicated."

Nobara has channeled her competitive drive into intensive self-improvement, developing new techniques and refining existing ones with an almost obsessive focus. The approach is effective for skill development but may be avoiding deeper psychological work that needs to happen.

"If I'm stronger next time, if I'm more skilled, more prepared, more tactically aware," she explains, "then maybe I won't have to make those kinds of choices. Maybe I can be good enough to find better solutions."

Junpei's position in the group remains complex because of his unique history with Mahito and soul manipulation. His growth has been remarkable, but the Shibuya incident forced him to confront aspects of his technique and his past that he's still working through.

"Using my abilities to counter Mahito's transformations felt like justice," he reflects. "But it also felt like completing a circle I never wanted to be part of in the first place. I'm glad I could help, but I'm also troubled by how natural it felt to manipulate souls, even for healing purposes."

The individual processing patterns create opportunities for mutual support, but they also generate potential friction points that require careful navigation. How do you balance respect for individual coping mechanisms with the need for team cohesion and shared understanding?

"We're all different people than we were before Shibuya," you observe during a quiet moment in the group conversation. "The question is whether we're becoming the people we want to be, or just the people that circumstances have forced us to become."

How do you want to guide the team's continued development and integration?"""

        character_resolution_choices = [
            StoryChoice(
                "Encourage everyone to embrace their post-Shibuya growth while maintaining core values",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.ANALYTICAL: 10, Trait.DETERMINED: 10},
                    "story_flags": {"growth_embrace": True, "value_preservation": True, "positive_integration": True},
                    "next_scene": "positive_growth_integration",
                    "experience": 65,
                    "relationships": {"team": 20}
                }
            ),
            StoryChoice(
                "Focus on rebuilding team unity while respecting individual differences",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 15, Trait.PROTECTIVE: 15},
                    "story_flags": {"unity_rebuilding": True, "individual_respect": True, "team_harmony": True},
                    "next_scene": "team_unity_rebuilding",
                    "experience": 60,
                    "relationships": {"team": 25}
                }
            ),
            StoryChoice(
                "Work on developing new shared goals that reflect your evolved perspectives",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15, Trait.DETERMINED: 15},
                    "story_flags": {"new_goals_development": True, "evolved_perspective": True, "shared_purpose": True},
                    "next_scene": "evolved_purpose_development",
                    "experience": 70,
                    "relationships": {"team": 20}
                }
            )
        ]
        
        self.scenes["character_growth_resolution"] = StoryScene(
            "Who We've Become",
            character_resolution_description,
            character_resolution_choices,
            "Tokyo Jujutsu High - Team Meeting Room"
        )
        
    def _add_long_term_consequence_scenes(self):
        """Add scenes exploring the long-term consequences of the Shibuya incident."""
        
        long_term_consequences_description = """Six months after the Shibuya incident, its impacts continue to ripple through jujutsu society in ways that are still being understood and addressed. The crisis exposed vulnerabilities in institutional preparedness that have prompted fundamental changes in how sorcerer education and emergency response are structured.

You attend a faculty meeting as a student representative, a role that was created in direct response to the lessons learned from Shibuya. The recognition that students may be called upon to handle major crises has led to their inclusion in policy discussions that were previously restricted to adult sorcerers.

"The emergency response protocols have been completely restructured," Principal Yaga explains to the assembled group. "Multiple simultaneous threats designed to separate our most capable responders from crisis zones has forced us to rethink resource allocation and backup systems."

The changes are extensive and reflect a sobering acknowledgment of how unprepared the jujutsu community was for coordinated attacks targeting their institutional weaknesses. New communication systems, distributed authority structures, and cross-institutional cooperation agreements represent fundamental shifts in how the community operates.

"Student training curricula have also been modified," Nanami adds. "The previous focus on individual technique development and small-team tactics has been expanded to include crisis management, ethical decision-making under pressure, and psychological resilience training."

The curriculum changes directly reflect the lessons your team learned through traumatic experience. Future students will receive formal training in the kinds of moral complexity and tactical decision-making that you were forced to develop through trial by fire.

"What about the civilians?" you ask, thinking about the transformed humans and the families affected by the incident. "Have there been improvements in victim support and recovery programs?"

Gojo-sensei fields this question with uncharacteristic seriousness. "That's been one of the most challenging aspects of the aftermath. Mahito's soul manipulation creates damage that traditional medical intervention can't address. We've had to develop entirely new approaches to helping people recover their sense of identity and humanity."

The implications are staggering - not just for the immediate victims, but for the precedent it sets regarding what kinds of damage cursed spirits can inflict on human society. If enemies can systematically transform civilians into weapons or psychological casualties, then protection strategies must evolve far beyond simple threat elimination.

"There's another concern," Megumi raises during the discussion. "The Shibuya incident demonstrated that enemies are willing to sacrifice significant resources to gather intelligence on our capabilities and decision-making patterns. How do we prepare for threats that are specifically designed to counter our current approaches?"

The question highlights the escalating nature of the conflict between jujutsu society and its enemies. Simple power increases aren't sufficient when facing opponents who study and adapt to your methods. The challenge becomes maintaining effectiveness while preventing predictability.

"Adaptation and innovation become crucial," you observe. "But we also need to be careful not to abandon the principles that justify our existence in the first place. The goal isn't just to become more effective - it's to remain worthy of the trust that people place in us."

The conversation continues as the group works through the complex balance between necessary evolution and core value preservation.

What long-term changes do you think are most important for jujutsu society?"""

        long_term_consequences_choices = [
            StoryChoice(
                "Advocate for increased focus on preventing civilian casualties in crisis situations",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.PROTECTIVE: 20, Trait.ANALYTICAL: 10},
                    "story_flags": {"civilian_protection_priority": True, "prevention_focus": True, "humanitarian_emphasis": True},
                    "next_scene": "civilian_protection_initiatives",
                    "experience": 75,
                    "relationships": {"civilians": 25, "faculty": 15}
                }
            ),
            StoryChoice(
                "Support development of more flexible and adaptive training programs",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15, Trait.DETERMINED: 10},
                    "story_flags": {"adaptive_training": True, "flexible_preparation": True, "evolution_emphasis": True},
                    "next_scene": "adaptive_training_development",
                    "experience": 70,
                    "relationships": {"faculty": 20, "future_students": 15}
                }
            ),
            StoryChoice(
                "Emphasize the importance of ethical decision-making frameworks for crisis situations",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 15, Trait.FOCUSED: 15},
                    "story_flags": {"ethical_framework_priority": True, "moral_preparation": True, "value_preservation": True},
                    "next_scene": "ethical_framework_development",
                    "experience": 80,
                    "relationships": {"faculty": 20, "philosophical_community": 15}
                }
            )
        ]
        
        self.scenes["long_term_societal_consequences"] = StoryScene(
            "Ripples Through Time",
            long_term_consequences_description,
            long_term_consequences_choices,
            "Tokyo Jujutsu High - Policy Development Meeting"
        )
        
    def _add_growth_integration_scenes(self):
        """Add scenes focusing on integrating growth and lessons learned."""
        
        growth_integration_description = """A year after the Shibuya incident, you stand once again on a rooftop overlooking Tokyo, but this time the view represents hope rather than impending crisis. The city below bustles with normal life - people going about their daily routines, unaware of the supernatural threats that are constantly being managed to keep them safe.

Your team has evolved in ways that would have been unimaginable before the crisis. The shared trauma and growth have created bonds that go deeper than friendship or professional cooperation. You've become people who understand each other's moral frameworks, tactical thinking, and psychological responses in ways that allow for seamless collaboration even in the most stressful situations.

"Sometimes I think about who we were before Shibuya," Yuji says quietly, joining you at the rooftop's edge. "We were so... innocent isn't the right word, but maybe naive? We thought that being strong and wanting to do good would be enough."

The observation captures something important about the maturation process that crisis can accelerate. The fundamental desire to protect people remains unchanged, but the understanding of what that requires has become far more sophisticated and, inevitably, more complex.

"I don't think we lost our innocence," Nobara counters as she and the others join the conversation. "I think we gained wisdom. There's a difference between becoming cynical and becoming realistic about the challenges we face."

Megumi nods thoughtfully. "The tactical frameworks we developed for handling moral complexity have actually made us more effective at protecting people, not less. We can make difficult decisions quickly because we've already worked through the philosophical foundations."

Junpei's perspective, as always, carries unique weight because of his journey from victim to potential weapon to protector. "What I've learned is that having power - whether physical, moral, or emotional - means accepting responsibility for how you use it. The ability to reshape souls is terrifying, but it's also an opportunity to heal damage that nothing else can address."

The conversation represents more than just reflection on past experiences - it's a foundation for understanding how your continued development as sorcerers should proceed. The lessons learned through trauma have become tools for preventing similar trauma for others.

"We've talked about how much we've changed," you say, looking out over the city that you've helped protect, "but I think it's important to recognize what hasn't changed. We still care about people. We still want to prevent suffering. We still believe that the power to protect others comes with the responsibility to use it wisely."

The continuity between your pre-Shibuya and post-Shibuya selves represents perhaps the most important achievement of your development - growing through crisis without losing the fundamental motivations that make growth worthwhile.

From the school grounds below, you can hear sounds of training as new students work through exercises that now include the moral complexity scenarios that your team helped develop. The next generation will be better prepared for the challenges you faced, but they'll also face new challenges that will require their own growth and adaptation.

"I think our job now," Megumi observes, "is to make sure that the lessons we learned through trauma can be taught through education instead. No one should have to learn about moral complexity the way we did."

The goal represents an evolution in how you understand your role as sorcerers - not just protectors of people in immediate danger, but contributors to systems and frameworks that make protection more effective and less traumatic for future generations.

How do you want to apply the lessons learned from your experiences moving forward?"""

        growth_integration_choices = [
            StoryChoice(
                "Focus on mentoring and teaching future students based on your experiences",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.ANALYTICAL: 15, Trait.PROTECTIVE: 10},
                    "story_flags": {"mentorship_focus": True, "education_contribution": True, "wisdom_sharing": True},
                    "next_scene": "mentorship_career_path",
                    "experience": 85,
                    "relationships": {"future_students": 25, "faculty": 20}
                }
            ),
            StoryChoice(
                "Work on developing better crisis prevention and early intervention systems",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15, Trait.DETERMINED: 15},
                    "story_flags": {"prevention_focus": True, "system_development": True, "proactive_approach": True},
                    "next_scene": "prevention_system_development",
                    "experience": 90,
                    "relationships": {"jujutsu_community": 20}
                }
            ),
            StoryChoice(
                "Continue field operations with enhanced focus on minimizing civilian impact",
                {
                    "traits": {Trait.PROTECTIVE: 20, Trait.DETERMINED: 15, Trait.COMPASSIONATE: 15},
                    "story_flags": {"field_operations_focus": True, "civilian_priority": True, "direct_protection": True},
                    "next_scene": "advanced_field_operations",
                    "experience": 80,
                    "relationships": {"civilians": 25, "team": 20}
                }
            )
        ]
        
        self.scenes["growth_integration_reflection"] = StoryScene(
            "Lessons Learned, Wisdom Gained",
            growth_integration_description,
            growth_integration_choices,
            "Tokyo Jujutsu High - Rooftop Reflection"
        )
        
    def get_all_scenes(self):
        """Return all scenes in the Shibuya Incident Arc."""
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