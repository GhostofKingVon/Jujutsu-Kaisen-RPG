"""
Character Customization and Crafting System

Allows players to customize characters with outfits, accessories, skill loadouts,
and craft weapons, items, and consumables.
"""

from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
import random
from datetime import datetime


class ItemType(Enum):
    """Types of items in the game."""
    WEAPON = "weapon"
    ARMOR = "armor"
    ACCESSORY = "accessory"
    CONSUMABLE = "consumable"
    MATERIAL = "material"
    TOOL = "tool"
    OUTFIT = "outfit"


class ItemRarity(Enum):
    """Rarity levels for items."""
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"
    ARTIFACT = "artifact"


class Item:
    """Base item class."""
    
    def __init__(self, name: str, description: str, item_type: ItemType, 
                 rarity: ItemRarity, level_requirement: int = 1):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.rarity = rarity
        self.level_requirement = level_requirement
        self.stats = {}  # Stat bonuses provided by item
        self.special_effects = []  # Special abilities or effects
        self.equipped = False
        self.stack_size = 1
        self.durability = 100  # For weapons and armor
        self.max_durability = 100
        self.crafted_by = None
        self.crafted_date = None
        self.enchantments = []
    
    def add_stat_bonus(self, stat: str, value: int):
        """Add a stat bonus to the item."""
        self.stats[stat] = self.stats.get(stat, 0) + value
    
    def add_special_effect(self, effect: str, description: str):
        """Add a special effect to the item."""
        self.special_effects.append({"name": effect, "description": description})
    
    def can_equip(self, character_level: int) -> bool:
        """Check if character can equip this item."""
        return character_level >= self.level_requirement
    
    def get_display_name(self) -> str:
        """Get formatted display name with rarity color coding."""
        rarity_symbols = {
            ItemRarity.COMMON: "⚪",
            ItemRarity.UNCOMMON: "🟢",
            ItemRarity.RARE: "🔵",
            ItemRarity.EPIC: "🟣",
            ItemRarity.LEGENDARY: "🟠",
            ItemRarity.ARTIFACT: "🔴"
        }
        symbol = rarity_symbols.get(self.rarity, "⚪")
        return f"{symbol} {self.name}"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert item to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "item_type": self.item_type.value,
            "rarity": self.rarity.value,
            "level_requirement": self.level_requirement,
            "stats": self.stats,
            "special_effects": self.special_effects,
            "equipped": self.equipped,
            "durability": self.durability,
            "max_durability": self.max_durability,
            "enchantments": self.enchantments
        }


class Equipment:
    """Character equipment management."""
    
    def __init__(self):
        self.equipped_items = {
            "weapon": None,
            "armor": None,
            "accessory_1": None,
            "accessory_2": None,
            "outfit": None
        }
        self.total_stats = {}
        self.active_effects = []
    
    def equip_item(self, item: Item, slot: str = None) -> bool:
        """Equip an item to the appropriate slot."""
        if not slot:
            slot = self._get_default_slot(item.item_type)
        
        if slot not in self.equipped_items:
            return False
        
        # Unequip current item if any
        current_item = self.equipped_items[slot]
        if current_item:
            self.unequip_item(slot)
        
        # Equip new item
        self.equipped_items[slot] = item
        item.equipped = True
        self._recalculate_stats()
        
        return True
    
    def unequip_item(self, slot: str) -> Optional[Item]:
        """Unequip item from slot."""
        if slot in self.equipped_items and self.equipped_items[slot]:
            item = self.equipped_items[slot]
            item.equipped = False
            self.equipped_items[slot] = None
            self._recalculate_stats()
            return item
        return None
    
    def _get_default_slot(self, item_type: ItemType) -> str:
        """Get default equipment slot for item type."""
        slot_mapping = {
            ItemType.WEAPON: "weapon",
            ItemType.ARMOR: "armor",
            ItemType.ACCESSORY: "accessory_1",
            ItemType.OUTFIT: "outfit"
        }
        return slot_mapping.get(item_type, "accessory_1")
    
    def _recalculate_stats(self):
        """Recalculate total stats from all equipped items."""
        self.total_stats = {}
        self.active_effects = []
        
        for item in self.equipped_items.values():
            if item:
                # Add stat bonuses
                for stat, value in item.stats.items():
                    self.total_stats[stat] = self.total_stats.get(stat, 0) + value
                
                # Add special effects
                self.active_effects.extend(item.special_effects)
    
    def get_stat_bonus(self, stat: str) -> int:
        """Get total bonus for a specific stat."""
        return self.total_stats.get(stat, 0)
    
    def get_equipment_summary(self) -> str:
        """Get summary of equipped items."""
        equipped = [item.get_display_name() for item in self.equipped_items.values() if item]
        return f"Equipped: {', '.join(equipped)}" if equipped else "No items equipped"


