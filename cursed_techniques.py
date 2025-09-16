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
        
        # Elemental Mastery Techniques
        
        # Flame Element techniques
        self.techniques["crimson_inferno"] = CursedTechnique(
            "Crimson Inferno",
            damage=80,
            cost=30,
            description="Channel cursed energy through flames to create devastating fire attacks that burn enemies over time.",
            technique_type="offensive",
            cooldown=5
        )
        
        self.techniques["ember_strike"] = CursedTechnique(
            "Ember Strike",
            damage=35,
            cost=15,
            description="A precise attack that ignites cursed energy on impact, causing delayed burning damage.",
            technique_type="offensive",
            cooldown=2
        )
        
        # Void Element techniques
        self.techniques["void_grasp"] = CursedTechnique(
            "Void Grasp",
            damage=60,
            cost=40,
            description="Manipulate the void between spaces to pull enemies into damaging dimensional tears.",
            technique_type="offensive",
            cooldown=4
        )
        
        self.techniques["dimensional_rift"] = CursedTechnique(
            "Dimensional Rift",
            damage=75,
            cost=50,
            description="Tear open a rift in space that violently expels enemies with crushing void energy.",
            technique_type="offensive",
            cooldown=5
        )
        
        # Nature Bond techniques
        self.techniques["thorn_guardians"] = CursedTechnique(
            "Thorn Guardians",
            damage=40,
            cost=25,
            description="Summon plant-like cursed spirits that protect you while attacking enemies with razor-sharp thorns.",
            technique_type="offensive",
            cooldown=3
        )
        
        self.techniques["spirit_mirage"] = CursedTechnique(
            "Spirit Mirage",
            damage=35,
            cost=25,
            description="Create ethereal copies of yourself that confuse enemies and strike from unexpected angles.",
            technique_type="offensive",
            cooldown=2
        )
        
        # Soul Resonance techniques
        self.techniques["soul_pierce"] = CursedTechnique(
            "Soul Pierce",
            damage=45,
            cost=30,
            description="Channel cursed energy to directly attack the enemy's soul, bypassing physical defenses.",
            technique_type="offensive",
            cooldown=3
        )
        
        # Temporal Arts techniques
        self.techniques["time_dilation"] = CursedTechnique(
            "Time Dilation",
            damage=50,
            cost=20,
            description="Manipulate time around yourself to move faster and strike with temporal-enhanced precision.",
            technique_type="offensive",
            cooldown=2
        )
        
        # Mind Arts techniques
        self.techniques["psychic_command"] = CursedTechnique(
            "Psychic Command",
            damage=0,
            cost=35,
            description="Project your will to force enemies to hesitate and lose their next action.",
            technique_type="utility",
            cooldown=4
        )
        
        # Quantum techniques
        self.techniques["quantum_shift"] = CursedTechnique(
            "Quantum Shift",
            damage=0,
            cost=25,
            description="Phase between quantum states to confuse enemies and position for devastating attacks.",
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
        
        # Original Domain Expansion techniques (Late game)
        self.techniques["eternal_nexus"] = CursedTechnique(
            "Domain Expansion: Eternal Nexus",
            damage=100,
            cost=80,
            description="Create a domain where time flows differently, allowing multiple attacks while enemies are slowed.",
            technique_type="offensive",
            cooldown=10
        )
        
        self.techniques["voidborne_cathedral"] = CursedTechnique(
            "Domain Expansion: Voidborne Cathedral",
            damage=120,
            cost=90,
            description="Manifest a domain of pure void energy where enemies are torn apart by dimensional forces.",
            technique_type="offensive",
            cooldown=12
        )
        
        # Master-level Original Techniques
        self.techniques["harmonic_resonance"] = CursedTechnique(
            "Harmonic Resonance",
            damage=95,
            cost=55,
            description="Synchronize cursed energy with reality's frequency to phase through defenses and strike directly.",
            technique_type="offensive",
            cooldown=7
        )
        
        self.techniques["astral_projection"] = CursedTechnique(
            "Astral Projection",
            damage=85,
            cost=60,
            description="Project your consciousness to attack enemies from multiple dimensional angles simultaneously.",
            technique_type="offensive",
            cooldown=8
        )
        
        self.techniques["entropy_manipulation"] = CursedTechnique(
            "Entropy Manipulation",
            damage=70,
            cost=45,
            description="Accelerate decay and chaos around enemies, weakening them while strengthening yourself.",
            technique_type="offensive",
            cooldown=6
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
            available.extend(["spirit_mirage", "ember_strike"])
        
        if level >= 5:
            available.extend(["cursed_energy_burst", "thorn_guardians"])
        
        if level >= 7:
            available.extend(["wukong_technique", "soul_pierce"])
        
        if level >= 10:
            available.extend(["crimson_inferno", "time_dilation", "monkey_king_staff"])
        
        if level >= 12:
            available.extend(["void_grasp", "quantum_shift", "cloud_somersault"])
        
        if level >= 15:
            available.extend(["dimensional_rift", "psychic_command", "energy_drain"])
        
        if level >= 18:
            available.extend(["ultra_instinct_strike", "seventy_two_transformations"])
        
        if level >= 20:
            available.extend(["autonomous_counter", "barrier_technique"])
        
        if level >= 22:
            available.extend(["entropy_manipulation"])
        
        if level >= 25:
            available.extend(["eternal_nexus", "harmonic_resonance"])
        
        if level >= 28:
            available.extend(["astral_projection"])
        
        if level >= 30:
            available.extend(["voidborne_cathedral"])
        
        return available
    
    def get_techniques_by_trait(self, dominant_traits: List) -> List[str]:
        """Get techniques that match character traits."""
        trait_techniques = []
        
        for trait in dominant_traits:
            if trait.value == "Compassionate":
                trait_techniques.extend(["barrier_technique", "cursed_energy_guard", "thorn_guardians"])
            elif trait.value == "Focused":
                trait_techniques.extend(["crimson_inferno", "ultra_instinct_strike", "harmonic_resonance"])
            elif trait.value == "Aggressive":
                trait_techniques.extend(["cursed_energy_burst", "voidborne_cathedral", "entropy_manipulation"])
            elif trait.value == "Protective":
                trait_techniques.extend(["thorn_guardians", "barrier_technique", "astral_projection"])
            elif trait.value == "Analytical":
                trait_techniques.extend(["quantum_shift", "seventy_two_transformations", "time_dilation"])
            elif trait.value == "Reckless":
                trait_techniques.extend(["ember_strike", "dimensional_rift", "entropy_manipulation"])
            elif trait.value == "Determined":
                trait_techniques.extend(["wukong_technique", "autonomous_counter", "harmonic_resonance"])
            elif trait.value == "Cautious":
                trait_techniques.extend(["spirit_mirage", "psychic_command", "astral_projection"])
        
        return trait_techniques


class TechniqueEffects:
    """Handles special effects and interactions of cursed techniques."""
    
    @staticmethod
    def apply_crimson_inferno_effect(user, target):
        """Apply Crimson Inferno burning effect."""
        # Burning effect over time
        target.add_status_effect("burning", 3)
        print(f"🔥 {target.name} is set ablaze by the Crimson Inferno!")
        
        # Restore some cursed energy to user from the flames
        restored = user.restore_cursed_energy(12)
        if restored > 0:
            print(f"🔥 The flames restore {restored} cursed energy to {user.name}!")
    
    @staticmethod
    def apply_void_grasp_effect(user, target):
        """Apply Void Grasp dimensional tear effect."""
        # Void tears have a chance to pull enemy into vulnerable state
        if random.random() < 0.4:
            target.add_status_effect("void_touched", 2)
            print(f"🌌 {target.name} is marked by the void!")
    
    @staticmethod
    def apply_dimensional_rift_effect(user, target):
        """Apply Dimensional Rift crushing void effect."""
        # Rift has a chance to disorient and weaken enemy
        if random.random() < 0.5:
            target.add_status_effect("disoriented", 3)
            target.add_status_effect("weakened", 2)
            print(f"🕳️ {target.name} is crushed by dimensional forces!")
    
    @staticmethod
    def apply_psychic_command_effect(user, target):
        """Apply Psychic Command mind control effect."""
        # Force target to skip their next action
        target.add_status_effect("mind_controlled", 1)
        print(f"🧠 {target.name} is controlled by psychic force!")
    
    @staticmethod
    def apply_quantum_shift_effect(user, target):
        """Apply Quantum Shift phase effect."""
        # Confuse the enemy and set up for enhanced next attack
        target.add_status_effect("phased", 2)
        user.add_status_effect("quantum_advantage", 1)
        print(f"⚛️ Quantum state shifted! {target.name} is phased!")
    
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
    def apply_time_dilation_effect(user, target):
        """Apply Time Dilation temporal effect."""
        # Speed boost and chance for extra action
        user.add_status_effect("time_dilated", 2)
        if random.random() < 0.3:
            user.add_status_effect("extra_action", 1)
        print(f"⏰ {user.name} moves through dilated time!")
    
    @staticmethod
    def apply_soul_pierce_effect(user, target):
        """Apply Soul Pierce spiritual damage effect."""
        # Bypasses physical defenses and causes spiritual trauma
        target.add_status_effect("soul_damaged", 3)
        print(f"👻 {target.name}'s soul is pierced and damaged!")
    
    @staticmethod
    def apply_thorn_guardians_effect(user, target):
        """Apply Thorn Guardians nature spirit effect."""
        # Summon protective spirits that counter-attack
        user.add_status_effect("thorn_protection", 4)
        print(f"🌿 Thorn Guardians protect {user.name}!")
    
    @staticmethod
    def apply_harmonic_resonance_effect(user, target):
        """Apply Harmonic Resonance reality sync effect."""
        # Phase through defenses and resonate with reality
        target.add_status_effect("resonance_vulnerable", 2)
        user.add_status_effect("reality_synced", 2)
        print(f"🎵 {user.name} resonates with reality itself!")
    
    @staticmethod
    def apply_entropy_manipulation_effect(user, target):
        """Apply Entropy Manipulation chaos effect."""
        # Accelerate decay in enemy while strengthening user
        target.add_status_effect("decaying", 4)
        user.add_status_effect("entropy_mastery", 2)
        print(f"🌀 Entropy bends to {user.name}'s will!")
    
    @staticmethod
    def apply_domain_expansion_effect(user, target, domain_name: str):
        """Apply Domain Expansion overwhelming effect."""
        print(f"🌐 DOMAIN EXPANSION: {domain_name.upper()}!")
        
        if "Eternal Nexus" in domain_name:
            # Time manipulation domain
            target.add_status_effect("time_locked", 3)
            user.add_status_effect("temporal_mastery", 3)
            print(f"⏳ {target.name} is locked in temporal stasis!")
        
        elif "Voidborne Cathedral" in domain_name:
            # Void energy domain
            target.add_status_effect("void_consumed", 3)
            target.add_status_effect("reality_torn", 2)
            print(f"🌌 {target.name} is consumed by void forces!")


def get_technique_library() -> TechniqueLibrary:
    """Get the global technique library instance."""
    return TechniqueLibrary()