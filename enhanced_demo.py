#!/usr/bin/env python3
"""
Enhanced Demo Script - Showcasing New Gameplay Features

Demonstrates the enhanced combat mechanics, character techniques,
and character development systems added to the Jujutsu Kaisen RPG.
"""

from character import Player, Enemy, Trait, CursedTechnique
from combat import CombatSystem
from game_state import GameState
from story import StoryManager
from npcs import NPCManager


def demo_enhanced_combat():
    """Demonstrate enhanced combat with combos, ultimates, and environmental effects."""
    print("=== ENHANCED COMBAT SYSTEM DEMO ===")
    
    player = Player("Enhanced Fighter")
    player.gain_experience(200)  # Level up to test features
    
    enemy = Enemy("Enhanced Curse", 100, 50)
    
    combat = CombatSystem()
    
    print(f"\n🎯 Testing Enhanced Combat Features:")
    print(f"Player: {player.name} (Level {player.level})")
    print(f"Enemy: {enemy.name}")
    
    # Test terrain effects
    print(f"\n🌍 Testing Environmental Effects:")
    print("Combat in forest terrain with shadowy cover and natural energy...")
    combat._initialize_terrain_effects("forest")
    print(f"Environmental effects: {combat.environmental_effects}")
    
    # Test combo system
    print(f"\n💥 Testing Combo System:")
    print("Simulating successful attacks...")
    combat.process_combo_system(player, "attack", True)
    combat.process_combo_system(player, "technique", True)
    combat.process_combo_system(player, "attack", True)
    print(f"Combo count: {combat.combo_count}, Multiplier: {combat.combo_multiplier:.1f}x")
    
    # Test ultimate system
    print(f"\n🌟 Testing Ultimate System:")
    combat.ultimate_energy = 100  # Simulate building ultimate
    if combat.check_ultimate_available(player):
        print("Ultimate technique available!")
        ultimate_result = combat.use_ultimate_technique(player, enemy)
        print(f"Ultimate used: {ultimate_result.get('name', 'Unknown')}")
    
    # Test environmental interactions
    print(f"\n🌿 Testing Environmental Interactions:")
    env_result = combat.apply_environmental_interaction("technique", player, enemy)
    if env_result.get("interactions"):
        print(f"Environmental bonus: +{env_result.get('bonus_damage', 0)} damage")
    
    print()


def demo_skill_tree_system():
    """Demonstrate the skill tree and technique mastery system."""
    print("=== SKILL TREE AND MASTERY SYSTEM DEMO ===")
    
    player = Player("Skill Apprentice")
    
    # Simulate gaining levels and skill points
    player.gain_experience(300)
    player.gain_skill_point(5)
    
    # Set some dominant traits
    player.modify_trait(Trait.FOCUSED, 80)
    player.modify_trait(Trait.ANALYTICAL, 70)
    
    print(f"\n🎯 Player Status:")
    print(f"Level: {player.level}")
    print(f"Skill Points: {player.skill_points}")
    print(f"Dominant Traits: {[t.value for t in player.get_dominant_traits()]}")
    
    # Show available upgrades
    print(f"\n📚 Available Technique Upgrades:")
    upgrades = player.get_available_technique_upgrades()
    for i, upgrade in enumerate(upgrades[:5], 1):  # Show first 5
        print(f"{i}. {upgrade['type'].title()}: {upgrade['technique_name']}")
        print(f"   Cost: {upgrade['cost']} SP - {upgrade['description']}")
        if upgrade.get('requirements'):
            print(f"   Requirements: {', '.join(upgrade['requirements'])}")
    
    # Test technique mastery
    print(f"\n🌟 Testing Technique Mastery:")
    if player.techniques:
        technique = player.techniques[0]
        print(f"Technique: {technique.name}")
        print(f"Before: {technique.get_mastery_description()}")
        
        # Simulate using technique multiple times
        for _ in range(10):
            technique.gain_mastery_exp(2)
        
        print(f"After training: {technique.get_mastery_description()}")
    
    # Test spending skill points
    print(f"\n💰 Testing Skill Point Spending:")
    if upgrades:
        first_upgrade = upgrades[0]
        success = player.spend_skill_points(first_upgrade['type'], first_upgrade['technique_name'])
        if success:
            print(f"Successfully purchased: {first_upgrade['technique_name']}")
        else:
            print(f"Failed to purchase: {first_upgrade['technique_name']}")
    
    print()


def demo_character_development():
    """Demonstrate enhanced character development features."""
    print("=== CHARACTER DEVELOPMENT SYSTEM DEMO ===")
    
    game_state = GameState()
    player = Player("Character Developer")
    game_state.set_player(player)
    
    story_manager = StoryManager()
    
    # Set up character for development features
    player.gain_experience(400)
    player.modify_trait(Trait.COMPASSIONATE, 90)
    player.modify_trait(Trait.PROTECTIVE, 75)
    
    # Simulate relationship building
    game_state.update_relationship("yuji", 65)
    game_state.update_relationship("gojo", 45)
    
    print(f"\n🎭 Character Status:")
    print(f"Level: {player.level}")
    print(f"Dominant Traits: {[t.value for t in player.get_dominant_traits()]}")
    print(f"Relationships:")
    for npc, level in game_state.relationships.items():
        if level > 0:
            print(f"  • {npc.title()}: {level}")
    
    # Show available personal missions
    print(f"\n🎯 Available Personal Missions:")
    missions = story_manager.get_available_personal_missions(game_state)
    for i, mission in enumerate(missions, 1):
        print(f"{i}. {mission['title']}")
        print(f"   {mission['description']}")
        print(f"   Chapters: {mission.get('chapters', 'Any')}")
        print(f"   Requirements: {', '.join(mission['requirements'])}")
        print(f"   Rewards: {', '.join(mission['rewards'])}")
        print()
    
    # Test backstory event simulation
    print(f"\n📖 Testing Character Backstory Events:")
    print("Simulating discovery of character backstory...")
    
    # Simulate finding a backstory trigger
    print("You discover an old letter with your family name...")
    print("This would normally trigger an interactive backstory event.")
    
    # Show character arc progression
    print(f"\n📈 Character Development Progress:")
    print(f"Total trait growth: {sum(player.traits.values())}")
    print(f"Relationship bonds: {len([r for r in game_state.relationships.values() if r > 50])}")
    print(f"Techniques mastered: {len([t for t in player.techniques if t.mastery_level > 1])}")
    
    print()


