"""
Game State Management System

Handles saving/loading game progress, player state, and story progression.
"""

import json
import os
import pickle
from typing import Dict, Any, Optional
from datetime import datetime


class GameState:
    """Manages the overall game state including player progress, story state, and save/load functionality."""
    
    def __init__(self):
        self.player = None
        self.current_chapter = 1
        self.current_location = "Tokyo Jujutsu High"
        self.story_flags = {}  # Track story progression and choices
        self.relationships = {}  # NPC relationships
        self.unlocked_techniques = []
        self.completed_missions = []
        self.inventory = []
        self.save_file = "jjk_save.dat"
    
    def set_player(self, player):
        """Set the current player."""
        self.player = player
    
    def add_story_flag(self, flag_name: str, value: Any):
        """Add or update a story flag."""
        self.story_flags[flag_name] = value
    
    def get_story_flag(self, flag_name: str, default=None):
        """Get a story flag value."""
        return self.story_flags.get(flag_name, default)
    
    def update_relationship(self, npc_name: str, change: int):
        """Update relationship with an NPC."""
        if npc_name not in self.relationships:
            self.relationships[npc_name] = 0
        self.relationships[npc_name] += change
        
        # Clamp between -100 and 100
        self.relationships[npc_name] = max(-100, min(100, self.relationships[npc_name]))
    
    def get_relationship(self, npc_name: str) -> int:
        """Get relationship level with an NPC."""
        return self.relationships.get(npc_name, 0)
    
    def unlock_technique(self, technique_name: str):
        """Unlock a new cursed technique."""
        if technique_name not in self.unlocked_techniques:
            self.unlocked_techniques.append(technique_name)
    
    def has_technique(self, technique_name: str) -> bool:
        """Check if a technique is unlocked."""
        return technique_name in self.unlocked_techniques
    
    def complete_mission(self, mission_name: str):
        """Mark a mission as completed."""
        if mission_name not in self.completed_missions:
            self.completed_missions.append(mission_name)
    
    def is_mission_completed(self, mission_name: str) -> bool:
        """Check if a mission is completed."""
        return mission_name in self.completed_missions
    
    def advance_chapter(self, new_chapter: int = None):
        """Advance to the next chapter or set a specific chapter."""
        if new_chapter:
            self.current_chapter = new_chapter
        else:
            self.current_chapter += 1
    
    def set_location(self, location: str):
        """Set the current location."""
        self.current_location = location
    
    def add_to_inventory(self, item: str):
        """Add an item to inventory."""
        self.inventory.append(item)
    
    def remove_from_inventory(self, item: str) -> bool:
        """Remove an item from inventory. Returns True if successful."""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def has_item(self, item: str) -> bool:
        """Check if an item is in inventory."""
        return item in self.inventory
    
    def save_game(self) -> bool:
        """Save the current game state to file."""
        try:
            save_data = {
                'timestamp': datetime.now().isoformat(),
                'player_data': self.player.to_dict() if self.player else None,
                'current_chapter': self.current_chapter,
                'current_location': self.current_location,
                'story_flags': self.story_flags,
                'relationships': self.relationships,
                'unlocked_techniques': self.unlocked_techniques,
                'completed_missions': self.completed_missions,
                'inventory': self.inventory
            }
            
            with open(self.save_file, 'wb') as f:
                pickle.dump(save_data, f)
            
            print(f"Game saved successfully! ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
            return True
            
        except Exception as e:
            print(f"Failed to save game: {e}")
            return False
    
    def load_game(self) -> bool:
        """Load game state from file."""
        try:
            if not os.path.exists(self.save_file):
                return False
            
            with open(self.save_file, 'rb') as f:
                save_data = pickle.load(f)
            
            # Import Player class here to avoid circular imports
            from character import Player
            
            # Restore game state
            if save_data.get('player_data'):
                self.player = Player.from_dict(save_data['player_data'])
            
            self.current_chapter = save_data.get('current_chapter', 1)
            self.current_location = save_data.get('current_location', "Tokyo Jujutsu High")
            self.story_flags = save_data.get('story_flags', {})
            self.relationships = save_data.get('relationships', {})
            self.unlocked_techniques = save_data.get('unlocked_techniques', [])
            self.completed_missions = save_data.get('completed_missions', [])
            self.inventory = save_data.get('inventory', [])
            
            timestamp = save_data.get('timestamp', 'Unknown')
            print(f"Game loaded successfully! (Saved: {timestamp})")
            return True
            
        except Exception as e:
            print(f"Failed to load game: {e}")
            return False
    
    def get_save_info(self) -> Optional[Dict[str, Any]]:
        """Get information about the save file without loading it."""
        try:
            if not os.path.exists(self.save_file):
                return None
            
            with open(self.save_file, 'rb') as f:
                save_data = pickle.load(f)
            
            return {
                'timestamp': save_data.get('timestamp', 'Unknown'),
                'chapter': save_data.get('current_chapter', 1),
                'location': save_data.get('current_location', 'Unknown'),
                'player_name': save_data.get('player_data', {}).get('name', 'Unknown') if save_data.get('player_data') else 'Unknown'
            }
            
        except Exception:
            return None
    
    def delete_save(self) -> bool:
        """Delete the save file."""
        try:
            if os.path.exists(self.save_file):
                os.remove(self.save_file)
                return True
            return False
        except Exception:
            return False