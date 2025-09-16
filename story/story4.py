"""
Story Arc 4: Shibuya Incident Arc

This module contains the preparation and setup for the major Shibuya Incident:
- Pre-incident briefing and tension building
- Strategic role assignment choices
- Character positioning for the major arc
"""

from .base import StoryChoice, StoryScene
from character import Trait


def get_story4_scenes():
    """
    Returns all story scenes for Arc 4: Shibuya Incident Arc.
    
    This arc sets up one of the most significant events in the Jujutsu Kaisen
    storyline, allowing players to choose their approach to the crisis.
    """
    scenes = {}
    
    # Shibuya Incident preparation
    scenes["shibuya_preparation"] = StoryScene(
        "Before the Shibuya Incident",
        """Halloween night approaches, and intelligence suggests a major cursed spirit 
incident will occur in Shibuya. You've grown stronger, but this will be your biggest 
challenge yet. The atmosphere is tense as everyone prepares.

Gojo-sensei is nowhere to be found, and there's a sense of unease among the students 
and faculty.""",
        [
            StoryChoice(
                "Volunteer for the front-line assault team",
                {
                    "traits": {Trait.DETERMINED: 10, Trait.PROTECTIVE: 5},
                    "story_flags": {"frontline_volunteer": True},
                    "next_scene": "shibuya_frontline"
                }
            ),
            StoryChoice(
                "Request to support rescue operations",
                {
                    "traits": {Trait.COMPASSIONATE: 10, Trait.ANALYTICAL: 5},
                    "story_flags": {"rescue_volunteer": True},
                    "next_scene": "shibuya_rescue"
                }
            ),
            StoryChoice(
                "Suggest gathering more intelligence first",
                {
                    "traits": {Trait.CAUTIOUS: 10, Trait.ANALYTICAL: 5},
                    "story_flags": {"intelligence_focused": True},
                    "next_scene": "shibuya_intel"
                }
            )
        ],
        "Tokyo Jujutsu High - Meeting Room"
    )
    
    return scenes