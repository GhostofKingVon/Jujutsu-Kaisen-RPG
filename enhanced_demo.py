#!/usr/bin/env python3
"""
Enhanced Demo for Jujutsu Kaisen RPG

Demonstrates all the new features including enhanced character creation,
manga-accurate story progression, improved NPCs, and expanded cursed techniques.
"""

import sys
import os

def demonstrate_enhanced_features():
    """Demonstrate all enhanced features of the RPG."""
    
    print("🎮 ENHANCED JUJUTSU KAISEN RPG - FEATURE DEMONSTRATION")
    print("=" * 60)
    
    # Import enhanced modules
    from character_creation import CharacterCreator, MoralitySystem, Background
    from enhanced_npcs import EnhancedNPCManager
    from manga_story import MangaStoryManager, StoryArc
    from cursed_techniques import TechniqueLibrary
    from character import Player, Trait
    from game_state import GameState
    
    print("\n=== 1. ENHANCED CHARACTER CREATION ===")
    print("Character creation now includes:")
    print("- Detailed appearance customization")
    print("- Background selection affecting story")
    print("- Personality trait selection")
    print("- Starting cursed technique choice")
    print("- Morality system for decision consequences")
    
    # Create sample character
    player = Player("Akira Yamamoto")
    
    # Set up enhanced attributes
    from character_creation import Appearance, MoralitySystem, Background
    
    # Sample appearance
    appearance = Appearance()
    appearance.hair_color = "Black"
    appearance.eye_color = "Golden"
    appearance.height = "Tall (5'9\"-6'2\")"
    appearance.build = "Athletic"
    appearance.distinguishing_features = "Scar across left eyebrow"
    
    player.appearance = appearance
    player.background = Background.CURSE_VICTIM_SURVIVOR
    player.morality = MoralitySystem()
    
    # Set personality traits
    player.modify_trait(Trait.DETERMINED, 70)
    player.modify_trait(Trait.PROTECTIVE, 60)
    player.modify_trait(Trait.ANALYTICAL, 50)
    
    print(f"\nSample Character: {player.name}")
    print(f"Appearance: {appearance.hair_color} hair, {appearance.eye_color} eyes")
    print(f"Background: {player.background.value.replace('_', ' ').title()}")
    print(f"Moral Alignment: {player.morality.get_alignment()}")
    print(f"Dominant Traits: {[trait.value for trait in player.get_dominant_traits()]}")
    
    print("\n=== 2. ENHANCED CURSED TECHNIQUES ===")
    technique_lib = TechniqueLibrary()
    print(f"Total techniques available: {len(technique_lib.techniques)}")
    
    # Showcase different technique categories
    categories = {
        "Basic": ["cursed_energy_strike", "cursed_energy_guard"],
        "Canon - Yuji Line": ["divergent_fist", "black_flash"],
        "Canon - Megumi Line": ["divine_dogs", "nue", "max_elephant"],
        "Canon - Gojo Line": ["limitless_blue", "limitless_red", "hollow_purple"],
        "Domain Expansions": ["infinite_void", "chimera_shadow_garden"],
        "Original": ["wukong_technique", "ultra_instinct_monkey"]
    }
    
    for category, techniques in categories.items():
        print(f"\n{category} Techniques:")
        for tech_name in techniques:
            if tech_name in technique_lib.techniques:
                tech = technique_lib.techniques[tech_name]
                print(f"  • {tech.name} - {tech.description}")
    
    print("\n=== 3. MANGA-ACCURATE STORY ARCS ===")
    manga_story = MangaStoryManager()
    print("Story follows official Jujutsu Kaisen manga arcs:")
    
    arcs = [
        ("Introduction", "Meet classmates, encounter Gojo-sensei"),
        ("Fearsome Womb", "First major mission, Sukuna awakening"),
        ("Kyoto Goodwill Event", "School rivalry, Todo's questions"),
        ("Shibuya Incident", "Major battle, Gojo sealed"),
        ("Culling Game", "New regulations, survival game")
    ]
    
    for arc_name, description in arcs:
        print(f"  📖 {arc_name}: {description}")
    
    # Show sample scene
    print(f"\nSample Scene Count: {len(manga_story.manga_scenes)}")
    
    print("\n=== 4. ENHANCED NPC INTERACTIONS ===")
    npc_manager = EnhancedNPCManager()
    print("Canonical characters with personality-based interactions:")
    
    npcs_info = [
        ("Yuji Itadori", "Compassionate vessel of Sukuna"),
        ("Megumi Fushiguro", "Strategic Ten Shadows user"),
        ("Nobara Kugisaki", "Confident Straw Doll technique user"),
        ("Satoru Gojo", "The strongest sorcerer"),
        ("Ryomen Sukuna", "The King of Curses"),
        ("Aoi Todo", "Eccentric Boogie Woogie user")
    ]
    
    for npc_name, description in npcs_info:
        print(f"  🎭 {npc_name}: {description}")
    
    # Demonstrate relationship system
    print(f"\nRelationship System:")
    yuji_npc = npc_manager.get_npc("yuji")
    if yuji_npc:
        interaction = yuji_npc.get_dialogue(50, "casual", player.get_dominant_traits())
        print(f"  Yuji (Friend level): \"{interaction['dialogue']}\"")
    
    print("\n=== 5. MORALITY SYSTEM DEMONSTRATION ===")
    morality = player.morality
    print("Morality affects story choices and relationships:")
    print(f"  • Altruism: {morality.altruism}/100")
    print(f"  • Pragmatism: {morality.pragmatism}/100") 
    print(f"  • Justice: {morality.justice}/100")
    print(f"  • Mercy: {morality.mercy}/100")
    print(f"  • Current Alignment: {morality.get_alignment()}")
    
    # Demonstrate morality changes
    print("\nMorality change example:")
    print("Choice: 'Spare the weakened enemy'")
    morality.modify_morality("mercy", 15)
    morality.modify_morality("altruism", 10)
    print(f"  → Mercy +15, Altruism +10")
    print(f"  → New Alignment: {morality.get_alignment()}")
    
    print("\n=== 6. TECHNIQUE PROGRESSION PATHS ===")
    print("Starting techniques lead to advanced abilities:")
    
    progression_examples = [
        ("Divergent Fist Path", ["Divergent Fist", "Enhanced Strikes", "Black Flash", "Perfect Black Flash"]),
        ("Ten Shadows Path", ["Shadow Manifestation", "Divine Dogs", "Nue", "Great Serpent", "Max Elephant"]),
        ("Pure Energy Path", ["Energy Shaping", "Energy Blasts", "Energy Shields", "Energy Domain"])
    ]
    
    for path_name, techniques in progression_examples:
        print(f"\n{path_name}:")
        for i, tech in enumerate(techniques):
            print(f"  {i+1}. {tech}")
    
    print("\n=== 7. ENHANCED COMBAT FEATURES ===")
    print("Combat improvements include:")
    print("  • Dynamic taunts and dialogue during battle")
    print("  • Multi-phase boss battles with story significance")
    print("  • Emotional cutscenes during technique awakenings")
    print("  • Environmental interactions and team combinations")
    print("  • Reverse Cursed Technique healing mechanics")
    
    print("\n=== 8. CHOICE CONSEQUENCE SYSTEM ===")
    print("Decisions affect multiple aspects:")
    print("  • Character traits evolve based on choices")
    print("  • Relationships change with different NPCs")
    print("  • Morality shifts affect available options")
    print("  • Story branches based on player decisions")
    print("  • Technique unlocks through relationships")
    
    print("\n" + "=" * 60)
    print("🌟 ENHANCED FEATURES SUMMARY:")
    print("✅ Expanded character creation with appearance, background, traits")
    print("✅ Manga-accurate story arcs with player choice integration")
    print("✅ 42+ cursed techniques including canon and original abilities")
    print("✅ 6 detailed NPCs with personality-based interactions") 
    print("✅ Morality system affecting relationships and endings")
    print("✅ Technique progression paths with meaningful choices")
    print("✅ Enhanced combat with emotional story beats")
    print("✅ Deep narrative integration with Jujutsu Kaisen universe")
    
    print("\n🎮 Ready to experience the enhanced Jujutsu Kaisen RPG!")
    print("Run 'python3 main.py' to start your journey!")


if __name__ == "__main__":
    try:
        demonstrate_enhanced_features()
    except ImportError as e:
        print(f"Error importing modules: {e}")
        print("Make sure all enhanced modules are in the same directory.")
    except Exception as e:
        print(f"Error during demonstration: {e}")