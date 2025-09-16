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
            
            # Auto-save progress
            if self.game_state.current_chapter % 5 == 0:  # Save every 5 chapters
                self.game_state.save_game()
    
    def display_actions(self, actions):
        """Display available actions to the player."""
        print("\nWhat would you like to do?")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action['text']}")
        print(f"{len(actions) + 1}. Save Game")
        print(f"{len(actions) + 2}. Return to Main Menu")
    
    def get_player_choice(self, num_actions):
        """Get and validate player choice."""
        try:
            choice = int(input(f"\nEnter your choice (1-{num_actions + 2}): "))
            
            if choice == num_actions + 1:
                self.game_state.save_game()
                print("Game saved!")
                return None
            elif choice == num_actions + 2:
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