"""
Stamina and Fatigue System

Adds strategic depth through action costs, recovery mechanics, and fatigue management.
"""

from typing import Dict, Any, Optional
from enum import Enum
import random


class StaminaState(Enum):
    """Character stamina states affecting performance."""
    ENERGETIC = "energetic"
    NORMAL = "normal"
    TIRED = "tired"
    EXHAUSTED = "exhausted"
    DEPLETED = "depleted"


class StaminaSystem:
    """Manages stamina and fatigue mechanics for strategic gameplay."""
    
    def __init__(self, max_stamina: int = 100):
        self.max_stamina = max_stamina
        self.current_stamina = max_stamina
        self.fatigue_level = 0  # 0-100, affects stamina regeneration
        self.action_costs = {
            "basic_attack": 10,
            "technique": 15,
            "dodge": 8,
            "guard": 5,
            "move": 12,
            "transform": 25,
            "domain_expansion": 40
        }
    
    def get_stamina_state(self) -> StaminaState:
        """Get current stamina state."""
        percentage = (self.current_stamina / self.max_stamina) * 100
        
        if percentage >= 80:
            return StaminaState.ENERGETIC
        elif percentage >= 60:
            return StaminaState.NORMAL
        elif percentage >= 40:
            return StaminaState.TIRED
        elif percentage >= 20:
            return StaminaState.EXHAUSTED
        else:
            return StaminaState.DEPLETED
    
    def can_perform_action(self, action_type: str) -> bool:
        """Check if character has enough stamina for action."""
        cost = self.action_costs.get(action_type, 10)
        return self.current_stamina >= cost
    
    def use_stamina(self, action_type: str) -> bool:
        """Use stamina for an action. Returns True if successful."""
        cost = self.action_costs.get(action_type, 10)
        
        if self.current_stamina >= cost:
            self.current_stamina -= cost
            
            # Add fatigue based on action intensity
            fatigue_gain = cost // 5
            self.add_fatigue(fatigue_gain)
            
            return True
        return False
    
    def add_fatigue(self, amount: int):
        """Add fatigue (reduces stamina regeneration)."""
        self.fatigue_level = min(100, self.fatigue_level + amount)
    
    def rest_turn(self) -> int:
        """Regenerate stamina during rest. Returns amount restored."""
        base_regen = 20
        
        # Fatigue reduces regeneration
        fatigue_penalty = self.fatigue_level * 0.1
        actual_regen = max(5, int(base_regen * (1 - fatigue_penalty)))
        
        old_stamina = self.current_stamina
        self.current_stamina = min(self.max_stamina, self.current_stamina + actual_regen)
        
        # Reduce fatigue slightly when resting
        self.fatigue_level = max(0, self.fatigue_level - 2)
        
        return self.current_stamina - old_stamina
    
    def full_rest(self):
        """Full recovery after combat or long rest."""
        self.current_stamina = self.max_stamina
        self.fatigue_level = max(0, self.fatigue_level - 20)
    
    def get_performance_modifier(self) -> float:
        """Get performance modifier based on stamina state."""
        state = self.get_stamina_state()
        
        modifiers = {
            StaminaState.ENERGETIC: 1.1,
            StaminaState.NORMAL: 1.0,
            StaminaState.TIRED: 0.9,
            StaminaState.EXHAUSTED: 0.7,
            StaminaState.DEPLETED: 0.5
        }
        
        return modifiers[state]
    
    def get_status_display(self) -> str:
        """Get stamina status for display."""
        state = self.get_stamina_state()
        stamina_bar = "█" * (self.current_stamina // 10) + "░" * (10 - (self.current_stamina // 10))
        
        state_emoji = {
            StaminaState.ENERGETIC: "💪",
            StaminaState.NORMAL: "😐",
            StaminaState.TIRED: "😓",
            StaminaState.EXHAUSTED: "😵",
            StaminaState.DEPLETED: "💀"
        }
        
        return f"{state_emoji[state]} [{stamina_bar}] {self.current_stamina}/{self.max_stamina} Stamina"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for saving."""
        return {
            "max_stamina": self.max_stamina,
            "current_stamina": self.current_stamina,
            "fatigue_level": self.fatigue_level
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'StaminaSystem':
        """Create from dictionary for loading."""
        system = cls(data.get("max_stamina", 100))
        system.current_stamina = data.get("current_stamina", 100)
        system.fatigue_level = data.get("fatigue_level", 0)
        return system


class EnvironmentalAdvantages:
    """System for environmental combat advantages."""
    
    def __init__(self):
        self.environments = {
            "high_ground": {
                "damage_bonus": 1.2,
                "dodge_bonus": 0.1,
                "description": "Fighting from elevated position"
            },
            "shadows": {
                "stealth_bonus": 0.3,
                "surprise_chance": 0.2,
                "description": "Hidden in shadows"
            },
            "open_space": {
                "movement_bonus": 1.5,
                "aoe_efficiency": 1.3,
                "description": "Wide open battlefield"
            },
            "narrow_corridor": {
                "defense_bonus": 1.2,
                "aoe_penalty": 0.7,
                "description": "Confined fighting space"
            },
            "cursed_ground": {
                "cursed_energy_regen": 1.5,
                "technique_power": 1.1,
                "description": "Ground saturated with cursed energy"
            },
            "sanctified_ground": {
                "curse_resistance": 0.8,
                "healing_bonus": 1.3,
                "description": "Blessed or purified area"
            }
        }
    
    def get_advantage(self, environment: str) -> Dict[str, Any]:
        """Get environmental advantage data."""
        return self.environments.get(environment, {})
    
    def apply_environmental_effects(self, character, environment: str) -> str:
        """Apply environmental effects to character actions."""
        advantage = self.get_advantage(environment)
        if not advantage:
            return ""
        
        effects = []
        
        # Apply bonuses based on environment
        if "damage_bonus" in advantage:
            effects.append(f"📈 Damage increased by {int((advantage['damage_bonus'] - 1) * 100)}%")
        
        if "dodge_bonus" in advantage:
            effects.append(f"🏃 Dodge chance increased by {int(advantage['dodge_bonus'] * 100)}%")
        
        if "cursed_energy_regen" in advantage:
            regen = int(character.max_cursed_energy * 0.1 * advantage['cursed_energy_regen'])
            character.restore_cursed_energy(regen)
            effects.append(f"⚡ Restored {regen} cursed energy from environment")
        
        return " | ".join(effects) if effects else ""