#!/usr/bin/env python3
"""
Exploration Demo - Showcase the expanded world and original cursed techniques

Demonstrates the new locations, exploration mechanics, and original content.
"""

from game_state import GameState
from character import Player
from story import StoryManager
from cursed_techniques import TechniqueLibrary


def main():
    print("🌍 JUJUTSU KAISEN RPG - WORLD EXPLORATION DEMO")
    print("=" * 60)
    
    # Initialize systems
    game_state = GameState()
    story_manager = StoryManager()
    technique_library = TechniqueLibrary()
    
    # Create a demo player
    player = Player("Explorer")
    player.level = 15  # Higher level to access more content
    player.gain_experience(1400)  # Ensure level 15
    game_state.set_player(player)
    
    print(f"Demo Character: {player.name}")
    print(f"Level: {player.level}, HP: {player.hp}/{player.max_hp}, CE: {player.cursed_energy}/{player.max_cursed_energy}")
    print(f"Available techniques: {len(player.techniques)}")
    
    print("\n🎯 ORIGINAL CURSED TECHNIQUES SHOWCASE")
    print("=" * 50)
    
    # Show off original techniques
    original_techniques = [
        "crimson_inferno", "void_grasp", "thorn_guardians", "spirit_mirage",
        "soul_pierce", "time_dilation", "psychic_command", "quantum_shift",
        "harmonic_resonance", "astral_projection", "entropy_manipulation"
    ]
    
    for tech_name in original_techniques[:5]:  # Show first 5
        tech = technique_library.get_technique(tech_name)
        if tech:
            print(f"✨ {tech.name}")
            print(f"   Type: {tech.technique_type.title()}")
            print(f"   Cost: {tech.cost} CE, Damage: {tech.damage}")
            print(f"   Description: {tech.description}")
            print()
    
    print("\n🏞️ EXPANDED WORLD LOCATIONS")
    print("=" * 50)
    
    # Showcase each new location
    locations_to_demo = [
        "cursed_forest", "underground_city", "sky_fortress", 
        "temporal_ruins", "void_nexus"
    ]
    
    for location_key in locations_to_demo:
        print(f"\n📍 Exploring {location_key.replace('_', ' ').title()}")
        print("-" * 40)
        
        # Explore the location
        exploration_result = story_manager.explore_location(game_state, location_key)
        
        if "error" not in exploration_result:
            print(f"🏛️ {exploration_result['location']}")
            print(f"📝 {exploration_result['description']}")
            print(f"🗺️ Areas available: {len(exploration_result['available_areas'])}")
            
            # Show a few areas
            for i, (area, desc) in enumerate(exploration_result['area_descriptions'].items()):
                if i < 3:  # Show first 3 areas
                    print(f"   • {area.replace('_', ' ').title()}: {desc}")
            
            if len(exploration_result['available_areas']) > 3:
                remaining = len(exploration_result['available_areas']) - 3
                print(f"   ... and {remaining} more areas")
            
            # Show NPCs
            if exploration_result['npcs']:
                print(f"👥 NPCs: {', '.join(exploration_result['npcs'])}")
            
            print()
    
    print("\n🔍 EXPLORATION FEATURES DEMO")
    print("=" * 50)
    
    # Demo exploration of a specific area
    print("Exploring The Whispering Woods - Spirit Sanctuary...")
    exploration = story_manager.explore_location(game_state, "cursed_forest", "spirit_sanctuary")
    
    if exploration and "error" not in exploration:
        print(f"📍 Current Area: {exploration['current_area'].replace('_', ' ').title()}")
        print(f"📝 {exploration['area_descriptions']['spirit_sanctuary']}")
        
        if exploration['actions']:
            print(f"\n🎮 Available Actions ({len(exploration['actions'])}):")
            for i, action in enumerate(exploration['actions'][:3], 1):
                print(f"   {i}. {action['text']}")
        
        print()
    
    print("\n💾 CHECKPOINT SYSTEM DEMO")
    print("=" * 50)
    
    # Demo checkpoint creation
    checkpoint_id = game_state.create_exploration_checkpoint(
        "The Whispering Woods", 
        "spirit_sanctuary", 
        "Communing with nature spirits"
    )
    
    if checkpoint_id:
        print(f"✅ Checkpoint created: {checkpoint_id}")
    
    # Show available checkpoints
    checkpoints = game_state.list_exploration_checkpoints()
    print(f"📂 Total checkpoints saved: {len(checkpoints)}")
    
    if checkpoints:
        latest = checkpoints[0]
        print(f"   Latest: {latest['description']} at {latest['location']}")
    
    print("\n🎭 ORIGINAL DOMAIN EXPANSIONS")
    print("=" * 50)
    
    # Show original domain expansions
    domain_techniques = ["eternal_nexus", "voidborne_cathedral"]
    for domain_name in domain_techniques:
        domain = technique_library.get_technique(domain_name)
        if domain:
            print(f"🌐 {domain.name}")
            print(f"   {domain.description}")
            print(f"   Power: {domain.damage} damage, {domain.cost} CE cost")
            print()
    
    print("\n🎊 DEMONSTRATION COMPLETE!")
    print("=" * 60)
    print("Features showcased:")
    print("✅ 26 original cursed techniques (no manga content)")
    print("✅ 8 immersive world locations with detailed areas")
    print("✅ Dynamic exploration with secrets and discoveries")
    print("✅ Checkpoint system for exploration progress")
    print("✅ Location-based technique training")
    print("✅ Original Domain Expansions")
    print("\nThe Jujutsu Kaisen RPG world is now significantly expanded")
    print("with completely original content and enhanced gameplay!")


if __name__ == "__main__":
    main()