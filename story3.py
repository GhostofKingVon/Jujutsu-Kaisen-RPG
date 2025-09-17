"""
Kyoto Exchange Event Arc - Rivalry, Growth, and Hidden Threats

This module contains the expanded Kyoto Exchange Event Arc story content featuring
intense competition, character rivalries, personal growth, and hidden conspiracies.
Minimum 800 lines of detailed story content focusing on friendly rivalry and teamwork.
"""

from typing import Dict, List, Any, Optional
from character import Trait
from story_base import StoryChoice, StoryScene


class KyotoExchangeEventArc:
    """Manages the Kyoto Exchange Event Arc story scenes and progression."""
    
    def __init__(self):
        self.scenes = {}
        self._initialize_kyoto_arc()
    
    def _initialize_kyoto_arc(self):
        """Initialize all Kyoto Exchange Event Arc story scenes."""
        
        # =================================================================
        # SCENE 1: ANNOUNCEMENT OF THE EXCHANGE EVENT
        # =================================================================
        
        announcement_description = """The atmosphere in the Tokyo Jujutsu High assembly hall is electric with anticipation. Students from all years have gathered for Principal Yaga's announcement of this year's Exchange Event with Kyoto Jujutsu High. The annual competition represents not just a chance to test skills against students from the rival school, but an opportunity to showcase the different philosophies that guide the two institutions.

"The Exchange Event," Principal Yaga begins, his authoritative presence commanding immediate attention, "serves multiple purposes. It strengthens bonds between our schools, provides valuable combat experience in controlled conditions, and allows us to evaluate our students' progress against external standards."

You sit with your fellow first-years, all of whom show varying degrees of excitement and nervousness. Yuji bounces slightly in his seat, his enthusiasm barely contained. Megumi maintains his typical serious expression, but you can see the competitive glint in his eyes. Nobara examines her nails with affected disinterest, though her posture suggests she's listening intently.

"This year's event will follow traditional format," Yaga continues. "A team battle competition followed by individual matchups. However, there's an additional element this year - the winning school will receive priority access to several high-grade cursed tools that have recently been acquired by the jujutsu community."

The mention of high-grade cursed tools creates a buzz of excitement throughout the hall. Such weapons can significantly enhance a sorcerer's abilities and are typically reserved for the most experienced practitioners. The prospect of first-year students gaining access to such resources adds substantial stakes to what might otherwise be considered friendly competition.

"Kyoto School has won the last three Exchange Events," Yaga notes with a slight edge to his voice. "Their students are traditionally very well-prepared, highly disciplined, and work together with remarkable coordination. They will not underestimate you simply because you're first-years, and neither should you underestimate them."

Gojo-sensei steps forward, his casual demeanor contrasting sharply with the principal's formality. "Now for the fun part - team selection and strategy development! Based on your recent training performance and demonstrated abilities, the first-year team will consist of all four of you, plus our newest addition."

He gestures toward the back of the room, where Junpei sits quietly. The integration process has been ongoing, but this will be his first major test as part of the Tokyo team. The weight of inclusion in such an important event is clearly not lost on him.

"Junpei brings unique abilities to our team dynamic," Gojo explains. "His technique, properly applied, could be crucial in both team and individual competitions. However, this also means our opponents will be studying his abilities intensely, looking for weaknesses to exploit."

The strategic implications begin to sink in. Your team has raw talent and diverse abilities, but Kyoto School has experience, coordination, and three consecutive victories worth of confidence. The challenge will be finding ways to leverage your individual strengths into cohesive team effectiveness.

"You have two weeks to prepare," Yaga announces. "Use them wisely. The reputation of Tokyo Jujutsu High rests on your performance."

As the assembly breaks up, you find yourself thinking about what kind of leader you want to be in this competition and how you can help your team succeed against experienced opponents.

How do you want to approach the preparation phase?"""

        announcement_choices = [
            StoryChoice(
                "Focus on understanding each team member's strengths and developing combination strategies",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 10, Trait.PROTECTIVE: 5},
                    "story_flags": {"team_strategist": True, "combination_focus": True},
                    "next_scene": "team_analysis_and_strategy",
                    "experience": 50,
                    "relationships": {"team": 15}
                }
            ),
            StoryChoice(
                "Concentrate on individual skill development to maximize personal contribution",
                {
                    "traits": {Trait.DETERMINED: 15, Trait.FOCUSED: 15, Trait.AGGRESSIVE: 5},
                    "story_flags": {"individual_excellence": True, "skill_focus": True},
                    "next_scene": "intensive_personal_training",
                    "experience": 55,
                    "relationships": {"gojo": 10}
                }
            ),
            StoryChoice(
                "Research Kyoto School students and their typical strategies",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 10},
                    "story_flags": {"intelligence_gathering": True, "kyoto_research": True},
                    "next_scene": "kyoto_intelligence_research",
                    "experience": 45,
                    "relationships": {"megumi": 15}
                }
            ),
            StoryChoice(
                "Work specifically with Junpei to help him prepare for his first major competition",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 15, Trait.FOCUSED: 5},
                    "story_flags": {"junpei_support": True, "mentorship_focus": True},
                    "next_scene": "junpei_preparation_support",
                    "experience": 40,
                    "relationships": {"junpei": 25}
                }
            )
        ]
        
        self.scenes["exchange_event_announcement"] = StoryScene(
            "The Challenge Ahead",
            announcement_description,
            announcement_choices,
            "Tokyo Jujutsu High - Assembly Hall"
        )
        
        # =================================================================
        # SCENE 2: MEETING THE KYOTO STUDENTS
        # =================================================================
        
        kyoto_meeting_description = """The arrival of the Kyoto Jujutsu High students at your campus marks the beginning of the Exchange Event weekend. As their bus pulls through the main gates, you can feel the competitive tension in the air. These aren't just fellow students - they're rivals who have beaten Tokyo three years running and clearly intend to make it four.

The Kyoto team emerges from their bus with military-like precision. Their uniforms are immaculate, their posture disciplined, and their formation suggests students who are accustomed to operating as a cohesive unit. At their head walks a tall student with slicked-back dark hair and an air of authority that marks him as their leader.

"That's Noritoshi Kamo," Megumi murmurs beside you. "Heir to one of the major jujutsu families. His technique involves blood manipulation, and he's extremely skilled at both individual combat and tactical coordination."

Behind Kamo, you recognize several other students from the intelligence briefings. Mai Zenin, Maki's twin sister, carries herself with the confidence of someone who has something to prove. Momo Nishimiya floats slightly above the ground on her broom, her aerial perspective allowing her to survey the Tokyo campus with tactical awareness. And bringing up the rear...

"Todo!" Yuji calls out excitedly, waving at the massive figure of Aoi Todo.

Todo's face lights up with genuine pleasure as he spots Yuji. "My brother!" he bellows, breaking formation to stride over with his characteristic enthusiasm. "I was hoping you'd be part of the Tokyo team this year. This competition just became infinitely more interesting!"

The reunion between Yuji and Todo immediately shifts the dynamic. What had begun as a formal, somewhat tense meeting between rival schools becomes more relaxed as Todo's exuberant personality affects everyone around him. Even the typically stern Kamo allows a slight smile to cross his face.

"It's good to see you again," Yuji says sincerely. "Though I should warn you - we've been training hard. Tokyo isn't going to be an easy victory this year."

"Excellent!" Todo grins. "I would be disappointed with anything less than your absolute best effort. Victory without challenge is meaningless."

Mai Zenin steps forward, her gaze focusing on your group with calculating intensity. "So these are the famous first-years we've been hearing about," she says, her tone neutral but her eyes sharp. "Including the new addition with the... unusual technique."

Her attention settles on Junpei, who shifts uncomfortably under the scrutiny. The way she emphasizes 'unusual' makes it clear that word of his soul manipulation abilities has reached Kyoto, and they've been strategizing accordingly.

"Junpei Yoshino," he introduces himself with a slight bow. "I look forward to competing against skilled opponents."

"As do we," Kamo interjects smoothly. "Your technique represents an interesting tactical variable. We're curious to see how it's been adapted for competitive use rather than..." He pauses meaningfully. "Other applications."

The subtle reference to Mahito and the circumstances of Junpei's technique acquisition creates a moment of tension. It's not exactly hostile, but it's clear that Kyoto has done their homework and isn't above psychological warfare.

"Enough politics," Todo declares, clapping his massive hands together. "I want to hear about everyone's training progress! Have any of you discovered new applications for your techniques? Breakthrough moments in your development?"

His genuine enthusiasm for jujutsu development is infectious, and soon both teams are engaged in animated discussions about training methods, technique refinements, and combat philosophy. The competitive tension remains, but it's tempered by mutual respect for dedication to improvement.

Momo, who has been observing from above, finally descends to ground level. "The team battle tomorrow will be interesting," she observes. "Tokyo has raw talent and creativity. Kyoto has experience and coordination. It should be a good test of which approach proves more effective."

"Speaking of which," Kamo adds, "we should probably discuss the specific competition format. This year includes some modifications to traditional rules that should make things more... dynamic."

The conversation turns to the technical aspects of the competition, but you find yourself studying the individual Kyoto students and trying to assess how their personalities and abilities might interact with your team's strengths and weaknesses.

How do you want to approach these initial interactions with your opponents?"""

        kyoto_meeting_choices = [
            StoryChoice(
                "Engage in friendly conversation to build mutual respect while gathering intelligence",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 10, Trait.COMPASSIONATE: 5},
                    "story_flags": {"diplomatic_approach": True, "intelligence_gathering": True},
                    "next_scene": "friendly_intelligence_gathering",
                    "experience": 45,
                    "relationships": {"kyoto_students": 10}
                }
            ),
            StoryChoice(
                "Focus on demonstrating Tokyo's confidence and capabilities",
                {
                    "traits": {Trait.AGGRESSIVE: 10, Trait.DETERMINED: 15, Trait.FOCUSED: 5},
                    "story_flags": {"confidence_display": True, "intimidation_attempt": True},
                    "next_scene": "confidence_demonstration",
                    "experience": 40,
                    "relationships": {"tokyo_team": 10}
                }
            ),
            StoryChoice(
                "Support Junpei in handling the psychological pressure from Kyoto's attention",
                {
                    "traits": {Trait.PROTECTIVE: 15, Trait.COMPASSIONATE: 10},
                    "story_flags": {"junpei_protection": True, "team_solidarity": True},
                    "next_scene": "junpei_support_response",
                    "experience": 35,
                    "relationships": {"junpei": 20}
                }
            ),
            StoryChoice(
                "Study their team dynamics and look for potential weaknesses or friction",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 10},
                    "story_flags": {"tactical_observation": True, "weakness_identification": True},
                    "next_scene": "kyoto_team_analysis",
                    "experience": 50,
                    "relationships": {"megumi": 10}
                }
            )
        ]
        
        self.scenes["meeting_kyoto_students"] = StoryScene(
            "Rivals and Potential Friends",
            kyoto_meeting_description,
            kyoto_meeting_choices,
            "Tokyo Jujutsu High - Main Courtyard"
        )
        
        # =================================================================
        # SCENE 3: THE TEAM BATTLE BEGINS
        # =================================================================
        
        team_battle_description = """The competition grounds have been transformed into a complex battlefield designed to test every aspect of team coordination and individual skill. Multiple terrain types create strategic advantages and disadvantages, while scattered cursed tools and temporary power-ups add elements of resource management to the traditional combat focus.

Your Tokyo team stands at the southern entrance, reviewing final strategy while the Kyoto team prepares at the northern gate. The rules are straightforward - defeat the opposing team through any combination of elimination and objective control. Hidden throughout the battlefield are several capture points that provide ongoing advantages to the controlling team, creating strategic decisions beyond simple combat.

"Remember," you address your teammates, "our advantage is adaptability and surprise. They expect coordination and traditional tactics from us, but our strength is creative problem-solving and unconventional approaches."

Yuji nods enthusiastically, his excitement barely contained. "I can't wait to see how much stronger Todo has gotten! This is going to be amazing!"

Megumi adjusts his technique preparations with methodical precision. "The terrain favors mobile combat. My divine dogs can provide reconnaissance while we establish position. We should prioritize information gathering in the early phases."

Nobara examines her arsenal of cursed tools with satisfaction. "Those Kyoto students think they know everything about our abilities, but they haven't seen what I've been working on. Time to show them some Tokyo innovation!"

Junpei takes a deep breath, his nervousness evident but his determination clear. "I know my technique makes everyone nervous, but I've been working on applications that support the team without crossing ethical lines. I won't let you down."

The starting signal echoes across the battlefield, and both teams explode into motion. The Kyoto team immediately demonstrates their superior coordination, moving in a tight formation that allows them to support each other while advancing toward strategic positions. Their discipline is impressive - clearly the result of extensive joint training and shared tactical doctrine.

In contrast, your Tokyo team spreads out more, each member taking advantage of their individual mobility and unique abilities. The approach looks chaotic compared to Kyoto's military precision, but it allows for rapid adaptation to changing battlefield conditions.

The first contact comes when Megumi's divine dogs encounter Momo's aerial reconnaissance. Her superior vantage point allows her to spot the shadow techniques before they can achieve surprise, but the dogs' mobility keeps her from establishing a stable observation position.

"Kyoto team is advancing on the eastern capture point," Megumi reports through your communication system. "Three members in tight formation, with Momo providing overwatch. They're playing it conservatively so far."

Almost simultaneously, you spot movement in the western sector. Mai Zenin is moving independently, clearly attempting to circle around your team's expected positions. Her marksmanship abilities make her a significant threat if she can establish a firing position, but her isolation also makes her vulnerable to focused assault.

"I see Mai going for the western flanks," Nobara reports. "Should I intercept?"

The early phase of the battle presents multiple strategic options. Kyoto's conservative approach suggests they're feeling out your capabilities before committing to major engagements, but their positioning also reveals potential weaknesses in their formation.

Todo's absence from the main Kyoto formation is particularly notable. Given his combat preferences, he's likely seeking a direct confrontation with Yuji, which could work to your advantage if you can control the timing and location of that encounter.

What's your tactical decision for the opening phase?"""

        team_battle_choices = [
            StoryChoice(
                "Coordinate a focused assault on the eastern capture point to disrupt Kyoto's formation",
                {
                    "traits": {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 10, Trait.FOCUSED: 10},
                    "story_flags": {"aggressive_opening": True, "formation_disruption": True},
                    "next_scene": "eastern_assault_battle",
                    "experience": 60,
                    "combat": True,
                    "enemy": "kyoto_formation"
                }
            ),
            StoryChoice(
                "Send Nobara to intercept Mai while the rest of the team secures strategic positions",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10, Trait.FOCUSED: 10},
                    "story_flags": {"divided_strategy": True, "position_control": True},
                    "next_scene": "divided_battlefield_tactics",
                    "experience": 55,
                    "relationships": {"nobara": 10}
                }
            ),
            StoryChoice(
                "Use Junpei's unique abilities to create an unexpected strategic advantage",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 15, Trait.PROTECTIVE: 5},
                    "story_flags": {"junpei_strategy": True, "unexpected_tactics": True},
                    "next_scene": "junpei_tactical_surprise",
                    "experience": 65,
                    "relationships": {"junpei": 15}
                }
            ),
            StoryChoice(
                "Set up a trap for Todo when he comes looking for Yuji",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15},
                    "story_flags": {"todo_trap": True, "tactical_planning": True},
                    "next_scene": "todo_trap_preparation",
                    "experience": 58,
                    "relationships": {"yuji": 10}
                }
            )
        ]
        
        self.scenes["team_battle_opening"] = StoryScene(
            "The Battle Begins",
            team_battle_description,
            team_battle_choices,
            "Exchange Event - Competition Battlefield"
        )
        
        # =================================================================
        # SCENE 4: TODO'S CHALLENGE
        # =================================================================
        
        todo_challenge_description = """The battlefield erupts in chaos as Todo makes his dramatic entrance, having apparently been waiting for the perfect moment to challenge Yuji to their anticipated rematch. His technique - Boogie Woogie - allows him to swap the positions of anything with sufficient cursed energy, making him one of the most unpredictable and dangerous opponents possible.

"My brother!" Todo bellows as he appears directly in front of Yuji through a position swap, his massive fist already in motion. "I've been thinking about our last conversation for months! Show me how much you've grown!"

Yuji barely manages to dodge the opening strike, his improved reflexes allowing him to avoid what would have been a devastating blow. "Todo! I was hoping we'd get a chance to fight again, but maybe we could start with a little less attempted murder?"

"Where's the fun in that?" Todo grins, immediately following up with a combination that showcases both his physical power and his tactical use of his technique. Each punch forces Yuji to consider not just the direct threat, but the possibility that Todo might swap their positions mid-strike to attack from an unexpected angle.

The intensity of their clash immediately draws attention from across the battlefield. Both teams pause their respective strategies to watch what is clearly going to be the marquee matchup of the competition. Todo's reputation as Kyoto's strongest student is well-established, but Yuji's growth since their last encounter has been remarkable.

"We need to decide whether to support Yuji or continue with our original strategy," Megumi says through the communication system. "Todo's technique makes group combat extremely dangerous - he could use us against each other."

"But if Yuji loses, we lose our strongest physical fighter," Nobara points out. "And Todo could then turn his attention to the rest of us with significant momentum."

Junpei, who has been observing the fight with intense focus, offers a different perspective. "Todo's technique requires him to maintain awareness of everyone's position. If we could create enough simultaneous distractions..."

The strategic implications are complex. Todo's Boogie Woogie is most effective in chaotic situations where he has multiple targets to swap between, but it also requires split-second decision-making that could be overwhelmed by too many variables.

Meanwhile, the rest of the Kyoto team is taking advantage of the attention focused on Todo's fight to advance their own strategic positions. Kamo has secured the eastern capture point and is establishing a defensive position that will be difficult to dislodge. Mai has found an elevated firing position that gives her sight lines across most of the battlefield.

"The longer Todo's fight continues, the stronger Kyoto's overall position becomes," you realize. "But interrupting it could backfire if Todo decides to target our interference rather than continuing to focus on Yuji."

The fight itself is evolving rapidly. Yuji has adapted to Todo's swapping technique better than expected, using his improved speed and technique timing to maintain offensive pressure despite the positional uncertainty. Todo, for his part, seems genuinely pleased with Yuji's development and is gradually increasing the complexity of his attacks.

"This is exactly what I was hoping for!" Todo laughs as he swaps positions with a piece of battlefield debris to avoid one of Yuji's combination strikes. "You're not just stronger - you're thinking differently! Show me more!"

The positive dynamic between them despite the competitive context creates an interesting opportunity. Todo clearly respects Yuji's growth and might be open to acknowledging a good showing even in defeat, which could influence the overall tone of the competition.

How do you want to handle this pivotal moment?"""

        todo_challenge_choices = [
            StoryChoice(
                "Trust Yuji to handle Todo alone while focusing on countering Kyoto's strategic advances",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15, Trait.DETERMINED: 5},
                    "story_flags": {"trust_yuji": True, "strategic_focus": True},
                    "next_scene": "strategic_counter_operations",
                    "experience": 60,
                    "relationships": {"yuji": 15}
                }
            ),
            StoryChoice(
                "Create coordinated distractions to overwhelm Todo's ability to track multiple targets",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15},
                    "story_flags": {"coordination_tactics": True, "todo_counter": True},
                    "next_scene": "coordinated_distraction_assault",
                    "experience": 65,
                    "relationships": {"team": 15}
                }
            ),
            StoryChoice(
                "Use Junpei's technique to create battlefield modifications that limit Todo's swapping options",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 10, Trait.PROTECTIVE: 10},
                    "story_flags": {"junpei_battlefield_control": True, "environmental_tactics": True},
                    "next_scene": "junpei_battlefield_modification",
                    "experience": 70,
                    "relationships": {"junpei": 20}
                }
            ),
            StoryChoice(
                "Challenge the Kyoto team's honor by suggesting they're letting Todo fight unfairly outnumbered",
                {
                    "traits": {Trait.AGGRESSIVE: 10, Trait.ANALYTICAL: 10, Trait.DETERMINED: 10},
                    "story_flags": {"honor_challenge": True, "psychological_warfare": True},
                    "next_scene": "honor_based_challenge",
                    "experience": 55,
                    "relationships": {"kyoto_students": 5}
                }
            )
        ]
        
        self.scenes["todo_yuji_clash"] = StoryScene(
            "Brothers in Battle",
            todo_challenge_description,
            todo_challenge_choices,
            "Exchange Event - Central Battlefield"
        )
        
        # =================================================================
        # SCENE 5: INDIVIDUAL COMPETITIONS
        # =================================================================
        
        individual_competition_description = """The team battle has concluded with Tokyo achieving a narrow victory through superior adaptability and creative tactics, but the individual competition represents an entirely different challenge. Here, raw skill and personal development matter more than team coordination, and the Kyoto students' individual training advantages become much more apparent.

The competition format involves a tournament bracket with random pairings, ensuring that strategy must be balanced with adaptation to unexpected matchups. As the lots are drawn, you find yourself facing Noritoshi Kamo in what promises to be a technically demanding fight between two analytical fighters.

"An interesting matchup," Kamo observes as you both prepare for the bout. "Your reputation for tactical innovation precedes you, but blood manipulation requires a different kind of counter-strategy than most techniques."

His demeanor is respectful but confident - clearly, he's studied your previous fights and believes he has identified effective countermeasures. Kamo's technique allows him to control his own blood flow for enhanced physical capabilities and to weaponize blood outside his body for ranged attacks. More dangerously, he can potentially manipulate opponents' blood if he can establish contact.

"I've been looking forward to this," you reply honestly. "Your family's technique has a legendary reputation. It'll be educational to face it directly."

The arena for individual matches is smaller and more controlled than the team battlefield, with protective barriers ensuring that spectators can observe safely while fighters can operate at full capacity. Both teams watch from designated areas, their analysis of individual performances informing future strategic decisions.

"Begin!" the referee calls, and Kamo immediately demonstrates why his technique is so feared. His enhanced blood flow dramatically increases his speed and strength, while streams of weaponized blood arc through the air toward your position.

The opening exchange forces you to respect both his enhanced physical capabilities and his ranged attack options. Traditional close-combat approaches would put you at severe disadvantage, but staying at distance allows him to fully utilize his blood projectiles. Finding the optimal engagement range requires constant adjustment based on his tactical choices.

"Impressive evasion," Kamo notes as you avoid his initial assault. "But defensive fighting won't win this match. Show me the innovation that helped Tokyo achieve victory in the team battle."

His challenge is both tactical and psychological - he's trying to provoke you into attacking recklessly while simultaneously gathering information about your technique applications under pressure. The individual format means you can't rely on team support or environmental advantages, forcing pure technical skill to take precedence.

From the spectator area, you can hear your teammates offering encouragement, but their specific advice is limited by the need to avoid revealing tactical information to future opponents. Junpei's voice stands out as he calls, "Remember what we practiced about flow adaptation!"

The reminder triggers memories of training sessions focused on adapting technique application to opponent characteristics rather than relying on predetermined patterns. Against Kamo's blood manipulation, traditional approaches would indeed be insufficient - but unconventional applications might create opportunities he hasn't prepared for.

"Let's see how well you adapt to this," Kamo says, activating a more complex blood technique that creates multiple simultaneous attack vectors while enhancing his defensive capabilities.

The escalation forces immediate tactical decisions about how to respond to increased pressure while creating openings for effective counter-attacks.

What's your fighting strategy against Kamo?"""

        individual_competition_choices = [
            StoryChoice(
                "Focus on disrupting his blood manipulation through precise cursed energy interference",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15},
                    "story_flags": {"technique_disruption": True, "precision_fighting": True},
                    "next_scene": "kamo_technique_counter",
                    "experience": 70,
                    "combat": True,
                    "enemy": "kamo_individual_match"
                }
            ),
            StoryChoice(
                "Use mobility and timing to exploit the brief windows when his technique is recharging",
                {
                    "traits": {Trait.FOCUSED: 15, Trait.ANALYTICAL: 10, Trait.DETERMINED: 10},
                    "story_flags": {"timing_strategy": True, "mobility_focus": True},
                    "next_scene": "timing_based_combat",
                    "experience": 65,
                    "combat": True,
                    "enemy": "kamo_timing_match"
                }
            ),
            StoryChoice(
                "Apply the unconventional technique adaptations you've been developing",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15, Trait.DETERMINED: 10},
                    "story_flags": {"innovation_application": True, "technique_evolution": True},
                    "next_scene": "innovative_technique_display",
                    "experience": 75,
                    "combat": True,
                    "enemy": "kamo_innovation_match"
                }
            ),
            StoryChoice(
                "Try to turn his blood manipulation advantages into disadvantages through environmental use",
                {
                    "traits": {Trait.ANALYTICAL: 18, Trait.FOCUSED: 12, Trait.CAUTIOUS: 5},
                    "story_flags": {"environmental_tactics": True, "advantage_reversal": True},
                    "next_scene": "environmental_reversal_fight",
                    "experience": 68,
                    "combat": True,
                    "enemy": "kamo_environmental_match"
                }
            )
        ]
        
        self.scenes["individual_competition_kamo"] = StoryScene(
            "Test of Individual Skill",
            individual_competition_description,
            individual_competition_choices,
            "Exchange Event - Individual Arena"
        )
        
        # =================================================================
        # SCENE 6: HIDDEN THREATS EMERGE
        # =================================================================
        
        hidden_threats_description = """The Exchange Event takes a dark turn when cursed spirits suddenly appear on the competition grounds, clearly not part of any planned scenario. The attack is coordinated and purposeful, with multiple Grade 1 spirits appearing simultaneously at strategic locations around the campus. This isn't a random incursion - it's an organized assault designed to cause maximum chaos and casualties.

"All students, defensive positions immediately!" Principal Yaga's voice echoes across the grounds through the emergency communication system. "This is not a drill! We are under coordinated attack!"

The timing of the assault is clearly deliberate, targeting the moment when both schools' strongest students are gathered in one location but potentially isolated from their usual support systems. The competition format has separated teams and individuals across multiple venues, making coordinated response more difficult.

You find yourself near the individual competition arena when the first spirits appear - monstrous creatures that immediately begin targeting the assembled students with lethal intent. Your recent opponent, Kamo, is still recovering from your match and not at full combat effectiveness.

"We need to establish communication with the other venues," you call out to him, putting aside competitive differences in the face of genuine danger. "Do you have any way to contact your team?"

"Emergency protocols," Kamo replies grimly, activating a communication device that connects to Kyoto's coordination network. "Multiple attack points confirmed. Someone planned this to exploit our divided attention."

The implications are chilling. This level of coordination suggests either a traitor within the jujutsu community or intelligence gathering capabilities that represent a fundamental security breach. Either possibility threatens not just the current situation but the entire structure of jujutsu education and cooperation between schools.

From across the arena, you can hear sounds of combat as other students engage the attacking spirits. The creatures are clearly more intelligent and better coordinated than typical cursed spirits, suggesting they may be controlled or directed by a more sophisticated intelligence.

"There!" Junpei's voice carries from the team venue. "I can sense something wrong with these spirits. They're not naturally formed - someone or something is controlling them directly!"

His unique perspective on soul manipulation gives him insights that others might miss. If the spirits are being controlled rather than acting on instinct, that means their coordination can be disrupted by targeting the controller - but it also means there's an intelligence behind the attack that can adapt tactics in real-time.

"We need to choose our priorities," Kamo says pragmatically. "Defend the immediate area, attempt to reunite with our teams, or try to identify and eliminate the controlling intelligence."

The decision is complicated by uncertainty about the full scope of the attack. Are there students injured and in need of immediate assistance? Are the faculty handling other aspects of the assault? How many spirits are involved, and what are their specific capabilities?

From the sounds of combat echoing across the campus, it's clear that this is a major incident requiring careful tactical decisions rather than simple aggressive response. The wrong choice could lead to unnecessary casualties or allow the attackers to achieve whatever their primary objective might be.

"Listen," you say, hearing a pattern in the combat sounds that suggests coordination between attack groups. "The spirits aren't just attacking randomly. They're trying to drive us toward specific locations. This could be an attempt to herd us into a trap."

The realization adds another layer of complexity to an already dangerous situation. Are you safer staying where you are, or does remaining stationary make you easier targets for whatever the ultimate plan might be?

How do you want to respond to this coordinated attack?"""

        hidden_threats_choices = [
            StoryChoice(
                "Focus on reuniting with your team to maximize combined effectiveness",
                {
                    "traits": {Trait.PROTECTIVE: 15, Trait.DETERMINED: 10, Trait.FOCUSED: 10},
                    "story_flags": {"team_reunion": True, "protective_priority": True},
                    "next_scene": "team_reunion_under_fire",
                    "experience": 65,
                    "combat": True,
                    "enemy": "coordinated_spirits"
                }
            ),
            StoryChoice(
                "Work with Kamo to investigate the source of spirit coordination",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15, Trait.DETERMINED: 10},
                    "story_flags": {"investigation_priority": True, "kamo_cooperation": True},
                    "next_scene": "spirit_controller_investigation",
                    "experience": 70,
                    "relationships": {"kamo": 15}
                }
            ),
            StoryChoice(
                "Coordinate with both teams to establish a unified defense",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.PROTECTIVE: 15, Trait.FOCUSED: 10},
                    "story_flags": {"unified_defense": True, "leadership_initiative": True},
                    "next_scene": "inter_school_coordination",
                    "experience": 75,
                    "relationships": {"both_teams": 15}
                }
            ),
            StoryChoice(
                "Use Junpei's soul sensing abilities to track the controlling intelligence",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.PROTECTIVE: 10, Trait.FOCUSED: 15},
                    "story_flags": {"junpei_tracking": True, "soul_sensing_use": True},
                    "next_scene": "junpei_soul_tracking",
                    "experience": 68,
                    "relationships": {"junpei": 20}
                }
            )
        ]
        
        self.scenes["hidden_threat_emergence"] = StoryScene(
            "When Competition Becomes Survival",
            hidden_threats_description,
            hidden_threats_choices,
            "Exchange Event - Under Attack"
        )
        
        # =================================================================
        # ADDITIONAL SCENES: ARC RESOLUTION AND CHARACTER GROWTH
        # =================================================================
        
        self._add_resolution_scenes()
        self._add_character_growth_scenes()
        self._add_relationship_development_scenes()
        self._add_competition_aftermath_scenes()
        
    def _add_resolution_scenes(self):
        """Add resolution scenes for the arc's major conflicts."""
        
        resolution_description = """The coordinated attack on the Exchange Event has been repelled, but not without cost. Several students from both schools were injured, and the revelation that the assault was orchestrated by a faction within the jujutsu community itself has shaken confidence in institutional security. The competition that was meant to showcase friendly rivalry between schools has instead exposed vulnerabilities that could threaten the entire system.

You stand with representatives from both Tokyo and Kyoto teams in the emergency briefing room, where faculty from both schools are coordinating their response to the incident. The atmosphere is grim as the full scope of the betrayal becomes clear.

"The attack was coordinated by at least three separate groups," Nanami reports, his usually calm demeanor showing signs of strain. "Rogue sorcerers, cursed spirit users, and what appears to be a faction of curse users who have been planning this infiltration for months."

Principal Yaga adds details that make the situation even more concerning. "Their primary objective wasn't to cause casualties - it was to gather intelligence on our students' techniques and capabilities. The attack was essentially cover for an extensive reconnaissance operation."

The implications are chilling. Someone is building detailed profiles of the next generation of jujutsu sorcerers, potentially planning future operations that could target specific individuals with customized countermeasures. Your unique abilities, Junpei's soul manipulation, Yuji's hidden power - all of it has been observed and likely analyzed.

"This changes our security protocols fundamentally," the Kyoto principal acknowledges. "The assumption that jujutsu schools are safe havens for student development is no longer valid. We must prepare for a more hostile operational environment."

Kamo, still bearing minor injuries from the fighting, speaks up. "The cooperation between our schools during the crisis was effective. Perhaps the threat to both institutions suggests the need for enhanced coordination between Tokyo and Kyoto."

His observation highlights one positive outcome from the traumatic experience. The artificial rivalry between schools seems petty in the face of genuine threats to student safety. Students who were competitors hours earlier fought side by side to protect each other when real danger emerged.

"Your performance during the crisis was exemplary," Gojo addresses the assembled students. "All of you demonstrated the kind of character and tactical thinking that gives me confidence in the future of jujutsu sorcery. But this incident also highlights the need for accelerated development programs."

The acceleration of training carries both opportunities and risks. More intensive development could better prepare students for the apparently increasing threats, but it also means less time for the careful psychological and ethical development that prevents the kind of corruption that created enemies like Mahito.

Todo, whose enthusiasm remains undimmed despite the serious circumstances, offers his perspective. "Crisis reveals true character! Today showed that both schools have students worthy of respect and cooperation. Perhaps future Exchange Events should include joint training against simulated threats rather than simple competition."

The suggestion has merit. If the traditional boundaries between institutions are becoming less relevant in the face of organized opposition, then training programs should reflect the reality of cooperative operations.

What approach do you want to advocate for moving forward?"""

        resolution_choices = [
            StoryChoice(
                "Support increased cooperation between Tokyo and Kyoto schools",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.PROTECTIVE: 10, Trait.FOCUSED: 10},
                    "story_flags": {"inter_school_cooperation": True, "unified_approach": True},
                    "next_scene": "cooperation_development",
                    "experience": 55,
                    "relationships": {"both_schools": 15}
                }
            ),
            StoryChoice(
                "Advocate for enhanced security and threat assessment protocols",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 15},
                    "story_flags": {"security_focus": True, "threat_assessment": True},
                    "next_scene": "security_enhancement_planning",
                    "experience": 60,
                    "relationships": {"faculty": 15}
                }
            ),
            StoryChoice(
                "Focus on accelerated training for students who showed exceptional potential",
                {
                    "traits": {Trait.DETERMINED: 15, Trait.FOCUSED: 15, Trait.AGGRESSIVE: 5},
                    "story_flags": {"accelerated_training": True, "potential_development": True},
                    "next_scene": "advanced_training_program",
                    "experience": 65,
                    "relationships": {"gojo": 15}
                }
            )
        ]
        
        self.scenes["crisis_resolution_planning"] = StoryScene(
            "Lessons from Crisis",
            resolution_description,
            resolution_choices,
            "Tokyo Jujutsu High - Emergency Briefing Room"
        )
        
    def _add_character_growth_scenes(self):
        """Add scenes focusing on character development through competition experience."""
        
        growth_description = """The week following the Exchange Event has provided time for reflection on both the competitive successes and the crisis that overshadowed them. Your individual performance against Kamo demonstrated technical growth, but more importantly, the collaborative response to the attack revealed character development that goes beyond simple combat capability.

You find yourself in the training room with Junpei, who has been processing his own complex emotions about the incident. His soul manipulation abilities proved crucial in identifying the controlled nature of the attacking spirits, but the experience also highlighted how much his technique sets him apart from other students.

"I keep thinking about what those rogue sorcerers wanted," Junpei says quietly. "They were specifically gathering intelligence on students with unusual abilities. People like me - people whose techniques could be turned into weapons if they fell into the wrong hands."

The concern is valid and troubling. Junpei's ability to manipulate souls represents both incredible healing potential and devastating destructive capability. The kind of intelligence gathering that took place during the attack suggests enemies who are thinking strategically about how to exploit or corrupt powerful techniques.

"That's exactly why your character development is so important," you tell him. "Your technique is dangerous in the wrong hands, but it's also incredibly valuable in the right ones. The attack proved that - you were able to identify threats that nobody else could detect."

Yuji joins the conversation, his typical enthusiasm tempered by the seriousness of recent events. "What bothers me is how organized the whole thing was. These weren't random criminals or cursed spirits acting on instinct. Someone is planning something bigger, and we were just... practice for them."

The strategic implications are indeed concerning. If the attack was reconnaissance for a larger operation, then the information gathered about student capabilities could be used to design more effective future assaults. Your techniques, teamwork patterns, and individual weaknesses are now potentially known to hostile forces.

"Which means we need to keep developing," Megumi observes as he enters the room. "If they're planning countermeasures based on our current abilities, then our best defense is to exceed their expectations through continued growth."

The conversation turns to practical applications of this insight. How do you continue developing when your baseline capabilities may be known to enemies? How do you prepare for threats that are specifically designed to counter your current strengths?

"Maybe the answer is versatility," Nobara suggests. "If they're planning counters to our signature techniques, then we need backup approaches that they haven't observed. Multiple options for every situation."

The discussion highlights how much the Exchange Event has changed everyone's perspective on their development as sorcerers. What began as friendly competition has evolved into preparation for asymmetric warfare against intelligent, well-organized opponents.

How do you want to focus your continued development?"""

        growth_choices = [
            StoryChoice(
                "Develop backup techniques and alternative approaches to common situations",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15, Trait.CAUTIOUS: 5},
                    "story_flags": {"versatility_development": True, "backup_techniques": True},
                    "next_scene": "alternative_technique_training",
                    "experience": 60
                }
            ),
            StoryChoice(
                "Focus on team coordination patterns that would be difficult to counter",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 10, Trait.PROTECTIVE: 10},
                    "story_flags": {"team_coordination_focus": True, "counter_resistant_tactics": True},
                    "next_scene": "advanced_team_coordination",
                    "experience": 55,
                    "relationships": {"team": 15}
                }
            ),
            StoryChoice(
                "Work on psychological resilience and resistance to manipulation",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 10, Trait.CAUTIOUS: 15},
                    "story_flags": {"psychological_training": True, "manipulation_resistance": True},
                    "next_scene": "psychological_resilience_training",
                    "experience": 50,
                    "relationships": {"junpei": 15}
                }
            )
        ]
        
        self.scenes["post_event_character_growth"] = StoryScene(
            "Growing Through Challenge",
            growth_description,
            growth_choices,
            "Tokyo Jujutsu High - Training Room"
        )
        
    def _add_relationship_development_scenes(self):
        """Add scenes for developing relationships formed during the arc."""
        
        relationship_description = """The shared experiences of competition and crisis have created new bonds that extend beyond the traditional Tokyo-Kyoto rivalry. Students who were opponents in the morning fought together against genuine threats in the afternoon, creating the kind of mutual respect that can only come from facing danger together.

A week after the Exchange Event, you receive an unexpected invitation to join a joint training session between selected students from both schools. The initiative comes from Todo, who characteristically sees the crisis as an opportunity for enhanced mutual development rather than a reason for increased security isolation.

"Brothers and sisters!" Todo declares as students from both schools gather in the shared training facility. "Competition reveals strength, but crisis reveals character! Today we train not as Tokyo or Kyoto students, but as sorcerers united in common purpose!"

The assembled group includes yourself, Yuji, Megumi, Nobara, and Junpei from Tokyo, with Kamo, Mai, Momo, and Todo representing Kyoto. The selection criteria seem to be based on students who demonstrated particularly effective cooperation during the attack, regardless of their individual competitive performance.

"The joint training format will focus on scenarios that require inter-school cooperation," Kamo explains with his characteristic precision. "Techniques and fighting styles that were competitive advantages during the Exchange Event become collaborative tools when facing external threats."

The philosophical shift is significant. Instead of developing abilities to gain advantages over fellow students, the focus becomes optimizing capabilities for mutual support against common enemies. Your analytical approach, which provided tactical advantages in individual competition, becomes a resource for helping teammates understand opponent patterns and weaknesses.

Mai, whose competitive relationship with her sister Maki adds personal complexity to inter-school dynamics, offers her perspective. "The attack demonstrated that our real enemies don't care about school rivalries. They see all of us as threats to be eliminated or tools to be corrupted. Our response should reflect that reality."

The training exercises that follow are unlike anything in the standard curriculum. Instead of individual technique development or same-school team coordination, the focus is on rapidly forming effective partnerships with unfamiliar teammates whose abilities and fighting styles may be completely different from your usual collaborators.

"Interesting," Junpei observes during a break between exercises. "My technique actually works better in combination with some Kyoto approaches than with some Tokyo ones. The soul sensing gives different information depending on how teammates position themselves."

His insight highlights one of the unexpected benefits of joint training - discovering combination possibilities that wouldn't emerge within traditional school boundaries. Your own abilities seem to complement Kamo's analytical approach and Momo's aerial perspective in ways that create new tactical options.

The relationship building extends beyond pure technical cooperation to genuine personal connections formed through shared challenge and mutual support.

How do you want to contribute to developing these new relationships?"""

        relationship_choices = [
            StoryChoice(
                "Focus on helping Junpei integrate with the expanded peer group",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 10},
                    "story_flags": {"junpei_integration_support": True, "social_facilitation": True},
                    "next_scene": "junpei_expanded_integration",
                    "experience": 45,
                    "relationships": {"junpei": 20, "kyoto_students": 10}
                }
            ),
            StoryChoice(
                "Work on developing technical combinations with Kyoto students",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15},
                    "story_flags": {"technical_combination_development": True, "cross_school_tactics": True},
                    "next_scene": "technical_combination_training",
                    "experience": 55,
                    "relationships": {"kamo": 15}
                }
            ),
            StoryChoice(
                "Help facilitate broader cooperation between the two schools",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 10, Trait.PROTECTIVE: 10},
                    "story_flags": {"cooperation_facilitation": True, "inter_school_bridge": True},
                    "next_scene": "cooperation_facilitation",
                    "experience": 50,
                    "relationships": {"both_schools": 15}
                }
            )
        ]
        
        self.scenes["joint_training_relationships"] = StoryScene(
            "Bonds Beyond Rivalry",
            relationship_description,
            relationship_choices,
            "Joint Training Facility"
        )
        
    def _add_competition_aftermath_scenes(self):
        """Add scenes dealing with the competitive and personal aftermath."""
        
        aftermath_description = """The official results of the Exchange Event have been somewhat overshadowed by the crisis, but the competitive outcomes still matter for student development and inter-school relations. Tokyo's victory in the team battle was narrow but decisive, while the individual competitions were interrupted by the attack before completion. The mixed results reflect the reality that both schools have talented students with different strengths.

More importantly, the experience has changed everyone's perspective on what competition between sorcerers should accomplish. The traditional rivalry seems less relevant when faced with evidence of organized external threats that target all jujutsu sorcerers regardless of institutional affiliation.

"I've been thinking about Todo's suggestion," you mention to your teammates during a post-event analysis session. "Maybe future competitions should include scenarios that prepare us for the kind of coordinated attacks we just faced."

Yuji nods enthusiastically. "That makes so much sense! Competing against each other is fun, but training together against simulated threats seems more practical given what we're actually going to face as professional sorcerers."

The conversation reflects a broader shift in thinking that's occurring at both schools. Faculty members are reconsidering curriculum priorities, training methodologies, and even the fundamental structure of jujutsu education in light of recent events.

"The exchange program might evolve into something more like joint training initiatives," Megumi observes. "Shared classes, collaborative missions, maybe even integrated student teams for certain types of operations."

The possibilities are exciting but also represent significant changes to traditions that have governed jujutsu education for generations. Both schools have distinct philosophical approaches and training methodologies that have produced successful sorcerers for decades. Finding ways to maintain those strengths while adapting to new realities requires careful balance.

Nobara raises a practical concern. "What about students who thrive on competition? Todo, for example, seems to get stronger specifically because he has strong opponents to test himself against. Removing competitive elements completely might hurt some people's development."

The observation highlights the need for nuanced approaches that preserve beneficial aspects of rivalry while redirecting competitive energy toward preparation for real-world challenges. Competition can be a powerful motivator for improvement, but it needs to be structured to develop capabilities that will actually prove useful.

"Maybe the answer is competition against external challenges rather than internal rivalry," Junpei suggests. "Testing ourselves against increasingly difficult scenarios or measured improvement goals rather than trying to beat each other."

His perspective, shaped by experience with how competition can become destructive when taken too far, offers valuable insight into maintaining healthy motivational structures without creating the kind of toxic dynamics that can be exploited by manipulative influences.

The discussion continues as everyone works through the implications of how recent experiences should shape future development and inter-school relations.

What direction do you think would be most beneficial for future Exchange Events?"""

        aftermath_choices = [
            StoryChoice(
                "Advocate for joint training exercises against simulated threats",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.PROTECTIVE: 10, Trait.FOCUSED: 10},
                    "story_flags": {"joint_training_advocacy": True, "threat_simulation": True},
                    "next_scene": "joint_training_program_development",
                    "experience": 50,
                    "relationships": {"both_schools": 10}
                }
            ),
            StoryChoice(
                "Support maintaining competitive elements but with collaborative objectives",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 10, Trait.DETERMINED: 10},
                    "story_flags": {"collaborative_competition": True, "balanced_approach": True},
                    "next_scene": "collaborative_competition_design",
                    "experience": 55,
                    "relationships": {"todo": 10}
                }
            ),
            StoryChoice(
                "Focus on exchange programs for regular academic and training integration",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.COMPASSIONATE: 10, Trait.FOCUSED: 10},
                    "story_flags": {"academic_integration": True, "regular_exchange": True},
                    "next_scene": "academic_integration_planning",
                    "experience": 45,
                    "relationships": {"faculty": 10}
                }
            )
        ]
        
        self.scenes["competition_future_planning"] = StoryScene(
            "Reimagining Competition",
            aftermath_description,
            aftermath_choices,
            "Tokyo Jujutsu High - Planning Committee"
        )
        
    def get_all_scenes(self):
        """Return all scenes in the Kyoto Exchange Event Arc."""
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