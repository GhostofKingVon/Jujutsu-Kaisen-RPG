"""
Character System with Traits and Evolution

Defines player and NPC characters, trait systems, and character progression.
"""

from typing import Dict, List, Any, Optional
from enum import Enum
import random


class Trait(Enum):
    """Character traits that evolve based on player actions."""
    COMPASSIONATE = "Compassionate"
    FOCUSED = "Focused"
    AGGRESSIVE = "Aggressive"
    PROTECTIVE = "Protective"
    ANALYTICAL = "Analytical"
    RECKLESS = "Reckless"
    DETERMINED = "Determined"
    CAUTIOUS = "Cautious"


class CursedTechnique:
    """Represents a cursed technique with its properties."""
    
    def __init__(self, name: str, damage: int, cost: int, description: str, 
                 technique_type: str = "offensive", cooldown: int = 0):
        self.name = name
        self.damage = damage
        self.cost = cost  # Cursed energy cost
        self.description = description
        self.technique_type = technique_type  # offensive, defensive, utility
        self.cooldown = cooldown
        self.current_cooldown = 0
    
    def can_use(self, cursed_energy: int) -> bool:
        """Check if the technique can be used."""
        return cursed_energy >= self.cost and self.current_cooldown == 0
    
    def use(self) -> int:
        """Use the technique and return damage/effect value."""
        if self.current_cooldown > 0:
            return 0
        
        self.current_cooldown = self.cooldown
        return self.damage
    
    def reduce_cooldown(self):
        """Reduce cooldown by 1 turn."""
        if self.current_cooldown > 0:
            self.current_cooldown -= 1


class Character:
    """Base character class for players and NPCs."""
    
    def __init__(self, name: str, max_hp: int = 100, max_cursed_energy: int = 50):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_cursed_energy = max_cursed_energy
        self.cursed_energy = max_cursed_energy
        self.level = 1
        self.experience = 0
        self.techniques: List[CursedTechnique] = []
        self.status_effects = {}  # Effects like poison, paralysis, etc.
    
    def is_alive(self) -> bool:
        """Check if character is alive."""
        return self.hp > 0
    
    def take_damage(self, damage: int) -> int:
        """Take damage and return actual damage taken."""
        actual_damage = min(damage, self.hp)
        self.hp -= actual_damage
        return actual_damage
    
    def heal(self, amount: int) -> int:
        """Heal HP and return actual healing done."""
        actual_healing = min(amount, self.max_hp - self.hp)
        self.hp += actual_healing
        return actual_healing
    
    def use_cursed_energy(self, amount: int) -> bool:
        """Use cursed energy. Returns True if successful."""
        if self.cursed_energy >= amount:
            self.cursed_energy -= amount
            return True
        return False
    
    def restore_cursed_energy(self, amount: int) -> int:
        """Restore cursed energy and return actual amount restored."""
        actual_restore = min(amount, self.max_cursed_energy - self.cursed_energy)
        self.cursed_energy += actual_restore
        return actual_restore
    
    def add_technique(self, technique: CursedTechnique):
        """Add a new cursed technique."""
        self.techniques.append(technique)
    
    def get_available_techniques(self) -> List[CursedTechnique]:
        """Get list of techniques that can currently be used."""
        return [t for t in self.techniques if t.can_use(self.cursed_energy)]
    
    def add_status_effect(self, effect: str, duration: int):
        """Add a status effect."""
        self.status_effects[effect] = duration
    
    def remove_status_effect(self, effect: str):
        """Remove a status effect."""
        if effect in self.status_effects:
            del self.status_effects[effect]
    
    def process_status_effects(self):
        """Process all status effects for one turn."""
        effects_to_remove = []
        
        for effect, duration in self.status_effects.items():
            # Apply effect
            if effect == "poison":
                self.take_damage(5)
                print(f"{self.name} takes 5 poison damage!")
            elif effect == "regeneration":
                healed = self.heal(10)
                if healed > 0:
                    print(f"{self.name} regenerates {healed} HP!")
            
            # Reduce duration
            self.status_effects[effect] -= 1
            if self.status_effects[effect] <= 0:
                effects_to_remove.append(effect)
        
        # Remove expired effects
        for effect in effects_to_remove:
            self.remove_status_effect(effect)
            print(f"{self.name} recovers from {effect}!")


