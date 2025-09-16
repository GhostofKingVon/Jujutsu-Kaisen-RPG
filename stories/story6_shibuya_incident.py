"""
Arc 6: Shibuya Incident Arc

Covers the devastating Halloween incident in Shibuya:
- Gojo's sealing in the Prison Realm
- Major battles with special grade curses and curse users
- High stakes with civilian lives at risk
- Character development under extreme pressure
- Multiple storylines and perspectives
- Lasting consequences for the jujutsu world
"""

from typing import Dict, Any
from character import Trait, Enemy
from .base_arc import BaseStoryArc, StoryChoice, StoryScene


class ShibuyaIncidentArc(BaseStoryArc):
    """Sixth arc focusing on the pivotal Shibuya Incident."""
    
    def __init__(self):
        super().__init__("Shibuya Incident Arc", 6)
    
    def initialize_arc(self):
        """Initialize all scenes for the Shibuya Incident Arc."""
        
        # Arc starting scene
        self.add_scene("start", StoryScene(
            "Halloween Night in Shibuya",
            """Halloween night, October 31st. Shibuya Station is packed with civilians 
in costumes, unaware of the supernatural trap being set around them. Intelligence 
reports indicate that a coordinated attack by curse users is imminent.

The curtain drops over Shibuya, trapping thousands of civilians inside with a 
barrier that allows only sorcerers to enter but prevents anyone from leaving. 
The barrier specifically requests Gojo Satoru.

"This is clearly a trap," Nanami states grimly as your team prepares outside 
the barrier. "But we can't abandon the civilians."

Your team consists of yourself, Yuji, Megumi, Nobara, Ino, and Nanami. The 
mission is rescue and evacuation, but you all know it won't be that simple.""",
            [
                StoryChoice(
                    "Volunteer to enter with the main rescue team",
                    {
                        "traits": {Trait.PROTECTIVE: 15, Trait.DETERMINED: 10},
                        "story_flags": {"main_rescue_team": True},
                        "next_scene": "rescue_team_entry"
                    }
                ),
                StoryChoice(
                    "Suggest reconnaissance to gather intelligence first",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10},
                        "story_flags": {"intelligence_priority": True},
                        "next_scene": "reconnaissance_mission"
                    }
                ),
                StoryChoice(
                    "Propose splitting into smaller teams for efficiency",
                    {
                        "traits": {Trait.FOCUSED: 10, Trait.ANALYTICAL: 5},
                        "story_flags": {"tactical_split": True},
                        "next_scene": "team_division"
                    }
                )
            ],
            "Shibuya Station - Outside the Barrier"
        ))
        
        # Main rescue team path
        self.add_scene("rescue_team_entry", StoryScene(
            "Into the Heart of Chaos",
            """Entering the barrier with the main rescue team, you're immediately struck 
by the oppressive cursed energy saturating the air. The station is in chaos - 
civilians huddle in terror while weak curses roam freely.

Nanami takes charge immediately. "Our priority is civilian evacuation. Yuji, 
Megumi, clear a path to the platforms. Nobara, Ino, establish a safe zone. 
You're with me - we'll handle any special grades that show up."

As you move deeper into the station, you encounter your first major threat: 
Jogo, the volcano-headed special grade curse, is systematically hunting civilians.""",
            [
                StoryChoice(
                    "Challenge Jogo directly to protect the civilians",
                    {
                        "traits": {Trait.PROTECTIVE: 20, Trait.RECKLESS: 10},
                        "story_flags": {"challenged_jogo": True},
                        "combat": True,
                        "enemy": "jogo_initial",
                        "next_scene": "jogo_confrontation"
                    }
                ),
                StoryChoice(
                    "Focus on evacuation while avoiding direct confrontation",
                    {
                        "traits": {Trait.PROTECTIVE: 15, Trait.CAUTIOUS: 10},
                        "story_flags": {"evacuation_focus": True},
                        "next_scene": "civilian_evacuation"
                    }
                ),
                StoryChoice(
                    "Coordinate with your team to outmaneuver Jogo",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 10},
                        "story_flags": {"team_coordination": True},
                        "next_scene": "tactical_maneuvers"
                    }
                )
            ],
            "Shibuya Station - Main Concourse"
        ))
        
        # Gojo's arrival and sealing
        self.add_scene("gojo_arrival", StoryScene(
            "The Strongest Arrives",
            """Gojo Satoru arrives at Shibuya Station, his presence immediately felt 
throughout the barrier. The civilians look up with hope - if the strongest 
jujutsu sorcerer is here, they'll be saved.

But something's wrong. Geto Suguru is here - or someone wearing his face. 
The sight of his former friend, supposedly dead, stops Gojo in his tracks 
for just a moment.

That moment is all the enemy needed. The Prison Realm activates, and the 
unthinkable happens - Gojo Satoru is sealed away.

The balance of power in the jujutsu world has just shifted catastrophically.""",
            [
                StoryChoice(
                    "Try to interfere with the sealing process",
                    {
                        "traits": {Trait.RECKLESS: 20, Trait.DETERMINED: 15},
                        "story_flags": {"attempted_gojo_rescue": True},
                        "next_scene": "sealing_interference"
                    }
                ),
                StoryChoice(
                    "Focus on protecting civilians while Gojo is distracted",
                    {
                        "traits": {Trait.PROTECTIVE: 20, Trait.FOCUSED: 10},
                        "story_flags": {"civilian_priority": True},
                        "next_scene": "civilian_protection"
                    }
                ),
                StoryChoice(
                    "Gather intelligence on the enemy's plan",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10},
                        "story_flags": {"intelligence_gathering": True},
                        "next_scene": "enemy_analysis"
                    }
                )
            ],
            "Shibuya Station - Platform B5F"
        ))
        
        # Post-sealing chaos
        self.add_scene("post_sealing_chaos", StoryScene(
            "Without the Strongest",
            """With Gojo sealed, the situation in Shibuya deteriorates rapidly. The 
special grade curses and curse users launch their coordinated assault with 
renewed confidence. The very air seems heavier without Gojo's overwhelming 
presence.

Nanami's voice crackles over the radio: "All units, Gojo-sensei has been 
neutralized. We're now operating under worst-case scenario protocols. 
Prioritize civilian evacuation above all else."

You find yourself separated from your team, surrounded by chaos. Multiple 
special grade threats are now active throughout Shibuya, and coordinated 
curse user attacks are overwhelming the sorcerer response teams.""",
            [
                StoryChoice(
                    "Seek out and reunite with your teammates",
                    {
                        "traits": {Trait.FOCUSED: 15, Trait.PROTECTIVE: 10},
                        "story_flags": {"team_reunion_priority": True},
                        "next_scene": "team_reunion_attempt"
                    }
                ),
                StoryChoice(
                    "Take independent action to save as many civilians as possible",
                    {
                        "traits": {Trait.PROTECTIVE: 20, Trait.DETERMINED: 15},
                        "story_flags": {"lone_hero": True},
                        "next_scene": "independent_rescue"
                    }
                ),
                StoryChoice(
                    "Try to gather information about the enemy's objectives",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 5},
                        "story_flags": {"strategic_intelligence": True},
                        "next_scene": "strategic_reconnaissance"
                    }
                )
            ],
            "Shibuya District - Various Locations"
        ))
        
        # Major battle sequence with Mahito
        self.add_scene("mahito_encounter", StoryScene(
            "The Soul-Manipulating Curse",
            """Your path through Shibuya leads you to a confrontation with Mahito, 
the special grade curse who manipulates souls. He's been systematically 
transforming humans into grotesque forms, experimenting with his Idle 
Transfiguration technique.

"Oh, if it isn't one of Gojo's little students," Mahito grins with his 
stitched smile. "Don't worry about your teacher - he's taking a nice, 
long nap. But I'm curious about your soul's shape."

Around you, the transformed humans moan in agony. Some still retain enough 
consciousness to beg for death. The true horror of Mahito's curse technique 
is on full display.""",
            [
                StoryChoice(
                    "Attack Mahito with everything you have",
                    {
                        "traits": {Trait.AGGRESSIVE: 20, Trait.DETERMINED: 15},
                        "story_flags": {"all_out_mahito_attack": True},
                        "combat": True,
                        "enemy": "mahito_full_power",
                        "next_scene": "mahito_battle_intense"
                    }
                ),
                StoryChoice(
                    "Try to rescue the transformed humans first",
                    {
                        "traits": {Trait.COMPASSIONATE: 25, Trait.PROTECTIVE: 15},
                        "story_flags": {"rescue_attempt": True},
                        "next_scene": "human_rescue_attempt"
                    }
                ),
                StoryChoice(
                    "Engage Mahito tactically while looking for weaknesses",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15},
                        "story_flags": {"tactical_mahito_fight": True},
                        "combat": True,
                        "enemy": "mahito_tactical",
                        "next_scene": "mahito_tactical_battle"
                    }
                )
            ],
            "Shibuya Underground - Abandoned Platform"
        ))
        
        # Critical choice point - Nanami's fate
        self.add_scene("nanami_in_danger", StoryScene(
            "The Salaryman Sorcerer's Last Stand",
            """You arrive to find Nanami gravely injured, having fought through 
multiple special grade curses and suffered severe burns from Jogo's flames. 
Despite his injuries, he's still trying to protect a group of trapped civilians.

"I'm at my limit," Nanami admits, his usual composure cracked. "But I can't 
leave these people."

Mahito appears, sensing Nanami's weakened state like a predator scenting blood. 
"Perfect timing. I've been wanting to see what happens when I touch a sorcerer 
who's already close to death."

This is a critical moment - your actions here will determine Nanami's fate.""",
            [
                StoryChoice(
                    "Throw yourself between Mahito and Nanami",
                    {
                        "traits": {Trait.PROTECTIVE: 25, Trait.RECKLESS: 15},
                        "story_flags": {"protected_nanami": True},
                        "relationships": {"nanami": 50},
                        "next_scene": "nanami_saved"
                    }
                ),
                StoryChoice(
                    "Create a diversion to help Nanami escape",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15},
                        "story_flags": {"diversion_tactic": True},
                        "combat": True,
                        "enemy": "mahito_distracted",
                        "next_scene": "escape_attempt"
                    }
                ),
                StoryChoice(
                    "Rally nearby sorcerers to help overwhelm Mahito",
                    {
                        "traits": {Trait.FOCUSED: 20, Trait.DETERMINED: 10},
                        "story_flags": {"coordinated_rescue": True},
                        "next_scene": "team_coordination"
                    }
                )
            ],
            "Shibuya Station - Emergency Exit"
        ))
        
        # Successful Nanami rescue
        self.add_scene("nanami_saved", StoryScene(
            "A Life Preserved",
            """Your heroic intervention saves Nanami from Mahito's deadly touch. 
Taking the hit meant for him, you manage to resist Mahito's soul manipulation 
through sheer force of will and determination.

"Impossible," Mahito snarls. "Your soul... it's unusually stable."

Nanami, despite his injuries, manages to land a critical blow on Mahito while 
the curse is distracted by your resistance. The combination of your sacrifice 
and his experience drives Mahito back temporarily.

"Thank you," Nanami says simply, but the gratitude in his eyes speaks volumes. 
"Now let's get these civilians to safety."

Your choice to protect others has saved one of the most respected sorcerers 
and earned his deep respect.""",
            [
                StoryChoice(
                    "Help evacuate the civilians with Nanami",
                    {
                        "traits": {Trait.PROTECTIVE: 15, Trait.COMPASSIONATE: 10},
                        "relationships": {"nanami": 30, "civilians": 25},
                        "story_flags": {"nanami_ally": True},
                        "experience": 300,
                        "achievements": ["Saved Nanami Kento"],
                        "next_scene": "evacuation_success"
                    }
                )
            ],
            "Shibuya Station - Emergency Exit"
        ))
        
        # Arc climax and resolution
        self.add_scene("incident_climax", StoryScene(
            "The Price of Victory",
            """As dawn breaks over Shibuya, the incident finally comes to an end. 
The barrier falls, and the surviving civilians are evacuated. But the cost 
has been enormous - the jujutsu world has been forever changed.

Gojo remains sealed in the Prison Realm. Many sorcerers have fallen, and 
the balance of power between sorcerers and curses has shifted dramatically. 
The age of Gojo Satoru's absolute deterrence is over.

However, your actions throughout the night have made a difference. The 
civilians you saved, the teammates you protected, and the bonds you 
strengthened will be crucial for the trials ahead.""",
            [
                StoryChoice(
                    "Vow to become stronger to fill the void left by Gojo's sealing",
                    {
                        "traits": {Trait.DETERMINED: 25, Trait.FOCUSED: 15},
                        "story_flags": {"power_seeker": True},
                        "experience": 500,
                        "next_scene": "arc_completion_determination"
                    }
                ),
                StoryChoice(
                    "Focus on protecting those who survived and rebuilding",
                    {
                        "traits": {Trait.PROTECTIVE: 20, Trait.COMPASSIONATE: 15},
                        "story_flags": {"protector_path": True},
                        "relationships": {"all_civilians": 50},
                        "next_scene": "arc_completion_protector"
                    }
                )
            ],
            "Shibuya District - Dawn"
        ))
        
        # Arc completion
        self.add_scene("arc_completion_determination", StoryScene(
            "A New Path Forward",
            """The Shibuya Incident has ended, but its consequences will reshape 
the entire jujutsu world. With Gojo sealed, the burden of protecting humanity 
from curses falls more heavily on the remaining sorcerers.

Your determination to grow stronger and fill the void left by Gojo's absence 
has been noted by the higher-ups in jujutsu society. You've proven yourself 
capable of making difficult decisions under extreme pressure.

The road ahead will be more dangerous than ever, but you're ready to face 
whatever challenges come next.""",
            [
                StoryChoice(
                    "Prepare for the new world without Gojo",
                    {
                        "story_flags": {"shibuya_survivor": True, "gojo_successor_path": True},
                        "next_arc": 7,
                        "next_scene": "start"
                    }
                )
            ],
            "Tokyo Jujutsu High - Emergency Meeting Room"
        ))
    
    def create_enemy(self, enemy_type: str, player_level: int) -> Enemy:
        """Create arc-specific enemies for the Shibuya Incident."""
        if enemy_type == "jogo_initial":
            enemy = Enemy("Jogo (Volcano Curse)", 350, 180, "special")
            enemy.ai_pattern = "aggressive"
            enemy.special_abilities = ["maximum_meteor", "lava_flow", "volcanic_eruption"]
            enemy.weaknesses = ["water_techniques", "cold_attacks"]
        elif enemy_type == "mahito_full_power":
            enemy = Enemy("Mahito (Full Power)", 400, 200, "special")
            enemy.ai_pattern = "cunning"
            enemy.special_abilities = ["idle_transfiguration", "body_manipulation", "polymorphic_soul_isomer"]
            enemy.weaknesses = ["soul_protection", "strong_will"]
        elif enemy_type == "mahito_tactical":
            enemy = Enemy("Mahito (Tactical Fight)", 300, 160, "special")
            enemy.ai_pattern = "defensive"
            enemy.special_abilities = ["idle_transfiguration", "body_manipulation"]
        elif enemy_type == "mahito_distracted":
            enemy = Enemy("Mahito (Distracted)", 250, 140, "special")
            enemy.ai_pattern = "aggressive"
            enemy.special_abilities = ["idle_transfiguration"]
        else:
            return super().create_enemy(enemy_type, player_level)
        
        # Special grade enemies don't scale normally - they're always dangerous
        enemy.level = max(player_level + 8, 20)
        return enemy
