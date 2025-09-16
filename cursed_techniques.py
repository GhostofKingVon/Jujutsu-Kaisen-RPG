"""
Cursed Techniques System

Defines canon and original cursed techniques from the Jujutsu Kaisen universe,
including their effects, requirements, and progression.
"""

from typing import Dict, List, Any, Optional
from character import CursedTechnique
import random


class TechniqueLibrary:
    """Library of all available cursed techniques in the game."""
    
    def __init__(self):
        self.techniques = {}
        self._initialize_techniques()
    
    def _initialize_techniques(self):
        """Initialize all cursed techniques."""
        # Basic Techniques (Available early)
        self.techniques["cursed_energy_strike"] = CursedTechnique(
            "Cursed Energy Strike",
            damage=25,
            cost=10,
            description="A basic attack enhanced with cursed energy.",
            technique_type="offensive"
        )
        
        self.techniques["cursed_energy_guard"] = CursedTechnique(
            "Cursed Energy Guard",
            damage=0,
            cost=15,
            description="Defensive technique that reduces incoming damage.",
            technique_type="defensive"
        )
        
        # Canon JJK Techniques - Yuji Itadori Line
        self.techniques["divergent_fist"] = CursedTechnique(
            "Divergent Fist",
            damage=35,
            cost=15,
            description="A delayed cursed energy impact that follows the physical blow.",
            technique_type="offensive",
            cooldown=2
        )
        
        self.techniques["black_flash"] = CursedTechnique(
            "Black Flash",
            damage=80,
            cost=30,
            description="A critical hit with cursed energy applied within 0.000001 seconds of impact.",
            technique_type="offensive",
            cooldown=5
        )
        
        # Megumi Fushiguro - Ten Shadows Technique Line
        self.techniques["divine_dogs"] = CursedTechnique(
            "Divine Dogs",
            damage=40,
            cost=25,
            description="Summon divine dogs to attack the enemy.",
            technique_type="offensive",
            cooldown=3
        )
        
        self.techniques["nue"] = CursedTechnique(
            "Nue", 
            damage=50,
            cost=35,
            description="Summon the flying shikigami Nue with electrical attacks.",
            technique_type="offensive",
            cooldown=4
        )
        
        self.techniques["great_serpent"] = CursedTechnique(
            "Great Serpent",
            damage=60,
            cost=40,
            description="Summon a massive serpent shikigami.",
            technique_type="offensive", 
            cooldown=5
        )
        
        self.techniques["max_elephant"] = CursedTechnique(
            "Max Elephant",
            damage=90,
            cost=60,
            description="Summon the massive elephant shikigami with tremendous force.",
            technique_type="offensive",
            cooldown=6
        )
        
        # Nobara Kugisaki - Straw Doll Technique Line
        self.techniques["straw_doll"] = CursedTechnique(
            "Straw Doll Technique",
            damage=45,
            cost=30,
            description="Use cursed energy to damage enemies through connection.",
            technique_type="offensive",
            cooldown=3
        )
        
        self.techniques["resonance"] = CursedTechnique(
            "Resonance",
            damage=70,
            cost=45,
            description="Create sympathetic resonance for devastating damage.",
            technique_type="offensive",
            cooldown=5
        )
        
        self.techniques["hairpin"] = CursedTechnique(
            "Hairpin",
            damage=55,
            cost=35,
            description="Enhanced nail attacks with explosive cursed energy.",
            technique_type="offensive",
            cooldown=3
        )
        
        # Satoru Gojo - Limitless Technique Line
        self.techniques["limitless_blue"] = CursedTechnique(
            "Limitless: Blue",
            damage=60,
            cost=40,
            description="Creates an attractive force that pulls and damages enemies.",
            technique_type="offensive",
            cooldown=4
        )
        
        self.techniques["limitless_red"] = CursedTechnique(
            "Limitless: Red",
            damage=75,
            cost=50,
            description="Creates a repulsive force that pushes and damages enemies.",
            technique_type="offensive",
            cooldown=5
        )
        
        self.techniques["hollow_purple"] = CursedTechnique(
            "Hollow Purple",
            damage=120,
            cost=80,
            description="The combination of Blue and Red creating imaginary mass.",
            technique_type="offensive",
            cooldown=8
        )
        
        # Toge Inumaki - Cursed Speech Line
        self.techniques["cursed_speech_stop"] = CursedTechnique(
            "Cursed Speech: Stop",
            damage=0,
            cost=35,
            description="Force the enemy to stop moving for one turn.",
            technique_type="utility",
            cooldown=4
        )
        
        self.techniques["cursed_speech_sleep"] = CursedTechnique(
            "Cursed Speech: Sleep",
            damage=0,
            cost=50,
            description="Force weaker enemies to fall unconscious.",
            technique_type="utility",
            cooldown=6
        )
        
        self.techniques["cursed_speech_explode"] = CursedTechnique(
            "Cursed Speech: Explode",
            damage=85,
            cost=60,
            description="Command objects to explode near the enemy.",
            technique_type="offensive",
            cooldown=7
        )
        
        # Aoi Todo - Boogie Woogie Line
        self.techniques["boogie_woogie"] = CursedTechnique(
            "Boogie Woogie",
            damage=0,
            cost=25,
            description="Switch positions to confuse the enemy and set up attacks.",
            technique_type="utility",
            cooldown=3
        )
        
        self.techniques["simple_domain"] = CursedTechnique(
            "Simple Domain",
            damage=0,
            cost=40,
            description="Create a barrier that neutralizes domain effects.",
            technique_type="defensive",
            cooldown=5
        )
        
        # Maki Zenin - Heavenly Restriction Line
        self.techniques["weapon_mastery"] = CursedTechnique(
            "Weapon Mastery",
            damage=50,
            cost=20,
            description="Enhanced weapon techniques with superior skill.",
            technique_type="offensive",
            cooldown=2
        )
        
        self.techniques["superhuman_strength"] = CursedTechnique(
            "Superhuman Strength",
            damage=65,
            cost=25,
            description="Physical prowess beyond normal human limits.",
            technique_type="offensive",
            cooldown=3
        )
        
        self.techniques["precognition"] = CursedTechnique(
            "Precognition",
            damage=0,
            cost=30,
            description="Supernatural awareness allows perfect dodging.",
            technique_type="defensive",
            cooldown=4
        )
        
        # Domain Expansion Techniques (High Level)
        self.techniques["infinite_void"] = CursedTechnique(
            "Domain Expansion: Infinite Void",
            damage=150,
            cost=100,
            description="Gojo's domain that overwhelms with infinite information.",
            technique_type="domain",
            cooldown=10
        )
        
        self.techniques["chimera_shadow_garden"] = CursedTechnique(
            "Domain Expansion: Chimera Shadow Garden",
            damage=130,
            cost=90,
            description="Megumi's shadow domain with unlimited shikigami.",
            technique_type="domain",
            cooldown=10
        )
        
        # Original Techniques
        self.techniques["wukong_technique"] = CursedTechnique(
            "Wukong Technique",
            damage=60,
            cost=40,
            description="Original technique inspired by the Monkey King's agility and strength.",
            technique_type="offensive",
            cooldown=4
        )
        
        self.techniques["ultra_instinct_monkey"] = CursedTechnique(
            "Ultra Instinct Monkey",
            damage=0,
            cost=50,
            description="Transformation granting enhanced reflexes and combat instincts.",
            technique_type="transformation",
            cooldown=8
        )
        
        self.techniques["monkey_king_staff"] = CursedTechnique(
            "Monkey King Staff",
            damage=70,
            cost=45,
            description="Summon an extendable staff with devastating power.",
            technique_type="offensive",
            cooldown=5
        )
        
        # Reverse Cursed Technique Line
        self.techniques["reverse_cursed_healing"] = CursedTechnique(
            "Reverse Cursed Technique: Healing",
            damage=-50,  # Negative damage = healing
            cost=60,
            description="Use reverse cursed energy to heal wounds.",
            technique_type="healing",
            cooldown=6
        )
        
        self.techniques["rct_regeneration"] = CursedTechnique(
            "RCT: High-Speed Regeneration", 
            damage=-80,
            cost=80,
            description="Rapidly regenerate from severe injuries.",
            technique_type="healing",
            cooldown=8
        )
        
        # Special Grades and Curse Techniques
        self.techniques["idle_transfiguration"] = CursedTechnique(
            "Idle Transfiguration",
            damage=100,
            cost=70,
            description="Alter the enemy's soul structure for massive damage.",
            technique_type="special",
            cooldown=7
        )
        
        self.techniques["disaster_flames"] = CursedTechnique(
            "Disaster Flames",
            damage=95,
            cost=65,
            description="Jogo's volcanic cursed technique.",
            technique_type="offensive",
            cooldown=6
        )
        
        self.techniques["maximum_meteor"] = CursedTechnique(
            "Maximum: Meteor",
            damage=140,
            cost=85,
            description="Summon a massive meteor attack.",
            technique_type="maximum",
            cooldown=9
        )
        
        self.techniques["divergent_fist"] = CursedTechnique(
            "Divergent Fist",
            damage=35,
            cost=15,
            description="A delayed cursed energy impact that follows the physical blow.",
            technique_type="offensive",
            cooldown=2
        )
        
        # Gojo-inspired techniques
        self.techniques["limitless_blue"] = CursedTechnique(
            "Limitless: Blue",
            damage=60,
            cost=40,
            description="Creates an attractive force that pulls and damages enemies.",
            technique_type="offensive",
            cooldown=4
        )
        
        self.techniques["limitless_red"] = CursedTechnique(
            "Limitless: Red",
            damage=75,
            cost=50,
            description="Creates a repulsive force that pushes and damages enemies.",
            technique_type="offensive",
            cooldown=5
        )
        
        # Megumi-inspired techniques
        self.techniques["divine_dogs"] = CursedTechnique(
            "Divine Dogs",
            damage=40,
            cost=25,
            description="Summon divine dogs to attack the enemy.",
            technique_type="offensive",
            cooldown=3
        )
        
        self.techniques["shadow_clone"] = CursedTechnique(
            "Shadow Clone",
            damage=35,
            cost=25,
            description="Create a shadow clone to attack the enemy.",
            technique_type="offensive",
            cooldown=2
        )
        
        # Nobara-inspired techniques
        self.techniques["straw_doll"] = CursedTechnique(
            "Straw Doll Technique",
            damage=45,
            cost=30,
            description="Use cursed energy to damage enemies through connection.",
            technique_type="offensive",
            cooldown=3
        )
        
        # Maki-inspired techniques
        self.techniques["weapon_mastery"] = CursedTechnique(
            "Weapon Mastery",
            damage=50,
            cost=20,
            description="Enhanced weapon techniques with superior skill.",
            technique_type="offensive",
            cooldown=2
        )
        
        # Inumaki-inspired techniques
        self.techniques["cursed_speech"] = CursedTechnique(
            "Cursed Speech: Stop",
            damage=0,
            cost=35,
            description="Force the enemy to stop moving for one turn.",
            technique_type="utility",
            cooldown=4
        )
        
        # Todo-inspired techniques
        self.techniques["boogie_woogie"] = CursedTechnique(
            "Boogie Woogie",
            damage=0,
            cost=25,
            description="Switch positions to confuse the enemy and set up attacks.",
            technique_type="utility",
            cooldown=3
        )
        
        # Original Techniques
        
        # Wukong-inspired techniques (Original)
        self.techniques["wukong_technique"] = CursedTechnique(
            "Wukong Technique",
            damage=60,
            cost=40,
            description="Original technique inspired by the Monkey King's agility and strength.",
            technique_type="offensive",
            cooldown=4
        )
        
        self.techniques["monkey_king_staff"] = CursedTechnique(
            "Monkey King's Staff",
            damage=55,
            cost=35,
            description="Manifest a powerful staff with extending reach and devastating power.",
            technique_type="offensive",
            cooldown=3
        )
        
        self.techniques["seventy_two_transformations"] = CursedTechnique(
            "Seventy-Two Transformations",
            damage=0,
            cost=45,
            description="Change form to adapt to different combat situations.",
            technique_type="utility",
            cooldown=6
        )
        
        self.techniques["cloud_somersault"] = CursedTechnique(
            "Cloud Somersault",
            damage=30,
            cost=20,
            description="Swift movement technique that can evade and strike simultaneously.",
            technique_type="offensive",
            cooldown=2
        )
        
        # Ultra Instinct Monkey techniques
        self.techniques["ultra_instinct_strike"] = CursedTechnique(
            "Ultra Instinct Strike",
            damage=90,
            cost=50,
            description="A perfectly timed strike that bypasses most defenses.",
            technique_type="offensive",
            cooldown=6
        )
        
        self.techniques["autonomous_counter"] = CursedTechnique(
            "Autonomous Counter",
            damage=70,
            cost=40,
            description="Body moves automatically to counter any attack.",
            technique_type="defensive",
            cooldown=5
        )
        
        # Advanced original techniques
        self.techniques["cursed_energy_burst"] = CursedTechnique(
            "Cursed Energy Burst",
            damage=50,
            cost=35,
            description="A powerful burst of raw cursed energy.",
            technique_type="offensive",
            cooldown=3
        )
        
        self.techniques["energy_drain"] = CursedTechnique(
            "Energy Drain",
            damage=25,
            cost=20,
            description="Drain the enemy's cursed energy while dealing damage.",
            technique_type="offensive",
            cooldown=4
        )
        
        self.techniques["barrier_technique"] = CursedTechnique(
            "Barrier Technique",
            damage=0,
            cost=30,
            description="Create a protective barrier that reduces damage for several turns.",
            technique_type="defensive",
            cooldown=5
        )
        
        # Domain Expansion techniques (Late game)
        self.techniques["infinite_void"] = CursedTechnique(
            "Domain Expansion: Infinite Void",
            damage=100,
            cost=80,
            description="Create a domain where enemies are overwhelmed with infinite information.",
            technique_type="offensive",
            cooldown=10
        )
        
        self.techniques["malevolent_shrine"] = CursedTechnique(
            "Domain Expansion: Malevolent Shrine",
            damage=120,
            cost=90,
            description="Create a domain of slashing attacks that cannot be avoided.",
            technique_type="offensive",
            cooldown=12
        )
    
    def get_technique(self, technique_name: str) -> Optional[CursedTechnique]:
        """Get a technique by name."""
        if technique_name in self.techniques:
            # Return a copy to avoid modifying the original
            original = self.techniques[technique_name]
            return CursedTechnique(
                original.name,
                original.damage,
                original.cost,
                original.description,
                original.technique_type,
                original.cooldown
            )
        return None
    
    def get_techniques_by_level(self, level: int) -> List[str]:
        """Get technique names available at a specific level."""
        available = []
        
        # Level-based availability
        if level >= 1:
            available.extend(["cursed_energy_strike", "cursed_energy_guard"])
        
        if level >= 3:
            available.extend(["shadow_clone", "divergent_fist"])
        
        if level >= 5:
            available.extend(["cursed_energy_burst", "divine_dogs"])
        
        if level >= 7:
            available.extend(["wukong_technique", "straw_doll"])
        
        if level >= 10:
            available.extend(["black_flash", "weapon_mastery", "monkey_king_staff"])
        
        if level >= 12:
            available.extend(["limitless_blue", "boogie_woogie", "cloud_somersault"])
        
        if level >= 15:
            available.extend(["limitless_red", "cursed_speech", "energy_drain"])
        
        if level >= 18:
            available.extend(["ultra_instinct_strike", "seventy_two_transformations"])
        
        if level >= 20:
            available.extend(["autonomous_counter", "barrier_technique"])
        
        if level >= 25:
            available.extend(["infinite_void"])
        
        if level >= 30:
            available.extend(["malevolent_shrine"])
        
        return available
    
    def get_techniques_by_trait(self, dominant_traits: List) -> List[str]:
        """Get techniques that match character traits."""
        trait_techniques = []
        
        for trait in dominant_traits:
            if trait.value == "Compassionate":
                trait_techniques.extend(["barrier_technique", "cursed_energy_guard"])
            elif trait.value == "Focused":
                trait_techniques.extend(["black_flash", "ultra_instinct_strike"])
            elif trait.value == "Aggressive":
                trait_techniques.extend(["cursed_energy_burst", "malevolent_shrine"])
            elif trait.value == "Protective":
                trait_techniques.extend(["divine_dogs", "barrier_technique"])
            elif trait.value == "Analytical":
                trait_techniques.extend(["boogie_woogie", "seventy_two_transformations"])
            elif trait.value == "Reckless":
                trait_techniques.extend(["divergent_fist", "limitless_red"])
            elif trait.value == "Determined":
                trait_techniques.extend(["wukong_technique", "autonomous_counter"])
            elif trait.value == "Cautious":
                trait_techniques.extend(["shadow_clone", "cursed_speech"])
        
        return trait_techniques