class Inventory:
    """Character inventory management."""
    
    def __init__(self, max_capacity: int = 50):
        self.items: Dict[str, Dict[str, Any]] = {}  # item_name -> {item: Item, quantity: int}
        self.max_capacity = max_capacity
        self.current_capacity = 0
    
    def add_item(self, item: Item, quantity: int = 1) -> bool:
        """Add item to inventory."""
        if self.current_capacity + quantity > self.max_capacity:
            return False
        
        if item.name in self.items:
            self.items[item.name]["quantity"] += quantity
        else:
            self.items[item.name] = {"item": item, "quantity": quantity}
        
        self.current_capacity += quantity
        return True
    
    def remove_item(self, item_name: str, quantity: int = 1) -> bool:
        """Remove item from inventory."""
        if item_name not in self.items:
            return False
        
        if self.items[item_name]["quantity"] < quantity:
            return False
        
        self.items[item_name]["quantity"] -= quantity
        self.current_capacity -= quantity
        
        if self.items[item_name]["quantity"] == 0:
            del self.items[item_name]
        
        return True
    
    def has_item(self, item_name: str, quantity: int = 1) -> bool:
        """Check if inventory has item in required quantity."""
        return (item_name in self.items and 
                self.items[item_name]["quantity"] >= quantity)
    
    def get_item(self, item_name: str) -> Optional[Item]:
        """Get item object by name."""
        if item_name in self.items:
            return self.items[item_name]["item"]
        return None
    
    def get_items_by_type(self, item_type: ItemType) -> List[Item]:
        """Get all items of a specific type."""
        return [data["item"] for data in self.items.values() 
                if data["item"].item_type == item_type]
    
    def get_capacity_info(self) -> str:
        """Get inventory capacity information."""
        return f"Inventory: {self.current_capacity}/{self.max_capacity}"


class Recipe:
    """Crafting recipe for items."""
    
    def __init__(self, result_item: Item, materials: Dict[str, int], 
                 tools_required: List[str], skill_requirement: int = 1):
        self.result_item = result_item
        self.materials = materials  # material_name -> quantity
        self.tools_required = tools_required
        self.skill_requirement = skill_requirement
        self.crafting_time = 1  # Time units to craft
        self.success_rate = 100  # Base success rate percentage
    
    def can_craft(self, inventory: Inventory, crafting_skill: int, available_tools: List[str]) -> bool:
        """Check if recipe can be crafted."""
        # Check skill requirement
        if crafting_skill < self.skill_requirement:
            return False
        
        # Check tools
        for tool in self.tools_required:
            if tool not in available_tools:
                return False
        
        # Check materials
        for material, quantity in self.materials.items():
            if not inventory.has_item(material, quantity):
                return False
        
        return True
    
    def get_success_rate(self, crafting_skill: int) -> int:
        """Calculate success rate based on skill."""
        skill_bonus = max(0, (crafting_skill - self.skill_requirement) * 5)
        return min(100, self.success_rate + skill_bonus)


