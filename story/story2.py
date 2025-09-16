"""
Story Arc 2: First Mission Arc

This module contains the branching paths from the player's first major choice:
- Compassionate path (helping the injured student with Yuji)
- Analytical path (strategic approach with Megumi)
- Aggressive path (direct combat with Nobara)

Each path develops different character traits and relationships.
"""

from .base import StoryChoice, StoryScene
from character import Trait


def get_story2_scenes():
    """
    Returns all story scenes for Arc 2: First Mission Arc.
    
    This arc contains the three branching paths based on the player's
    initial choice at Tokyo Jujutsu High.
    """
    scenes = {}
    
    # Compassionate Path - Working with Yuji
    scenes["first_mission_compassionate"] = StoryScene(
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
                    "next_scene": "post_first_battle"
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
    )
    
    # Analytical Path - Working with Megumi
    scenes["first_mission_analytical"] = StoryScene(
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
    )
    
    # Aggressive Path - Working with Nobara
    scenes["first_mission_aggressive"] = StoryScene(
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
    )
    
    return scenes