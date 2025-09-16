"""
Story Arc 1: Prologue & Introduction

This module contains the opening story content including:
- Player's arrival at Tokyo Jujutsu High
- First encounter with cursed spirits
- Initial character interactions and trait development
"""

from .base import StoryChoice, StoryScene
from character import Trait


def get_story1_scenes():
    """
    Returns all story scenes for Arc 1: Prologue & Introduction.
    
    This arc establishes the player's character through their first choices
    and interactions at Tokyo Jujutsu High.
    """
    scenes = {}
    
    # Introduction Scene - Player's first major choice
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
    
    scenes["intro"] = StoryScene(
        "Arrival at Tokyo Jujutsu High",
        """You arrive at Tokyo Jujutsu High as a new first-year student. The imposing 
traditional buildings are surrounded by powerful barriers, and you can feel the cursed 
energy in the air. As you walk through the courtyard, you notice a commotion ahead.

A fellow student has been cornered by a Grade 3 cursed spirit near the training grounds. 
The curse spirit writhes with malevolent energy, and the student looks terrified and injured.

What do you do?""",
        intro_choices,
        "Tokyo Jujutsu High - Courtyard"
    )
    
    return scenes