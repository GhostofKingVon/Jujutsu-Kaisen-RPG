#!/usr/bin/env python3
"""
Jujutsu Kaisen RPG - Main Game Entry Point

A turn-based RPG following the Jujutsu Kaisen manga with player choice-driven story,
character evolution, and strategic combat featuring cursed techniques.
"""

import os
import sys
from typing import Optional

from game_state import GameState
from character import Player
from story import StoryManager
from combat import CombatSystem


class JujutsuKaisenRPG:
    """Main game class that manages the overall game flow and systems."""
    
    def __init__(self):
        self.game_state = GameState()
        self.player: Optional[Player] = None
        self.story_manager = StoryManager()
        self.combat_system = CombatSystem()
        self.running = True
    
    def start_game(self):
        """Initialize and start the game."""
        self.display_title()
        self.show_main_menu()
    
    def display_title(self):
        """Display the game title and introduction."""
        print("=" * 60)
        print("           JUJUTSU KAISEN RPG")
        print("=" * 60)
        print("Welcome to the world of Jujutsu Sorcerers!")
        print("Face cursed spirits, master cursed techniques,")
        print("and shape your destiny through choices and bonds.")
        print("=" * 60)
        print()
    
    def show_main_menu(self):
        """Display the main menu and handle user choices."""
        while self.running:
            print("\n=== MAIN MENU ===")
            print("1. New Game")
            print("2. Load Game")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                self.new_game()
            elif choice == "2":
                self.load_game()
            elif choice == "3":
                self.exit_game()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    
    def new_game(self):
        """Start a new game with character creation."""
        print("\n=== NEW GAME ===")
        print("Creating your sorcerer...")
        
        # Character creation
        name = input("Enter your character's name: ").strip()
        if not name:
            name = "Unnamed Sorcerer"
        
        self.player = Player(name)
        self.game_state.set_player(self.player)
        
        print(f"\nWelcome, {name}!")
        print("Your journey as a Jujutsu Sorcerer begins...")
        
        # Start the story
        self.story_manager.start_story(self.game_state)
        self.game_loop()
    
    def load_game(self):
        """Load a saved game."""
        print("\n=== LOAD GAME ===")
        if self.game_state.load_game():
            self.player = self.game_state.player
            self.story_manager.load_story_state(self.game_state)
            print("Game loaded successfully!")
            self.game_loop()
        else:
            print("No saved game found or failed to load.")
    
    def game_loop(self):
        """Main game loop handling story progression and player actions."""
        while self.running and self.player and self.player.is_alive():
            print("\n" + "=" * 50)
            print(f"Chapter: {self.game_state.current_chapter}")
            print(f"Location: {self.game_state.current_location}")
            print("=" * 50)
            
            # Display current situation
            self.story_manager.display_current_scene(self.game_state)
            
            # Show available actions
            actions = self.story_manager.get_available_actions(self.game_state)
            self.display_actions(actions)
            
            # Get player choice
            choice = self.get_player_choice(len(actions))
            if choice is None:
                continue
            
            # Process the action
            result = self.story_manager.process_action(choice - 1, self.game_state)
            
            # Handle combat if triggered
            if result.get("combat"):
                enemy = result["enemy"]
                combat_result = self.combat_system.start_combat(self.player, enemy)
                if not combat_result:
                    print("Game Over!")
                    self.running = False
            
            # Check for game ending conditions
            if result.get("game_over"):
                print(result.get("message", "Game Over!"))
                self.running = False
            
            # Check personal mission progress
            self.story_manager.check_personal_mission_progress(self.game_state)
            
            # Auto-save progress
            if self.game_state.current_chapter % 5 == 0:  # Save every 5 chapters
                self.game_state.save_game()
    
    def display_actions(self, actions):
        """Display available actions to the player."""
        print("\nWhat would you like to do?")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action['text']}")
        print(f"{len(actions) + 1}. Character Development")
        print(f"{len(actions) + 2}. Save Game")
        print(f"{len(actions) + 3}. Return to Main Menu")
    
    def get_player_choice(self, num_actions):
        """Get and validate player choice."""
        try:
            choice = int(input(f"\nEnter your choice (1-{num_actions + 3}): "))
            
            if choice == num_actions + 1:
                self.show_character_development_menu()
                return None
            elif choice == num_actions + 2:
                self.game_state.save_game()
                print("Game saved!")
                return None
            elif choice == num_actions + 3:
                self.running = False
                return None
            elif 1 <= choice <= num_actions:
                return choice
            else:
                print("Invalid choice. Please try again.")
                return None
        except ValueError:
            print("Please enter a valid number.")
            return None
    
    def show_character_development_menu(self):
        """Show character development options."""
        print("\n=== CHARACTER DEVELOPMENT ===")
        print(f"🎭 {self.player.name} - Level {self.player.level}")
        print(f"💪 HP: {self.player.hp}/{self.player.max_hp}")
        print(f"⚡ CE: {self.player.cursed_energy}/{self.player.max_cursed_energy}")
        print(f"🌟 Skill Points: {self.player.skill_points}")
        print(f"🎯 Traits: {[t.value for t in self.player.get_dominant_traits()]}")
        
        while True:
            print("\n1. View Techniques and Mastery")
            print("2. Spend Skill Points")
            print("3. View Personal Missions")
            print("4. View Relationships")
            print("5. Return to Game")
            
            try:
                choice = int(input("\nChoose an option (1-5): "))
                
                if choice == 1:
                    self.show_techniques_menu()
                elif choice == 2:
                    self.show_skill_spending_menu()
                elif choice == 3:
                    self.show_personal_missions()
                elif choice == 4:
                    self.show_relationships()
                elif choice == 5:
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
    
    def show_techniques_menu(self):
        """Show player's techniques and their mastery levels."""
        print("\n=== TECHNIQUES & MASTERY ===")
        if not self.player.techniques:
            print("No techniques learned yet.")
            return
        
        for i, technique in enumerate(self.player.techniques, 1):
            print(f"{i}. {technique.name}")
            print(f"   {technique.get_mastery_description()}")
            print(f"   Type: {technique.technique_type.title()}")
            print(f"   Usage Count: {technique.usage_count}")
            if technique.current_cooldown > 0:
                print(f"   Cooldown: {technique.current_cooldown} turns")
            print()
    
    def show_skill_spending_menu(self):
        """Show skill point spending options."""
        print(f"\n=== SKILL POINT SPENDING ===")
        print(f"Available Skill Points: {self.player.skill_points}")
        
        upgrades = self.player.get_available_technique_upgrades()
        if not upgrades:
            print("No upgrades available at this time.")
            return
        
        print("\nAvailable Upgrades:")
        for i, upgrade in enumerate(upgrades, 1):
            print(f"{i}. {upgrade['technique_name']} ({upgrade['type'].title()})")
            print(f"   Cost: {upgrade['cost']} SP")
            print(f"   {upgrade['description']}")
            if upgrade.get('requirements'):
                print(f"   Requirements: {', '.join(upgrade['requirements'])}")
            print()
        
        try:
            choice = int(input(f"Choose upgrade (1-{len(upgrades)}) or 0 to cancel: "))
            if 1 <= choice <= len(upgrades):
                upgrade = upgrades[choice - 1]
                success = self.player.spend_skill_points(upgrade['type'], upgrade['technique_name'])
                if not success:
                    input("Press Enter to continue...")
            elif choice != 0:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
    
    def show_personal_missions(self):
        """Show available personal missions."""
        print("\n=== PERSONAL MISSIONS ===")
        missions = self.story_manager.get_available_personal_missions(self.game_state)
        
        if not missions:
            print("No personal missions available at this time.")
            print("Complete more story content and build relationships to unlock missions.")
            return
        
        for i, mission in enumerate(missions, 1):
            print(f"{i}. {mission['title']}")
            print(f"   {mission['description']}")
            print(f"   Requirements: {', '.join(mission['requirements'])}")
            print(f"   Rewards: {', '.join(mission['rewards'])}")
            print()
        
        try:
            choice = int(input(f"Start mission (1-{len(missions)}) or 0 to cancel: "))
            if 1 <= choice <= len(missions):
                mission = missions[choice - 1]
                result = self.story_manager.start_personal_mission(mission['id'], self.game_state)
                if result['success']:
                    print(f"✅ Started mission: {mission['title']}")
                else:
                    print(f"❌ {result['message']}")
                input("Press Enter to continue...")
            elif choice != 0:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
    
    def show_relationships(self):
        """Show relationship status with NPCs."""
        print("\n=== RELATIONSHIPS ===")
        
        from npcs import NPCManager
        npc_manager = NPCManager()
        
        if not self.game_state.relationships:
            print("No relationships established yet.")
            return
        
        for npc_name, level in self.game_state.relationships.items():
            if level > 0:
                status = npc_manager.get_relationship_status(npc_name, level)
                print(f"{npc_name.title()}: {level}/100 ({status})")
        
        # Show available team combos
        combos = npc_manager.check_team_combo_availability(self.game_state.relationships)
        if combos:
            print(f"\n🤝 Available Team Combinations:")
            for combo in combos:
                print(f"  • {combo}")
        
        input("\nPress Enter to continue...")
    
    def exit_game(self):
        """Exit the game."""
        print("\nThank you for playing Jujutsu Kaisen RPG!")
        print("May your cursed energy guide you well...")
        self.running = False


def main():
    """Main entry point for the game."""
    try:
        game = JujutsuKaisenRPG()
        game.start_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("The game will now exit.")
    finally:
        sys.exit(0)


if __name__ == "__main__":
    main()