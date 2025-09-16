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
        
        # Canon JJK Techniques with enhanced descriptions
        
        # Yuji-inspired techniques
        self.techniques["black_flash"] = CursedTechnique(
            "Black Flash",
            damage=80,
            cost=30,
            description="⚡ A critical hit with cursed energy applied within 0.000001 seconds of impact. The perfect synchronization of body and soul, creating a flash of black lightning that transcends normal limits.",
            technique_type="offensive",
            cooldown=5
        )
        
        self.techniques["divergent_fist"] = CursedTechnique(
            "Divergent Fist",
            damage=35,
            cost=15,
            description="💥 A delayed cursed energy impact that follows the physical blow. The lag in cursed energy creates a devastating two-hit combo that catches enemies off guard.",
            technique_type="offensive",
            cooldown=2
        )
        
        # Gojo-inspired techniques with enhanced descriptions
        self.techniques["limitless_blue"] = CursedTechnique(
            "Limitless: Blue",
            damage=60,
            cost=40,
            description="🌀 Manipulates space to create an attractive force of infinite magnitude. Reality bends as negative space pulls everything into its inescapable embrace.",
            technique_type="offensive",
            cooldown=4
        )
        
        self.techniques["limitless_red"] = CursedTechnique(
            "Limitless: Red",
            damage=75,
            cost=50,
            description="🔴 The reversal of Blue creates a repulsive force that obliterates anything in its path. Space itself rejects the target's existence.",
            technique_type="offensive",
            cooldown=5
        )
        
        # Megumi-inspired techniques with enhanced descriptions
        self.techniques["divine_dogs"] = CursedTechnique(
            "Divine Dogs",
            damage=40,
            cost=25,
            description="🐺 Summon loyal shadow wolves that emerge from darkness itself. These divine beasts hunt as one, their howls echoing from the shadow realm.",
            technique_type="offensive",
            cooldown=3
        )
        
        self.techniques["shadow_clone"] = CursedTechnique(
            "Shadow Clone",
            damage=35,
            cost=25,
            description="👤 Manipulate shadows to create a perfect duplicate. Born from darkness, it mirrors your every movement while hiding your true location.",
            technique_type="offensive",
            cooldown=2
        )
        
        # Nobara-inspired techniques with enhanced descriptions
        self.techniques["straw_doll"] = CursedTechnique(
            "Straw Doll Technique",
            damage=45,
            cost=30,
            description="🎎 Channel cursed energy through sympathetic connection. The doll becomes a conduit for pain, striking at the very essence of the target's being.",
            technique_type="offensive",
            cooldown=3
        )
        
        # Enhanced original techniques with awakening potential
        
        # Wukong-inspired techniques (Original) with mythical descriptions
        self.techniques["wukong_technique"] = CursedTechnique(
            "Wukong Technique",
            damage=60,
            cost=40,
            description="🐒 Channel the legendary Monkey King's boundless spirit. Ancient wisdom flows through your movements as you embody the trickster god's divine martial arts.",
            technique_type="offensive",
            cooldown=4
        )
        
        self.techniques["monkey_king_staff"] = CursedTechnique(
            "Monkey King's Staff",
            damage=55,
            cost=35,
            description="🥢 Manifest the legendary Ruyi Jingu Bang, a staff that can extend infinitely and weighs as much as a mountain. It responds only to one with a true monkey's heart.",
            technique_type="offensive",
            cooldown=3
        )
        
        self.techniques["seventy_two_transformations"] = CursedTechnique(
            "Seventy-Two Transformations",
            damage=0,
            cost=45,
            description="✨ Master the art of infinite change. Your cursed energy becomes fluid like water, adapting to any situation with the wisdom of the immortal sage.",
            technique_type="utility",
            cooldown=6
        )
        
        self.techniques["cloud_somersault"] = CursedTechnique(
            "Cloud Somersault",
            damage=30,
            cost=20,
            description="☁️ Move with the speed of wind and the grace of clouds. A single leap can carry you 108,000 li, striking like lightning from impossible angles.",
            technique_type="offensive",
            cooldown=2
        )
        
        # Ultra Instinct Monkey techniques with awakening descriptions
        self.techniques["ultra_instinct_strike"] = CursedTechnique(
            "Ultra Instinct Strike",
            damage=90,
            cost=50,
            description="💫 Transcend conscious thought as your body moves with perfect instinct. Mind becomes void, movement becomes absolute, and the strike becomes inevitable.",
            technique_type="offensive",
            cooldown=6
        )
        
        self.techniques["autonomous_counter"] = CursedTechnique(
            "Autonomous Counter",
            damage=70,
            cost=40,
            description="⚡ Your body responds faster than thought itself. Like a mirror reflecting light, every attack is met with perfect counteraction.",
            technique_type="defensive",
            cooldown=5
        )
        
        # Advanced techniques with awakening descriptions
        self.techniques["cursed_energy_burst"] = CursedTechnique(
            "Cursed Energy Burst",
            damage=50,
            cost=35,
            description="💥 Release all accumulated emotion as pure destructive force. Your very feelings become weapons that tear through reality.",
            technique_type="offensive",
            cooldown=3
        )
        
        self.techniques["energy_drain"] = CursedTechnique(
            "Energy Drain",
            damage=25,
            cost=20,
            description="🧛 Siphon the enemy's life force through cursed resonance. Their strength becomes yours as you feed on their spiritual essence.",
            technique_type="offensive",
            cooldown=4
        )
        
        self.techniques["barrier_technique"] = CursedTechnique(
            "Barrier Technique",
            damage=0,
            cost=30,
            description="🛡️ Weave cursed energy into an impenetrable shield of pure will. Your determination becomes a fortress that protects all you hold dear.",
            technique_type="defensive",
            cooldown=5
        )
        
        # Domain Expansion techniques with epic descriptions
        self.techniques["infinite_void"] = CursedTechnique(
            "Domain Expansion: Infinite Void",
            damage=100,
            cost=80,
            description="♾️ Create a realm where all information becomes infinite. Enemies drown in endless knowledge while your mind remains perfectly clear in the void.",
            technique_type="offensive",
            cooldown=10
        )
        
        self.techniques["malevolent_shrine"] = CursedTechnique(
            "Domain Expansion: Malevolent Shrine",
            damage=120,
            cost=90,
            description="⛩️ Manifest a shrine where cutting attacks are absolute. Within this sacred space, your slashes become divine judgment that cannot be avoided.",
            technique_type="offensive",
            cooldown=12
        )
        
        # New awakened techniques
        self.techniques["memories_of_resolve"] = CursedTechnique(
            "Domain Expansion: Memories of Resolve",
            damage=110,
            cost=85,
            description="🌌 Your personal journey becomes reality. Every struggle, every friendship, every moment of growth manifests as an unbreakable domain of shared resolve.",
            technique_type="offensive",
            cooldown=15
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