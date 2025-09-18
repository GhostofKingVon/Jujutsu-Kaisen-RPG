"""
Turn-Based Combat System

Handles combat mechanics including attacks, cursed techniques, dodging, counters,
and multi-phase boss battles. Enhanced with stamina system and environmental advantages.
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
        self.technique = None  # For technique actions


class CombatSystem:
    """Manages turn-based combat with strategic elements."""
    
    def __init__(self):
        self.turn_count = 0
        self.combat_log = []
        self.player_dodge_ready = False
        self.enemy_dodge_ready = False
        self.current_environment = "neutral"
        
        # Import environmental advantages
        from stamina_system import EnvironmentalAdvantages
        self.environmental_system = EnvironmentalAdvantages()
    
    def start_combat(self, player: Player, enemy: Enemy, environment: str = "neutral") -> bool:
        """Start a combat encounter. Returns True if player wins, False if defeated."""
        print(f"\n⚔️  COMBAT BEGINS ⚔️")
        print(f"{player.name} vs {enemy.name}")
        
        # Set environment
        self.current_environment = environment
        if environment != "neutral":
            env_data = self.environmental_system.get_advantage(environment)
            if env_data:
                print(f"🌍 Environment: {env_data.get('description', environment.title())}")
        
        print("=" * 50)
        
        self.turn_count = 0
        self.combat_log = []
        self.player_dodge_ready = False
        self.enemy_dodge_ready = False
        
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
        
        # Show stamina if available
        if hasattr(player, 'stamina_system'):
            print(f"  {player.stamina_system.get_status_display()}")
        
        if player.transformation_active:
            print(f"  🌟 {player.transformation_name} ({player.transformation_turns} turns left)")
        
        print(f"{enemy.name}: {enemy.hp}/{enemy.max_hp} HP | {enemy.cursed_energy}/{enemy.max_cursed_energy} CE")
        if enemy.phase > 1:
            print(f"  🔥 Phase {enemy.phase}")
        
        # Display status effects
        if player.status_effects:
            effects = ", ".join(player.status_effects.keys())
            print(f"  {player.name} effects: {effects}")
        
        if enemy.status_effects:
            effects = ", ".join(enemy.status_effects.keys())
            print(f"  {enemy.name} effects: {effects}")
        
        # Show environmental effects
        if self.current_environment != "neutral":
            env_effects = self.environmental_system.apply_environmental_effects(player, self.current_environment)
            if env_effects:
                print(f"  🌍 {env_effects}")
    
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
        actions = []
        
        # Check if player has stamina system
        has_stamina = hasattr(player, 'stamina_system')
        
        # Basic actions (always available)
        if not has_stamina or player.stamina_system.can_perform_action("basic_attack"):
            actions.append(CombatAction("attack", "Basic Attack", "A standard physical attack"))
        
        if not has_stamina or player.stamina_system.can_perform_action("dodge"):
            actions.append(CombatAction("dodge", "Dodge", "Prepare to dodge the next attack and counter"))
        
        if not has_stamina or player.stamina_system.can_perform_action("guard"):
            actions.append(CombatAction("guard", "Guard", "Reduce incoming damage this turn"))
        
        # Add rest action if stamina system exists
        if has_stamina:
            actions.append(CombatAction("rest", "Rest", "Recover stamina but forfeit attack"))
        
        # Add available techniques
        available_techniques = player.get_available_techniques()
        for technique in available_techniques:
            # Check both cursed energy and stamina requirements
            can_use = True
            description = f"{technique.description} (Cost: {technique.cost} CE"
            
            if has_stamina:
                if not player.stamina_system.can_perform_action("technique"):
                    can_use = False
                    description += " - Insufficient stamina"
                else:
                    description += f", {player.stamina_system.action_costs['technique']} Stamina"
            
            description += ")"
            
            if can_use:
                action = CombatAction(
                    "technique",
                    technique.name,
                    description
                )
                action.technique = technique
                actions.append(action)
        
        # Add transformation if available
        if player.level >= 10 and not player.transformation_active:
            can_transform = True
            transform_desc = "Activate transformation for enhanced abilities"
            
            if has_stamina:
                if not player.stamina_system.can_perform_action("transform"):
                    can_transform = False
                    transform_desc += " - Insufficient stamina"
                else:
                    transform_desc += f" (Cost: {player.stamina_system.action_costs['transform']} Stamina)"
            
            if can_transform:
                actions.append(CombatAction(
                    "transform",
                    "Ultra Instinct Monkey",
                    transform_desc
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
        # Use stamina if system exists
        if hasattr(player, 'stamina_system') and action.action_type != "flee":
            if action.action_type == "rest":
                restored = player.stamina_system.rest_turn()
                print(f"{player.name} rests and recovers {restored} stamina!")
                return
            
            # Try to use stamina for action
            action_type_map = {
                "attack": "basic_attack",
                "technique": "technique", 
                "dodge": "dodge",
                "guard": "guard",
                "transform": "transform"
            }
            
            stamina_action = action_type_map.get(action.action_type, action.action_type)
            if not player.stamina_system.use_stamina(stamina_action):
                print(f"{player.name} is too exhausted to perform {action.name}!")
                return
        
        # Apply performance modifier from stamina state
        performance_modifier = 1.0
        if hasattr(player, 'stamina_system'):
            performance_modifier = player.stamina_system.get_performance_modifier()
        
        if action.action_type == "attack":
            self.basic_attack(player, enemy, performance_modifier)
        
        elif action.action_type == "technique":
            self.use_technique(player, enemy, action.technique, performance_modifier)
        
        elif action.action_type == "dodge":
            self.player_dodge_ready = True
            print(f"{player.name} prepares to dodge the next attack!")
        
        elif action.action_type == "guard":
            player.add_status_effect("guarding", 1)
            print(f"{player.name} takes a defensive stance!")
        
        elif action.action_type == "transform":
            player.activate_transformation("Ultra Instinct Monkey", 5)
    
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
            self.basic_attack(enemy, player, 1.0, True)
        
        elif action == "technique":
            available_techniques = enemy.get_available_techniques()
            if available_techniques:
                technique = random.choice(available_techniques)
                self.use_technique(enemy, player, technique, 1.0, True)
            else:
                self.basic_attack(enemy, player, 1.0, True)
        
        elif action == "guard":
            enemy.add_status_effect("guarding", 1)
            print(f"{enemy.name} takes a defensive stance!")
    
    def basic_attack(self, attacker, defender, performance_modifier: float = 1.0, is_enemy: bool = False):
        """Execute a basic attack."""
        base_damage = 20 + (attacker.level * 2)
        
        # Apply performance modifier from stamina
        base_damage = int(base_damage * performance_modifier)
        
        # Check for dodge
        if self.check_dodge(attacker, defender, is_enemy):
            return
        
        # Apply environmental advantages
        if not is_enemy and self.current_environment != "neutral":
            env_data = self.environmental_system.get_advantage(self.current_environment)
            if "damage_bonus" in env_data:
                base_damage = int(base_damage * env_data["damage_bonus"])
        
        # Apply damage modifiers
        damage = self.calculate_damage(base_damage, attacker, defender)
        
        actual_damage = defender.take_damage(damage)
        print(f"{attacker.name} attacks {defender.name} for {actual_damage} damage!")
        
        # Show performance effects
        if performance_modifier != 1.0:
            if performance_modifier > 1.0:
                print(f"💪 High energy enhances the attack!")
            else:
                print(f"😓 Fatigue weakens the attack!")
        
        # Check for counter after successful dodge
        if not is_enemy and self.player_dodge_ready:
            self.execute_counter(defender, attacker)
            self.player_dodge_ready = False
    
    def use_technique(self, user, target, technique: CursedTechnique, performance_modifier: float = 1.0, is_enemy: bool = False):
        """Execute a cursed technique."""
        if not technique.can_use(user.cursed_energy):
            print(f"{user.name} doesn't have enough cursed energy for {technique.name}!")
            return
        
        # Use cursed energy
        user.use_cursed_energy(technique.cost)
        
        # Check for dodge
        if technique.technique_type == "offensive" and self.check_dodge(user, target, is_enemy):
            technique.current_cooldown = technique.cooldown  # Still goes on cooldown
            return
        
        # Execute technique
        if technique.technique_type == "offensive":
            base_damage = technique.damage
            
            # Apply performance modifier
            base_damage = int(base_damage * performance_modifier)
            
            # Apply environmental bonuses for player
            if not is_enemy and self.current_environment != "neutral":
                env_data = self.environmental_system.get_advantage(self.current_environment)
                if "technique_power" in env_data:
                    base_damage = int(base_damage * env_data["technique_power"])
            
            damage = self.calculate_damage(base_damage, user, target)
            actual_damage = target.take_damage(damage)
            print(f"{user.name} uses {technique.name} on {target.name} for {actual_damage} damage!")
            
            # Show performance effects
            if performance_modifier != 1.0:
                if performance_modifier > 1.0:
                    print(f"💪 Enhanced energy amplifies the technique!")
                else:
                    print(f"😓 Fatigue diminishes the technique's power!")
        
        elif technique.technique_type == "defensive":
            user.add_status_effect("enhanced_guard", 2)
            print(f"{user.name} uses {technique.name} to enhance their defenses!")
        
        # Apply cooldown
        technique.current_cooldown = technique.cooldown
        
        # Special technique effects
        self.apply_technique_effects(user, target, technique)
    
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