class CraftingSystem:
    """System for crafting items and equipment."""
    
    def __init__(self):
        self.recipes: Dict[str, Recipe] = {}
        self.crafting_skill = 1
        self.available_tools = []
        self.crafting_history = []
        self._initialize_recipes()
    
    def _initialize_recipes(self):
        """Initialize basic crafting recipes."""
        # Basic weapon recipes
        wooden_staff = Item("Wooden Staff", "A simple wooden staff for beginners", 
                          ItemType.WEAPON, ItemRarity.COMMON, 1)
        wooden_staff.add_stat_bonus("attack", 5)
        
        wooden_staff_recipe = Recipe(
            wooden_staff,
            {"wood": 3, "cloth": 1},
            ["crafting_bench"],
            1
        )
        self.recipes["wooden_staff"] = wooden_staff_recipe
        
        # Enhanced wooden staff
        enhanced_staff = Item("Enhanced Wooden Staff", "A reinforced wooden staff with metal fittings",
                            ItemType.WEAPON, ItemRarity.UNCOMMON, 3)
        enhanced_staff.add_stat_bonus("attack", 12)
        enhanced_staff.add_stat_bonus("cursed_energy", 5)
        
        enhanced_staff_recipe = Recipe(
            enhanced_staff,
            {"wood": 5, "metal_ore": 2, "cursed_crystal": 1},
            ["crafting_bench", "enchanting_table"],
            3
        )
        self.recipes["enhanced_staff"] = enhanced_staff_recipe
        
        # Basic armor
        leather_vest = Item("Leather Training Vest", "Basic protection for training",
                          ItemType.ARMOR, ItemRarity.COMMON, 1)
        leather_vest.add_stat_bonus("defense", 3)
        leather_vest.add_stat_bonus("hp", 10)
        
        leather_vest_recipe = Recipe(
            leather_vest,
            {"leather": 4, "thread": 2},
            ["crafting_bench"],
            1
        )
        self.recipes["leather_vest"] = leather_vest_recipe
        
        # Accessories
        energy_charm = Item("Cursed Energy Charm", "Increases cursed energy capacity",
                          ItemType.ACCESSORY, ItemRarity.UNCOMMON, 5)
        energy_charm.add_stat_bonus("cursed_energy", 15)
        energy_charm.add_special_effect("Energy Regeneration", "Slowly regenerates cursed energy")
        
        energy_charm_recipe = Recipe(
            energy_charm,
            {"cursed_crystal": 3, "silver": 2, "blessed_water": 1},
            ["enchanting_table"],
            5
        )
        self.recipes["energy_charm"] = energy_charm_recipe
        
        # Consumables
        healing_potion = Item("Healing Potion", "Restores health when consumed",
                            ItemType.CONSUMABLE, ItemRarity.COMMON, 1)
        healing_potion.add_special_effect("Healing", "Restores 50 HP")
        
        healing_potion_recipe = Recipe(
            healing_potion,
            {"healing_herb": 2, "pure_water": 1},
            ["alchemy_kit"],
            1
        )
        self.recipes["healing_potion"] = healing_potion_recipe
        
        # Outfit pieces
        school_uniform = Item("Tokyo Jujutsu High Uniform", "Official school uniform",
                            ItemType.OUTFIT, ItemRarity.COMMON, 1)
        school_uniform.add_stat_bonus("charisma", 5)
        school_uniform.add_special_effect("School Pride", "Improved reputation with teachers")
        
        # Battle outfit
        combat_gear = Item("Combat Sorcerer Gear", "Practical gear for dangerous missions",
                         ItemType.OUTFIT, ItemRarity.RARE, 10)
        combat_gear.add_stat_bonus("defense", 8)
        combat_gear.add_stat_bonus("agility", 10)
        combat_gear.add_special_effect("Combat Ready", "Faster technique casting")
        
        combat_gear_recipe = Recipe(
            combat_gear,
            {"reinforced_fabric": 6, "metal_plates": 4, "cursed_thread": 2},
            ["advanced_crafting_bench"],
            8
        )
        self.recipes["combat_gear"] = combat_gear_recipe
    
    def craft_item(self, recipe_name: str, inventory: Inventory) -> Dict[str, Any]:
        """Attempt to craft an item."""
        if recipe_name not in self.recipes:
            return {"success": False, "message": "Recipe not found"}
        
        recipe = self.recipes[recipe_name]
        
        if not recipe.can_craft(inventory, self.crafting_skill, self.available_tools):
            return {"success": False, "message": "Cannot craft - missing requirements"}
        
        # Calculate success
        success_rate = recipe.get_success_rate(self.crafting_skill)
        success = random.randint(1, 100) <= success_rate
        
        # Consume materials
        for material, quantity in recipe.materials.items():
            inventory.remove_item(material, quantity)
        
        result = {"success": success, "recipe": recipe_name}
        
        if success:
            # Create the item (potentially with random variations)
            crafted_item = self._create_crafted_item(recipe.result_item)
            
            if inventory.add_item(crafted_item):
                result["item"] = crafted_item
                result["message"] = f"Successfully crafted {crafted_item.get_display_name()}!"
                
                # Gain crafting experience
                self._gain_crafting_experience(recipe.skill_requirement)
            else:
                result["success"] = False
                result["message"] = "Inventory full - item lost!"
        else:
            result["message"] = "Crafting failed - materials lost!"
        
        # Record crafting attempt
        self.crafting_history.append({
            "recipe": recipe_name,
            "success": success,
            "date": datetime.now()
        })
        
        return result
    
    def _create_crafted_item(self, base_item: Item) -> Item:
        """Create a crafted item with potential variations."""
        # Create copy of base item
        crafted_item = Item(
            base_item.name,
            base_item.description,
            base_item.item_type,
            base_item.rarity,
            base_item.level_requirement
        )
        
        # Copy stats and effects
        crafted_item.stats = base_item.stats.copy()
        crafted_item.special_effects = base_item.special_effects.copy()
        
        # Add crafting metadata
        crafted_item.crafted_date = datetime.now()
        
        # Chance for quality variations
        quality_roll = random.randint(1, 100)
        
        if quality_roll <= 5:  # 5% chance for superior quality
            crafted_item.name = f"Superior {crafted_item.name}"
            crafted_item.description += " (Superior Quality)"
            # Boost all stats by 20%
            for stat in crafted_item.stats:
                crafted_item.stats[stat] = int(crafted_item.stats[stat] * 1.2)
        elif quality_roll <= 15:  # 10% chance for high quality
            crafted_item.name = f"Fine {crafted_item.name}"
            crafted_item.description += " (High Quality)"
            # Boost all stats by 10%
            for stat in crafted_item.stats:
                crafted_item.stats[stat] = int(crafted_item.stats[stat] * 1.1)
        elif quality_roll >= 95:  # 5% chance for poor quality
            crafted_item.name = f"Crude {crafted_item.name}"
            crafted_item.description += " (Poor Quality)"
            # Reduce all stats by 10%
            for stat in crafted_item.stats:
                crafted_item.stats[stat] = max(1, int(crafted_item.stats[stat] * 0.9))
        
        return crafted_item
    
    def _gain_crafting_experience(self, recipe_difficulty: int):
        """Gain crafting skill experience."""
        experience_gain = recipe_difficulty
        
        # Simplified skill progression
        if random.randint(1, 100) <= (experience_gain * 10):
            self.crafting_skill += 1
            return f"Crafting skill increased to {self.crafting_skill}!"
        
        return ""
    
    def add_tool(self, tool_name: str):
        """Add a crafting tool."""
        if tool_name not in self.available_tools:
            self.available_tools.append(tool_name)
    
    def get_available_recipes(self) -> List[str]:
        """Get list of recipes that can potentially be crafted."""
        available = []
        for recipe_name, recipe in self.recipes.items():
            if self.crafting_skill >= recipe.skill_requirement:
                tools_available = all(tool in self.available_tools for tool in recipe.tools_required)
                if tools_available:
                    available.append(recipe_name)
        
        return available
    
    def get_recipe_info(self, recipe_name: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a recipe."""
        if recipe_name not in self.recipes:
            return None
        
        recipe = self.recipes[recipe_name]
        return {
            "name": recipe_name,
            "result": recipe.result_item.get_display_name(),
            "materials": recipe.materials,
            "tools": recipe.tools_required,
            "skill_requirement": recipe.skill_requirement,
            "success_rate": recipe.get_success_rate(self.crafting_skill)
        }


class CharacterCustomization:
    """Complete character customization system."""
    
    def __init__(self):
        self.equipment = Equipment()
        self.inventory = Inventory()
        self.crafting = CraftingSystem()
        self.appearance = {
            "hair_color": "black",
            "eye_color": "brown",
            "height": "average",
            "build": "athletic"
        }
        self.skill_loadouts = {}
        self.active_loadout = "default"
        
        # Initialize with basic items
        self._initialize_starting_items()
    
    def _initialize_starting_items(self):
        """Give player starting items."""
        # Basic school uniform
        uniform = Item("Student Uniform", "Standard school uniform", 
                      ItemType.OUTFIT, ItemRarity.COMMON, 1)
        uniform.add_stat_bonus("charisma", 2)
        
        # Basic training weapon
        training_sword = Item("Training Sword", "Wooden sword for practice",
                            ItemType.WEAPON, ItemRarity.COMMON, 1)
        training_sword.add_stat_bonus("attack", 3)
        
        # Basic accessories
        student_badge = Item("Student Badge", "Identifies you as a Jujutsu student",
                           ItemType.ACCESSORY, ItemRarity.COMMON, 1)
        student_badge.add_stat_bonus("reputation", 5)
        
        # Add to inventory
        self.inventory.add_item(uniform)
        self.inventory.add_item(training_sword)
        self.inventory.add_item(student_badge)
        
        # Equip basic items
        self.equipment.equip_item(uniform, "outfit")
        self.equipment.equip_item(training_sword, "weapon")
        self.equipment.equip_item(student_badge, "accessory_1")
    
    def create_skill_loadout(self, name: str, techniques: List[str], 
                           passive_skills: List[str]) -> bool:
        """Create a skill loadout."""
        if len(techniques) > 6:  # Limit active techniques
            return False
        
        self.skill_loadouts[name] = {
            "techniques": techniques,
            "passive_skills": passive_skills,
            "created_date": datetime.now()
        }
        return True
    
    def switch_loadout(self, loadout_name: str) -> bool:
        """Switch to a different skill loadout."""
        if loadout_name in self.skill_loadouts:
            self.active_loadout = loadout_name
            return True
        return False
    
    def get_total_stats(self) -> Dict[str, int]:
        """Get total character stats including equipment bonuses."""
        base_stats = {
            "attack": 10,
            "defense": 5,
            "hp": 100,
            "cursed_energy": 50,
            "agility": 10,
            "charisma": 10
        }
        
        # Add equipment bonuses
        equipment_stats = self.equipment.total_stats
        
        total_stats = {}
        for stat in base_stats:
            total_stats[stat] = base_stats[stat] + equipment_stats.get(stat, 0)
        
        return total_stats
    
    def customize_appearance(self, feature: str, value: str):
        """Customize character appearance."""
        if feature in self.appearance:
            self.appearance[feature] = value
    
    def get_customization_summary(self) -> str:
        """Get summary of character customization."""
        lines = []
        lines.append("📝 Character Customization")
        lines.append(f"Outfit: {self.equipment.equipped_items['outfit'].name if self.equipment.equipped_items['outfit'] else 'None'}")
        lines.append(f"Weapon: {self.equipment.equipped_items['weapon'].name if self.equipment.equipped_items['weapon'] else 'None'}")
        lines.append(f"Active Loadout: {self.active_loadout}")
        lines.append(f"Crafting Skill: {self.crafting.crafting_skill}")
        lines.append(self.inventory.get_capacity_info())
        
        return "\n".join(lines)