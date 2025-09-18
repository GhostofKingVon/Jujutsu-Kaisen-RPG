"""
Enhanced Main Game Loop

Integrates all the new systems including stamina, gameplay modes, world-building,
journal system, and customization into a comprehensive RPG experience.
"""

import os
import sys
from typing import Optional, Dict, Any
from datetime import datetime

from game_state import GameState
from character import Player
from story import StoryManager
from combat import CombatSystem
from stamina_system import StaminaSystem
from gameplay_modes import MissionManager, MissionType
from world_building import WorldManager, WorldEventType
from journal_system import GameJournal, Quest
from customization_system import CharacterCustomization


class EnhancedJujutsuKaisenRPG:
    """Enhanced main game class with all new systems integrated."""
    
    def __init__(self):
        self.game_state = GameState()
        self.player: Optional[Player] = None
        self.story_manager = StoryManager()
        self.combat_system = CombatSystem()
        self.mission_manager = MissionManager()
        self.world_manager = WorldManager()
        self.journal = GameJournal()
        self.customization: Optional[CharacterCustomization] = None
        self.running = True
        self.current_menu = "main"
        
        # Enhanced UI state
        self.show_detailed_stats = False
        self.auto_save_enabled = True
        
    def start_game(self):
        """Initialize and start the enhanced game."""
        self.display_enhanced_title()
        self.show_main_menu()
    
    def display_enhanced_title(self):
        """Display enhanced game title and introduction."""
        print("=" * 70)
        print("           🏯 JUJUTSU KAISEN RPG - ENHANCED EDITION 🏯")
        print("=" * 70)
        print("Welcome to the most immersive Jujutsu Sorcerer experience!")
        print("🌟 New Features:")
        print("  • Advanced Combat with Stamina & Environmental Effects")
        print("  • Stealth, Investigation & Team Battle Missions")
        print("  • Deep Character Customization & Morality System")
        print("  • Dynamic World Events & Comprehensive Lore")
        print("  • In-Game Journal & Crafting Systems")
        print("=" * 70)
        print()
    
    def show_main_menu(self):
        """Display enhanced main menu with new options."""
        while self.running:
            print("\n" + "=" * 50)
            print("🎮 MAIN MENU")
            print("=" * 50)
            print("1. New Game")
            print("2. Load Game")
            print("3. Game Features Guide")
            print("4. Settings")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                self.new_enhanced_game()
            elif choice == "2":
                self.load_game()
            elif choice == "3":
                self.show_features_guide()
            elif choice == "4":
                self.show_settings_menu()
            elif choice == "5":
                self.exit_game()
            else:
                print("Invalid choice. Please enter 1-5.")
    
    def show_features_guide(self):
        """Display guide for new features."""
        print("\n" + "=" * 60)
        print("🌟 ENHANCED FEATURES GUIDE")
        print("=" * 60)
        
        guides = {
            "1": ("Stamina System", [
                "• Actions consume stamina - manage it strategically",
                "• Rest during combat to recover stamina",
                "• Fatigue builds up and affects regeneration",
                "• High stamina = enhanced performance"
            ]),
            "2": ("Morality & Alignment", [
                "• Your choices shape your moral alignment",
                "• Alignment affects story paths and abilities",
                "• Build reputation with different factions",
                "• Unlock unique abilities based on your character"
            ]),
            "3": ("Enhanced Combat", [
                "• Environmental advantages boost performance",
                "• Stamina affects all actions",
                "• Team battles with combo attacks",
                "• Advanced enemy AI and phases"
            ]),
            "4": ("Mission Types", [
                "• Stealth missions: avoid detection",
                "• Investigation: solve mysteries and gather clues",
                "• Team battles: coordinate with allies",
                "• Dynamic objectives and outcomes"
            ]),
            "5": ("Customization", [
                "• Craft weapons and equipment",
                "• Customize appearance and outfits",
                "• Create skill loadouts for different situations",
                "• Upgrade and enchant your gear"
            ]),
            "6": ("World & Lore", [
                "• Discover hidden locations and secrets",
                "• Dynamic world events affect the story",
                "• Comprehensive lore library to unlock",
                "• Artifacts with powerful abilities"
            ])
        }
        
        while True:
            print("\nSelect a topic to learn more (or 'back' to return):")
            for key, (title, _) in guides.items():
                print(f"{key}. {title}")
            
            choice = input("\nChoice: ").strip().lower()
            
            if choice == "back":
                break
            elif choice in guides:
                title, items = guides[choice]
                print(f"\n📖 {title.upper()}")
                print("-" * (len(title) + 4))
                for item in items:
                    print(item)
                input("\nPress Enter to continue...")
            else:
                print("Invalid choice.")
    
    def show_settings_menu(self):
        """Display settings and options."""
        while True:
            print("\n" + "=" * 40)
            print("⚙️ SETTINGS")
            print("=" * 40)
            print(f"1. Detailed Stats Display: {'ON' if self.show_detailed_stats else 'OFF'}")
            print(f"2. Auto-Save: {'ON' if self.auto_save_enabled else 'OFF'}")
            print("3. Reset Save Data")
            print("4. Back to Main Menu")
            
            choice = input("\nChoice: ").strip()
            
            if choice == "1":
                self.show_detailed_stats = not self.show_detailed_stats
                print(f"Detailed stats display {'enabled' if self.show_detailed_stats else 'disabled'}.")
            elif choice == "2":
                self.auto_save_enabled = not self.auto_save_enabled
                print(f"Auto-save {'enabled' if self.auto_save_enabled else 'disabled'}.")
            elif choice == "3":
                confirm = input("Are you sure you want to delete all save data? (yes/no): ").strip().lower()
                if confirm == "yes":
                    self.game_state.delete_save()
                    print("Save data deleted.")
                else:
                    print("Cancelled.")
            elif choice == "4":
                break
            else:
                print("Invalid choice.")
    
    def new_enhanced_game(self):
        """Start a new game with enhanced character creation."""
        print("\n" + "=" * 50)
        print("🌟 ENHANCED CHARACTER CREATION")
        print("=" * 50)
        
        # Basic character info
        name = input("Enter your sorcerer's name: ").strip()
        if not name:
            name = "Unnamed Sorcerer"
        
        # Character customization
        print(f"\nWelcome, {name}! Let's customize your character...")
        
        # Create enhanced player
        self.player = Player(name)
        self.game_state.set_player(self.player)
        
        # Initialize customization system
        self.customization = CharacterCustomization()
        
        # Character background setup
        self._setup_character_background()
        
        # Initialize journal with starting quest
        self._initialize_journal()
        
        print(f"\n✨ {name} is ready to begin their journey!")
        print("📖 Check your journal (J) to see your objectives.")
        print("⚙️ Visit the customization menu (C) to manage equipment.")
        
        # Start the enhanced story
        self.story_manager.start_story(self.game_state)
        self.enhanced_game_loop()
    
    def _setup_character_background(self):
        """Set up character background and goals."""
        print("\n📝 Character Background")
        print("What drives your character? (Choose up to 2)")
        print("1. Protect innocent people")
        print("2. Become the strongest sorcerer")
        print("3. Uncover hidden truths")
        print("4. Honor family legacy")
        print("5. Seek redemption")
        
        choices = input("Enter numbers separated by commas (e.g., 1,3): ").strip().split(',')
        
        motivations = {
            "1": "protect_innocent",
            "2": "become_strongest", 
            "3": "uncover_truths",
            "4": "honor_legacy",
            "5": "seek_redemption"
        }
        
        for choice in choices[:2]:
            choice = choice.strip()
            if choice in motivations:
                motivation = motivations[choice]
                self.player.character_background.add_backstory_element("motivation", motivation)
                
                # Set initial morality based on motivation
                if motivation == "protect_innocent":
                    self.player.update_morality("help_innocent", 2)
                elif motivation == "become_strongest":
                    self.player.update_morality("seek_revenge", 1)
                elif motivation == "uncover_truths":
                    self.player.update_morality("follow_rules", 1)
    
    def _initialize_journal(self):
        """Initialize journal with starting quest."""
        starting_quest = Quest(
            "first_steps",
            "First Steps as a Sorcerer",
            "Begin your journey at Tokyo Jujutsu High and learn the basics.",
            [
                "Attend your first class",
                "Meet your fellow students", 
                "Complete your first mission",
                "Learn a new cursed technique"
            ],
            {"experience": 100, "reputation": 20}
        )
        
        starting_quest.start_quest()
        self.journal.add_quest(starting_quest)
        
        # Add starting character entries
        self.journal.add_character("Gojo Satoru", "Your enigmatic and powerful teacher")
        self.journal.add_character("Yuji Itadori", "Enthusiastic pink-haired student") 
        self.journal.add_character("Megumi Fushiguro", "Serious and talented student")
        self.journal.add_character("Nobara Kugisaki", "Confident and fierce student")
    
    def enhanced_game_loop(self):
        """Enhanced main game loop with all new systems."""
        while self.running and self.player and self.player.is_alive():
            # Advance world state
            self.world_manager.advance_day()
            
            # Check for world events
            self._check_world_events()
            
            # Display enhanced status
            self._display_enhanced_status()
            
            # Show main game menu
            action = self._get_enhanced_action()
            
            if not action:
                continue
                
            # Process action
            self._process_enhanced_action(action)
            
            # Auto-save periodically
            if self.auto_save_enabled and self.game_state.current_chapter % 3 == 0:
                self.game_state.save_game()
    
    def _display_enhanced_status(self):
        """Display comprehensive game status."""
        print("\n" + "=" * 70)
        print(f"📍 Chapter {self.game_state.current_chapter} - {self.game_state.current_location}")
        print("=" * 70)
        
        # Character summary
        if self.player:
            summary = self.player.get_character_summary()
            print(f"👤 {summary}")
            
            if self.show_detailed_stats:
                # Detailed stats
                if hasattr(self.player, 'stamina_system'):
                    print(f"   {self.player.stamina_system.get_status_display()}")
                
                # Equipment summary
                if self.customization:
                    print(f"   {self.customization.equipment.get_equipment_summary()}")
        
        # World status
        world_status = self.world_manager.get_world_status()
        print(f"🌍 Day {world_status['day']} | Events: {world_status['active_events']} | Locations: {world_status['locations_discovered']}/{world_status['total_locations']}")
        
        # Journal summary
        active_quests = len(self.journal.get_active_quests())
        print(f"📖 Active Quests: {active_quests} | Journal Entries: {len(self.journal.lore_entries)}")
        
        print("=" * 70)
    
    def _get_enhanced_action(self):
        """Get enhanced action from player with new options."""
        print("\n🎯 What would you like to do?")
        print("S) Continue Story")
        print("M) Mission Menu") 
        print("J) Journal")
        print("C) Character & Customization")
        print("W) World & Exploration")
        print("I) Inventory & Crafting")
        print("Q) Save & Quit")
        print("H) Help")
        
        choice = input("\nAction: ").strip().lower()
        return choice if choice in ['s', 'm', 'j', 'c', 'w', 'i', 'q', 'h'] else None
    
    def _process_enhanced_action(self, action: str):
        """Process enhanced player actions."""
        if action == 's':
            self._continue_story()
        elif action == 'm':
            self._show_mission_menu()
        elif action == 'j':
            self._show_journal_menu()
        elif action == 'c':
            self._show_character_menu()
        elif action == 'w':
            self._show_world_menu()
        elif action == 'i':
            self._show_inventory_menu()
        elif action == 'q':
            self._save_and_quit()
        elif action == 'h':
            self._show_help()
    
    def _continue_story(self):
        """Continue the main story progression."""
        print("\n📖 Continuing story...")
        
        # Display current scene
        self.story_manager.display_current_scene(self.game_state)
        
        # Show available actions
        actions = self.story_manager.get_available_actions(self.game_state)
        if not actions:
            print("No story actions available. Explore other options.")
            return
            
        print("\nStory Choices:")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action['text']}")
        
        # Get player choice
        try:
            choice = int(input(f"\nChoice (1-{len(actions)}): ")) - 1
            if 0 <= choice < len(actions):
                result = self.story_manager.process_action(choice, self.game_state)
                
                # Handle combat if triggered
                if result.get("combat"):
                    self._handle_story_combat(result)
                
                # Update journal
                self._update_journal_from_story(result)
                
        except ValueError:
            print("Invalid choice.")
    
    def _show_mission_menu(self):
        """Show mission and special gameplay modes."""
        while True:
            print("\n🎯 MISSION MENU")
            print("1. Available Missions")
            print("2. Active Missions")
            print("3. Start Stealth Mission")
            print("4. Start Investigation")
            print("5. Form Team Battle")
            print("6. Back")
            
            choice = input("\nChoice: ").strip()
            
            if choice == "1":
                self._show_available_missions()
            elif choice == "2":
                self._show_active_missions()
            elif choice == "3":
                self._start_stealth_mission()
            elif choice == "4":
                self._start_investigation()
            elif choice == "5":
                self._start_team_battle()
            elif choice == "6":
                break
            else:
                print("Invalid choice.")
    
    def _show_journal_menu(self):
        """Show comprehensive journal interface."""
        while True:
            print("\n📖 JOURNAL MENU")
            print("1. Active Quests")
            print("2. Character Relationships")
            print("3. Lore & Discoveries")
            print("4. Locations Visited")
            print("5. Techniques Learned")
            print("6. Search Journal")
            print("7. Journal Summary")
            print("8. Back")
            
            choice = input("\nChoice: ").strip()
            
            if choice == "1":
                self._show_quest_log()
            elif choice == "2":
                self._show_relationships()
            elif choice == "3":
                self._show_lore_entries()
            elif choice == "4":
                self._show_visited_locations()
            elif choice == "5":
                self._show_learned_techniques()
            elif choice == "6":
                self._search_journal()
            elif choice == "7":
                print(self.journal.get_journal_summary())
                input("Press Enter to continue...")
            elif choice == "8":
                break
            else:
                print("Invalid choice.")
    
    def _show_character_menu(self):
        """Show character customization and development."""
        if not self.customization:
            print("Customization system not available.")
            return
            
        while True:
            print("\n👤 CHARACTER MENU")
            print("1. Character Stats")
            print("2. Equipment & Outfits")
            print("3. Skill Loadouts")
            print("4. Unique Abilities")
            print("5. Moral Alignment")
            print("6. Character Background")
            print("7. Back")
            
            choice = input("\nChoice: ").strip()
            
            if choice == "1":
                self._show_character_stats()
            elif choice == "2":
                self._show_equipment_menu()
            elif choice == "3":
                self._show_loadout_menu()
            elif choice == "4":
                self._show_unique_abilities()
            elif choice == "5":
                self._show_moral_alignment()
            elif choice == "6":
                self._show_character_background()
            elif choice == "7":
                break
            else:
                print("Invalid choice.")
    
    def _check_world_events(self):
        """Check for and handle world events."""
        # Chance for new events based on player level and story progress
        if len(self.world_manager.active_events) < 2:  # Limit concurrent events
            event_chance = min(20, self.player.level * 2)  # Higher level = more events
            
            if self.world_manager.day_count % 7 == 0:  # Weekly event check
                import random
                if random.randint(1, 100) <= event_chance:
                    event_types = list(WorldEventType)
                    event_type = random.choice(event_types)
                    
                    event = self.world_manager.trigger_world_event(
                        event_type, 
                        self.player.level, 
                        self.player.reputation
                    )
                    
                    if event:
                        print(f"\n🌍 WORLD EVENT: {event.name}")
                        print(f"📝 {event.description}")
                        print("This event will affect the world around you!")
                        input("Press Enter to continue...")
    
    def _save_and_quit(self):
        """Save game and quit."""
        print("\n💾 Saving game...")
        if self.game_state.save_game():
            print("Game saved successfully!")
        else:
            print("Failed to save game.")
        
        self.running = False
        print("Thank you for playing Jujutsu Kaisen RPG Enhanced Edition!")
    
    def _show_help(self):
        """Show help and controls."""
        print("\n❓ HELP & CONTROLS")
        print("=" * 40)
        print("S - Continue the main story")
        print("M - Access missions and special gameplay modes")
        print("J - View your journal, quests, and lore")
        print("C - Character customization and development")
        print("W - World exploration and location details")
        print("I - Inventory management and crafting")
        print("Q - Save your progress and quit")
        print("H - Show this help menu")
        print("\n💡 Tips:")
        print("• Manage your stamina during combat")
        print("• Explore thoroughly to find secrets")
        print("• Your choices affect your moral alignment")
        print("• Crafting can create powerful equipment")
        print("• Build relationships for unique abilities")
        input("\nPress Enter to continue...")
    
    # Additional methods would be implemented here for:
    # - _handle_story_combat()
    # - _start_stealth_mission()
    # - _show_equipment_menu()
    # - _show_character_stats()
    # - etc.
    
    def load_game(self):
        """Load a saved game."""
        print("\n=== LOAD GAME ===")
        if self.game_state.load_game():
            self.player = self.game_state.player
            self.story_manager.load_story_state(self.game_state)
            print("Game loaded successfully!")
            
            # Initialize systems for loaded player
            if self.player:
                self.customization = CharacterCustomization()
                # Load customization data if available
                
            self.enhanced_game_loop()
        else:
            print("No saved game found or failed to load.")
    
    def exit_game(self):
        """Exit the game."""
        print("\nThank you for playing Jujutsu Kaisen RPG Enhanced Edition!")
        print("May your cursed energy guide you well... ⚡")
        self.running = False


def main():
    """Main entry point for the enhanced game."""
    try:
        game = EnhancedJujutsuKaisenRPG()
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