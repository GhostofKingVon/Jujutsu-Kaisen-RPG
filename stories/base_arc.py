"""
Base Story Arc System

Provides the foundation for all story arcs with consistent structure
for scenes, choices, branching, and progression.
"""

from typing import Dict, List, Any, Optional
from character import Trait, Enemy


class StoryChoice:
    """Represents a story choice with its consequences."""
    
    def __init__(self, text: str, consequences: Dict[str, Any]):
        self.text = text
        self.consequences = consequences  # Effects on traits, relationships, story flags


class StoryScene:
    """Represents a story scene with description and choices."""
    
    def __init__(self, title: str, description: str, choices: List[StoryChoice], 
                 location: str = None, requirements: Dict = None):
        self.title = title
        self.description = description
        self.choices = choices
        self.location = location or "Unknown Location"
        self.requirements = requirements or {}  # Requirements to access this scene


class BaseStoryArc:
    """Base class for all story arcs."""
    
    def __init__(self, arc_name: str, arc_number: int):
        self.arc_name = arc_name
        self.arc_number = arc_number
        self.scenes = {}
        self.starting_scene = "start"
        self.achievements = []
        self.initialize_arc()
    
    def initialize_arc(self):
        """Initialize all scenes for this arc. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement initialize_arc()")
    
    def get_scene(self, scene_id: str) -> Optional[StoryScene]:
        """Get a specific scene from this arc."""
        return self.scenes.get(scene_id)
    
    def get_all_scenes(self) -> Dict[str, StoryScene]:
        """Get all scenes in this arc."""
        return self.scenes.copy()
    
    def add_scene(self, scene_id: str, scene: StoryScene):
        """Add a scene to this arc."""
        self.scenes[scene_id] = scene
    
    def get_starting_scene(self) -> str:
        """Get the starting scene ID for this arc."""
        return self.starting_scene
    
    def create_enemy(self, enemy_type: str, player_level: int) -> Enemy:
        """Create an enemy for this arc. Can be overridden by subclasses."""
        return self._create_default_enemy(enemy_type, player_level)
    
    def _create_default_enemy(self, enemy_type: str, player_level: int) -> Enemy:
        """Create a default enemy scaled to player level."""
        base_enemies = {
            "weak_curse": {"name": "Weak Cursed Spirit", "hp": 50, "energy": 30},
            "grade_4_curse": {"name": "Grade 4 Cursed Spirit", "hp": 60, "energy": 35},
            "grade_3_curse": {"name": "Grade 3 Cursed Spirit", "hp": 80, "energy": 40},
            "grade_2_curse": {"name": "Grade 2 Cursed Spirit", "hp": 120, "energy": 60},
            "grade_1_curse": {"name": "Grade 1 Cursed Spirit", "hp": 200, "energy": 100},
            "special_grade": {"name": "Special Grade Cursed Spirit", "hp": 350, "energy": 150}
        }
        
        enemy_data = base_enemies.get(enemy_type, base_enemies["grade_3_curse"])
        enemy = Enemy(enemy_data["name"], enemy_data["hp"], enemy_data["energy"])
        
        # Scale to player level
        level_modifier = max(1, player_level - 1)
        enemy.max_hp += level_modifier * 10
        enemy.hp = enemy.max_hp
        enemy.max_cursed_energy += level_modifier * 5
        enemy.cursed_energy = enemy.max_cursed_energy
        enemy.level = max(1, player_level)
        
        return enemy