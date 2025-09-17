"""
Turn-Based Combat System

Handles combat mechanics including attacks, cursed techniques, dodging, counters,
and multi-phase boss battles.
"""

import random
from typing import List, Optional, Dict, Any
from character import Player, Enemy, CursedTechnique


class CombatAction:
    """Represents a combat action with its properties."""
    
    def __init__(self, action_type: str, name: str, description: str):
        self.action_type = action_type  # attack, technique, dodge, guard, item
        self.name = name
        self.description = description


class CombatSystem:
    """Manages turn-based combat with strategic elements."""
    
    def __init__(self):
        self.turn_count = 0
        self.combat_log = []
        self.player_dodge_ready = False
        self.enemy_dodge_ready = False
        # Enhanced combat mechanics
        self.combo_count = 0
        self.max_combo = 3
        self.combo_multiplier = 1.0
        self.ultimate_energy = 0
        self.ultimate_threshold = 100
        self.environmental_effects = []
        self.terrain_type = "normal"
    
    def start_combat(self, player: Player, enemy: Enemy, terrain: str = "normal") -> bool:
        """Start a combat encounter. Returns True if player wins, False if defeated."""
        print(f"\n⚔️  COMBAT BEGINS ⚔️")
        print(f"{player.name} vs {enemy.name}")
        print("=" * 50)
        
        self.turn_count = 0
        self.combat_log = []
        self.player_dodge_ready = False
        self.enemy_dodge_ready = False
        # Reset enhanced mechanics
        self.combo_count = 0
        self.combo_multiplier = 1.0
        self.ultimate_energy = 0
        self.terrain_type = terrain
        self.environmental_effects = []
        
        # Set up terrain effects
        self._initialize_terrain_effects(terrain)
        if terrain != "normal":
            print(f"🌍 Battlefield: {terrain.title()}")
            print(f"   {self._get_terrain_description(terrain)}")
        
        # Combat loop
        while player.is_alive() and enemy.is_alive():
            self.turn_count += 1
            print(f"\n--- Turn {self.turn_count} ---")
            
            # Display status
            self.display_combat_status(player, enemy)
            
            # Player turn
            if not self.player_turn(player, enemy):
                break  # Player chose to flee
            
            if not enemy.is_alive():
                break
            
            # Enemy turn
            self.enemy_turn(enemy, player)
            
            if not player.is_alive():
                break
            
            # Process status effects and cooldowns
            self.process_turn_effects(player, enemy)
        
        # Combat resolution
        return self.resolve_combat(player, enemy)
    
    def display_combat_status(self, player: Player, enemy: Enemy):
        """Display current combat status for both characters."""
        print(f"\n{player.name}: {player.hp}/{player.max_hp} HP | {player.cursed_energy}/{player.max_cursed_energy} CE")
        if player.transformation_active:
            print(f"  🌟 {player.transformation_name} ({player.transformation_turns} turns left)")
        
        # Display combo and ultimate status
        if self.combo_count > 0:
            print(f"  💥 Combo: x{self.combo_count} (+{int((self.combo_multiplier - 1) * 100)}% damage)")
        
        ultimate_progress = min(100, int((self.ultimate_energy / self.ultimate_threshold) * 100))
        print(f"  ⚡ Ultimate Energy: {ultimate_progress}%", end="")
        if self.check_ultimate_available(player):
            print(" [READY!]")
        else:
            print()
        
        print(f"{enemy.name}: {enemy.hp}/{enemy.max_hp} HP | {enemy.cursed_energy}/{enemy.max_cursed_energy} CE")
        if enemy.phase > 1:
            print(f"  🔥 Phase {enemy.phase}")
        
        # Display environmental info
        if self.environmental_effects:
            print(f"🌍 Environment: {self.terrain_type.title()} - {', '.join(self.environmental_effects)}")
        
        # Display status effects
        if player.status_effects:
            effects = ", ".join(player.status_effects.keys())
            print(f"  {player.name} effects: {effects}")
        
        if enemy.status_effects:
            effects = ", ".join(enemy.status_effects.keys())
            print(f"  {enemy.name} effects: {effects}")
    
    def player_turn(self, player: Player, enemy: Enemy) -> bool:
        """Handle player's turn. Returns False if player flees."""
        print(f"\n{player.name}'s turn!")
        
        # Show available actions
        actions = self.get_player_actions(player)
        self.display_actions(actions)
        
        # Get player choice
        choice = self.get_player_choice(len(actions))
        if choice is None:
            return True  # Invalid choice, continue turn
        
        action = actions[choice - 1]
        
        # Process the action
        if action.action_type == "flee":
            print(f"{player.name} flees from combat!")
            return False
        
        self.execute_player_action(player, enemy, action)
        return True
    
    def get_player_actions(self, player: Player) -> List[CombatAction]:
        """Get list of available actions for the player."""
        actions = [
            CombatAction("attack", "Basic Attack", "A standard physical attack"),
            CombatAction("dodge", "Dodge", "Prepare to dodge the next attack and counter"),
            CombatAction("guard", "Guard", "Reduce incoming damage this turn"),
        ]
        
        # Add available techniques
        available_techniques = player.get_available_techniques()
        for technique in available_techniques:
            action = CombatAction(
                "technique",
                technique.name,
                f"{technique.description} (Cost: {technique.cost} CE)"
            )
            action.technique = technique
            actions.append(action)
        
        # Add ultimate technique if available
        if self.check_ultimate_available(player):
            ultimate_name = self._determine_ultimate_technique(player.get_dominant_traits())
            actions.append(CombatAction(
                "ultimate",
                f"🌟 {ultimate_name}",
                f"Ultimate technique based on your nature (Ultimate Energy: {self.ultimate_energy})"
            ))
        
        # Add transformation if available
        if player.level >= 10 and not player.transformation_active:
            actions.append(CombatAction(
                "transform",
                "Ultra Instinct Monkey",
                "Activate transformation for enhanced abilities"
            ))
        
        # Add environmental interactions if available
        if self.environmental_effects:
            actions.append(CombatAction(
                "environment",
                "Interact with Environment",
                f"Use the {self.terrain_type} terrain to your advantage"
            ))
        
        actions.append(CombatAction("flee", "Flee", "Escape from combat"))
        
        return actions
    
    def display_actions(self, actions: List[CombatAction]):
        """Display available actions to the player."""
        print("\nChoose your action:")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action.name} - {action.description}")
    
    def get_player_choice(self, num_actions: int) -> Optional[int]:
        """Get and validate player's action choice."""
        try:
            choice = int(input(f"\nEnter your choice (1-{num_actions}): "))
            if 1 <= choice <= num_actions:
                return choice
            else:
                print("Invalid choice. Please try again.")
                return None
        except ValueError:
            print("Please enter a valid number.")
            return None
    
    def execute_player_action(self, player: Player, enemy: Enemy, action: CombatAction):
        """Execute the player's chosen action."""
        action_successful = True
        
        if action.action_type == "attack":
            # Apply combo and environmental effects
            env_result = self.apply_environmental_interaction("attack", player, enemy)
            base_damage = 20 + (player.level * 2)
            
            # Apply combo multiplier
            if self.combo_multiplier > 1.0:
                base_damage = int(base_damage * self.combo_multiplier)
            
            # Check for dodge
            if not self.check_dodge(player, enemy, False):
                # Apply environmental bonus damage
                total_damage = base_damage + env_result.get("bonus_damage", 0)
                actual_damage = enemy.take_damage(total_damage)
                print(f"{player.name} attacks {enemy.name} for {actual_damage} damage!")
            else:
                action_successful = False
            
            # Process combo system
            self.process_combo_system(player, "attack", action_successful)
        
        elif action.action_type == "technique":
            # Apply environmental effects for techniques
            env_result = self.apply_environmental_interaction("technique", player, enemy)
            technique_multiplier = env_result.get("interactions", [{}])[0].get("multiplier", 1.0) if env_result.get("interactions") else 1.0
            
            # Modify technique damage if environmental boost
            original_damage = action.technique.damage
            if technique_multiplier > 1.0:
                action.technique.damage = int(action.technique.damage * technique_multiplier)
            
            success = self.use_technique(player, enemy, action.technique)
            
            # Restore original damage
            action.technique.damage = original_damage
            
            # Process combo system
            self.process_combo_system(player, "technique", success)
        
        elif action.action_type == "ultimate":
            result = self.use_ultimate_technique(player, enemy)
            if result["success"]:
                print(f"🌟 {result['name']} activated!")
            else:
                print(f"❌ {result['message']}")
            # Ultimates always break combo but don't reset ultimate energy on failure
            self.combo_count = 0
            self.combo_multiplier = 1.0
        
        elif action.action_type == "environment":
            self._execute_environmental_action(player, enemy)
            # Environmental actions don't affect combo
        
        elif action.action_type == "dodge":
            self.player_dodge_ready = True
            print(f"{player.name} prepares to dodge the next attack!")
            # Dodging breaks combo but builds ultimate energy
            self.combo_count = 0
            self.combo_multiplier = 1.0
            self.ultimate_energy += 5
        
        elif action.action_type == "guard":
            player.add_status_effect("guarding", 1)
            print(f"{player.name} takes a defensive stance!")
            # Guarding breaks combo but builds ultimate energy
            self.combo_count = 0
            self.combo_multiplier = 1.0
            self.ultimate_energy += 3
        
        elif action.action_type == "transform":
            player.activate_transformation("Ultra Instinct Monkey", 5)
            # Transformation breaks combo
            self.combo_count = 0
            self.combo_multiplier = 1.0
    
    def enemy_turn(self, enemy: Enemy, player: Player):
        """Handle enemy's turn with AI decision making."""
        print(f"\n{enemy.name}'s turn!")
        
        # Check for phase transition
        if enemy.should_transition_phase():
            enemy.transition_phase()
            return
        
        # AI chooses action
        action = enemy.choose_action(player)
        
        if action == "attack":
            self.basic_attack(enemy, player, is_enemy=True)
        
        elif action == "technique":
            available_techniques = enemy.get_available_techniques()
            if available_techniques:
                technique = random.choice(available_techniques)
                self.use_technique(enemy, player, technique, is_enemy=True)
            else:
                self.basic_attack(enemy, player, is_enemy=True)
        
        elif action == "guard":
            enemy.add_status_effect("guarding", 1)
            print(f"{enemy.name} takes a defensive stance!")
    
    def basic_attack(self, attacker, defender, is_enemy: bool = False) -> bool:
        """Execute a basic attack. Returns True if successful."""
        base_damage = 20 + (attacker.level * 2)
        
        # Check for dodge
        if self.check_dodge(attacker, defender, is_enemy):
            return False
        
        # Apply damage modifiers
        damage = self.calculate_damage(base_damage, attacker, defender)
        
        actual_damage = defender.take_damage(damage)
        print(f"{attacker.name} attacks {defender.name} for {actual_damage} damage!")
        
        # Check for counter after successful dodge
        if not is_enemy and self.player_dodge_ready:
            self.execute_counter(defender, attacker)
            self.player_dodge_ready = False
        
        return True
    
    def use_technique(self, user, target, technique: CursedTechnique, is_enemy: bool = False) -> bool:
        """Execute a cursed technique. Returns True if successful."""
        if not technique.can_use(user.cursed_energy):
            print(f"{user.name} doesn't have enough cursed energy for {technique.name}!")
            return False
        
        # Use cursed energy
        user.use_cursed_energy(technique.cost)
        
        # Check for dodge
        if technique.technique_type == "offensive" and self.check_dodge(user, target, is_enemy):
            technique.current_cooldown = technique.cooldown  # Still goes on cooldown
            return False
        
        # Execute technique
        if technique.technique_type == "offensive":
            damage = self.calculate_damage(technique.damage, user, target)
            actual_damage = target.take_damage(damage)
            print(f"{user.name} uses {technique.name} on {target.name} for {actual_damage} damage!")
        
        elif technique.technique_type == "defensive":
            user.add_status_effect("enhanced_guard", 2)
            print(f"{user.name} uses {technique.name} to enhance their defenses!")
        
        # Apply cooldown
        technique.current_cooldown = technique.cooldown
        
        # Special technique effects
        self.apply_technique_effects(user, target, technique)
        
        return True
    
    def check_dodge(self, attacker, defender, is_enemy_attacking: bool) -> bool:
        """Check if an attack is dodged."""
        dodge_chance = 0.0
        
        if not is_enemy_attacking and self.player_dodge_ready:
            # Player prepared to dodge
            dodge_chance = defender.get_dodge_chance()
        elif is_enemy_attacking:
            # Enemy's natural dodge chance
            dodge_chance = 0.1  # 10% base for enemies
        
        if random.random() < dodge_chance:
            print(f"💨 {defender.name} dodges the attack!")
            
            # Trigger counter if player dodged successfully
            if not is_enemy_attacking and self.player_dodge_ready:
                self.execute_counter(defender, attacker)
                self.player_dodge_ready = False
            
            return True
        
        # Reset dodge preparation if it failed
        if not is_enemy_attacking and self.player_dodge_ready:
            self.player_dodge_ready = False
        
        return False
    
    def execute_counter(self, counter_attacker, target):
        """Execute a counter attack after successful dodge."""
        print(f"⚡ {counter_attacker.name} counters!")
        
        # Counter attacks deal extra damage
        counter_damage = 15 + (counter_attacker.level * 3)
        
        # Apply transformation bonuses
        if hasattr(counter_attacker, 'transformation_active') and counter_attacker.transformation_active:
            if "Ultra Instinct" in counter_attacker.transformation_name:
                counter_damage = int(counter_damage * 1.5)
                print(f"🌟 Ultra Instinct enhances the counter!")
        
        actual_damage = target.take_damage(counter_damage)
        print(f"{counter_attacker.name}'s counter deals {actual_damage} damage to {target.name}!")
    
    def calculate_damage(self, base_damage: int, attacker, defender) -> int:
        """Calculate final damage after modifiers."""
        damage = base_damage
        
        # Attacker modifiers
        if hasattr(attacker, 'transformation_active') and attacker.transformation_active:
            damage = int(damage * 1.3)
        
        # Defender modifiers
        if "guarding" in defender.status_effects:
            damage = int(damage * 0.5)
        elif "enhanced_guard" in defender.status_effects:
            damage = int(damage * 0.3)
        
        # Add some randomness (±20%)
        variance = random.uniform(0.8, 1.2)
        damage = int(damage * variance)
        
        return max(1, damage)  # Minimum 1 damage
    
    def apply_technique_effects(self, user, target, technique: CursedTechnique):
        """Apply special effects based on technique."""
        if "Shadow" in technique.name:
            # Shadow techniques have a chance to cause confusion
            if random.random() < 0.3:
                target.add_status_effect("confused", 2)
                print(f"{target.name} is confused by the shadow technique!")
        
        elif "Wukong" in technique.name:
            # Wukong technique restores some cursed energy
            restored = user.restore_cursed_energy(10)
            if restored > 0:
                print(f"{user.name} gains {restored} cursed energy from Wukong's wisdom!")
        
        elif "Burst" in technique.name:
            # Energy burst techniques have a chance to stun
            if random.random() < 0.25:
                target.add_status_effect("stunned", 1)
                print(f"{target.name} is stunned by the energy burst!")
    
    def process_turn_effects(self, player: Player, enemy: Enemy):
        """Process status effects and cooldowns at turn end."""
        # Process status effects
        player.process_status_effects()
        enemy.process_status_effects()
        
        # Process transformations
        if hasattr(player, 'process_transformation'):
            player.process_transformation()
        
        # Reduce technique cooldowns
        for technique in player.techniques + enemy.techniques:
            technique.reduce_cooldown()
        
        # Natural cursed energy regeneration (small amount)
        player.restore_cursed_energy(5)
        enemy.restore_cursed_energy(3)
    
    def resolve_combat(self, player: Player, enemy: Enemy) -> bool:
        """Resolve combat and handle rewards/consequences."""
        print("\n" + "=" * 50)
        
        if player.is_alive():
            print(f"🎉 VICTORY! {player.name} defeats {enemy.name}!")
            
            # Calculate rewards
            exp_reward = enemy.level * 25 + enemy.max_hp // 5
            player.gain_experience(exp_reward)
            print(f"Gained {exp_reward} experience!")
            
            # Heal a small amount after victory
            heal_amount = player.max_hp // 10
            healed = player.heal(heal_amount)
            if healed > 0:
                print(f"Recovered {healed} HP from victory!")
            
            return True
        
        else:
            print(f"💀 DEFEAT! {player.name} has been defeated by {enemy.name}...")
            return False
    
    def _initialize_terrain_effects(self, terrain: str):
        """Initialize terrain-specific effects."""
        if terrain == "forest":
            self.environmental_effects = ["shadowy_cover", "natural_energy"]
        elif terrain == "urban":
            self.environmental_effects = ["destructible_objects", "concrete_cover"]
        elif terrain == "shrine":
            self.environmental_effects = ["sacred_energy", "spiritual_barrier"]
        elif terrain == "underground":
            self.environmental_effects = ["tight_spaces", "echo_chamber"]
        elif terrain == "rooftop":
            self.environmental_effects = ["elevated_position", "wind_effects"]
    
    def _get_terrain_description(self, terrain: str) -> str:
        """Get description of terrain effects."""
        descriptions = {
            "forest": "Dense trees provide cover but cursed spirits lurk in shadows",
            "urban": "Concrete and debris can be used tactically",
            "shrine": "Sacred energy enhances spiritual techniques",
            "underground": "Confined space limits movement but amplifies echoes",
            "rooftop": "High altitude affects technique range and wind patterns"
        }
        return descriptions.get(terrain, "Standard battlefield conditions")
    
    def process_combo_system(self, attacker, action_type: str, is_successful: bool):
        """Process combo mechanics for chaining successful actions."""
        if is_successful and action_type in ["attack", "technique"]:
            self.combo_count += 1
            if self.combo_count > 1:
                self.combo_multiplier = 1.0 + (self.combo_count * 0.15)  # 15% per combo
                print(f"💥 COMBO x{self.combo_count}! Damage increased by {int((self.combo_multiplier - 1) * 100)}%")
            
            # Ultimate energy buildup
            self.ultimate_energy += 15 + (self.combo_count * 5)
            
            if self.combo_count >= self.max_combo:
                print(f"🔥 MAX COMBO REACHED! Ultimate technique available!")
        else:
            # Reset combo on failure or non-combat action
            if self.combo_count > 0:
                print(f"💔 Combo broken!")
            self.combo_count = 0
            self.combo_multiplier = 1.0
    
    def check_ultimate_available(self, player: Player) -> bool:
        """Check if ultimate technique is available."""
        return self.ultimate_energy >= self.ultimate_threshold and player.level >= 5
    
    def use_ultimate_technique(self, user: Player, target: Enemy) -> Dict[str, Any]:
        """Execute an ultimate technique based on player's dominant traits."""
        if not self.check_ultimate_available(user):
            return {"success": False, "message": "Ultimate not available"}
        
        dominant_traits = user.get_dominant_traits()
        ultimate_name = self._determine_ultimate_technique(dominant_traits)
        
        print(f"🌟 ULTIMATE TECHNIQUE: {ultimate_name}!")
        
        # Reset ultimate energy
        self.ultimate_energy = 0
        
        # Execute ultimate based on type
        return self._execute_ultimate_effect(ultimate_name, user, target)
    
    def _determine_ultimate_technique(self, traits) -> str:
        """Determine ultimate technique based on dominant traits."""
        trait_ultimates = {
            "Compassionate": "Protective Spirit Barrier",
            "Focused": "Perfect Technique Mastery",
            "Aggressive": "Overwhelming Destruction",
            "Protective": "Guardian's Resolve",
            "Analytical": "Weakness Exploitation",
            "Reckless": "Berserker's Fury",
            "Determined": "Unbreakable Will",
            "Cautious": "Strategic Dominance"
        }
        
        if traits:
            return trait_ultimates.get(traits[0].value, "Cursed Energy Explosion")
        return "Cursed Energy Explosion"
    
    def _execute_ultimate_effect(self, ultimate_name: str, user: Player, target: Enemy) -> Dict[str, Any]:
        """Execute the specific ultimate technique effect."""
        effects = {
            "Protective Spirit Barrier": {
                "damage": 0,
                "effect": "heal_and_shield",
                "value": user.max_hp // 3,
                "description": "A barrier of protective energy heals and shields you!"
            },
            "Perfect Technique Mastery": {
                "damage": user.level * 20,
                "effect": "ignore_all_defenses",
                "description": "Perfect execution ignores all defenses!"
            },
            "Overwhelming Destruction": {
                "damage": user.level * 30,
                "effect": "massive_damage",
                "description": "Pure destructive force overwhelms the enemy!"
            },
            "Guardian's Resolve": {
                "damage": user.level * 15,
                "effect": "damage_and_heal",
                "value": user.max_hp // 4,
                "description": "Protective instincts fuel both offense and recovery!"
            },
            "Weakness Exploitation": {
                "damage": user.level * 25,
                "effect": "critical_analysis",
                "description": "Analytical precision finds the perfect weak point!"
            },
            "Berserker's Fury": {
                "damage": user.level * 35,
                "effect": "high_damage_self_damage",
                "self_damage": user.max_hp // 10,
                "description": "Reckless fury deals massive damage but injures you!"
            },
            "Unbreakable Will": {
                "damage": user.level * 22,
                "effect": "damage_and_status_immunity",
                "turns": 3,
                "description": "Determined will strikes hard and grants status immunity!"
            },
            "Strategic Dominance": {
                "damage": user.level * 18,
                "effect": "guaranteed_next_hit",
                "description": "Strategic positioning guarantees your next attack!"
            },
            "Cursed Energy Explosion": {
                "damage": user.level * 20,
                "effect": "area_damage",
                "description": "Raw cursed energy explodes outward!"
            }
        }
        
        ultimate = effects.get(ultimate_name, effects["Cursed Energy Explosion"])
        
        # Apply damage
        if ultimate["damage"] > 0:
            actual_damage = target.take_damage(ultimate["damage"])
            print(f"💥 {ultimate_name} deals {actual_damage} damage!")
        
        # Apply special effects
        effect_type = ultimate["effect"]
        if effect_type == "heal_and_shield":
            healed = user.heal(ultimate["value"])
            user.add_status_effect("shielded", 3)
            print(f"🛡️ Healed {healed} HP and gained protective shield!")
            
        elif effect_type == "damage_and_heal":
            healed = user.heal(ultimate["value"])
            print(f"❤️ Also healed {healed} HP!")
            
        elif effect_type == "high_damage_self_damage":
            self_damage = user.take_damage(ultimate["self_damage"])
            print(f"⚠️ The fury costs {self_damage} of your own HP!")
            
        elif effect_type == "damage_and_status_immunity":
            user.add_status_effect("status_immune", ultimate["turns"])
            print(f"🛡️ Gained status immunity for {ultimate['turns']} turns!")
            
        elif effect_type == "guaranteed_next_hit":
            user.add_status_effect("guaranteed_hit", 1)
            print(f"🎯 Your next attack will definitely hit!")
        
        print(f"   {ultimate['description']}")
        
        return {
            "success": True,
            "name": ultimate_name,
            "damage": ultimate["damage"],
            "effect": ultimate["effect"]
        }
    
    def apply_environmental_interaction(self, action_type: str, user, target) -> Dict[str, Any]:
        """Handle environmental interactions during combat."""
        if not self.environmental_effects:
            return {}
        
        interactions = []
        
        if "destructible_objects" in self.environmental_effects:
            if action_type == "attack" and random.random() < 0.3:
                bonus_damage = random.randint(5, 15)
                interactions.append({
                    "type": "debris_damage",
                    "damage": bonus_damage,
                    "description": f"💥 Debris from destroyed objects deals {bonus_damage} extra damage!"
                })
        
        if "natural_energy" in self.environmental_effects:
            if action_type == "technique" and random.random() < 0.25:
                energy_restore = random.randint(8, 15)
                interactions.append({
                    "type": "energy_restore",
                    "value": energy_restore,
                    "description": f"🌿 Natural energy restores {energy_restore} cursed energy!"
                })
        
        if "sacred_energy" in self.environmental_effects:
            if action_type == "technique" and random.random() < 0.2:
                interactions.append({
                    "type": "technique_boost",
                    "multiplier": 1.3,
                    "description": f"⛩️ Sacred energy amplifies your technique!"
                })
        
        if "echo_chamber" in self.environmental_effects:
            if action_type == "technique" and random.random() < 0.15:
                interactions.append({
                    "type": "echo_damage",
                    "damage": 10,
                    "description": f"🔊 Sound echoes deal additional damage!"
                })
        
        if "elevated_position" in self.environmental_effects:
            if action_type == "attack" and random.random() < 0.2:
                interactions.append({
                    "type": "height_advantage",
                    "damage_bonus": 8,
                    "description": f"⬆️ Height advantage increases impact!"
                })
        
        # Apply the interactions
        total_bonus_damage = 0
        for interaction in interactions:
            print(f"🌍 {interaction['description']}")
            
            if interaction["type"] == "debris_damage":
                total_bonus_damage += interaction["damage"]
            elif interaction["type"] == "energy_restore":
                user.restore_cursed_energy(interaction["value"])
            elif interaction["type"] == "echo_damage":
                total_bonus_damage += interaction["damage"]
            elif interaction["type"] == "height_advantage":
                total_bonus_damage += interaction["damage_bonus"]
        
        return {"bonus_damage": total_bonus_damage, "interactions": interactions}
    
    def _execute_environmental_action(self, player: Player, enemy: Enemy):
        """Execute environment-specific actions."""
        if not self.environmental_effects:
            print("No environmental features to interact with.")
            return
        
        print(f"🌍 {player.name} interacts with the {self.terrain_type} environment!")
        
        if "destructible_objects" in self.environmental_effects:
            # Throw debris
            debris_damage = random.randint(15, 25)
            actual_damage = enemy.take_damage(debris_damage)
            print(f"💥 Hurled debris deals {actual_damage} damage!")
            
        elif "shadowy_cover" in self.environmental_effects:
            # Use shadows for stealth
            player.add_status_effect("stealth", 2)
            print(f"🌑 Hidden in shadows - next attack will be a surprise!")
            
        elif "sacred_energy" in self.environmental_effects:
            # Channel sacred power
            restored = player.restore_cursed_energy(25)
            print(f"⛩️ Sacred energy restores {restored} cursed energy!")
            
        elif "tight_spaces" in self.environmental_effects:
            # Use confined space tactically
            enemy.add_status_effect("restricted", 2)
            print(f"🕳️ Enemy movement is restricted by tight spaces!")
            
        elif "elevated_position" in self.environmental_effects:
            # Gain high ground advantage
            player.add_status_effect("high_ground", 3)
            print(f"⬆️ High ground advantage - increased accuracy and damage!")
        
        # Environmental actions build ultimate energy
        self.ultimate_energy += 10