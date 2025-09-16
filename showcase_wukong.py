#!/usr/bin/env python3
"""
Showcase script for the enhanced Wukong Clan Cursed Technique system.
Demonstrates all 20 streamlined techniques and transformation system.
"""

from character import Player, Enemy, WukongTransformation
from combat import CombatSystem
from cursed_techniques import get_technique_library

def showcase_techniques():
    """Showcase all 20 streamlined cursed techniques."""
    print("🔥 ENHANCED CURSED TECHNIQUES SHOWCASE 🔥")
    print("=" * 60)
    
    library = get_technique_library()
    
    # Display manga-inspired techniques
    print("\n📚 MANGA-INSPIRED TECHNIQUES (10):")
    manga_techniques = [
        "cursed_energy_strike", "black_flash", "limitless_blue", "divine_dogs", 
        "straw_doll", "cursed_speech", "boogie_woogie", "simple_domain", 
        "infinite_void", "reverse_cursed_technique"
    ]
    
    for tech_name in manga_techniques:
        technique = library.get_technique(tech_name)
        if technique:
            print(f"  ⚡ {technique.name}")
            print(f"     {technique.description}")
            print(f"     Damage: {technique.damage}, Cost: {technique.cost} CE")

    # Display Wukong Clan techniques
    print("\n🐒 WUKONG CLAN TECHNIQUES (10):")
    wukong_techniques = [
        "monkey_king_combo", "power_pole_extend", "ki_blast", "cloud_dash",
        "kame_wave", "monkey_king_domain", "golden_combo", "instinct_strike",
        "ego_smash", "scarlet_barrage"
    ]
    
    for tech_name in wukong_techniques:
        technique = library.get_technique(tech_name)
        if technique:
            print(f"  🥇 {technique.name}")
            print(f"     {technique.description}")
            print(f"     Damage: {technique.damage}, Cost: {technique.cost} CE")
    
    print(f"\n📊 Total Techniques: {len(library.techniques)} (Perfectly streamlined!)")

def showcase_transformations():
    """Showcase the Wukong transformation system."""
    print("\n\n🔄 WUKONG TRANSFORMATION SHOWCASE 🔄")
    print("=" * 60)
    
    player = Player("Monkey King Showcase")
    player.level = 25  # High level for all transformations
    
    transformations = [
        (WukongTransformation.SUPER_MONKEY, "Golden power transformation"),
        (WukongTransformation.SCARLET_SAGE_MONKEY, "Crimson energy mastery"),
        (WukongTransformation.ULTRA_INSTINCT_MONKEY, "Perfect evasion form"),
        (WukongTransformation.ULTRA_EGO_MONKEY, "Damage-scaling berserker")
    ]
    
    for transformation, description in transformations:
        print(f"\n--- {transformation.value.upper()} ---")
        print(f"Description: {description}")
        
        player.activate_wukong_transformation(transformation, 5)
        
        print(f"Damage Multiplier: {player.get_technique_damage_multiplier():.1f}x")
        print(f"Critical Chance: {player.get_critical_chance()*100:.1f}%")
        print(f"Dodge Chance: {player.get_dodge_chance()*100:.1f}%")
        print(f"CE Efficiency: {player.get_cursed_energy_efficiency():.1f}x")
        
        if transformation == WukongTransformation.ULTRA_EGO_MONKEY:
            # Simulate taking damage for Ultra Ego
            player.take_damage(30)
            print(f"After taking damage - Ego Stacks: {player.ego_stacks}")
            print(f"Enhanced Damage Multiplier: {player.get_technique_damage_multiplier():.1f}x")
        
        player.deactivate_transformation()

def showcase_combat_integration():
    """Showcase how the system integrates with combat."""
    print("\n\n⚔️ COMBAT INTEGRATION SHOWCASE ⚔️")
    print("=" * 60)
    
    player = Player("Wukong Warrior")
    player.level = 20
    enemy = Enemy("Training Dummy", 200, 60)
    
    combat = CombatSystem()
    
    print(f"Player: {player.name} (Level {player.level})")
    print(f"Enemy: {enemy.name} (HP: {enemy.hp})")
    
    # Show available actions
    actions = combat.get_player_actions(player)
    print(f"\nAvailable Combat Actions: {len(actions)}")
    
    transformation_actions = [a for a in actions if a.action_type == "transform"]
    technique_actions = [a for a in actions if a.action_type == "technique"]
    
    print(f"  Transformations: {len(transformation_actions)}")
    for action in transformation_actions:
        print(f"    🔄 {action.name}")
    
    print(f"  Techniques: {len(technique_actions)}")
    for action in technique_actions[:5]:  # Show first 5
        print(f"    ⚡ {action.name}")
    if len(technique_actions) > 5:
        print(f"    ... and {len(technique_actions) - 5} more!")
    
    # Demonstrate transformation in combat
    print(f"\n--- Demonstrating Ultra Instinct Transformation ---")
    player.activate_wukong_transformation(WukongTransformation.ULTRA_INSTINCT_MONKEY, 4)
    
    # Show how actions change after transformation
    actions_after = combat.get_player_actions(player)
    detransform_actions = [a for a in actions_after if a.action_type == "detransform"]
    
    if detransform_actions:
        print(f"New action available: {detransform_actions[0].name}")
    
    print(f"Enhanced dodge chance: {player.get_dodge_chance()*100:.1f}%")
    print(f"Auto-counter available: {player.can_auto_counter()}")

def main():
    """Main showcase function."""
    print("🎮 JUJUTSU KAISEN RPG - WUKONG ENHANCEMENT SHOWCASE")
    print("🐒 Featuring 20 Streamlined Techniques + Full Transformation System")
    print("=" * 80)
    
    try:
        showcase_techniques()
        showcase_transformations()
        showcase_combat_integration()
        
        print("\n\n" + "=" * 80)
        print("🎉 SHOWCASE COMPLETE! 🎉")
        print("The enhanced Wukong Clan system is fully operational!")
        print("- 20 perfectly balanced techniques (10 manga + 10 original)")
        print("- 4 immersive transformation states with unique abilities")
        print("- Seamless combat integration with dramatic effects")
        print("- Enhanced player experience with visual storytelling")
        print("\nRun 'python3 main.py' to start the full RPG experience!")
        print("=" * 80)
        
    except Exception as e:
        print(f"Error during showcase: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()