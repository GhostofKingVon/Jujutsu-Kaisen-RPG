#!/usr/bin/env python3
"""
Demo script to showcase the Jujutsu Kaisen RPG functionality
"""

from character import Player, Enemy, Trait, CursedTechnique
from combat import CombatSystem
from game_state import GameState
from story import StoryManager
from npcs import NPCManager
from cursed_techniques import TechniqueLibrary


def demo_character_system():
    """Demonstrate the character system with traits and progression."""
    print("=== CHARACTER SYSTEM DEMO ===")
    
    # Create a player
    player = Player("Yuta Okkotsu")
    print(f"Created player: {player.name}")
    print(f"Level: {player.level}, HP: {player.hp}/{player.max_hp}, CE: {player.cursed_energy}/{player.max_cursed_energy}")
    
    # Modify traits
    player.modify_trait(Trait.COMPASSIONATE, 50)
    player.modify_trait(Trait.DETERMINED, 70)
    player.modify_trait(Trait.FOCUSED, 65)
    
    print(f"Dominant traits: {[trait.value for trait in player.get_dominant_traits()]}")
    
    # Level up
    player.gain_experience(250)
    print(f"After gaining experience - Level: {player.level}")
    
    # Show techniques
    print(f"Available techniques: {[t.name for t in player.techniques]}")
    
    print()


def demo_combat_system():
    """Demonstrate the combat system."""
    print("=== COMBAT SYSTEM DEMO ===")
    
    # Create player and enemy
    player = Player("Demo Player")
    player.level = 5
    player.gain_experience(0)  # Trigger level-based technique learning
    
    enemy = Enemy("Grade 2 Cursed Spirit", 80, 40)
    
    print(f"Combat: {player.name} vs {enemy.name}")
    print(f"Player techniques: {[t.name for t in player.techniques]}")
    
    # Simulate a few combat actions
    combat = CombatSystem()
    
    # Test basic attack
    print("\n--- Testing Basic Attack ---")
    combat.basic_attack(player, enemy)
    print(f"Enemy HP after attack: {enemy.hp}/{enemy.max_hp}")
    
    # Test technique usage
    if player.techniques:
        print("\n--- Testing Cursed Technique ---")
        technique = player.techniques[0]
        combat.use_technique(player, enemy, technique)
        print(f"Enemy HP after technique: {enemy.hp}/{enemy.max_hp}")
    
    print()


def demo_story_system():
    """Demonstrate the story and choice system."""
    print("=== STORY SYSTEM DEMO ===")
    
    # Create game state and story manager
    game_state = GameState()
    player = Player("Story Demo")
    game_state.set_player(player)
    
    story_manager = StoryManager()
    story_manager.start_story(game_state)
    
    print(f"Current chapter: {game_state.current_chapter}")
    print(f"Current location: {game_state.current_location}")
    
    # Show current scene
    story_manager.display_current_scene(game_state)
    
    # Show available actions
    actions = story_manager.get_available_actions(game_state)
    print(f"\nAvailable actions: {len(actions)}")
    for i, action in enumerate(actions, 1):
        print(f"  {i}. {action['text']}")
    
    print()


def demo_npc_system():
    """Demonstrate the NPC relationship system."""
    print("=== NPC SYSTEM DEMO ===")
    
    # Create NPC manager and game state
    npc_manager = NPCManager()
    game_state = GameState()
    player = Player("NPC Demo")
    player.modify_trait(Trait.COMPASSIONATE, 70)
    game_state.set_player(player)
    
    # Interact with Yuji
    print("Interacting with Yuji Itadori...")
    result = npc_manager.interact_with_npc("yuji", game_state)
    print(f"Yuji says: \"{result['dialogue']}\"")
    print(f"Relationship change: +{result['relationship_change']}")
    
    # Check relationship status
    relationship = game_state.get_relationship("yuji")
    status = npc_manager.get_relationship_status("yuji", relationship)
    print(f"Relationship with Yuji: {relationship} ({status})")
    
    # Simulate multiple interactions
    for i in range(5):
        npc_manager.interact_with_npc("yuji", game_state)
    
    final_relationship = game_state.get_relationship("yuji")
    final_status = npc_manager.get_relationship_status("yuji", final_relationship)
    print(f"After multiple interactions - Relationship: {final_relationship} ({final_status})")
    
    print()


def demo_cursed_techniques():
    """Demonstrate the cursed techniques system."""
    print("=== CURSED TECHNIQUES DEMO ===")
    
    technique_lib = TechniqueLibrary()
    
    # Show techniques available at different levels
    for level in [1, 5, 10, 15, 20]:
        techniques = technique_lib.get_techniques_by_level(level)
        print(f"Level {level} techniques: {len(techniques)} available")
        print(f"  Examples: {techniques[:3]}")
    
    # Get a specific technique
    black_flash = technique_lib.get_technique("black_flash")
    if black_flash:
        print(f"\nBlack Flash technique:")
        print(f"  Damage: {black_flash.damage}")
        print(f"  Cost: {black_flash.cost} CE")
        print(f"  Description: {black_flash.description}")
    
    print()


def demo_save_load():
    """Demonstrate save/load functionality."""
    print("=== SAVE/LOAD SYSTEM DEMO ===")
    
    # Create a game state with some progress
    game_state = GameState()
    player = Player("Save Demo")
    player.level = 3
    player.modify_trait(Trait.FOCUSED, 60)
    game_state.set_player(player)
    game_state.advance_chapter(5)
    game_state.set_location("Shibuya District")
    game_state.update_relationship("yuji", 45)
    
    print("Created game state with progress:")
    print(f"  Player: {player.name} (Level {player.level})")
    print(f"  Chapter: {game_state.current_chapter}")
    print(f"  Location: {game_state.current_location}")
    print(f"  Yuji relationship: {game_state.get_relationship('yuji')}")
    
    # Save the game
    print("\nSaving game...")
    success = game_state.save_game()
    print(f"Save successful: {success}")
    
    # Create a new game state and load
    print("\nLoading game...")
    new_game_state = GameState()
    load_success = new_game_state.load_game()
    print(f"Load successful: {load_success}")
    
    if load_success:
        print("Loaded game state:")
        print(f"  Player: {new_game_state.player.name} (Level {new_game_state.player.level})")
        print(f"  Chapter: {new_game_state.current_chapter}")
        print(f"  Location: {new_game_state.current_location}")
        print(f"  Yuji relationship: {new_game_state.get_relationship('yuji')}")
    
    print()


def main():
    """Run all demonstrations."""
    print("🎮 JUJUTSU KAISEN RPG - SYSTEM DEMONSTRATIONS")
    print("=" * 60)
    
    demo_character_system()
    demo_combat_system()
    demo_story_system()
    demo_npc_system()
    demo_cursed_techniques()
    demo_save_load()
    
    print("=" * 60)
    print("🎉 All systems demonstrated successfully!")
    print("Run 'python3 main.py' to start the actual game!")


if __name__ == "__main__":
    main()