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
        """Initialize all cursed techniques - exactly 20 total (10 manga-inspired + 10 original)."""
        
        # === 10 MANGA-INSPIRED TECHNIQUES ===
        
        # 1. Basic Cursed Energy Strike (Yuji-inspired)
        self.techniques["cursed_energy_strike"] = CursedTechnique(
            "Cursed Energy Strike",
            damage=25,
            cost=10,
            description="A basic attack enhanced with cursed energy.",
            technique_type="offensive"
        )
        
        # 2. Black Flash (Yuji's signature)
        self.techniques["black_flash"] = CursedTechnique(
            "Black Flash",
            damage=80,
            cost=30,
            description="A critical hit with cursed energy applied within 0.000001 seconds of impact.",
            technique_type="offensive",
            cooldown=5
        )
        
        # 3. Limitless: Blue (Gojo's technique)
        self.techniques["limitless_blue"] = CursedTechnique(
            "Limitless: Blue",
            damage=60,
            cost=40,
            description="Creates an attractive force that pulls and damages enemies.",
            technique_type="offensive",
            cooldown=4
        )
        
        # 4. Divine Dogs (Megumi's shikigami)
        self.techniques["divine_dogs"] = CursedTechnique(
            "Divine Dogs",
            damage=40,
            cost=25,
            description="Summon divine dogs to attack the enemy.",
            technique_type="offensive",
            cooldown=3
        )
        
        # 5. Straw Doll Technique (Nobara's signature)
        self.techniques["straw_doll"] = CursedTechnique(
            "Straw Doll Technique",
            damage=45,
            cost=30,
            description="Use cursed energy to damage enemies through connection.",
            technique_type="offensive",
            cooldown=3
        )
        
        # 6. Cursed Speech (Inumaki's technique)
        self.techniques["cursed_speech"] = CursedTechnique(
            "Cursed Speech: Stop",
            damage=0,
            cost=35,
            description="Force the enemy to stop moving for one turn.",
            technique_type="utility",
            cooldown=4
        )
        
        # 7. Boogie Woogie (Todo's technique)
        self.techniques["boogie_woogie"] = CursedTechnique(
            "Boogie Woogie",
            damage=0,
            cost=25,
            description="Switch positions to confuse the enemy and set up attacks.",
            technique_type="utility",
            cooldown=3
        )
        
        # 8. Simple Domain (Defensive barrier)
        self.techniques["simple_domain"] = CursedTechnique(
            "Simple Domain",
            damage=0,
            cost=30,
            description="Create a protective barrier that reduces damage for several turns.",
            technique_type="defensive",
            cooldown=5
        )
        
        # 9. Domain Expansion: Infinite Void (Gojo's domain)
        self.techniques["infinite_void"] = CursedTechnique(
            "Domain Expansion: Infinite Void",
            damage=100,
            cost=80,
            description="Create a domain where enemies are overwhelmed with infinite information.",
            technique_type="offensive",
            cooldown=10
        )
        
        # 10. Reverse Cursed Technique (Healing)
        self.techniques["reverse_cursed_technique"] = CursedTechnique(
            "Reverse Cursed Technique",
            damage=-50,  # Negative damage = healing
            cost=40,
            description="Convert cursed energy into positive energy for healing.",
            technique_type="defensive",
            cooldown=6
        )
        
        # === 10 ORIGINAL TECHNIQUES - WUKONG CLAN CURSED TECHNIQUE ===
        
        # Base Wukong Techniques (untransformed)
        
        # 11. Monkey King Combo
        self.techniques["monkey_king_combo"] = CursedTechnique(
            "Monkey King Combo",
            damage=45,
            cost=25,
            description="Multi-hit melee attack with increasing damage per hit.",
            technique_type="offensive",
            cooldown=2
        )
        
        # 12. Power Pole Extend
        self.techniques["power_pole_extend"] = CursedTechnique(
            "Power Pole Extend",
            damage=55,
            cost=30,
            description="Long-range strike with extending staff that can stun enemies.",
            technique_type="offensive",
            cooldown=3
        )
        
        # 13. Ki Blast
        self.techniques["ki_blast"] = CursedTechnique(
            "Ki Blast",
            damage=35,
            cost=20,
            description="Energy projectile that pierces through defenses.",
            technique_type="offensive",
            cooldown=1
        )
        
        # 14. Cloud Dash
        self.techniques["cloud_dash"] = CursedTechnique(
            "Cloud Dash",
            damage=25,
            cost=15,
            description="Swift movement technique that enhances evasion and striking.",
            technique_type="offensive",
            cooldown=2
        )
        
        # 15. Kame Wave
        self.techniques["kame_wave"] = CursedTechnique(
            "Kame Wave",
            damage=70,
            cost=45,
            description="Powerful energy beam that devastates enemies.",
            technique_type="offensive",
            cooldown=5
        )
        
        # 16. Monkey King's Domain Expansion
        self.techniques["monkey_king_domain"] = CursedTechnique(
            "Domain Expansion: Monkey King's Paradise",
            damage=85,
            cost=70,
            description="Create a domain where the user gains immense power and agility buffs.",
            technique_type="offensive",
            cooldown=8
        )
        
        # Transformation-Enhanced Techniques
        
        # 17. Golden Combo (Super Monkey transformation)
        self.techniques["golden_combo"] = CursedTechnique(
            "Golden Combo",
            damage=65,
            cost=35,
            description="Enhanced version of Monkey King Combo with golden energy and extra hits.",
            technique_type="offensive",
            cooldown=3
        )
        
        # 18. Instinct Strike (Ultra Instinct transformation)
        self.techniques["instinct_strike"] = CursedTechnique(
            "Instinct Strike",
            damage=90,
            cost=50,
            description="Perfect strike that ignores defense and triggers automatically.",
            technique_type="offensive",
            cooldown=6
        )
        
        # 19. Ego Smash (Ultra Ego transformation)
        self.techniques["ego_smash"] = CursedTechnique(
            "Ego Smash",
            damage=75,
            cost=40,
            description="Devastating attack that scales with damage received.",
            technique_type="offensive",
            cooldown=4
        )
        
        # 20. Scarlet Barrage (Scarlet Sage transformation)
        self.techniques["scarlet_barrage"] = CursedTechnique(
            "Scarlet Barrage",
            damage=80,
            cost=45,
            description="Fused Ki moves creating a devastating combo with high critical chance.",
            technique_type="offensive",
            cooldown=5
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
        
        # Level-based availability - distributed across 20 techniques
        if level >= 1:
            available.extend(["cursed_energy_strike", "ki_blast"])
        
        if level >= 3:
            available.extend(["cloud_dash", "divine_dogs"])
        
        if level >= 5:
            available.extend(["monkey_king_combo", "straw_doll"])
        
        if level >= 7:
            available.extend(["power_pole_extend", "simple_domain"])
        
        if level >= 10:
            available.extend(["black_flash", "boogie_woogie"])
        
        if level >= 12:
            available.extend(["limitless_blue", "kame_wave"])
        
        if level >= 15:
            available.extend(["cursed_speech", "reverse_cursed_technique"])
        
        if level >= 18:
            available.extend(["golden_combo", "ego_smash"])
        
        if level >= 20:
            available.extend(["instinct_strike", "scarlet_barrage"])
        
        if level >= 25:
            available.extend(["monkey_king_domain"])
        
        if level >= 30:
            available.extend(["infinite_void"])
        
        return available
    
    def get_techniques_by_trait(self, dominant_traits: List) -> List[str]:
        """Get techniques that match character traits."""
        trait_techniques = []
        
        for trait in dominant_traits:
            if trait.value == "Compassionate":
                trait_techniques.extend(["reverse_cursed_technique", "simple_domain"])
            elif trait.value == "Focused":
                trait_techniques.extend(["black_flash", "instinct_strike"])
            elif trait.value == "Aggressive":
                trait_techniques.extend(["ego_smash", "kame_wave"])
            elif trait.value == "Protective":
                trait_techniques.extend(["divine_dogs", "simple_domain"])
            elif trait.value == "Analytical":
                trait_techniques.extend(["boogie_woogie", "cursed_speech"])
            elif trait.value == "Reckless":
                trait_techniques.extend(["golden_combo", "scarlet_barrage"])
            elif trait.value == "Determined":
                trait_techniques.extend(["monkey_king_combo", "power_pole_extend"])
            elif trait.value == "Cautious":
                trait_techniques.extend(["cloud_dash", "limitless_blue"])
        
        return trait_techniques


class TechniqueEffects:
    """Handles special effects and interactions of cursed techniques."""
    
    @staticmethod
    def apply_black_flash_effect(user, target):
        """Apply Black Flash critical hit effect."""
        # Enhanced chance if Super Monkey transformation is active
        stun_chance = 0.3
        if hasattr(user, 'current_transformation') and user.current_transformation.name == "SUPER_MONKEY":
            stun_chance = 0.5
            print("🌟 Super Monkey enhances Black Flash!")
        
        if random.random() < stun_chance:
            target.add_status_effect("stunned", 1)
            print(f"💫 Black Flash stuns {target.name}!")
        
        # Restore cursed energy to user
        restored = user.restore_cursed_energy(15)
        if restored > 0:
            print(f"⚡ {user.name} gains {restored} cursed energy from Black Flash!")
    
    @staticmethod
    def apply_limitless_blue_effect(user, target):
        """Apply Limitless Blue attractive force effect."""
        if random.random() < 0.4:
            target.add_status_effect("pulled", 1)
            print(f"🌀 {target.name} is pulled by the attractive force!")
    
    @staticmethod
    def apply_cursed_speech_effect(user, target):
        """Apply Cursed Speech utility effect."""
        target.add_status_effect("commanded", 1)
        print(f"🗣️ {target.name} is compelled by Cursed Speech!")
    
    @staticmethod
    def apply_boogie_woogie_effect(user, target):
        """Apply Boogie Woogie position switch effect."""
        target.add_status_effect("confused", 2)
        user.add_status_effect("positioned", 1)
        print(f"🔄 Positions switched! {target.name} is confused!")
    
    # === WUKONG CLAN TECHNIQUE EFFECTS ===
    
    @staticmethod
    def apply_monkey_king_combo_effect(user, target):
        """Apply Monkey King Combo multi-hit effect."""
        hits = random.randint(2, 4)
        total_damage = 0
        print(f"🐒 Monkey King Combo unleashes {hits} hits!")
        
        for i in range(hits):
            hit_damage = random.randint(10, 20)
            total_damage += hit_damage
            print(f"  Hit {i+1}: {hit_damage} damage!")
        
        return total_damage
    
    @staticmethod
    def apply_power_pole_extend_effect(user, target):
        """Apply Power Pole Extend stun effect."""
        if random.random() < 0.6:  # 60% stun chance
            target.add_status_effect("stunned", 1)
            print(f"🥢 Power Pole stuns {target.name}!")
        print(f"📏 The pole extends to its maximum reach!")
    
    @staticmethod
    def apply_ki_blast_effect(user, target):
        """Apply Ki Blast piercing effect."""
        # Ki Blast ignores some defense
        print(f"💥 Ki Blast pierces through defenses!")
        return True  # Indicates defense bypass
    
    @staticmethod
    def apply_cloud_dash_effect(user, target):
        """Apply Cloud Dash evasion boost."""
        user.add_status_effect("enhanced_evasion", 2)
        print(f"☁️ {user.name} gains enhanced evasion from Cloud Dash!")
    
    @staticmethod
    def apply_kame_wave_effect(user, target):
        """Apply Kame Wave devastating beam effect."""
        print(f"🌊 KAME WAVE! A devastating energy beam erupts!")
        # Chance to ignore armor
        if random.random() < 0.4:
            print(f"⚡ The beam overwhelms {target.name}'s defenses!")
            return True  # Defense bypass
        return False
    
    @staticmethod
    def apply_monkey_king_domain_effect(user, target):
        """Apply Monkey King's Domain Expansion effect."""
        print(f"🌐 DOMAIN EXPANSION: MONKEY KING'S PARADISE!")
        print(f"🏞️ A mystical realm of infinite agility and power manifests!")
        
        # Apply multiple buffs to user
        user.add_status_effect("domain_agility", 4)
        user.add_status_effect("domain_power", 4)
        user.add_status_effect("domain_energy", 4)
        
        # Debuff target
        target.add_status_effect("domain_suppressed", 4)
        print(f"✨ {user.name} gains incredible buffs within the domain!")
        print(f"😵 {target.name} is suppressed by the domain's power!")
    
    # === TRANSFORMATION-ENHANCED TECHNIQUE EFFECTS ===
    
    @staticmethod
    def apply_golden_combo_effect(user, target):
        """Apply Golden Combo (Super Monkey enhanced) effect."""
        print(f"🥇 GOLDEN COMBO! Enhanced with Super Monkey power!")
        hits = random.randint(3, 6)  # More hits than base combo
        total_damage = 0
        
        for i in range(hits):
            hit_damage = random.randint(15, 25)  # Higher damage per hit
            total_damage += hit_damage
            print(f"  ✨ Golden Hit {i+1}: {hit_damage} damage!")
        
        # Chance for extra stun
        if random.random() < 0.3:
            target.add_status_effect("stunned", 1)
            print(f"💫 Golden energy stuns {target.name}!")
        
        return total_damage
    
    @staticmethod
    def apply_instinct_strike_effect(user, target):
        """Apply Instinct Strike (Ultra Instinct) effect."""
        print(f"🤍 INSTINCT STRIKE! A perfect, unavoidable attack!")
        print(f"👻 The strike transcends physical limitations!")
        
        # Always hits, ignores defense, chance for critical
        if random.random() < 0.8:  # 80% crit chance
            print(f"💥 CRITICAL HIT! Instinct guides the perfect strike!")
            return 2.0  # Double damage multiplier
        return 1.5  # Still enhanced damage
    
    @staticmethod
    def apply_ego_smash_effect(user, target):
        """Apply Ego Smash (Ultra Ego) effect with damage scaling."""
        damage_taken = user.max_hp - user.hp
        scaling_multiplier = 1.0 + (damage_taken * 0.01)  # 1% per HP lost
        
        print(f"💜 EGO SMASH! Power scales with battle damage!")
        print(f"😤 Damage multiplier: {scaling_multiplier:.1f}x")
        
        return scaling_multiplier
    
    @staticmethod
    def apply_scarlet_barrage_effect(user, target):
        """Apply Scarlet Barrage (Scarlet Sage) fused Ki effect."""
        print(f"🔴 SCARLET BARRAGE! Fused Ki techniques create devastation!")
        
        # Multiple Ki-based attacks in sequence
        techniques = ["Ki Blast", "Energy Wave", "Crimson Beam"]
        total_multiplier = 1.0
        
        for technique in techniques:
            if random.random() < 0.7:  # 70% chance each technique hits
                mini_damage = random.randint(15, 25)
                total_multiplier += 0.3
                print(f"  🔥 {technique}: {mini_damage} additional damage!")
        
        # High critical chance
        if random.random() < 0.6:  # 60% crit chance
            print(f"💥 CRITICAL! Scarlet energy overwhelms the target!")
            total_multiplier *= 1.5
        
        return total_multiplier
    
    @staticmethod
    def apply_simple_domain_effect(user, target):
        """Apply Simple Domain protective effect."""
        user.add_status_effect("simple_domain", 4)
        print(f"🛡️ {user.name} creates a Simple Domain barrier!")
    
    @staticmethod
    def apply_reverse_cursed_technique_effect(user, target):
        """Apply Reverse Cursed Technique healing effect."""
        # Heal the user instead of damaging target
        heal_amount = 50
        actual_healing = user.heal(heal_amount)
        print(f"💚 {user.name} heals {actual_healing} HP with Reverse Cursed Technique!")
        
        # Small chance to also restore cursed energy
        if random.random() < 0.3:
            restored = user.restore_cursed_energy(20)
            print(f"✨ Also restored {restored} cursed energy!")
    
    @staticmethod
    def apply_domain_expansion_effect(user, target, domain_name: str):
        """Apply Domain Expansion overwhelming effect."""
        print(f"🌐 DOMAIN EXPANSION: {domain_name.upper()}!")
        
        if "Infinite Void" in domain_name:
            target.add_status_effect("overwhelmed", 3)
            target.add_status_effect("paralyzed", 2)
            print(f"♾️ {target.name} is overwhelmed by infinite information!")
        
        elif "Monkey King's Paradise" in domain_name:
            TechniqueEffects.apply_monkey_king_domain_effect(user, target)


def get_technique_library() -> TechniqueLibrary:
    """Get the global technique library instance."""
    return TechniqueLibrary()