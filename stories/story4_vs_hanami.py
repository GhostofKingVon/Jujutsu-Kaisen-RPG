"""
Arc 4: Vs. Hanami Arc

Covers the Kyoto Goodwill Event and battle with Hanami:
- Inter-school competition with Kyoto students
- Strengthening bonds with Tokyo classmates
- Major battle against the special grade curse Hanami
- Team coordination under extreme pressure
- Character development and technique mastery
- Introduction to high-level jujutsu politics
"""

from typing import Dict, Any
from character import Trait, Enemy
from .base_arc import BaseStoryArc, StoryChoice, StoryScene


class VsHanamiArc(BaseStoryArc):
    """Fourth arc focusing on the Kyoto event and Hanami battle."""
    
    def __init__(self):
        super().__init__("Vs. Hanami Arc", 4)
    
    def initialize_arc(self):
        """Initialize all scenes for the Hanami Arc."""
        
        # Arc starting scene
        self.add_scene("start", StoryScene(
            "The Kyoto Goodwill Event Begins",
            """The annual Kyoto Goodwill Event has arrived - a competition between 
Tokyo and Kyoto Jujutsu High schools designed to foster cooperation and measure 
the strength of each institution's students.

Principal Yaga addresses both schools: "This event serves multiple purposes. 
It strengthens bonds between our schools, provides combat experience in a 
controlled environment, and allows us to evaluate student progress."

The Kyoto students stand across from your Tokyo team. You recognize Todo 
from your previous encounter, but there are others: Mai Zenin (Maki's twin), 
Noritoshi Kamo, Momo Nishimiya, and others. The tension between the schools 
is palpable.

The first event is a team battle in a forested area with cursed spirits.""",
            [
                StoryChoice(
                    "Focus on coordination with your Tokyo teammates",
                    {
                        "traits": {Trait.FOCUSED: 15, Trait.PROTECTIVE: 10},
                        "relationships": {"yuji": 10, "megumi": 10, "nobara": 10},
                        "story_flags": {"team_coordination": True},
                        "next_scene": "tokyo_teamwork"
                    }
                ),
                StoryChoice(
                    "Try to prove yourself individually against Kyoto students",
                    {
                        "traits": {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 10},
                        "relationships": {"todo": 10},
                        "story_flags": {"individual_focus": True},
                        "next_scene": "individual_prowess"
                    }
                ),
                StoryChoice(
                    "Study Kyoto students' techniques for strategic advantage",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 5},
                        "story_flags": {"strategic_analysis": True},
                        "next_scene": "technique_analysis"
                    }
                )
            ],
            "Kyoto Jujutsu High - Competition Grounds"
        ))
        
        # Tokyo teamwork path
        self.add_scene("tokyo_teamwork", StoryScene(
            "United We Stand",
            """Your focus on teamwork pays off as you and your Tokyo classmates 
develop excellent coordination. Yuji's raw power, Megumi's versatile shikigami, 
and Nobara's precise technique create a formidable combination.

"This is how it should be," Megumi observes as your team efficiently clears 
cursed spirits. "We know each other's abilities and can trust each other."

Your coordinated approach catches the attention of both the Kyoto students 
and the observing faculty. However, Todo seems particularly interested in 
challenging your team unity.""",
            [
                StoryChoice(
                    "Accept Todo's challenge as a team",
                    {
                        "traits": {Trait.DETERMINED: 10, Trait.FOCUSED: 10},
                        "story_flags": {"team_todo_challenge": True},
                        "combat": True,
                        "enemy": "todo_team_challenge",
                        "ally": "tokyo_team",
                        "next_scene": "team_vs_todo"
                    }
                ),
                StoryChoice(
                    "Continue focusing on the competition objectives",
                    {
                        "traits": {Trait.FOCUSED: 15, Trait.ANALYTICAL: 5},
                        "story_flags": {"objective_focused": True},
                        "next_scene": "competition_progress"
                    }
                )
            ],
            "Competition Forest - Eastern Sector"
        ))
        
        # Competition interrupted
        self.add_scene("competition_progress", StoryScene(
            "An Unexpected Interruption",
            """The competition is proceeding smoothly when suddenly, an overwhelming 
cursed energy signature appears. The forest itself seems to react, with plants 
and trees becoming unnaturally aggressive.

"This isn't part of the exercise," Megumi realizes grimly as a massive tree 
root bursts from the ground near Nobara.

Principal Yaga's voice echoes across the grounds: "All students, cease 
competition activities immediately. We have an unscheduled special grade 
curse manifestation. Evacuate to designated safe zones."

But as you try to evacuate, you realize the curse - Hanami, the forest-themed 
special grade - has specifically targeted the students.""",
            [
                StoryChoice(
                    "Rally both Tokyo and Kyoto students to work together",
                    {
                        "traits": {Trait.FOCUSED: 20, Trait.PROTECTIVE: 15},
                        "relationships": {"all_students": 15},
                        "story_flags": {"united_schools": True},
                        "next_scene": "schools_unite"
                    }
                ),
                StoryChoice(
                    "Focus on protecting your Tokyo teammates",
                    {
                        "traits": {Trait.PROTECTIVE: 20, Trait.CAUTIOUS: 10},
                        "relationships": {"yuji": 15, "megumi": 15, "nobara": 15},
                        "story_flags": {"tokyo_protection": True},
                        "next_scene": "tokyo_protection"
                    }
                ),
                StoryChoice(
                    "Take the initiative to engage Hanami directly",
                    {
                        "traits": {Trait.AGGRESSIVE: 15, Trait.RECKLESS: 10},
                        "story_flags": {"hanami_engagement": True},
                        "combat": True,
                        "enemy": "hanami_initial",
                        "next_scene": "early_hanami_fight"
                    }
                )
            ],
            "Competition Forest - Central Area"
        ))
        
        # Schools unite against Hanami
        self.add_scene("schools_unite", StoryScene(
            "Rivals Become Allies",
            """Your call for unity resonates with both schools. Todo steps forward 
first, grinning widely. "Now this is more interesting than any competition!"

Mai Zenin, despite her usual cynicism, nods grimly. "A special grade curse 
doesn't care which school we're from."

Even Noritoshi Kamo sets aside his pride: "Our duty as jujutsu sorcerers 
comes before school rivalry."

With both schools working together, you form a coordinated response to Hanami's 
threat. The curse seems surprised by the unified resistance, its ancient eyes 
narrowing as it reassesses the situation.""",
            [
                StoryChoice(
                    "Coordinate a multi-pronged attack strategy",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 15},
                        "relationships": {"all_students": 20},
                        "story_flags": {"master_strategist": True},
                        "next_scene": "coordinated_assault"
                    }
                ),
                StoryChoice(
                    "Focus on defense while looking for Hanami's weakness",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 15},
                        "story_flags": {"defensive_analysis": True},
                        "next_scene": "defensive_strategy"
                    }
                )
            ],
            "Competition Forest - Clearing"
        ))
        
        # Coordinated assault on Hanami
        self.add_scene("coordinated_assault", StoryScene(
            "The Art of War",
            """Your strategic coordination brings out the best in everyone. Megumi's 
shikigami provide reconnaissance and crowd control, while Todo uses his Boogie 
Woogie to constantly reposition attackers for optimal strikes.

Nobara and Mai coordinate their projectile attacks, and Yuji's raw power is 
channeled through precise timing orchestrated by your tactical commands.

"Impressive," Hanami speaks, its voice like rustling leaves. "Young sorcerers 
working in such harmony. It reminds me of how nature itself operates - each 
part serving the whole."

Your coordination is dealing significant damage to Hanami, but the special 
grade curse is far from defeated.""",
            [
                StoryChoice(
                    "Press the advantage with an all-out assault",
                    {
                        "traits": {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 15},
                        "story_flags": {"all_out_hanami": True},
                        "combat": True,
                        "enemy": "hanami_pressured",
                        "ally": "united_students",
                        "next_scene": "hanami_major_battle"
                    }
                ),
                StoryChoice(
                    "Maintain defensive coordination while seeking a decisive opening",
                    {
                        "traits": {Trait.ANALYTICAL: 20, Trait.FOCUSED: 10},
                        "story_flags": {"patient_strategy": True},
                        "next_scene": "tactical_patience"
                    }
                )
            ],
            "Competition Forest - Battle Zone"
        ))
        
        # Hanami's desperation and flower field domain
        self.add_scene("hanami_major_battle", StoryScene(
            "Domain of the Forest Spirit",
            """Hanami, pressed by your coordinated assault, decides to escalate. 
"You force my hand, young ones. Behold the beauty and terror of nature's domain."

The air fills with cursed energy as Hanami begins expanding its domain. Flower 
petals swirl around the battlefield, each one carrying deadly cursed energy 
that can drain life force from anyone who touches them.

"This is bad," Todo realizes. "In a domain expansion, the curse's technique 
is guaranteed to hit. We need to either escape or..."

"Or find a way to counter it," you finish, your mind racing through possibilities.""",
            [
                StoryChoice(
                    "Try to disrupt the domain expansion through coordinated attacks",
                    {
                        "traits": {Trait.ANALYTICAL: 25, Trait.RECKLESS: 5},
                        "story_flags": {"domain_disruption": True},
                        "next_scene": "domain_counter"
                    }
                ),
                StoryChoice(
                    "Focus on protecting everyone while enduring the domain",
                    {
                        "traits": {Trait.PROTECTIVE: 25, Trait.DETERMINED: 15},
                        "story_flags": {"protective_endurance": True},
                        "next_scene": "domain_survival"
                    }
                ),
                StoryChoice(
                    "Look for an escape route while the domain is forming",
                    {
                        "traits": {Trait.CAUTIOUS: 20, Trait.ANALYTICAL: 10},
                        "story_flags": {"tactical_retreat": True},
                        "next_scene": "domain_escape"
                    }
                )
            ],
            "Competition Forest - Hanami's Domain"
        ))
        
        # Successful domain counter
        self.add_scene("domain_counter", StoryScene(
            "Breaking the Unbreakable",
            """Your quick thinking leads to an unprecedented feat - disrupting a 
domain expansion through coordinated student efforts. By having everyone 
attack the same structural point of the domain simultaneously, you create 
a resonance that shatters Hanami's technique.

"Impossible," Hanami gasps as its domain crumbles. "No group of students 
should be capable of such coordination and power."

The domain's collapse leaves Hanami severely weakened and vulnerable. Todo 
grins widely. "That was the most beautiful thing I've ever seen! True 
cooperation between rival schools!"

Your success has created an opening that could end the battle.""",
            [
                StoryChoice(
                    "Lead the final assault on the weakened Hanami",
                    {
                        "traits": {Trait.DETERMINED: 20, Trait.FOCUSED: 15},
                        "story_flags": {"domain_breaker": True},
                        "achievements": ["Domain Disruptor"],
                        "combat": True,
                        "enemy": "hanami_weakened",
                        "ally": "united_students",
                        "experience": 400,
                        "next_scene": "hanami_victory"
                    }
                )
            ],
            "Competition Forest - Shattered Domain"
        ))
        
        # Victory over Hanami
        self.add_scene("hanami_victory", StoryScene(
            "The Forest Spirit Falls",
            """With Hanami weakened from the domain disruption, your coordinated 
final assault proves decisive. The special grade curse, overwhelmed by the 
united power of both schools, finally falls.

"You have... taught me something," Hanami says with its final breath. "Perhaps... 
humans and nature need not be enemies. Your cooperation... it reminds me of 
the harmony I sought to protect."

The forest returns to normal as Hanami's cursed energy dissipates. Both 
schools stand together, former rivals now united by shared triumph.""",
            [
                StoryChoice(
                    "Propose continued cooperation between the schools",
                    {
                        "traits": {Trait.COMPASSIONATE: 20, Trait.FOCUSED: 15},
                        "relationships": {"all_students": 30, "principals": 20},
                        "story_flags": {"school_alliance": True},
                        "achievements": ["Unity Bringer"],
                        "next_scene": "alliance_formation"
                    }
                ),
                StoryChoice(
                    "Focus on the lessons learned from the battle",
                    {
                        "traits": {Trait.ANALYTICAL: 15, Trait.FOCUSED: 15},
                        "story_flags": {"tactical_lessons": True},
                        "experience": 200,
                        "next_scene": "battle_analysis"
                    }
                )
            ],
            "Competition Forest - Aftermath"
        ))
        
        # Arc completion
        self.add_scene("alliance_formation", StoryScene(
            "A New Era of Cooperation",
            """Your proposal for continued cooperation between Tokyo and Kyoto 
Jujutsu High is met with enthusiastic support from students and cautious 
approval from faculty.

"The threat of special grade curses is real and growing," Principal Yaga 
observes. "Perhaps it's time our schools worked together more closely."

Todo claps you on the back. "You've shown true strength today - not just 
in power, but in bringing people together. That's the mark of a great leader."

The Goodwill Event has ended with an outcome no one expected, but one that 
may prove crucial for the challenges ahead.""",
            [
                StoryChoice(
                    "Look forward to future cooperation and challenges",
                    {
                        "story_flags": {"hanami_defeated": True, "schools_allied": True},
                        "relationships": {"all_students": 25},
                        "experience": 300,
                        "next_arc": 5,
                        "next_scene": "start"
                    }
                )
            ],
            "Kyoto Jujutsu High - Main Hall"
        ))
    
    def create_enemy(self, enemy_type: str, player_level: int) -> Enemy:
        """Create arc-specific enemies."""
        if enemy_type == "todo_team_challenge":
            enemy = Enemy("Aoi Todo (Team Challenge)", 200, 100, "hard")
            enemy.ai_pattern = "intelligent"
            enemy.special_abilities = ["boogie_woogie", "black_flash"]
        elif enemy_type == "hanami_initial":
            enemy = Enemy("Hanami (Forest Curse)", 300, 150, "special")
            enemy.ai_pattern = "defensive"
            enemy.special_abilities = ["plant_manipulation", "wooden_ball"]
        elif enemy_type == "hanami_pressured":
            enemy = Enemy("Hanami (Under Pressure)", 350, 180, "special")
            enemy.ai_pattern = "aggressive"
            enemy.special_abilities = ["plant_manipulation", "wooden_ball", "flower_field"]
        elif enemy_type == "hanami_weakened":
            enemy = Enemy("Hanami (Domain Shattered)", 200, 100, "special")
            enemy.ai_pattern = "desperate"
            enemy.special_abilities = ["plant_manipulation"]
        else:
            return super().create_enemy(enemy_type, player_level)
        
        # Scale appropriately for arc difficulty
        level_modifier = max(1, player_level)
        enemy.level = level_modifier + 3
        return enemy