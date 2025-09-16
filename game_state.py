"""
Game State Management System

Handles saving/loading game progress, player state, story progression, and exploration checkpoints.
"""

import json
import os
import pickle
from typing import Dict, Any, Optional, List
from datetime import datetime


class GameState:
    """Manages the overall game state including player progress, story state, and save/load functionality."""
    
    def __init__(self):
        self.player = None
        self.current_chapter = 1
        self.current_location = "Tokyo Jujutsu High"
        self.current_area = "courtyard"
        self.story_flags = {}  # Track story progression and choices
        self.relationships = {}  # NPC relationships
        self.unlocked_techniques = []
        self.completed_missions = []
        self.inventory = []
        self.discovered_secrets = []
        self.exploration_progress = {}  # Track exploration completion per location
        self.checkpoint_data = {}  # Save exploration checkpoints
        self.save_file = "jjk_save.dat"
        self.checkpoint_dir = "saves/checkpoints"
        self._ensure_save_directory()
    
    def _ensure_save_directory(self):
        """Ensure save directories exist."""
        os.makedirs(self.checkpoint_dir, exist_ok=True)
    
    def create_exploration_checkpoint(self, location: str, area: str, description: str = ""):
        """Create a checkpoint during exploration."""
        checkpoint_id = f"{location}_{area}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        checkpoint_data = {
            'id': checkpoint_id,
            'timestamp': datetime.now().isoformat(),
            'location': location,
            'area': area,
            'description': description,
            'player_data': self.player.to_dict() if self.player else None,
            'story_flags': self.story_flags.copy(),
            'relationships': self.relationships.copy(),
            'inventory': self.inventory.copy(),
            'discovered_secrets': self.discovered_secrets.copy()
        }
        
        checkpoint_file = os.path.join(self.checkpoint_dir, f"{checkpoint_id}.checkpoint")
        try:
            with open(checkpoint_file, 'wb') as f:
                pickle.dump(checkpoint_data, f)
            print(f"📍 Exploration checkpoint created: {description or f'{location} - {area}'}")
            return checkpoint_id
        except Exception as e:
            print(f"Failed to create checkpoint: {e}")
            return None
    
    def load_exploration_checkpoint(self, checkpoint_id: str) -> bool:
        """Load a specific exploration checkpoint."""
        checkpoint_file = os.path.join(self.checkpoint_dir, f"{checkpoint_id}.checkpoint")
        try:
            if not os.path.exists(checkpoint_file):
                return False
            
            with open(checkpoint_file, 'rb') as f:
                checkpoint_data = pickle.load(f)
            
            # Import Player class here to avoid circular imports
            from character import Player
            
            # Restore checkpoint state
            if checkpoint_data.get('player_data'):
                self.player = Player.from_dict(checkpoint_data['player_data'])
            
            self.current_location = checkpoint_data.get('location', self.current_location)
            self.current_area = checkpoint_data.get('area', self.current_area)
            self.story_flags = checkpoint_data.get('story_flags', {})
            self.relationships = checkpoint_data.get('relationships', {})
            self.inventory = checkpoint_data.get('inventory', [])
            self.discovered_secrets = checkpoint_data.get('discovered_secrets', [])
            
            print(f"📍 Checkpoint loaded: {checkpoint_data.get('description', checkpoint_id)}")
            return True
            
        except Exception as e:
            print(f"Failed to load checkpoint: {e}")
            return False
    
    def list_exploration_checkpoints(self) -> List[Dict[str, Any]]:
        """List all available exploration checkpoints."""
        checkpoints = []
        if not os.path.exists(self.checkpoint_dir):
            return checkpoints
            
        for filename in os.listdir(self.checkpoint_dir):
            if filename.endswith('.checkpoint'):
                checkpoint_file = os.path.join(self.checkpoint_dir, filename)
                try:
                    with open(checkpoint_file, 'rb') as f:
                        checkpoint_data = pickle.load(f)
                    
                    checkpoints.append({
                        'id': checkpoint_data.get('id', filename),
                        'timestamp': checkpoint_data.get('timestamp', 'Unknown'),
                        'location': checkpoint_data.get('location', 'Unknown'),
                        'area': checkpoint_data.get('area', 'Unknown'),
                        'description': checkpoint_data.get('description', ''),
                        'file': filename
                    })
                except Exception:
                    continue
        
        # Sort by timestamp (newest first)
        checkpoints.sort(key=lambda x: x['timestamp'], reverse=True)
        return checkpoints
    
    def discover_secret(self, secret_name: str, location: str):
        """Mark a secret as discovered."""
        secret_key = f"{location}:{secret_name}"
        if secret_key not in self.discovered_secrets:
            self.discovered_secrets.append(secret_key)
            print(f"🔍 Secret discovered: {secret_name} in {location}!")
            return True
        return False
    
    def update_exploration_progress(self, location: str, area: str, completion_percentage: float):
        """Update exploration progress for a location/area."""
        if location not in self.exploration_progress:
            self.exploration_progress[location] = {}
        self.exploration_progress[location][area] = completion_percentage
    
    def get_exploration_progress(self, location: str, area: str = None) -> float:
        """Get exploration progress for a location or specific area."""
        if location not in self.exploration_progress:
            return 0.0
        
        if area:
            return self.exploration_progress[location].get(area, 0.0)
        else:
            # Return average progress across all areas in location
            areas = self.exploration_progress[location]
            if not areas:
                return 0.0
            return sum(areas.values()) / len(areas)
    
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
                'current_area': self.current_area,
                'story_flags': self.story_flags,
                'relationships': self.relationships,
                'unlocked_techniques': self.unlocked_techniques,
                'completed_missions': self.completed_missions,
                'inventory': self.inventory,
                'discovered_secrets': self.discovered_secrets,
                'exploration_progress': self.exploration_progress
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
            self.current_area = save_data.get('current_area', "courtyard")
            self.story_flags = save_data.get('story_flags', {})
            self.relationships = save_data.get('relationships', {})
            self.unlocked_techniques = save_data.get('unlocked_techniques', [])
            self.completed_missions = save_data.get('completed_missions', [])
            self.inventory = save_data.get('inventory', [])
            self.discovered_secrets = save_data.get('discovered_secrets', [])
            self.exploration_progress = save_data.get('exploration_progress', {})
            
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