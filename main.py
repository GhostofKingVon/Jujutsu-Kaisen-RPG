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
        
        # Enhanced character creation
        self._character_creation_process()
        
        self.game_state.set_player(self.player)
        
        print(f"\nWelcome, {name}!")
        print("Your journey as a Jujutsu Sorcerer begins...")
        
        # Start the story
        self.story_manager.start_story(self.game_state)
        self.game_loop()
    
    def _character_creation_process(self):
        """Enhanced character creation process for traits and techniques."""
        print("\n" + "=" * 60)
        print("            CHARACTER CREATION")
        print("=" * 60)
        print("Before beginning your journey, let's shape your character's")
        print("personality and innate abilities.")
        
        # Trait selection
        self._select_initial_traits()
        
        # Cursed technique selection
        self._select_initial_techniques()
        
        # Display final character summary
        self._display_character_summary()
    
    def _select_initial_traits(self):
        """Allow player to select initial dominant traits."""
        print("\n🌟 TRAIT SELECTION")
        print("-" * 30)
        print("Choose 2 dominant traits that define your character's personality.")
        print("These will affect your dialogue options, relationships, and available techniques.\n")
        
        from character import Trait
        traits = list(Trait)
        trait_descriptions = {
            Trait.COMPASSIONATE: "Shows empathy and care for others, unlocks protective techniques",
            Trait.FOCUSED: "Maintains concentration and precision, enhances accuracy and critical hits",
            Trait.AGGRESSIVE: "Favors direct confrontation, increases offensive technique power",
            Trait.PROTECTIVE: "Prioritizes defending others, unlocks barrier and support techniques",
            Trait.ANALYTICAL: "Studies situations carefully, gains tactical advantages and utility techniques",
            Trait.RECKLESS: "Acts without hesitation, increases risk/reward and explosive techniques",
            Trait.DETERMINED: "Never gives up, improves endurance and recovery abilities",
            Trait.CAUTIOUS: "Plans ahead carefully, improves defensive capabilities and evasion"
        }
        
        # Display trait options
        for i, trait in enumerate(traits, 1):
            print(f"{i}. {trait.value}")
            print(f"   {trait_descriptions[trait]}\n")
        
        selected_traits = []
        while len(selected_traits) < 2:
            try:
                choice = int(input(f"Select trait {len(selected_traits) + 1} (1-{len(traits)}): ")) - 1
                if 0 <= choice < len(traits):
                    selected_trait = traits[choice]
                    if selected_trait not in selected_traits:
                        selected_traits.append(selected_trait)
                        print(f"✓ Selected: {selected_trait.value}")
                    else:
                        print("You've already selected that trait. Choose a different one.")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Set selected traits to high values (60+)
        for trait in selected_traits:
            self.player.modify_trait(trait, 65)
        
        print(f"\n🎭 Your dominant traits: {', '.join(t.value for t in selected_traits)}")
    
    def _select_initial_techniques(self):
        """Allow player to select initial cursed techniques."""
        print("\n⚡ CURSED TECHNIQUE SELECTION")
        print("-" * 35)
        print("Choose your innate cursed technique. This will be your signature ability")
        print("that grows stronger as you progress.\n")
        
        from cursed_techniques import TechniqueLibrary
        technique_lib = TechniqueLibrary()
        
        # Offer a curated selection of starter techniques
        starter_techniques = {
            "shadow_manipulation": {
                "name": "Shadow Manipulation",
                "description": "Control shadows to create constructs and attacks. Grows into powerful shikigami.",
                "techniques": ["shadow_clone", "divine_dogs"]
            },
            "energy_enhancement": {
                "name": "Cursed Energy Enhancement", 
                "description": "Enhance physical abilities with cursed energy. Masters critical timing.",
                "techniques": ["cursed_energy_burst", "divergent_fist"]
            },
            "monkey_king_style": {
                "name": "Monkey King Style",
                "description": "Original technique inspired by Sun Wukong. Emphasizes agility and adaptability.",
                "techniques": ["wukong_technique", "cloud_somersault"]
            },
            "barrier_arts": {
                "name": "Barrier Arts",
                "description": "Specialize in defensive and support techniques. Protects allies and controls space.",
                "techniques": ["barrier_technique", "cursed_energy_guard"]
            },
            "tool_mastery": {
                "name": "Cursed Tool Mastery",
                "description": "Expert use of cursed tools and weapons. Combines skill with cursed energy.",
                "techniques": ["weapon_mastery", "straw_doll"]
            }
        }
        
        # Display technique options
        technique_choices = list(starter_techniques.keys())
        for i, tech_key in enumerate(technique_choices, 1):
            tech_info = starter_techniques[tech_key]
            print(f"{i}. {tech_info['name']}")
            print(f"   {tech_info['description']}")
            print(f"   Starting techniques: {', '.join(tech_info['techniques'])}\n")
        
        while True:
            try:
                choice = int(input(f"Select your cursed technique specialization (1-{len(technique_choices)}): ")) - 1
                if 0 <= choice < len(technique_choices):
                    selected_key = technique_choices[choice]
                    selected_tech = starter_techniques[selected_key]
                    
                    # Add the specialized techniques
                    for tech_name in selected_tech["techniques"]:
                        technique = technique_lib.get_technique(tech_name)
                        if technique:
                            self.player.add_technique(technique)
                            self.game_state.unlock_technique(tech_name)
                    
                    print(f"\n⚡ Specialized in: {selected_tech['name']}")
                    print(f"✓ Learned: {', '.join(selected_tech['techniques'])}")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    def _display_character_summary(self):
        """Display final character creation summary."""
        print("\n" + "=" * 60)
        print("            CHARACTER SUMMARY")
        print("=" * 60)
        print(f"Name: {self.player.name}")
        print(f"Level: {self.player.level}")
        print(f"HP: {self.player.hp}/{self.player.max_hp}")
        print(f"Cursed Energy: {self.player.cursed_energy}/{self.player.max_cursed_energy}")
        
        dominant_traits = self.player.get_dominant_traits()
        print(f"Dominant Traits: {', '.join(t.value for t in dominant_traits)}")
        
        techniques = [t.name for t in self.player.techniques]
        print(f"Known Techniques: {', '.join(techniques)}")
        
        print("\nYour character is ready for the world of Jujutsu Sorcery!")
        print("=" * 60)
        input("\nPress Enter to continue...")
    
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
        if self.story_manager.in_downtime:
            print("\n🎯 Available Activities:")
            for i, action in enumerate(actions, 1):
                if action.get("description"):
                    print(f"{i}. {action['text']}")
                    print(f"   {action['description']}")
                else:
                    print(f"{i}. {action['text']}")
                print()
        else:
            print("\nWhat would you like to do?")
            for i, action in enumerate(actions, 1):
                if action.get("description"):
                    print(f"{i}. {action['text']}")
                    print(f"   {action['description']}")
                else:
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