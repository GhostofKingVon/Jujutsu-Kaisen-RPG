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
    
    def start_combat(self, player: Player, enemy: Enemy) -> bool:
        """Start a combat encounter. Returns True if player wins, False if defeated."""
        print(f"\n⚔️  COMBAT BEGINS ⚔️")
        print(f"{player.name} vs {enemy.name}")
        print("=" * 50)
        
        # Play combat intro cutscene for special enemies
        try:
            from cutscenes import get_cutscene_manager
            cutscene_manager = get_cutscene_manager()
            
            if "Special Grade" in enemy.name or "Boss" in enemy.name:
                cutscene_manager.show_dramatic_transition("boss_encounter", 
                    f"💀 {enemy.name} emerges from the shadows, radiating malevolent power!")
            
        except ImportError:
            pass
        
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
            
            # Check for dramatic moments mid-combat
            self._check_combat_drama(player, enemy)
        
        # Combat resolution
        return self.resolve_combat(player, enemy)
    
    def display_combat_status(self, player: Player, enemy: Enemy):
        """Display current combat status for both characters."""
        print(f"\n{player.name}: {player.hp}/{player.max_hp} HP | {player.cursed_energy}/{player.max_cursed_energy} CE")
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
        
        # Add transformation if available
        if player.level >= 10 and not player.transformation_active:
            actions.append(CombatAction(
                "transform",
                "Ultra Instinct Monkey",
                "Activate transformation for enhanced abilities"
            ))
        
        # Add team combos if allies are available (simulated)
        try:
            from team_combos import get_team_combo_manager
            combo_manager = get_team_combo_manager()
            
            # For demo purposes, assume some allies might be available
            # In full implementation, this would check actual ally availability
            available_allies = ["yuji", "megumi", "nobara"]  # Simplified
            relationships = getattr(player, '_temp_relationships', {"yuji": 80, "megumi": 70, "nobara": 85})
            
            available_combos = combo_manager.get_available_combos(relationships, available_allies)
            
            for combo in available_combos[:2]:  # Limit to 2 combos for menu size
                action = CombatAction(
                    "team_combo",
                    combo.name,
                    f"Team technique with {', '.join([p for p in combo.participants if p != 'player'])}"
                )
                action.combo = combo
                actions.append(action)
                
        except ImportError:
            pass
        
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
        if action.action_type == "attack":
            self.basic_attack(player, enemy)
        
        elif action.action_type == "technique":
            self.use_technique(player, enemy, action.technique)
        
        elif action.action_type == "dodge":
            self.player_dodge_ready = True
            print(f"{player.name} prepares to dodge the next attack!")
        
        elif action.action_type == "guard":
            player.add_status_effect("guarding", 1)
            print(f"{player.name} takes a defensive stance!")
        
        elif action.action_type == "transform":
            player.activate_transformation("Ultra Instinct Monkey", 5)
        
        elif action.action_type == "team_combo":
            try:
                from team_combos import get_team_combo_manager
                combo_manager = get_team_combo_manager()
                
                base_damage = 40 + (player.level * 5)
                participants = ["player"] + [p for p in action.combo.participants if p != "player"]
                
                result = combo_manager.execute_combo(action.combo, base_damage, participants)
                
                # Apply combo damage to enemy
                enemy.take_damage(result["damage"])
                
                # Apply special effects
                for effect in result["special_effects"]:
                    if effect == "stun_chance" and random.random() < 0.5:
                        enemy.add_status_effect("stunned", 2)
                    elif effect == "energy_restoration":
                        player.restore_cursed_energy(20)
                    elif effect == "healing":
                        player.heal(15)
                
            except ImportError:
                print("Team combo system not available")
    
    def enemy_turn(self, enemy: Enemy, player: Player):
        """Handle enemy's turn with AI decision making."""
        print(f"\n{enemy.name}'s turn!")
        
        # Check for phase transition
        if enemy.should_transition_phase():
            try:
                from cutscenes import get_cutscene_manager
                cutscene_manager = get_cutscene_manager()
                cutscene_manager.create_boss_phase_transition(enemy.name, enemy.phase + 1)
            except ImportError:
                pass
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
    
    def basic_attack(self, attacker, defender, is_enemy: bool = False):
        """Execute a basic attack."""
        base_damage = 20 + (attacker.level * 2)
        
        # Check for dodge
        if self.check_dodge(attacker, defender, is_enemy):
            return
        
        # Apply damage modifiers
        damage = self.calculate_damage(base_damage, attacker, defender)
        
        actual_damage = defender.take_damage(damage)
        print(f"{attacker.name} attacks {defender.name} for {actual_damage} damage!")
        
        # Check for counter after successful dodge
        if not is_enemy and self.player_dodge_ready:
            self.execute_counter(defender, attacker)
            self.player_dodge_ready = False
    
    def use_technique(self, user, target, technique: CursedTechnique, is_enemy: bool = False):
        """Execute a cursed technique."""
        if not technique.can_use(user.cursed_energy):
            print(f"{user.name} doesn't have enough cursed energy for {technique.name}!")
            return
        
        # Use cursed energy
        user.use_cursed_energy(technique.cost)
        
        # Create technique animation
        try:
            from cutscenes import get_cutscene_manager
            cutscene_manager = get_cutscene_manager()
            
            # Special techniques get full animations
            if any(special in technique.name.lower() for special in ["black flash", "domain expansion", "wukong"]):
                cutscene_manager.create_technique_animation(
                    technique.name, user.name, target.name, True
                )
            else:
                # Regular techniques get brief dramatic moment
                cutscene_manager.show_dramatic_transition("technique_success", 
                    f"⚡ {user.name} channels their cursed energy into {technique.name}!")
                
        except ImportError:
            pass
        
        # Check for dodge
        if technique.technique_type == "offensive" and self.check_dodge(user, target, is_enemy):
            technique.current_cooldown = technique.cooldown  # Still goes on cooldown
            return
        
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
    
    def _check_combat_drama(self, player: Player, enemy: Enemy):
        """Check for dramatic moments during combat."""
        try:
            from cutscenes import get_cutscene_manager
            cutscene_manager = get_cutscene_manager()
            
            # Low HP dramatic moments
            if player.hp <= player.max_hp * 0.2 and random.random() < 0.3:
                taunts = cutscene_manager.get_combat_taunts(player.name, "losing")
                print(f"\n💪 {player.name}: '{random.choice(taunts)}'")
            
            elif enemy.hp <= enemy.max_hp * 0.2 and random.random() < 0.3:
                taunts = cutscene_manager.get_combat_taunts(enemy.name, "losing")
                print(f"\n👹 {enemy.name}: '{random.choice(taunts)}'")
            
            # Transformation moments
            if (player.transformation_active and 
                not hasattr(self, '_transformation_announced')):
                cutscene_manager.show_dramatic_transition("transformation", 
                    f"✨ {player.name}'s {player.transformation_name} power surges!")
                self._transformation_announced = True
                
        except ImportError:
            pass
    
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