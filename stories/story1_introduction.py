"""
Arc 1: Introduction Arc

Covers the beginning of the story at Tokyo Jujutsu High, including:
- Character introduction and first mission
- Meeting main characters (Yuji, Megumi, Nobara)
- Basic training and understanding cursed energy
- First real combat experiences
"""

from typing import Dict, Any
from character import Trait, Enemy
from .base_arc import BaseStoryArc, StoryChoice, StoryScene


class IntroductionArc(BaseStoryArc):
    """First arc introducing the player to Tokyo Jujutsu High and main characters."""
    
    def __init__(self):
        super().__init__("Introduction Arc", 1)
    
    def initialize_arc(self):
        """Initialize all scenes for the Introduction Arc."""
        
        # Starting scene - arrival at Tokyo Jujutsu High
        intro_choices = [
            StoryChoice(
                "Help the injured student immediately",
                {
                    "traits": {Trait.COMPASSIONATE: 10, Trait.PROTECTIVE: 5},
                    "next_scene": "first_mission_compassionate",
                    "relationships": {"yuji": 10},
                    "story_flags": {"helped_student": True}
                }
            ),
            StoryChoice(
                "Assess the situation carefully first",
                {
                    "traits": {Trait.ANALYTICAL: 10, Trait.CAUTIOUS: 5},
                    "next_scene": "first_mission_analytical",
                    "relationships": {"megumi": 10},
                    "story_flags": {"assessed_situation": True}
                }
            ),
            StoryChoice(
                "Charge in to fight the curse immediately",
                {
                    "traits": {Trait.AGGRESSIVE: 10, Trait.RECKLESS: 5},
                    "next_scene": "first_mission_aggressive",
                    "relationships": {"nobara": 10},
                    "story_flags": {"fought_immediately": True}
                }
            )
        ]
        
        self.add_scene("start", StoryScene(
            "Arrival at Tokyo Jujutsu High",
            """You arrive at Tokyo Jujutsu High as a new first-year student. The imposing 
traditional buildings are surrounded by powerful barriers, and you can feel the cursed 
energy in the air. As you walk through the courtyard, you notice a commotion ahead.

A fellow student has been cornered by a Grade 3 cursed spirit near the training grounds. 
The curse spirit writhes with malevolent energy, and the student looks terrified and injured.

What do you do?""",
            intro_choices,
            "Tokyo Jujutsu High - Courtyard"
        ))
        
        # Compassionate path
        self.add_scene("first_mission_compassionate", StoryScene(
            "The Rescuer's Path",
            """You rush to help the injured student without hesitation. Your quick action 
surprises the cursed spirit, giving you the advantage. As you engage the curse, 
Yuji Itadori appears, impressed by your immediate response to help others.

"That was brave!" Yuji says with a grin. "You remind me of myself when I first got here."

The curse spirit snarls and prepares to attack both of you.""",
            [
                StoryChoice(
                    "Fight alongside Yuji",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse",
                        "ally": "yuji",
                        "traits": {Trait.DETERMINED: 5},
                        "next_scene": "post_first_battle_compassionate"
                    }
                ),
                StoryChoice(
                    "Protect the injured student while Yuji fights",
                    {
                        "traits": {Trait.PROTECTIVE: 10},
                        "relationships": {"yuji": 5, "injured_student": 15},
                        "next_scene": "protective_outcome"
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        ))
        
        # Analytical path
        self.add_scene("first_mission_analytical", StoryScene(
            "The Strategist's Path",
            """You carefully observe the cursed spirit, noting its movement patterns and energy 
signature. Your analytical approach catches the attention of Megumi Fushiguro, who nods 
approvingly from nearby.

"Smart. Understanding your enemy before acting is crucial," Megumi says quietly. 
"That curse has a weakness on its left side."

Your careful observation reveals the optimal strategy for defeating this spirit.""",
            [
                StoryChoice(
                    "Use Megumi's advice to exploit the weakness",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse_weakened",
                        "traits": {Trait.FOCUSED: 10},
                        "relationships": {"megumi": 10},
                        "next_scene": "strategic_victory"
                    }
                ),
                StoryChoice(
                    "Share your own analysis with Megumi",
                    {
                        "traits": {Trait.ANALYTICAL: 5, Trait.FOCUSED: 5},
                        "relationships": {"megumi": 15},
                        "story_flags": {"impressed_megumi": True},
                        "next_scene": "analytical_bond"
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        ))
        
        # Aggressive path
        self.add_scene("first_mission_aggressive", StoryScene(
            "The Warrior's Path",
            """You charge directly at the cursed spirit with fierce determination. Your bold 
approach catches everyone off guard, including Nobara Kugisaki who was approaching 
from the other side.

"Finally, someone who doesn't overthink everything!" Nobara grins, readying her hammer 
and nails. "Let's crush this thing!"

The curse spirit, startled by your aggressive approach, becomes more dangerous but 
also more reckless.""",
            [
                StoryChoice(
                    "Coordinate with Nobara for a combined assault",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse_enraged",
                        "ally": "nobara",
                        "traits": {Trait.AGGRESSIVE: 5},
                        "relationships": {"nobara": 15},
                        "next_scene": "aggressive_victory"
                    }
                ),
                StoryChoice(
                    "Go all-out on your own",
                    {
                        "combat": True,
                        "enemy": "grade_3_curse_enraged",
                        "traits": {Trait.RECKLESS: 10, Trait.DETERMINED: 5},
                        "next_scene": "solo_battle"
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        ))
        
        # Post-battle outcomes
        self.add_scene("post_first_battle_compassionate", StoryScene(
            "Victory with Yuji",
            """Together with Yuji, you defeat the cursed spirit. The injured student is safe, 
and Yuji looks at you with newfound respect.

"You've got real potential," Yuji says. "And more importantly, you've got the right heart 
for this job. Protecting people is what matters most."

Gojo-sensei appears, having watched the entire encounter.""",
            [
                StoryChoice(
                    "Ask Gojo about your potential",
                    {
                        "traits": {Trait.FOCUSED: 5},
                        "relationships": {"gojo": 10},
                        "next_scene": "gojo_evaluation"
                    }
                ),
                StoryChoice(
                    "Check on the injured student first",
                    {
                        "traits": {Trait.COMPASSIONATE: 5},
                        "relationships": {"injured_student": 20},
                        "story_flags": {"student_grateful": True},
                        "next_scene": "caring_reputation"
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        ))
        
        # Gojo evaluation scene
        self.add_scene("gojo_evaluation", StoryScene(
            "Gojo's Assessment",
            """Gojo removes his blindfold, revealing his striking blue eyes. He studies you 
intently for a moment before breaking into his characteristic grin.

"Interesting," he says. "Your cursed energy flow is unique. You have natural talent, 
but more importantly, you understand that strength without purpose is meaningless."

He gestures toward the main building. "Come on, let's get you properly introduced to 
the world of jujutsu sorcery. You're going to fit in just fine here.""",
            [
                StoryChoice(
                    "Express excitement about learning",
                    {
                        "traits": {Trait.DETERMINED: 10},
                        "relationships": {"gojo": 15},
                        "story_flags": {"eager_student": True},
                        "next_scene": "training_introduction"
                    }
                ),
                StoryChoice(
                    "Ask about the responsibilities of being a sorcerer",
                    {
                        "traits": {Trait.ANALYTICAL: 5, Trait.CAUTIOUS: 5},
                        "relationships": {"gojo": 10},
                        "story_flags": {"thoughtful_student": True},
                        "next_scene": "responsibility_discussion"
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Grounds"
        ))
        
        # Training introduction
        self.add_scene("training_introduction", StoryScene(
            "Your First Training Session",
            """Gojo leads you to the main training facility where you'll learn the fundamentals 
of cursed energy manipulation. The other first-years - Yuji, Megumi, and Nobara - are 
already there, practicing their techniques.

"Today, we'll start with the basics," Gojo announces. "Understanding and controlling 
your cursed energy is the foundation of everything else. Everyone has a different 
approach to this."

You notice each student has their own unique training style and focus.""",
            [
                StoryChoice(
                    "Focus on defensive techniques first",
                    {
                        "traits": {Trait.CAUTIOUS: 10, Trait.PROTECTIVE: 5},
                        "techniques": ["basic_barrier"],
                        "experience": 50,
                        "next_scene": "defensive_training"
                    }
                ),
                StoryChoice(
                    "Work on offensive cursed energy attacks",
                    {
                        "traits": {Trait.AGGRESSIVE: 10, Trait.DETERMINED: 5},
                        "techniques": ["cursed_energy_blast"],
                        "experience": 50,
                        "next_scene": "offensive_training"
                    }
                ),
                StoryChoice(
                    "Study the theory behind cursed energy first",
                    {
                        "traits": {Trait.ANALYTICAL: 10, Trait.FOCUSED: 5},
                        "experience": 75,
                        "story_flags": {"theory_focused": True},
                        "next_scene": "theoretical_foundation"
                    }
                )
            ],
            "Tokyo Jujutsu High - Training Facility"
        ))
        
        # End of arc transition
        self.add_scene("arc_completion", StoryScene(
            "Ready for Greater Challenges",
            """After several weeks of training and bonding with your classmates, you've proven 
yourself as a capable jujutsu sorcerer. Gojo gathers the first-years for an important 
announcement.

"You've all shown remarkable progress," he says. "It's time for your first real mission 
outside the school. There have been reports of unusual cursed spirit activity that 
requires investigation."

The Introduction Arc has ended. Your choices have shaped your character and relationships, 
setting the foundation for the challenges ahead.""",
            [
                StoryChoice(
                    "Express readiness for the mission",
                    {
                        "traits": {Trait.DETERMINED: 5},
                        "story_flags": {"ready_for_mission": True},
                        "next_arc": 2,
                        "next_scene": "start"
                    }
                )
            ],
            "Tokyo Jujutsu High - Meeting Room"
        ))
    
    def create_enemy(self, enemy_type: str, player_level: int) -> Enemy:
        """Create arc-specific enemies."""
        if enemy_type == "grade_3_curse_weakened":
            enemy = Enemy("Weakened Grade 3 Cursed Spirit", 60, 30)
            enemy.ai_pattern = "defensive"
        elif enemy_type == "grade_3_curse_enraged":
            enemy = Enemy("Enraged Grade 3 Cursed Spirit", 100, 50)
            enemy.ai_pattern = "aggressive"
        else:
            return super().create_enemy(enemy_type, player_level)
        
        # Scale to player level
        level_modifier = max(1, player_level - 1)
        enemy.max_hp += level_modifier * 10
        enemy.hp = enemy.max_hp
        enemy.max_cursed_energy += level_modifier * 5
        enemy.cursed_energy = enemy.max_cursed_energy
        enemy.level = max(1, player_level)
        
        return enemy