class Player(Character):
    """Player character with traits, relationships, and progression."""
    
    def __init__(self, name: str):
        super().__init__(name, max_hp=120, max_cursed_energy=60)
        self.traits: Dict[Trait, int] = {trait: 0 for trait in Trait}
        self.dominant_traits: List[Trait] = []
        self.relationships: Dict[str, int] = {}
        self.transformation_active = False
        self.transformation_name = ""
        self.transformation_turns = 0
        
        # Start with basic techniques
        self._initialize_basic_techniques()
    
    def _initialize_basic_techniques(self):
        """Initialize the player with basic cursed techniques."""
        basic_strike = CursedTechnique(
            "Cursed Energy Strike",
            damage=25,
            cost=10,
            description="A basic attack enhanced with cursed energy."
        )
        
        energy_guard = CursedTechnique(
            "Cursed Energy Guard",
            damage=0,
            cost=15,
            description="Defensive technique that reduces incoming damage.",
            technique_type="defensive"
        )
        
        self.add_technique(basic_strike)
        self.add_technique(energy_guard)
    
    def modify_trait(self, trait: Trait, change: int):
        """Modify a character trait and update dominant traits."""
        self.traits[trait] += change
        self.traits[trait] = max(0, min(100, self.traits[trait]))  # Clamp 0-100
        
        # Update dominant traits (traits with value >= 60)
        self.dominant_traits = [trait for trait, value in self.traits.items() if value >= 60]
    
    def get_dominant_traits(self) -> List[Trait]:
        """Get list of dominant traits."""
        return self.dominant_traits.copy()
    
    def gain_experience(self, amount: int):
        """Gain experience and handle leveling up."""
        self.experience += amount
        
        # Check for level up (every 100 XP)
        new_level = (self.experience // 100) + 1
        if new_level > self.level:
            old_level = self.level
            self.level = new_level
            self._level_up(old_level, new_level)
    
    def _level_up(self, old_level: int, new_level: int):
        """Handle level up bonuses."""
        print(f"\n🎉 {self.name} leveled up! Level {old_level} → {new_level}")
        
        # Increase stats
        hp_increase = 20
        ce_increase = 10
        
        self.max_hp += hp_increase
        self.max_cursed_energy += ce_increase
        self.hp = self.max_hp  # Full heal on level up
        self.cursed_energy = self.max_cursed_energy
        
        print(f"HP increased by {hp_increase}! (Now: {self.max_hp})")
        print(f"Cursed Energy increased by {ce_increase}! (Now: {self.max_cursed_energy})")
        
        # Learn new techniques at certain levels
        self._check_new_techniques()
    
    def _check_new_techniques(self):
        """Check if new techniques should be unlocked at current level."""
        new_techniques = []
        
        if self.level >= 3 and not any(t.name == "Shadow Clone" for t in self.techniques):
            shadow_clone = CursedTechnique(
                "Shadow Clone",
                damage=35,
                cost=25,
                description="Create a shadow clone to attack the enemy.",
                cooldown=2
            )
            new_techniques.append(shadow_clone)
        
        if self.level >= 5 and not any(t.name == "Cursed Energy Burst" for t in self.techniques):
            burst = CursedTechnique(
                "Cursed Energy Burst",
                damage=50,
                cost=35,
                description="A powerful burst of cursed energy.",
                cooldown=3
            )
            new_techniques.append(burst)
        
        if self.level >= 8 and not any(t.name == "Wukong Technique" for t in self.techniques):
            wukong = CursedTechnique(
                "Wukong Technique",
                damage=60,
                cost=40,
                description="Original technique inspired by the Monkey King.",
                cooldown=4
            )
            new_techniques.append(wukong)
        
        for technique in new_techniques:
            self.add_technique(technique)
            print(f"🌟 New technique learned: {technique.name}!")
            print(f"   {technique.description}")
    
    def activate_transformation(self, transformation_name: str, duration: int):
        """Activate a transformation like Ultra Instinct Monkey."""
        self.transformation_active = True
        self.transformation_name = transformation_name
        self.transformation_turns = duration
        
        print(f"\n✨ {self.name} activates {transformation_name}!")
        
        # Apply transformation bonuses
        if "Ultra Instinct" in transformation_name:
            print("Enhanced reflexes and dodge chance activated!")
        elif "Monkey" in transformation_name:
            print("Agility and technique power increased!")
    
    def process_transformation(self):
        """Process transformation effects each turn."""
        if self.transformation_active:
            self.transformation_turns -= 1
            if self.transformation_turns <= 0:
                print(f"{self.transformation_name} transformation ends.")
                self.transformation_active = False
                self.transformation_name = ""
    
    def get_dodge_chance(self) -> float:
        """Calculate dodge chance based on traits and transformations."""
        base_chance = 0.15  # 15% base dodge chance
        
        # Trait bonuses
        if Trait.FOCUSED in self.dominant_traits:
            base_chance += 0.1
        if Trait.CAUTIOUS in self.dominant_traits:
            base_chance += 0.05
        
        # Transformation bonuses
        if self.transformation_active and "Ultra Instinct" in self.transformation_name:
            base_chance += 0.3
        
        return min(0.8, base_chance)  # Cap at 80%
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert player to dictionary for saving."""
        return {
            'name': self.name,
            'max_hp': self.max_hp,
            'hp': self.hp,
            'max_cursed_energy': self.max_cursed_energy,
            'cursed_energy': self.cursed_energy,
            'level': self.level,
            'experience': self.experience,
            'traits': {trait.value: value for trait, value in self.traits.items()},
            'relationships': self.relationships,
            'transformation_active': self.transformation_active,
            'transformation_name': self.transformation_name,
            'transformation_turns': self.transformation_turns,
            'techniques': [
                {
                    'name': t.name,
                    'damage': t.damage,
                    'cost': t.cost,
                    'description': t.description,
                    'technique_type': t.technique_type,
                    'cooldown': t.cooldown,
                    'current_cooldown': t.current_cooldown
                }
                for t in self.techniques
            ]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Player':
        """Create player from dictionary data."""
        player = cls(data['name'])
        player.max_hp = data['max_hp']
        player.hp = data['hp']
        player.max_cursed_energy = data['max_cursed_energy']
        player.cursed_energy = data['cursed_energy']
        player.level = data['level']
        player.experience = data['experience']
        
        # Restore traits
        player.traits = {}
        for trait_name, value in data['traits'].items():
            trait = next((t for t in Trait if t.value == trait_name), None)
            if trait:
                player.traits[trait] = value
        
        # Update dominant traits
        player.dominant_traits = [trait for trait, value in player.traits.items() if value >= 60]
        
        player.relationships = data['relationships']
        player.transformation_active = data['transformation_active']
        player.transformation_name = data['transformation_name']
        player.transformation_turns = data['transformation_turns']
        
        # Restore techniques
        player.techniques = []
        for tech_data in data['techniques']:
            technique = CursedTechnique(
                tech_data['name'],
                tech_data['damage'],
                tech_data['cost'],
                tech_data['description'],
                tech_data['technique_type'],
                tech_data['cooldown']
            )
            technique.current_cooldown = tech_data['current_cooldown']
            player.techniques.append(technique)
        
        return player


class Enemy(Character):
    """Enemy character with AI behavior patterns."""
    
    def __init__(self, name: str, max_hp: int, max_cursed_energy: int, 
                 difficulty: str = "normal"):
        super().__init__(name, max_hp, max_cursed_energy)
        self.difficulty = difficulty
        self.ai_pattern = "aggressive"  # aggressive, defensive, mixed
        self.phase = 1
        self.max_phases = 1
        self.phase_transition_messages = []
        
        self._initialize_enemy_techniques()
    
    def _initialize_enemy_techniques(self):
        """Initialize enemy with appropriate techniques."""
        # Basic enemy attack
        basic_attack = CursedTechnique(
            f"{self.name}'s Assault",
            damage=20,
            cost=5,
            description=f"{self.name} launches a fierce attack."
        )
        self.add_technique(basic_attack)
    
    def choose_action(self, player) -> str:
        """AI chooses an action based on pattern and situation."""
        available_techniques = self.get_available_techniques()
        
        # Check for phase transition
        if self.should_transition_phase():
            return "phase_transition"
        
        # Choose based on AI pattern
        if self.ai_pattern == "aggressive":
            if available_techniques and random.random() < 0.7:
                return "technique"
            else:
                return "attack"
        elif self.ai_pattern == "defensive":
            if self.hp < self.max_hp * 0.3 and random.random() < 0.5:
                return "guard"
            elif available_techniques and random.random() < 0.5:
                return "technique"
            else:
                return "attack"
        else:  # mixed
            return random.choice(["attack", "technique", "guard"])
    
    def should_transition_phase(self) -> bool:
        """Check if enemy should transition to next phase."""
        if self.phase >= self.max_phases:
            return False
        
        phase_threshold = (self.max_phases - self.phase + 1) / self.max_phases
        return self.hp / self.max_hp <= phase_threshold * 0.6
    
    def transition_phase(self):
        """Transition to the next phase."""
        if self.phase < self.max_phases:
            self.phase += 1
            
            # Heal partially and restore energy
            heal_amount = int(self.max_hp * 0.2)
            self.heal(heal_amount)
            self.restore_cursed_energy(20)
            
            # Display transition message
            if self.phase - 1 < len(self.phase_transition_messages):
                print(f"\n🔥 {self.phase_transition_messages[self.phase - 1]}")
            else:
                print(f"\n🔥 {self.name} enters phase {self.phase}!")
            
            print(f"{self.name} recovers {heal_amount} HP and gains power!")