# Story Arc Development Guide

This guide explains how to create and expand story arcs in the Jujutsu Kaisen RPG.

## Architecture Overview

The game uses a modular story arc system where each major story arc is implemented as a separate Python file. This provides:

- **Better Organization**: Each arc is self-contained and manageable
- **Scalability**: Easy to add new arcs without modifying existing code
- **Maintainability**: Changes to one arc don't affect others
- **Replayability**: Different paths and outcomes within each arc

## File Structure

```
stories/
├── __init__.py                    # Registry of all story arcs
├── base_arc.py                    # Base classes and common functionality
├── story1_introduction.py         # Arc 1: Introduction Arc
├── story2_mahito_junpei.py        # Arc 2: Vs. Mahito/Junpei Arc
├── story3_cursed_womb.py          # Arc 3: Cursed Womb Arc
├── story4_vs_hanami.py            # Arc 4: Vs. Hanami Arc (placeholder)
├── story5_origin_obedience.py     # Arc 5: Origin of Obedience Arc (placeholder)
├── story6_shibuya_incident.py     # Arc 6: Shibuya Incident Arc
├── story7_itadori_past.py         # Arc 7: Itadori's Past & Prison Realm Arc (placeholder)
├── story8_perfect_preparation.py  # Arc 8: Perfect Preparation Arc (placeholder)
├── story9_culling_game.py         # Arc 9: Culling Game Arc (placeholder)
└── story10_final_arc.py           # Arc 10: Final Arc (placeholder)
```

## Creating a New Story Arc

### Step 1: Create the Arc Class

```python
from typing import Dict, Any
from character import Trait, Enemy
from .base_arc import BaseStoryArc, StoryChoice, StoryScene

class YourNewArc(BaseStoryArc):
    """Description of your arc."""
    
    def __init__(self):
        super().__init__("Your Arc Name", arc_number)
    
    def initialize_arc(self):
        """Initialize all scenes for this arc."""
        # Add scenes here
        pass
```

### Step 2: Add Scenes with Choices

```python
def initialize_arc(self):
    # Starting scene
    self.add_scene("start", StoryScene(
        "Scene Title",
        """Scene description with engaging narrative.
        
        This supports multi-line descriptions that set the scene
        and provide context for player choices.""",
        [
            StoryChoice(
                "Choice text that player sees",
                {
                    "traits": {Trait.COMPASSIONATE: 10},  # Character development
                    "relationships": {"npc_name": 15},    # NPC relationship changes
                    "story_flags": {"flag_name": True},   # Story progression flags
                    "next_scene": "next_scene_id",       # Scene progression
                    "experience": 100,                   # XP reward
                    "combat": True,                      # Trigger combat
                    "enemy": "enemy_type",               # Enemy to fight
                    "techniques": ["new_technique"],     # Unlock techniques
                    "achievements": ["Achievement Name"], # Special achievements
                    "next_arc": 2,                       # Progress to next arc
                    "cursed_energy_cost": 30            # CE cost for actions
                }
            )
        ],
        "Location Name"
    ))
```

### Step 3: Register the Arc

Add your new arc to `stories/__init__.py`:

```python
from .your_new_file import YourNewArc

STORY_ARCS = {
    # existing arcs...
    11: YourNewArc,  # Add your arc
}
```

## Story Choice Consequences

### Character Development
- `traits`: Modify character personality traits
- `experience`: Grant experience points
- `techniques`: Unlock new cursed techniques
- `cursed_energy_cost`: Consume cursed energy for actions

### Narrative Progression
- `next_scene`: Move to another scene in the same arc
- `next_arc`: Progress to a different arc
- `story_flags`: Set flags for conditional content
- `achievements`: Grant special recognition

### Relationships
- `relationships`: Modify NPC relationship values
- Use NPC names as keys, values as relationship changes

### Combat
- `combat`: Set to `True` to trigger battle
- `enemy`: Specify enemy type for the battle
- `ally`: Add an NPC ally for the fight

## Advanced Features

### Conditional Scenes

Use requirements to gate content:

```python
scene = StoryScene(
    "Advanced Scene",
    "This scene requires specific conditions.",
    choices,
    requirements={
        "min_level": 10,
        "required_traits": [Trait.FOCUSED],
        "required_flags": ["specific_story_flag"]
    }
)
```

### Branching Narratives

Create multiple paths through an arc:

```python
# Path A
self.add_scene("path_a_start", ...)
self.add_scene("path_a_middle", ...)
self.add_scene("path_a_end", ...)

# Path B  
self.add_scene("path_b_start", ...)
self.add_scene("path_b_middle", ...)
self.add_scene("path_b_end", ...)

# Convergence point
self.add_scene("paths_converge", ...)
```

### Custom Enemies

Override the `create_enemy` method for arc-specific enemies:

```python
def create_enemy(self, enemy_type: str, player_level: int) -> Enemy:
    if enemy_type == "special_arc_boss":
        enemy = Enemy("Arc Boss Name", 500, 250, "special")
        enemy.ai_pattern = "intelligent"
        enemy.special_abilities = ["unique_ability"]
        enemy.max_phases = 3
        return enemy
    else:
        return super().create_enemy(enemy_type, player_level)
```

## Best Practices

### Narrative Structure
1. **Opening Hook**: Start with an engaging situation
2. **Rising Action**: Build tension through choices and consequences
3. **Climax**: Major confrontation or decision point
4. **Resolution**: Conclude with meaningful consequences

### Character Development
- Use trait modifications to reflect player choices
- Build relationships gradually through multiple interactions
- Make choices feel meaningful with lasting consequences

### Pacing
- Mix action, dialogue, and exploration scenes
- Use shorter scenes for intense moments
- Longer scenes for character development

### Player Agency
- Provide meaningful choices with different outcomes
- Avoid "fake" choices where all options lead to the same result
- Let player personality shape the narrative

## Testing Your Arc

1. **Syntax Check**: Ensure Python syntax is correct
2. **Flow Testing**: Verify all scenes connect properly
3. **Balance Testing**: Check combat difficulty and rewards
4. **Narrative Testing**: Ensure story makes sense and is engaging

```python
# Test your arc
from stories.your_new_file import YourNewArc
arc = YourNewArc()
print(f"Arc created: {arc.arc_name}")
print(f"Scenes: {list(arc.scenes.keys())}")
```

## Integration with Main Game

The story manager automatically loads and manages all registered arcs. Your arc will be:

- Automatically included in the game progression
- Save/load compatible
- Integrated with the combat and character systems
- Available for replay and exploration

## Examples

See the fully implemented arcs for examples:
- `story1_introduction.py`: Basic arc structure and character introduction
- `story2_mahito_junpei.py`: Branching narrative with major consequences
- `story3_cursed_womb.py`: Combat-focused arc with strategic choices
- `story6_shibuya_incident.py`: Complex arc with multiple storylines

## Troubleshooting

### Common Issues
1. **Import Errors**: Ensure all imports are correct in `__init__.py`
2. **Scene Loops**: Verify all scenes have valid exit conditions
3. **Missing Requirements**: Check that all referenced flags/traits exist
4. **Combat Errors**: Ensure enemy types are properly defined

### Debugging Tips
- Use print statements to trace scene progression
- Test individual scenes before connecting them
- Verify all choice consequences are properly formatted
- Check that arc numbers don't conflict with existing arcs