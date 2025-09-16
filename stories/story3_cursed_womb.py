"""
Arc 3: Cursed Womb Arc

Covers the mission to investigate and eliminate the cursed womb:
- First real life-threatening mission outside school
- Encountering the finger bearer special grade curse
- Teamwork dynamics under extreme pressure
- Potential character deaths if wrong choices are made
- Introduction to the true danger of special grade curses
"""

from typing import Dict, Any
from character import Trait, Enemy
from .base_arc import BaseStoryArc, StoryChoice, StoryScene


class CursedWombArc(BaseStoryArc):
    """Third arc focusing on the cursed womb mission."""
    
    def __init__(self):
        super().__init__("Cursed Womb Arc", 3)
    
    def initialize_arc(self):
        """Initialize all scenes for the Cursed Womb Arc."""
        
        # Arc starting scene
        self.add_scene("start", StoryScene(
            "Emergency Mission",
            """An urgent report comes in from the Eishu Juvenile Detention Center. A cursed 
womb has manifested and is rapidly developing. Several people are trapped inside, 
including civilians who accidentally entered the barrier.

Gojo is away on another mission, leaving Megumi, Nobara, and you to handle this dangerous 
situation. Yuji has been assigned to train with higher-year students, so your team is 
down a member.

"This should have been a Grade 2 mission at most," Ijichi explains nervously as you 
arrive at the detention center. "But the cursed energy readings are... unprecedented."

The building looms before you, wrapped in a dark barrier that pulses with malevolent energy.""",
            [
                StoryChoice(
                    "Suggest waiting for backup before entering",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.ANALYTICAL: 5},
                        "relationships": {"megumi": 10},
                        "story_flags": {"cautious_approach": True},
                        "next_scene": "backup_discussion"
                    }
                ),
                StoryChoice(
                    "Insist on entering immediately to save the civilians",
                    {
                        "traits": {Trait.PROTECTIVE: 15, Trait.DETERMINED: 10},
                        "relationships": {"nobara": 10},
                        "story_flags": {"immediate_rescue": True},
                        "next_scene": "immediate_entry"
                    }
                ),
                StoryChoice(
                    "Propose a strategic reconnaissance first",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 5},
                        "story_flags": {"strategic_recon": True},
                        "next_scene": "reconnaissance_phase"
                    }
                )
            ],
            "Eishu Juvenile Detention Center - Outside"
        ))
        
        # Strategic entry
        self.add_scene("reconnaissance_phase", StoryScene(
            "Gathering Intelligence",
            """Your suggestion to gather intelligence first proves wise. Using Megumi's 
Divine Dogs, you scout the building's layout and identify multiple cursed spirits 
of varying grades throughout the structure.

"Smart thinking," Megumi acknowledges. "There are at least a dozen Grade 3 and 4 curses, 
plus something much stronger in the center. The civilians are trapped on the third floor."

Nobara taps her hammer impatiently. "Great, so we know what we're up against. Can we 
go save those people now?"

Your reconnaissance reveals three possible routes: a direct path to the civilians, 
a route that clears out smaller curses first, or a dangerous shortcut through the 
building's center where the strongest presence waits.""",
            [
                StoryChoice(
                    "Take the direct path to the civilians",
                    {
                        "traits": {Trait.PROTECTIVE: 10, Trait.DETERMINED: 5},
                        "story_flags": {"direct_rescue": True},
                        "next_scene": "direct_path"
                    }
                ),
                StoryChoice(
                    "Clear out smaller curses systematically first",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.CAUTIOUS: 5},
                        "story_flags": {"systematic_approach": True},
                        "next_scene": "systematic_clearing"
                    }
                ),
                StoryChoice(
                    "Take the dangerous shortcut through the center",
                    {
                        "traits": {Trait.AGGRESSIVE: 10, Trait.RECKLESS: 10},
                        "story_flags": {"risky_shortcut": True},
                        "next_scene": "center_route"
                    }
                )
            ],
            "Eishu Juvenile Detention Center - Inside"
        ))
        
        # Systematic approach - safest but slowest
        self.add_scene("systematic_clearing", StoryScene(
            "Methodical Approach",
            """Your team moves through the building methodically, eliminating smaller curses 
before they can overwhelm you. It's slower progress, but much safer.

"This is the right way to do it," Megumi says as his Divine Dogs dispatch another 
Grade 4 curse. "Rushing in would just get us killed."

Nobara nods grudgingly. "Boring, but effective. Though those civilians better hold 
on a bit longer."

As you reach the third floor, you find the civilians - five people huddled together 
in a classroom, protected by a weak barrier that's barely holding against the cursed 
energy saturating the building.""",
            [
                StoryChoice(
                    "Evacuate the civilians immediately",
                    {
                        "traits": {Trait.PROTECTIVE: 15},
                        "story_flags": {"civilians_saved": True},
                        "next_scene": "civilian_evacuation"
                    }
                ),
                StoryChoice(
                    "Leave Nobara to protect civilians while you and Megumi find the source",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.DETERMINED: 5},
                        "story_flags": {"split_team": True},
                        "next_scene": "team_split"
                    }
                )
            ],
            "Eishu Juvenile Detention Center - Third Floor"
        ))
        
        # Direct path - medium difficulty
        self.add_scene("direct_path", StoryScene(
            "Racing Against Time",
            """You decide to make a beeline for the civilians. The path is treacherous, 
with multiple curses blocking your way, but your determination drives you forward.

"Stay close!" you shout as a Grade 3 curse lunges at Nobara. Megumi's Divine Dogs 
intercept it just in time.

The building seems to pulse around you, the cursed womb growing stronger with each 
passing moment. You can feel something massive stirring in the building's depths.

When you reach the civilians, they're in worse shape than expected. One elderly man 
is unconscious, and a young woman is showing signs of curse poisoning.""",
            [
                StoryChoice(
                    "Use your cursed energy to stabilize the poisoned woman",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 5},
                        "story_flags": {"healed_civilian": True},
                        "cursed_energy_cost": 30,
                        "next_scene": "healing_attempt"
                    }
                ),
                StoryChoice(
                    "Focus on getting everyone out quickly",
                    {
                        "traits": {Trait.FOCUSED: 10, Trait.PROTECTIVE: 5},
                        "story_flags": {"quick_evacuation": True},
                        "next_scene": "quick_escape"
                    }
                )
            ],
            "Eishu Juvenile Detention Center - Third Floor"
        ))
        
        # The finger bearer encounter
        self.add_scene("finger_bearer_encounter", StoryScene(
            "The Special Grade Emerges",
            """As you're evacuating the civilians, the building suddenly shakes violently. 
From the basement emerges a massive, grotesque creature - the cursed womb has fully 
matured into a special grade curse.

The finger bearer towers above you, its multiple eyes gleaming with intelligence and 
malice. It clutches one of Sukuna's fingers, the source of its immense power.

"That's... that's a special grade," Megumi says, his voice barely concealing his fear. 
"We're not equipped to handle this."

Nobara readies her tools, but you can see the doubt in her eyes. "So what's the plan? 
We can't exactly run with civilians to protect.""",
            [
                StoryChoice(
                    "Challenge the finger bearer to protect your team and civilians",
                    {
                        "traits": {Trait.PROTECTIVE: 20, Trait.DETERMINED: 15},
                        "story_flags": {"heroic_stand": True},
                        "combat": True,
                        "enemy": "finger_bearer",
                        "next_scene": "finger_bearer_battle"
                    }
                ),
                StoryChoice(
                    "Try to find an alternative escape route",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10},
                        "story_flags": {"seek_escape": True},
                        "next_scene": "escape_attempt"
                    }
                ),
                StoryChoice(
                    "Coordinate a team strategy to exploit the curse's weaknesses",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 10},
                        "story_flags": {"team_strategy": True},
                        "next_scene": "strategic_battle"
                    }
                )
            ],
            "Eishu Juvenile Detention Center - Main Hall"
        ))
        
        # Heroic battle outcome
        self.add_scene("finger_bearer_battle", StoryScene(
            "Against Overwhelming Odds",
            """Your decision to face the finger bearer head-on is both heroic and terrifying. 
The special grade curse is far beyond your current abilities, but your determination 
to protect others gives you strength you didn't know you had.

The battle is brutal. The finger bearer's immense strength and cursed techniques push 
your team to their absolute limits. Megumi's shikigami are destroyed one by one, 
and Nobara's attacks barely scratch the creature's hide.

Just when it seems hopeless, your unwavering resolve triggers something unexpected - 
a surge of cursed energy that allows you to land a significant blow.""",
            [
                StoryChoice(
                    "Press the advantage with everything you have",
                    {
                        "traits": {Trait.DETERMINED: 20, Trait.RECKLESS: 10},
                        "story_flags": {"desperate_gambit": True},
                        "cursed_energy_cost": 50,
                        "next_scene": "desperate_victory"
                    }
                ),
                StoryChoice(
                    "Use the opening to evacuate while the curse is stunned",
                    {
                        "traits": {Trait.PROTECTIVE: 15, Trait.CAUTIOUS: 10},
                        "story_flags": {"tactical_retreat": True},
                        "next_scene": "tactical_evacuation"
                    }
                )
            ],
            "Eishu Juvenile Detention Center - Main Hall"
        ))
        
        # Victory against the finger bearer
        self.add_scene("desperate_victory", StoryScene(
            "Impossible Victory",
            """Through sheer determination and teamwork, your group manages to defeat the 
finger bearer. The victory comes at a cost - you're all exhausted, injured, and pushed 
far beyond your normal limits.

"I can't believe we actually did it," Nobara pants, leaning heavily on her hammer.

Megumi looks at you with newfound respect. "That surge of cursed energy... I've never 
seen anything like it. You might have unlocked something significant."

The finger bearer's defeat causes the cursed womb barrier to collapse, freeing the 
building. All civilians are saved, and you've proven that even first-year students 
can face special grade threats when they work together and refuse to give up.""",
            [
                StoryChoice(
                    "Reflect on the power you accessed during the battle",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 5},
                        "story_flags": {"power_awakening": True},
                        "techniques": ["surge_technique"],
                        "experience": 300,
                        "next_scene": "power_reflection"
                    }
                ),
                StoryChoice(
                    "Focus on the fact that you saved everyone",
                    {
                        "traits": {Trait.COMPASSIONATE: 15, Trait.PROTECTIVE: 10},
                        "story_flags": {"savior_mindset": True},
                        "relationships": {"civilians": 25, "megumi": 15, "nobara": 15},
                        "experience": 250,
                        "next_scene": "savior_recognition"
                    }
                )
            ],
            "Eishu Juvenile Detention Center - Outside"
        ))
        
        # Arc completion
        self.add_scene("arc_completion", StoryScene(
            "A Mission Completed",
            """Your successful completion of the cursed womb mission sends shockwaves through 
the jujutsu sorcery community. First-year students defeating a special grade curse is 
almost unprecedented.

Gojo returns to find his students have accomplished something extraordinary. "I'm 
impressed," he says with genuine pride. "You've all grown stronger than I expected. 
This mission has proven you're ready for greater challenges."

The experience has bonded your team more closely and established your reputation as 
a formidable group of sorcerers. The techniques and insights gained from this battle 
will serve you well in the trials ahead.""",
            [
                StoryChoice(
                    "Prepare for whatever comes next",
                    {
                        "story_flags": {"ready_for_escalation": True},
                        "experience": 100,
                        "next_arc": 4,
                        "next_scene": "start"
                    }
                )
            ],
            "Tokyo Jujutsu High - Faculty Office"
        ))
    
    def create_enemy(self, enemy_type: str, player_level: int) -> Enemy:
        """Create arc-specific enemies."""
        if enemy_type == "finger_bearer":
            enemy = Enemy("Finger Bearer (Special Grade)", 400, 200, "special")
            enemy.ai_pattern = "intelligent"
            enemy.special_abilities = ["finger_power", "regeneration", "cursed_blast"]
            enemy.max_phases = 2
            enemy.phase_transition_messages = [
                "The finger bearer's power increases dramatically!",
                "Sukuna's finger pulses with malevolent energy!"
            ]
        else:
            return super().create_enemy(enemy_type, player_level)
        
        # Special grade - don't scale normally
        enemy.level = max(player_level + 5, 15)  # Significantly stronger
        return enemy