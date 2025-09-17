"""
Arc 1: Introduction Arc - Tokyo Jujutsu High Beginnings

This arc introduces the player to the world of Jujutsu Kaisen, covering their
arrival at Tokyo Jujutsu High, meeting the main characters, and first missions.
Expanded to provide rich storytelling and character development.
"""

from typing import Dict, List, Any
from character import Trait
from story import StoryChoice, StoryScene


def get_arc1_scenes() -> Dict[str, StoryScene]:
    """Return all scenes for Arc 1: Introduction Arc."""
    scenes = {}
    
    # ============================================================================
    # INTRODUCTION SEQUENCE - Arrival and First Impressions
    # ============================================================================
    
    scenes["intro"] = StoryScene(
        "Arrival at Tokyo Jujutsu High",
        """The train pulls into Tokyo Station with a mechanical hiss, and you step onto the platform 
with your single bag containing everything you own. The city sprawls endlessly before you, a maze 
of concrete and glass that seems to pulse with unseen energy. But you're not here for the city - 
you're here for something far more dangerous and extraordinary.

Tokyo Jujutsu High School sits nestled in the mountains outside the city, accessible only by a 
winding path that seems to grow more ominous with each step. Ancient torii gates mark the way, 
their red paint faded but still radiating an unmistakable spiritual power. As you approach the 
school grounds, the weight of cursed energy in the air becomes almost tangible.

The school itself is a blend of traditional Japanese architecture and modern facilities. Wooden 
buildings with curved roofs stand alongside concrete training facilities, all surrounded by 
barriers that shimmer faintly in the afternoon light. Students in dark uniforms move between 
buildings, some carrying weapons, others with visible wounds from training.

As you pass through the main gates, a senior student approaches you with a knowing smile.

"First day?" she asks, adjusting the sword strapped to her back. "Don't worry, everyone survives 
their first week. Well, almost everyone."

Before you can respond, a commotion erupts from the direction of the training grounds. Shouts 
echo across the courtyard, followed by an inhuman shriek that makes your skin crawl. Through 
the chaos, you see a younger student backed against a wall, cornered by something that shouldn't 
exist - a writhing mass of shadows and malice with too many teeth.

The cursed spirit has somehow breached the school's defenses, and the injured student is running 
out of time. Other students are rushing toward the scene, but you're closest. In this moment, 
your first real choice as a jujutsu sorcerer will define who you become.

What do you do?""",
        [
            StoryChoice(
                "Rush in to help immediately - every second counts",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 10, Trait.RECKLESS: 5},
                    "next_scene": "rescue_path_immediate",
                    "relationships": {"injured_student": 20, "yuji": 15},
                    "story_flags": {"first_action": "immediate_help", "reputation": "hero"},
                    "experience": 10
                }
            ),
            StoryChoice(
                "Quickly assess the situation and the curse's weaknesses",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10, Trait.FOCUSED: 10},
                    "next_scene": "rescue_path_analytical",
                    "relationships": {"megumi": 15, "gojo": 10},
                    "story_flags": {"first_action": "strategic_analysis", "reputation": "tactician"},
                    "experience": 15
                }
            ),
            StoryChoice(
                "Charge the curse head-on with everything you've got",
                {
                    "traits": {Trait.AGGRESSIVE: 15, Trait.RECKLESS: 10, Trait.DETERMINED: 10},
                    "next_scene": "rescue_path_aggressive",
                    "relationships": {"nobara": 15, "todo": 10},
                    "story_flags": {"first_action": "direct_assault", "reputation": "berserker"},
                    "experience": 12
                }
            ),
            StoryChoice(
                "Call for help while moving to assist",
                {
                    "traits": {Trait.CAUTIOUS: 15, Trait.FOCUSED: 10, Trait.PROTECTIVE: 10},
                    "next_scene": "rescue_path_team",
                    "relationships": {"faculty": 15, "classmates": 10},
                    "story_flags": {"first_action": "team_coordination", "reputation": "leader"},
                    "experience": 13
                }
            )
        ],
        "Tokyo Jujutsu High - Main Courtyard"
    )
    
    # ============================================================================
    # IMMEDIATE RESCUE PATH - Compassionate Response
    # ============================================================================
    
    scenes["rescue_path_immediate"] = StoryScene(
        "The Rescuer's Courage",
        """Without hesitation, you sprint toward the cornered student. Your feet pound against the 
stone courtyard as adrenaline floods your system. The cursed spirit - a writhing mass of shadow 
and fury - turns at your approach, its multiple eyes fixing on you with predatory interest.

"Stay back!" the injured student shouts, blood streaming from scratches on his arms. "It's too 
strong for a first-year!"

But you're already moving, your body acting on pure instinct. As you close the distance, the 
curse lashes out with a tendril of darkness. You dodge to the side, feeling the malevolent energy 
brush past your cheek like ice-cold fingers.

Just as you reach for your cursed energy, a familiar pink-haired figure vaults over a nearby 
fence with impossible athleticism. Yuji Itadori lands beside you with a grin that seems completely 
inappropriate for the situation.

"Nice reflexes!" he says, bouncing on his feet like a boxer ready for round one. "I was wondering 
when someone interesting would show up. Mind if I join the party?"

The curse spirit seems to sense the increased threat and grows larger, its form becoming more 
defined and menacing. Claws extend from what might be considered hands, and its shriek echoes 
off the surrounding buildings.

"That's a Grade 3," Yuji continues, his expression becoming more serious. "Nasty little thing, 
but nothing we can't handle together. What's your plan, hero?"

The injured student behind you whimpers as the curse advances, clearly terrified but unable to 
move. You can feel your cursed energy responding to your emotions, ready to be shaped by your will. 
This is your first real combat situation, and how you handle it will set the tone for your entire 
time at the school.

What's your approach?""",
        [
            StoryChoice(
                "Fight alongside Yuji as equals",
                {
                    "combat": True,
                    "enemy": "grade_3_curse",
                    "ally": "yuji",
                    "traits": {Trait.DETERMINED: 10, Trait.FOCUSED: 15},
                    "relationships": {"yuji": 25},
                    "next_scene": "post_battle_yuji_partnership",
                    "story_flags": {"combat_style": "teamwork", "yuji_first_impression": "partner"}
                }
            ),
            StoryChoice(
                "Create a distraction while Yuji gets the injured student to safety",
                {
                    "traits": {Trait.PROTECTIVE: 20, Trait.FOCUSED: 15, Trait.ANALYTICAL: 10},
                    "relationships": {"yuji": 20, "injured_student": 30},
                    "next_scene": "distraction_gambit",
                    "story_flags": {"combat_style": "protector", "self_sacrifice": True}
                }
            ),
            StoryChoice(
                "Try to defeat the curse yourself to prove your worth",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_solo",
                    "traits": {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 10, Trait.FOCUSED: 10},
                    "relationships": {"yuji": 5},
                    "next_scene": "solo_battle_outcome",
                    "story_flags": {"combat_style": "solo", "independence": True}
                }
            ),
            StoryChoice(
                "Suggest a coordinated tactical approach",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15, Trait.ANALYTICAL: 10},
                    "relationships": {"yuji": 20, "faculty": 10},
                    "next_scene": "tactical_coordination",
                    "story_flags": {"combat_style": "tactical", "leadership_potential": True}
                }
            )
        ],
        "Tokyo Jujutsu High - Training Grounds"
    )
    
    # ============================================================================
    # ANALYTICAL RESCUE PATH - Strategic Response  
    # ============================================================================
    
    scenes["rescue_path_analytical"] = StoryScene(
        "The Strategist's Mind",
        """You force yourself to stop and think, even as every instinct screams at you to rush 
forward. Your eyes scan the scene with methodical precision: the curse's positioning, the 
injured student's location, potential escape routes, and the flow of cursed energy around the area.

The curse is a Grade 3, its form unstable but clearly aggressive. It's positioned itself between 
the student and the main path, cutting off easy escape. But you notice something - its movements 
favor its right side, and there's a slight delay in its reactions when attacked from the left.

More importantly, you sense another presence nearby. Hidden in the shadows of a building, 
someone else is watching and analyzing the situation just as you are. A figure steps forward - 
tall, dark-haired, with an serious expression that matches your own analytical approach.

"Megumi Fushiguro," he introduces himself quietly, never taking his eyes off the curse. "You're 
the new student, right? Good instincts - most people would have rushed in blindly by now."

He raises his hands in a specific gesture, shadows beginning to gather around his fingers. 
"That curse has been feeding on the negative emotions from the training grounds. It's stronger 
than a typical Grade 3, but it has a critical weakness - it can't maintain its form if attacked 
from multiple angles simultaneously."

The injured student's breathing is becoming labored, and you can see fear overwhelming his 
ability to think clearly. The curse seems to be feeding on this terror, growing slightly larger 
with each passing moment.

"We need to act soon," Megumi continues, "but smart action will save more lives than heroic 
action. What's your assessment?"

You feel a deep respect growing for this methodical approach to danger. This could be the 
beginning of a partnership built on mutual understanding and tactical thinking.

How do you proceed?""",
        [
            StoryChoice(
                "Share your own analysis and coordinate with Megumi",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15, Trait.FOCUSED: 10},
                    "relationships": {"megumi": 30},
                    "next_scene": "analytical_partnership",
                    "story_flags": {"megumi_first_impression": "intellectual_equal", "tactical_bond": True}
                }
            ),
            StoryChoice(
                "Suggest using the environment to trap the curse",
                {
                    "traits": {Trait.ANALYTICAL: 15, Trait.ANALYTICAL: 20, Trait.ANALYTICAL: 10},
                    "relationships": {"megumi": 25, "faculty": 15},
                    "next_scene": "environmental_trap",
                    "story_flags": {"creative_tactics": True, "environmental_awareness": True}
                }
            ),
            StoryChoice(
                "Propose a psychological approach to weaken the curse",
                {
                    "traits": {Trait.COMPASSIONATE: 15, Trait.ANALYTICAL: 20, Trait.FOCUSED: 15},
                    "relationships": {"megumi": 20, "injured_student": 20},
                    "next_scene": "psychological_warfare",
                    "story_flags": {"curse_psychology": True, "deep_understanding": True}
                }
            ),
            StoryChoice(
                "Execute a precision strike based on your observations",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_weakened",
                    "traits": {Trait.FOCUSED: 20, Trait.FOCUSED: 15, Trait.FOCUSED: 10},
                    "relationships": {"megumi": 25},
                    "next_scene": "precision_victory",
                    "story_flags": {"precision_fighter": True, "calculated_risk": True}
                }
            )
        ],
        "Tokyo Jujutsu High - Training Grounds"
    )
    
    # ============================================================================
    # AGGRESSIVE RESCUE PATH - Direct Combat
    # ============================================================================
    
    scenes["rescue_path_aggressive"] = StoryScene(
        "The Warrior's Fire",
        """Raw determination floods through your veins as you charge directly at the cursed spirit. 
There's no time for hesitation, no room for doubt - only action. Your cursed energy responds to 
your emotions, flaring around you like an aura of barely controlled power.

The curse turns to face you, surprised by your direct approach. Its multiple eyes widen in what 
might be shock - clearly, it expected fear, not aggression. You use this moment of hesitation 
to close the distance, your fist already charged with cursed energy.

Your first strike connects with a satisfying impact that sends shockwaves through both you and 
the creature. It staggers backward, dark ichor spraying from the wound, but quickly recovers and 
lashes out with razor-sharp claws.

Just as the curse's counterattack is about to connect, a hammer made of what looks like cursed 
energy slams into the creature's side, sending it flying into a nearby wall. You turn to see a 
girl with short brown hair and a fierce expression, wielding a straw doll that pulses with power.

"Not bad for a rookie," Nobara Kugisaki says with a smirk, spinning her hammer-tool with practiced 
ease. "But charging in without a plan? That's exactly the kind of reckless stupidity I can respect."

The curse pulls itself from the crater in the wall, clearly more damaged but also more furious. 
Its form begins to shift and bubble, becoming more monstrous and desperate. The injured student 
behind you has managed to crawl further away, but he's still in danger if this fight goes badly.

"This thing's getting desperate," Nobara observes, her eyes calculating distances and angles. 
"Desperate curses are either really dangerous or really stupid. Sometimes both. You ready to 
finish what you started?"

Your cursed energy is still burning hot from the initial clash, and you can feel your fighting 
instincts sharpening. This is what you came here for - the chance to pit your strength against 
the darkness that threatens innocent people.

How do you continue the battle?""",
        [
            StoryChoice(
                "Coordinate a devastating combo attack with Nobara",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_desperate",
                    "ally": "nobara",
                    "traits": {Trait.AGGRESSIVE: 10, Trait.FOCUSED: 15, Trait.FOCUSED: 10},
                    "relationships": {"nobara": 25},
                    "next_scene": "nobara_combo_victory",
                    "story_flags": {"combat_style": "aggressive_team", "nobara_respect": True}
                }
            ),
            StoryChoice(
                "Press your solo assault to overwhelm the curse",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_enraged",
                    "traits": {Trait.AGGRESSIVE: 20, Trait.AGGRESSIVE: 15, Trait.AGGRESSIVE: 10},
                    "relationships": {"nobara": 15},
                    "next_scene": "relentless_victory",
                    "story_flags": {"combat_style": "berserker", "solo_dominance": True}
                }
            ),
            StoryChoice(
                "Use your raw power to intimidate the curse into retreat",
                {
                    "traits": {Trait.FOCUSED: 20, Trait.FOCUSED: 15, Trait.FOCUSED: 10},
                    "relationships": {"nobara": 20, "curse_spirits": -10},
                    "next_scene": "intimidation_success",
                    "story_flags": {"intimidation_tactics": True, "curse_fear": True}
                }
            ),
            StoryChoice(
                "Channel your emotions into a desperate finishing move",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_final",
                    "traits": {Trait.RECKLESS: 15, Trait.FOCUSED: 20, Trait.RECKLESS: 15},
                    "relationships": {"nobara": 20},
                    "next_scene": "emotional_breakthrough",
                    "story_flags": {"emotional_power": True, "breakthrough_moment": True}
                }
            )
        ],
        "Tokyo Jujutsu High - Training Grounds"
    )
    
    # ============================================================================
    # TEAM COORDINATION PATH - Leadership Response
    # ============================================================================
    
    scenes["rescue_path_team"] = StoryScene(
        "The Leader's Call",
        """Your voice cuts through the chaos as you shout for assistance while moving toward the 
danger. "Help! Cursed spirit in the training grounds! Student in danger!" Your call echoes across 
the courtyard, immediately drawing attention from multiple directions.

As you run, you're already formulating a plan. The curse is strong, but it's isolated and 
outnumbered. With proper coordination, this could be handled efficiently with minimal risk to 
everyone involved.

Within seconds, several people respond to your call. A tall man with white hair and a blindfold 
appears as if from nowhere, moving with the casual confidence of someone for whom danger is merely 
an inconvenience. This can only be Satoru Gojo, the famous special grade sorcerer.

"Well, well," Gojo says with an amused tone, "looks like our new student has good instincts for 
leadership. Most people either freeze or charge in blindly." He seems completely relaxed despite 
the ongoing crisis.

Two other first-years arrive almost simultaneously - Yuji Itadori vaulting over a fence with 
incredible athleticism, and Megumi Fushiguro approaching with calculated steps, his hands already 
forming the gestures for a summoning technique.

"Four sorcerers against one Grade 3," you call out, quickly assessing the situation. "We can 
end this quickly if we coordinate properly."

The injured student looks up with desperate hope as he sees help arriving. The curse, sensing 
the shift in odds, begins to back against the wall, its form growing more aggressive and spiky 
in response to feeling cornered.

"I like this one," Gojo announces cheerfully. "Tactical thinking, natural leadership, and the 
good sense to call for backup. These are exactly the qualities we need more of around here."

The curse lets out a bone-chilling shriek, clearly preparing for a desperate final assault 
against what it perceives as overwhelming force.

How do you coordinate the team response?""",
        [
            StoryChoice(
                "Assign specific roles to each team member based on their abilities",
                {
                    "traits": {Trait.FOCUSED: 25, Trait.ANALYTICAL: 20, Trait.FOCUSED: 15},
                    "relationships": {"gojo": 25, "yuji": 20, "megumi": 20},
                    "next_scene": "tactical_leadership",
                    "story_flags": {"leadership_style": "tactical", "gojo_approval": True, "team_coordination": True}
                }
            ),
            StoryChoice(
                "Let Gojo take point while you support and learn",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.FOCUSED: 25, Trait.PROTECTIVE: 15},
                    "relationships": {"gojo": 30, "classmates": 15},
                    "next_scene": "mentorship_moment",
                    "story_flags": {"learning_attitude": True, "mentorship_path": True}
                }
            ),
            StoryChoice(
                "Suggest a coordinated simultaneous attack",
                {
                    "combat": True,
                    "enemy": "grade_3_curse_overwhelmed",
                    "allies": ["yuji", "megumi", "gojo"],
                    "traits": {Trait.FOCUSED: 20, Trait.FOCUSED: 15, Trait.ANALYTICAL: 15},
                    "relationships": {"team": 20},
                    "next_scene": "perfect_teamwork",
                    "story_flags": {"perfect_coordination": True, "team_synergy": True}
                }
            ),
            StoryChoice(
                "Focus on evacuation while the others handle combat",
                {
                    "traits": {Trait.PROTECTIVE: 25, Trait.PROTECTIVE: 20, Trait.FOCUSED: 15},
                    "relationships": {"injured_student": 35, "faculty": 20},
                    "next_scene": "evacuation_specialist",
                    "story_flags": {"protection_focus": True, "civilian_priority": True}
                }
            )
        ],
        "Tokyo Jujutsu High - Training Grounds"
    )
    
    # ============================================================================
    # POST-RESCUE SCENES - Character Development & Relationships
    # ============================================================================
    
    scenes["post_battle_yuji_partnership"] = StoryScene(
        "Bonds Forged in Battle",
        """The cursed spirit dissolves into wisps of dark energy, its dying shriek echoing off the 
training ground walls before fading into silence. You and Yuji stand back-to-back, both breathing 
heavily but victorious. The injured student slumps against the wall in relief, his wounds already 
being tended to by arriving medical staff.

"That was incredible!" Yuji exclaims, his face lighting up with genuine excitement. "The way you 
moved in sync with my attacks - it's like we've been training together for months instead of 
meeting five minutes ago!"

You can feel the adrenaline still coursing through your veins, mixed with a deep satisfaction 
at having successfully protected someone. But more than that, there's a sense of connection with 
Yuji that goes beyond just successful teamwork. You fought as equals, trusted each other instantly, 
and emerged victorious.

"Most people are either too scared to keep up or too reckless to coordinate with," Yuji continues, 
wiping sweat from his forehead. "But you... you found that perfect balance. I think we're going 
to make a great team."

The injured student manages to stand with help from the medical staff. "Thank you," he says weakly, 
looking between you and Yuji. "I thought I was done for. That curse came out of nowhere during 
training, and my technique just... failed."

Gojo appears beside you without warning, having apparently watched the entire encounter. "Excellent 
work, both of you. Teamwork like that usually takes months to develop. You," he points at you, 
"have natural combat instincts and the wisdom to recognize a strong partner when you see one."

"Does this mean I pass some kind of test?" you ask, suddenly wondering if this whole situation 
was planned.

Gojo's grin is mysterious behind his blindfold. "Every day at this school is a test. Today, you 
passed with flying colors. But tomorrow will bring new challenges."

As the immediate crisis fades, you realize this was just your first day. If this is what passes 
for a normal afternoon at Tokyo Jujutsu High, you're going to need to adapt quickly.

What's your next priority?""",
        [
            StoryChoice(
                "Ask Yuji to show you around the school and introduce you to others",
                {
                    "traits": {Trait.FOCUSED: 15, Trait.ANALYTICAL: 10, Trait.FOCUSED: 15},
                    "relationships": {"yuji": 20, "classmates": 15},
                    "next_scene": "school_tour_yuji",
                    "story_flags": {"social_integration": True, "yuji_guide": True}
                }
            ),
            StoryChoice(
                "Request immediate training to improve your combat abilities",
                {
                    "traits": {Trait.DETERMINED: 20, Trait.FOCUSED: 15, Trait.DETERMINED: 10},
                    "relationships": {"gojo": 15, "training_staff": 10},
                    "next_scene": "immediate_training",
                    "story_flags": {"training_priority": True, "improvement_drive": True}
                }
            ),
            StoryChoice(
                "Check on the injured student and learn about curse prevention",
                {
                    "traits": {Trait.COMPASSIONATE: 20, Trait.FOCUSED: 15, Trait.PROTECTIVE: 10},
                    "relationships": {"injured_student": 25, "medical_staff": 15},
                    "next_scene": "medical_learning",
                    "story_flags": {"medical_interest": True, "prevention_focus": True}
                }
            ),
            StoryChoice(
                "Ask Gojo about the school's defenses and how the curse got in",
                {
                    "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15, Trait.FOCUSED: 10},
                    "relationships": {"gojo": 20, "faculty": 10},
                    "next_scene": "security_discussion",
                    "story_flags": {"security_interest": True, "strategic_thinking": True}
                }
            )
        ],
        "Tokyo Jujutsu High - Training Grounds"
    )
    
    # Continue with more scenes...
    # This is just the beginning of the expanded Arc 1
    # The complete implementation would include dozens more scenes
    # covering all the branching paths and character development
    
    return scenes