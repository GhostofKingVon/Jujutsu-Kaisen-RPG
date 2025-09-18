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


class MoralAlignment(Enum):
    """Character moral alignment affecting story paths and abilities."""
    LAWFUL_GOOD = "Lawful Good"
    NEUTRAL_GOOD = "Neutral Good"
    CHAOTIC_GOOD = "Chaotic Good"
    LAWFUL_NEUTRAL = "Lawful Neutral"
    TRUE_NEUTRAL = "True Neutral"
    CHAOTIC_NEUTRAL = "Chaotic Neutral"
    LAWFUL_EVIL = "Lawful Evil"
    NEUTRAL_EVIL = "Neutral Evil"
    CHAOTIC_EVIL = "Chaotic Evil"


class CharacterBackground:
    """Detailed character background and history."""
    
    def __init__(self):
        self.backstory = ""
        self.family_history = {}
        self.personal_goals = []
        self.fears = []
        self.motivations = []
        self.significant_events = []
        self.character_arc_progress = 0
        self.unlocked_memories = []
    
    def add_backstory_element(self, element_type: str, content: str):
        """Add a backstory element."""
        if element_type == "goal":
            self.personal_goals.append(content)
        elif element_type == "fear":
            self.fears.append(content)
        elif element_type == "motivation":
            self.motivations.append(content)
        elif element_type == "event":
            self.significant_events.append(content)
        elif element_type == "memory":
            self.unlocked_memories.append(content)
    
    def get_background_summary(self) -> str:
        """Get a summary of the character's background."""
        summary = []
        
        if self.personal_goals:
            summary.append(f"Goals: {', '.join(self.personal_goals[:3])}")
        
        if self.fears:
            summary.append(f"Fears: {', '.join(self.fears[:2])}")
        
        if self.motivations:
            summary.append(f"Driven by: {', '.join(self.motivations[:2])}")
        
        return " | ".join(summary) if summary else "A mysterious past shrouded in secrets..."


