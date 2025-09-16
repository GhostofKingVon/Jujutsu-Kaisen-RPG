"""
Story Arc 3: Kyoto School Arc

This module contains the encounter with Todo and other Kyoto School students:
- Todo's famous question and character assessment
- Different response options that affect relationships
- Introduction to inter-school dynamics
"""

from .base import StoryChoice, StoryScene
from character import Trait


def get_story3_scenes():
    """
    Returns all story scenes for Arc 3: Kyoto School Arc.
    
    This arc introduces the rivalry and interactions with Kyoto Jujutsu High,
    particularly the memorable encounter with Aoi Todo.
    """
    scenes = {}
    
    # Meeting Todo Scene - The famous question
    scenes["meet_todo"] = StoryScene(
        "Encounter with Todo",
        """During a joint training exercise with Kyoto School, you encounter the imposing 
figure of Aoi Todo. His massive frame and confident stance make it clear he's evaluating 
you as a potential sparring partner.

"What's your type of woman?" Todo asks with complete seriousness.

The question catches you off guard, but you realize this might be Todo's way of 
understanding your character.""",
        [
            StoryChoice(
                "Give a thoughtful, honest answer",
                {
                    "traits": {Trait.COMPASSIONATE: 5},
                    "relationships": {"todo": 20},
                    "story_flags": {"todo_approves": True},
                    "next_scene": "todo_training"
                }
            ),
            StoryChoice(
                "Deflect with humor",
                {
                    "traits": {Trait.FOCUSED: 5},
                    "relationships": {"todo": 5},
                    "next_scene": "todo_neutral"
                }
            ),
            StoryChoice(
                "Challenge him to a fight instead",
                {
                    "traits": {Trait.AGGRESSIVE: 10},
                    "combat": True,
                    "enemy": "todo_sparring",
                    "next_scene": "todo_fight"
                }
            )
        ],
        "Kyoto Jujutsu High - Training Grounds"
    )
    
    return scenes