def demo_exploration_enhancements():
    """Demonstrate enhanced exploration features."""
    print("=== ENHANCED EXPLORATION SYSTEM DEMO ===")
    
    game_state = GameState()
    player = Player("Explorer")
    game_state.set_player(player)
    game_state.set_location("Tokyo Jujutsu High - Hidden Areas")
    
    story_manager = StoryManager()
    
    print(f"\n🗺️ Current Location: {game_state.current_location}")
    
    # Test various exploration outcomes
    print(f"\n🔍 Testing Enhanced Exploration Outcomes:")
    
    exploration_scenarios = [
        "hidden shrine discovery",
        "character backstory trigger", 
        "technique knowledge finding",
        "spiritual encounter"
    ]
    
    for scenario in exploration_scenarios:
        print(f"\n📍 Scenario: {scenario.title()}")
        
        if scenario == "hidden shrine discovery":
            story_manager._spiritual_encounter(game_state)
        elif scenario == "character backstory trigger":
            print("Would trigger: Interactive backstory event with multiple choices")
            print("Example: Discovering family legacy, facing past trauma, or hidden talent")
        elif scenario == "technique knowledge finding":
            story_manager._find_technique_knowledge(game_state)
        elif scenario == "spiritual encounter":
            story_manager._spiritual_encounter(game_state)
    
    # Show discovery flags
    print(f"\n🏆 Story Flags and Discoveries:")
    for flag, value in game_state.story_flags.items():
        if value:
            print(f"  ✓ {flag.replace('_', ' ').title()}")
    
    print()


def demo_integration_showcase():
    """Show how all systems work together."""
    print("=== INTEGRATED SYSTEMS SHOWCASE ===")
    
    game_state = GameState()
    player = Player("Master Sorcerer")
    game_state.set_player(player)
    
    # Build up character through gameplay simulation
    print("🎮 Simulating Complete Character Journey:")
    
    # Level progression
    player.gain_experience(500)
    print(f"✓ Reached Level {player.level}")
    
    # Trait development through choices
    player.modify_trait(Trait.DETERMINED, 85)
    player.modify_trait(Trait.FOCUSED, 70)
    player.modify_trait(Trait.PROTECTIVE, 60)
    print(f"✓ Developed traits: {[t.value for t in player.get_dominant_traits()]}")
    
    # Relationship building
    game_state.update_relationship("yuji", 80)
    game_state.update_relationship("megumi", 70)
    game_state.update_relationship("nobara", 75)
    print(f"✓ Built strong relationships with first-year students")
    
    # Technique mastery
    for technique in player.techniques:
        for _ in range(15):
            technique.gain_mastery_exp(2)
    print(f"✓ Mastered techniques to higher levels")
    
    # Skills and abilities unlocked
    player.gain_skill_point(10)
    available_upgrades = player.get_available_technique_upgrades()
    print(f"✓ {len(available_upgrades)} technique upgrades available")
    
    # Personal missions available
    story_manager = StoryManager()
    missions = story_manager.get_available_personal_missions(game_state)
    print(f"✓ {len(missions)} personal missions unlocked")
    
    # Combat capabilities
    combat = CombatSystem()
    combat.ultimate_energy = 100
    print(f"✓ Ultimate techniques ready for combat")
    
    print(f"\n🎉 Character fully developed with interconnected systems!")
    print(f"📊 Final Stats:")
    print(f"   Level: {player.level}")
    print(f"   HP: {player.max_hp}")
    print(f"   Cursed Energy: {player.max_cursed_energy}")
    print(f"   Skill Points: {player.skill_points}")
    print(f"   Techniques: {len(player.techniques)}")
    print(f"   Relationships: {len([r for r in game_state.relationships.values() if r > 0])}")
    print(f"   Missions Available: {len(missions)}")


def main():
    """Run all enhanced feature demonstrations."""
    print("🎮 JUJUTSU KAISEN RPG - ENHANCED FEATURES DEMONSTRATION")
    print("=" * 80)
    print("Showcasing new gameplay mechanics, character techniques,")
    print("and character development features.")
    print("=" * 80)
    
    demo_enhanced_combat()
    demo_skill_tree_system()
    demo_character_development()
    demo_exploration_enhancements()
    demo_integration_showcase()
    
    print("=" * 80)
    print("🎉 Enhanced features demonstration complete!")
    print("New systems include:")
    print("✓ Combo system with damage multipliers")
    print("✓ Ultimate techniques based on character traits")
    print("✓ Environmental interactions and terrain effects")
    print("✓ Technique mastery and skill tree progression")
    print("✓ Personal missions and character development")
    print("✓ Enhanced exploration with backstory events")
    print("✓ Integrated progression systems")
    print("=" * 80)


if __name__ == "__main__":
    main()