class UniqueAbility:
    """Special character abilities based on traits and experiences."""
    
    def __init__(self, name: str, description: str, ability_type: str, requirements: Dict[str, Any]):
        self.name = name
        self.description = description
        self.ability_type = ability_type  # leadership, analytical, combat, social
        self.requirements = requirements
        self.uses_per_day = requirements.get("uses_per_day", 3)
        self.current_uses = self.uses_per_day
        self.is_unlocked = False
    
    def check_unlock_requirements(self, character) -> bool:
        """Check if character meets requirements to unlock this ability."""
        # Check trait requirements
        if "traits" in self.requirements:
            for trait, min_value in self.requirements["traits"].items():
                if character.traits.get(trait, 0) < min_value:
                    return False
        
        # Check level requirement
        if "level" in self.requirements:
            if character.level < self.requirements["level"]:
                return False
        
        # Check alignment requirement
        if "alignment" in self.requirements:
            if character.moral_alignment != self.requirements["alignment"]:
                return False
        
        return True
    
    def use_ability(self, character, context: Dict[str, Any]) -> Dict[str, Any]:
        """Use the ability if available."""
        if not self.is_unlocked:
            return {"success": False, "message": "Ability not unlocked"}
        
        if self.current_uses <= 0:
            return {"success": False, "message": "No uses remaining today"}
        
        self.current_uses -= 1
        return self._execute_ability(character, context)
    
    def _execute_ability(self, character, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the specific ability effect."""
        # Override in specific ability implementations
        return {"success": True, "message": f"Used {self.name}"}
    
    def daily_reset(self):
        """Reset daily uses."""
        self.current_uses = self.uses_per_day


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
        
        # Enhanced character systems
        self.moral_alignment = MoralAlignment.TRUE_NEUTRAL
        self.character_background = CharacterBackground()
        self.unique_abilities: List[UniqueAbility] = []
        self.morality_points = {"lawful": 0, "chaotic": 0, "good": 0, "evil": 0}
        self.reputation = {"jujutsu_society": 50, "students": 50, "teachers": 50, "civilians": 50}
        
        # Stamina system integration
        from stamina_system import StaminaSystem
        self.stamina_system = StaminaSystem()
        
        # Start with basic techniques
        self._initialize_basic_techniques()
        self._initialize_unique_abilities()
    
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
    
    def _initialize_unique_abilities(self):
        """Initialize unique abilities based on potential character development."""
        # Leadership abilities
        leadership_ability = UniqueAbility(
            "Inspire Allies",
            "Boost team morale and performance in team battles",
            "leadership",
            {"traits": {Trait.PROTECTIVE: 70, Trait.DETERMINED: 60}, "level": 10}
        )
        
        # Analytical abilities  
        tactical_analysis = UniqueAbility(
            "Tactical Analysis",
            "Gain detailed information about enemies and optimal strategies",
            "analytical",
            {"traits": {Trait.ANALYTICAL: 80, Trait.FOCUSED: 60}, "level": 8}
        )
        
        # Combat abilities
        berserker_rage = UniqueAbility(
            "Berserker's Fury",
            "Enter a rage state increasing damage but reducing defense",
            "combat",
            {"traits": {Trait.AGGRESSIVE: 80, Trait.RECKLESS: 60}, "level": 12}
        )
        
        # Social abilities
        diplomatic_immunity = UniqueAbility(
            "Diplomatic Resolution",
            "Resolve conflicts through negotiation instead of combat",
            "social",
            {"traits": {Trait.COMPASSIONATE: 70, Trait.CAUTIOUS: 50}, "level": 15}
        )
        
        self.unique_abilities = [leadership_ability, tactical_analysis, berserker_rage, diplomatic_immunity]
    
    def update_morality(self, action_type: str, magnitude: int = 1):
        """Update morality based on player actions."""
        morality_changes = {
            "help_innocent": {"good": 2, "lawful": 1},
            "harm_innocent": {"evil": 3, "chaotic": 1},
            "follow_rules": {"lawful": 2},
            "break_rules": {"chaotic": 2},
            "sacrifice_self": {"good": 3, "lawful": 1},
            "betray_ally": {"evil": 3, "chaotic": 2},
            "show_mercy": {"good": 2},
            "show_cruelty": {"evil": 2, "chaotic": 1},
            "uphold_justice": {"good": 2, "lawful": 2},
            "seek_revenge": {"chaotic": 2, "evil": 1}
        }
        
        if action_type in morality_changes:
            changes = morality_changes[action_type]
            for axis, change in changes.items():
                self.morality_points[axis] += change * magnitude
        
        # Update alignment based on morality points
        self._calculate_alignment()
    
    def _calculate_alignment(self):
        """Calculate moral alignment based on morality points."""
        law_chaos_axis = self.morality_points["lawful"] - self.morality_points["chaotic"]
        good_evil_axis = self.morality_points["good"] - self.morality_points["evil"]
        
        # Determine alignment
        if law_chaos_axis >= 10:
            law_axis = "LAWFUL"
        elif law_chaos_axis <= -10:
            law_axis = "CHAOTIC"
        else:
            law_axis = "NEUTRAL"
        
        if good_evil_axis >= 10:
            good_axis = "GOOD"
        elif good_evil_axis <= -10:
            good_axis = "EVIL"
        else:
            good_axis = "NEUTRAL"
        
        # Map to alignment enum
        alignment_map = {
            ("LAWFUL", "GOOD"): MoralAlignment.LAWFUL_GOOD,
            ("LAWFUL", "NEUTRAL"): MoralAlignment.LAWFUL_NEUTRAL,
            ("LAWFUL", "EVIL"): MoralAlignment.LAWFUL_EVIL,
            ("NEUTRAL", "GOOD"): MoralAlignment.NEUTRAL_GOOD,
            ("NEUTRAL", "NEUTRAL"): MoralAlignment.TRUE_NEUTRAL,
            ("NEUTRAL", "EVIL"): MoralAlignment.NEUTRAL_EVIL,
            ("CHAOTIC", "GOOD"): MoralAlignment.CHAOTIC_GOOD,
            ("CHAOTIC", "NEUTRAL"): MoralAlignment.CHAOTIC_NEUTRAL,
            ("CHAOTIC", "EVIL"): MoralAlignment.CHAOTIC_EVIL
        }
        
        old_alignment = self.moral_alignment
        self.moral_alignment = alignment_map.get((law_axis, good_axis), MoralAlignment.TRUE_NEUTRAL)
        
        # Notify if alignment changed
        if old_alignment != self.moral_alignment:
            print(f"\n🔄 {self.name}'s moral alignment has shifted to {self.moral_alignment.value}!")
    
    def update_reputation(self, faction: str, change: int):
        """Update reputation with a specific faction."""
        if faction in self.reputation:
            old_rep = self.reputation[faction]
            self.reputation[faction] = max(0, min(100, self.reputation[faction] + change))
            
            # Notify of significant changes
            if abs(change) >= 10:
                direction = "increased" if change > 0 else "decreased"
                print(f"📊 Reputation with {faction} {direction} by {abs(change)}!")
    
    def check_unique_ability_unlocks(self):
        """Check if any unique abilities can be unlocked."""
        newly_unlocked = []
        
        for ability in self.unique_abilities:
            if not ability.is_unlocked and ability.check_unlock_requirements(self):
                ability.is_unlocked = True
                newly_unlocked.append(ability)
                print(f"🌟 New unique ability unlocked: {ability.name}!")
                print(f"   {ability.description}")
        
        return newly_unlocked
    
    def use_unique_ability(self, ability_name: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Use a unique ability if available."""
        for ability in self.unique_abilities:
            if ability.name == ability_name:
                return ability.use_ability(self, context)
        
        return {"success": False, "message": "Ability not found"}
    
    def get_character_summary(self) -> str:
        """Get a comprehensive character summary."""
        summary = []
        summary.append(f"Level {self.level} {self.moral_alignment.value} Sorcerer")
        
        if self.dominant_traits:
            trait_names = [trait.value for trait in self.dominant_traits[:3]]
            summary.append(f"Traits: {', '.join(trait_names)}")
        
        background_summary = self.character_background.get_background_summary()
        if background_summary:
            summary.append(background_summary)
        
        return " | ".join(summary)
    
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
            'moral_alignment': self.moral_alignment.value,
            'morality_points': self.morality_points,
            'reputation': self.reputation,
            'stamina_system': self.stamina_system.to_dict(),
            'character_background': {
                'backstory': self.character_background.backstory,
                'personal_goals': self.character_background.personal_goals,
                'fears': self.character_background.fears,
                'motivations': self.character_background.motivations,
                'significant_events': self.character_background.significant_events,
                'character_arc_progress': self.character_background.character_arc_progress,
                'unlocked_memories': self.character_background.unlocked_memories
            },
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
        
        # Restore enhanced features
        if 'moral_alignment' in data:
            for alignment in MoralAlignment:
                if alignment.value == data['moral_alignment']:
                    player.moral_alignment = alignment
                    break
        
        if 'morality_points' in data:
            player.morality_points = data['morality_points']
        
        if 'reputation' in data:
            player.reputation = data['reputation']
        
        if 'stamina_system' in data:
            from stamina_system import StaminaSystem
            player.stamina_system = StaminaSystem.from_dict(data['stamina_system'])
        
        if 'character_background' in data:
            bg_data = data['character_background']
            player.character_background.backstory = bg_data.get('backstory', '')
            player.character_background.personal_goals = bg_data.get('personal_goals', [])
            player.character_background.fears = bg_data.get('fears', [])
            player.character_background.motivations = bg_data.get('motivations', [])
            player.character_background.significant_events = bg_data.get('significant_events', [])
            player.character_background.character_arc_progress = bg_data.get('character_arc_progress', 0)
            player.character_background.unlocked_memories = bg_data.get('unlocked_memories', [])
        
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