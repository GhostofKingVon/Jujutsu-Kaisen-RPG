# Story Module Documentation

This document provides guidelines for working with the modular story system in the Jujutsu Kaisen RPG.

## Overview

The story system has been refactored into separate modules for better organization and maintainability:

```
story/
├── __init__.py          # Story module exports
├── base.py             # Shared story classes (StoryChoice, StoryScene)
├── story_manager.py    # Main story management logic
├── story1.py           # Arc 1: Prologue & Introduction
├── story2.py           # Arc 2: First Mission Arc
├── story3.py           # Arc 3: Kyoto School Arc
└── story4.py           # Arc 4: Shibuya Incident Arc
```

## Story Arc Structure

Each story arc module follows a consistent pattern:

### File Structure
- **Module docstring**: Describes the arc's purpose and content
- **get_storyX_scenes()**: Function that returns all scenes for the arc
- **Scene definitions**: Individual StoryScene objects with choices

### Example Arc Module
```python
"""
Story Arc X: Arc Name

Description of what this arc contains and its role in the overall story.
"""

from .base import StoryChoice, StoryScene
from character import Trait

def get_storyX_scenes():
    """
    Returns all story scenes for Arc X.
    
    Detailed description of the arc's content and purpose.
    """
    scenes = {}
    
    scenes["scene_id"] = StoryScene(
        "Scene Title",
        "Scene description...",
        [
            StoryChoice("Choice text", {"consequences": "dict"}),
            # More choices...
        ],
        "Location Name"
    )
    
    return scenes
```

## Adding New Story Arcs

To add a new story arc:

1. **Create the arc module** (e.g., `story5.py`)
2. **Follow the naming convention**: `get_story5_scenes()`
3. **Import in story_manager.py**:
   ```python
   from . import story1, story2, story3, story4, story5
   ```
4. **Load scenes in _initialize_story()**:
   ```python
   self.story_scenes.update(story5.get_story5_scenes())
   ```

## Modifying Existing Arcs

To modify an existing story arc:

1. **Edit the appropriate storyX.py file**
2. **Modify scenes, choices, or consequences as needed**
3. **Update the arc's get_storyX_scenes() function**
4. **Test the changes by running the game**

## Story Choice Consequences

StoryChoice consequences can include:

- **traits**: `{Trait.COMPASSIONATE: 10}` - Modify character traits
- **relationships**: `{"yuji": 15}` - Change NPC relationships
- **story_flags**: `{"helped_student": True}` - Set story progression flags
- **next_scene**: `"scene_id"` - Navigate to the next scene
- **combat**: `True` - Trigger combat encounter
- **enemy**: `"enemy_type"` - Specify enemy for combat
- **ally**: `"npc_name"` - Combat ally
- **experience**: `50` - Grant experience points
- **requirements**: `{"min_level": 5}` - Prerequisites for the choice

## Best Practices

1. **Keep arcs focused**: Each arc should cover a specific narrative segment
2. **Use descriptive scene IDs**: Make scene names self-explanatory
3. **Document major story branches**: Add comments for complex choice trees
4. **Test story flow**: Ensure scene transitions work correctly
5. **Maintain consistency**: Follow established patterns and conventions

## Testing Changes

After modifying story content:

```bash
# Test story initialization
python -c "from story import StoryManager; s = StoryManager(); print('Success!')"

# Test scene count
python -c "from story import StoryManager; s = StoryManager(); print(f'Scenes: {len(s.story_scenes)}')"

# Test specific scenes
python -c "from story import StoryManager; s = StoryManager(); print(list(s.story_scenes.keys()))"
```