class TechniqueEffects:
    """Handles special effects and interactions of cursed techniques."""
    
    @staticmethod
    def apply_black_flash_effect(user, target):
        """Apply Black Flash critical hit effect."""
        # Black Flash has a chance to stun and restore cursed energy
        if random.random() < 0.3:
            target.add_status_effect("stunned", 1)
            print(f"💫 Black Flash stuns {target.name}!")
        
        # Restore cursed energy to user
        restored = user.restore_cursed_energy(15)
        if restored > 0:
            print(f"⚡ {user.name} gains {restored} cursed energy from Black Flash!")
    
    @staticmethod
    def apply_limitless_blue_effect(user, target):
        """Apply Limitless Blue attractive force effect."""
        # Blue has a chance to pull enemy into a follow-up attack
        if random.random() < 0.4:
            target.add_status_effect("pulled", 1)
            print(f"🌀 {target.name} is pulled by the attractive force!")
    
    @staticmethod
    def apply_limitless_red_effect(user, target):
        """Apply Limitless Red repulsive force effect."""
        # Red has a chance to push enemy away, reducing their next attack
        if random.random() < 0.4:
            target.add_status_effect("pushed", 2)
            print(f"💥 {target.name} is pushed back by the repulsive force!")
    
    @staticmethod
    def apply_cursed_speech_effect(user, target):
        """Apply Cursed Speech utility effect."""
        # Force target to skip their next action
        target.add_status_effect("commanded", 1)
        print(f"🗣️ {target.name} is compelled by Cursed Speech!")
    
    @staticmethod
    def apply_boogie_woogie_effect(user, target):
        """Apply Boogie Woogie position switch effect."""
        # Confuse the enemy and set up for enhanced next attack
        target.add_status_effect("confused", 2)
        user.add_status_effect("positioned", 1)
        print(f"🔄 Positions switched! {target.name} is confused!")
    
    @staticmethod
    def apply_wukong_effect(user, target):
        """Apply Wukong technique Monkey King effect."""
        # Chance to gain agility boost and extra action
        if random.random() < 0.3:
            user.add_status_effect("agile", 3)
            print(f"🐒 {user.name} gains monkey-like agility!")
        
        # Always restores some cursed energy
        restored = user.restore_cursed_energy(10)
        if restored > 0:
            print(f"🌟 Wukong's wisdom restores {restored} cursed energy!")
    
    @staticmethod
    def apply_energy_drain_effect(user, target):
        """Apply Energy Drain vampire effect."""
        # Drain cursed energy from target and give to user
        drained = min(20, target.cursed_energy)
        target.cursed_energy -= drained
        user.restore_cursed_energy(drained)
        
        if drained > 0:
            print(f"🧛 {user.name} drains {drained} cursed energy from {target.name}!")
    
    @staticmethod
    def apply_barrier_effect(user, target):
        """Apply Barrier technique protective effect."""
        # Create a strong defensive barrier
        user.add_status_effect("barrier", 4)
        print(f"🛡️ {user.name} creates a protective barrier!")
    
    @staticmethod
    def apply_domain_expansion_effect(user, target, domain_name: str):
        """Apply Domain Expansion overwhelming effect."""
        print(f"🌐 DOMAIN EXPANSION: {domain_name.upper()}!")
        
        if "Infinite Void" in domain_name:
            # Overwhelm with information, causing paralysis
            target.add_status_effect("overwhelmed", 3)
            target.add_status_effect("paralyzed", 2)
            print(f"♾️ {target.name} is overwhelmed by infinite information!")
        
        elif "Malevolent Shrine" in domain_name:
            # Guaranteed hit with slashing attacks
            target.add_status_effect("marked", 3)
            print(f"⛩️ {target.name} is marked by the malevolent shrine!")


def get_technique_library() -> TechniqueLibrary:
    """Get the global technique library instance."""
    return TechniqueLibrary()