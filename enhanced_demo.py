#!/usr/bin/env python3
"""
Enhanced Jujutsu Kaisen RPG Demo

Demonstrates all the new enhanced features including stamina system,
gameplay modes, world-building, customization, and audio-visual effects.
"""

import random
import time
from character import Player, Enemy, Trait, MoralAlignment
from stamina_system import StaminaSystem, EnvironmentalAdvantages
from gameplay_modes import StealthSystem, InvestigationSystem, TeamBattleSystem, MissionType
from world_building import WorldManager, Location, LocationType
from journal_system import GameJournal, Quest, CharacterEntry
from customization_system import CharacterCustomization, ItemType, ItemRarity
from audio_visual_system import audio_visual, VisualEffect, SoundTrack, celebrate, combat_effect


def demo_title():
    """Display demo title."""
    print("=" * 80)
    print("🏯 JUJUTSU KAISEN RPG - ENHANCED EDITION DEMO 🏯")
    print("=" * 80)
    print("This demo showcases all the new enhanced features:")
    print("• Advanced Combat with Stamina & Environmental Effects")
    print("• Stealth, Investigation & Team Battle Systems")
    print("• Deep Character Customization & Morality")
    print("• Dynamic World & Comprehensive Lore")
    print("• Audio-Visual Effects & Enhanced UI")
    print("=" * 80)
    input("\nPress Enter to begin the demo...")


def demo_character_creation():
    """Demonstrate enhanced character creation."""
    print("\n" + "🌟 ENHANCED CHARACTER CREATION DEMO" + "🌟".center(50))
    audio_visual.play_sound_track(SoundTrack.PEACEFUL)
    
    # Create player with enhanced features
    player = Player("Demo Sorcerer")
    
    print(f"\n✨ Created character: {player.name}")
    print(f"📊 Moral Alignment: {player.moral_alignment.value}")
    print(f"⚡ Starting Stamina: {player.stamina_system.current_stamina}/{player.stamina_system.max_stamina}")
    
    # Demonstrate character background
    player.character_background.add_backstory_element("goal", "Protect innocent people")
    player.character_background.add_backstory_element("motivation", "Honor family legacy")
    player.character_background.add_backstory_element("fear", "Losing control of power")
    
    print(f"📖 Background: {player.character_background.get_background_summary()}")
    
    # Demonstrate morality system
    print("\n🤝 Demonstrating Morality System:")
    player.update_morality("help_innocent", 2)
    print(f"   After helping civilians: {player.moral_alignment.value}")
    
    player.update_morality("follow_rules", 2)
    print(f"   After following proper protocols: {player.moral_alignment.value}")
    
    # Show unique abilities
    player.check_unique_ability_unlocks()
    
    celebrate("level_up", f"{player.name} ready for adventure!")
    return player


def demo_stamina_system(player):
    """Demonstrate stamina and fatigue mechanics."""
    print("\n💪 STAMINA SYSTEM DEMO".center(50))
    audio_visual.play_sound_track(SoundTrack.EXPLORATION)
    
    print(f"\n{player.stamina_system.get_status_display()}")
    
    # Demonstrate stamina usage
    print("\n🎯 Performing various actions:")
    
    actions_to_demo = [
        ("basic_attack", "Basic Attack"),
        ("technique", "Cursed Technique"),
        ("dodge", "Dodge"),
        ("transform", "Transformation")
    ]
    
    for action_type, action_name in actions_to_demo:
        if player.stamina_system.can_perform_action(action_type):
            cost = player.stamina_system.action_costs[action_type]
            player.stamina_system.use_stamina(action_type)
            print(f"   • {action_name}: -{cost} stamina")
            print(f"     {player.stamina_system.get_status_display()}")
        else:
            print(f"   • {action_name}: Insufficient stamina!")
    
    # Demonstrate rest and recovery
    print(f"\n😴 Resting to recover...")
    recovered = player.stamina_system.rest_turn()
    print(f"   Recovered {recovered} stamina")
    print(f"   {player.stamina_system.get_status_display()}")
    
    # Show performance modifiers
    modifier = player.stamina_system.get_performance_modifier()
    print(f"\n⚡ Current performance modifier: {modifier:.1%}")


def demo_enhanced_combat(player):
    """Demonstrate enhanced combat with new features."""
    print("\n⚔️ ENHANCED COMBAT DEMO".center(50))
    audio_visual.play_sound_track(SoundTrack.COMBAT)
    
    # Create enemy
    enemy = Enemy("Cursed Spirit", 100, 60)
    
    print(f"\n🎭 {player.name} vs {enemy.name}")
    
    # Demonstrate environmental combat
    environment = "high_ground"
    env_system = EnvironmentalAdvantages()
    env_data = env_system.get_advantage(environment)
    
    print(f"🌍 Environment: {env_data.get('description', 'High Ground')}")
    
    # Simulate a few combat rounds
    for round_num in range(1, 4):
        print(f"\n--- Round {round_num} ---")
        
        # Show status with visual bars
        audio_visual.display_status_with_bars(
            player.name,
            (player.hp, player.max_hp),
            (player.cursed_energy, player.max_cursed_energy),
            (player.stamina_system.current_stamina, player.stamina_system.max_stamina)
        )
        
        # Player action
        if round_num == 1:
            action = "attack"
            damage = 25
        elif round_num == 2:
            action = "technique"
            damage = 40
        else:
            action = "dodge"
            damage = 0
        
        combat_effect(action, player.name, enemy.name, damage)
        
        if damage > 0:
            enemy.hp -= damage
            print(f"   {enemy.name} takes {damage} damage! HP: {enemy.hp}/{enemy.max_hp}")
        
        # Use stamina
        player.stamina_system.use_stamina(action)
        
        # Enemy response (simplified)
        if enemy.hp > 0:
            enemy_damage = random.randint(15, 25)
            player.hp -= enemy_damage
            combat_effect("attack", enemy.name, player.name, enemy_damage)
            print(f"   {player.name} takes {enemy_damage} damage! HP: {player.hp}/{player.max_hp}")
        
        time.sleep(1)
    
    # Victory
    celebrate("quest_complete", f"Defeated {enemy.name}!")


def demo_gameplay_modes():
    """Demonstrate different gameplay modes."""
    print("\n🎯 GAMEPLAY MODES DEMO".center(50))
    
    # Stealth Mission Demo
    print("\n🔍 STEALTH MISSION")
    audio_visual.play_sound_track(SoundTrack.STEALTH)
    
    stealth_system = StealthSystem()
    
    # Simulate stealth actions
    from character import Player, Trait
    demo_player = Player("Stealth Demo")
    demo_player.modify_trait(Trait.CAUTIOUS, 70)  # Good at stealth
    
    stealth_actions = ["hide", "sneak_past", "observe"]
    
    for action in stealth_actions:
        result = stealth_system.perform_stealth_action(demo_player, action)
        print(f"   • {action.replace('_', ' ').title()}: {'✅ Success' if result['success'] else '❌ Failed'}")
        print(f"     {result['message']}")
        if result.get('result'):
            reward = result['result']
            if 'experience' in reward:
                print(f"     Gained {reward['experience']} experience!")
    
    # Investigation Demo
    print(f"\n🔍 INVESTIGATION MISSION")
    audio_visual.play_sound_track(SoundTrack.INVESTIGATION)
    
    investigation = InvestigationSystem()
    
    # Search different areas
    areas = ["crime_scene", "witness_location", "suspect_hideout"]
    
    for area in areas:
        result = investigation.search_area(demo_player, area)
        if result['success']:
            clue = result['clue']
            print(f"   • Searched {area.replace('_', ' ').title()}: Found '{clue['name']}'")
            print(f"     Progress: {result['progress']}%")
        else:
            print(f"   • Searched {area.replace('_', ' ').title()}: Nothing found")
    
    # Analyze clues
    analysis = investigation.analyze_clues(demo_player)
    if analysis.get('case_solved'):
        celebrate("achievement", "Case solved!")
    elif analysis.get('breakthrough'):
        print("   🔍 Breakthrough! New leads discovered!")
    
    # Team Battle Demo
    print(f"\n🤝 TEAM BATTLE")
    audio_visual.play_sound_track(SoundTrack.COMBAT)
    
    team_battle = TeamBattleSystem()
    
    # Add team members
    teammates = [
        {"name": "Yuji", "level": 8, "traits": [Trait.DETERMINED, Trait.PROTECTIVE]},
        {"name": "Megumi", "level": 9, "traits": [Trait.ANALYTICAL, Trait.CAUTIOUS]}
    ]
    
    for teammate in teammates:
        team_battle.add_team_member(teammate)
        print(f"   • {teammate['name']} joined the team!")
    
    print(f"   Team Synergy: {team_battle.team_synergy}%")
    
    # Execute combo attack
    from character import Enemy
    boss = Enemy("Special Grade Curse", 200, 100)
    combo_result = team_battle.execute_combo_attack(demo_player, teammates, boss)
    
    if combo_result['success']:
        print(f"   🌟 {combo_result['combo_name']} deals {combo_result['damage']} damage!")
        combat_effect("technique", "Team", boss.name, combo_result['damage'])


def demo_world_building():
    """Demonstrate world-building and exploration."""
    print("\n🌍 WORLD BUILDING DEMO".center(50))
    audio_visual.play_sound_track(SoundTrack.EXPLORATION)
    
    world_manager = WorldManager()
    
    # Show available locations
    print("\n🏢 Available Locations:")
    for location_id, location in world_manager.locations.items():
        print(f"   • {location.name} ({location.location_type.value})")
        print(f"     {location.description}")
    
    # Explore a location
    tokyo_high = world_manager.locations["tokyo_jujutsu_high"]
    print(f"\n🔍 Exploring {tokyo_high.name}:")
    
    # Simulate exploration
    from character import Trait
    explorer = Player("Explorer")
    explorer.modify_trait(Trait.ANALYTICAL, 80)
    
    for area_name in ["hidden_library", "underground_training"]:
        if area_name in tokyo_high.areas:
            result = tokyo_high.explore_area(area_name, explorer.get_dominant_traits())
            if result['success']:
                print(f"   • {area_name.replace('_', ' ').title()}:")
                for discovery in result['discoveries']:
                    print(f"     🔍 Found: {discovery['type']} - {discovery['content']}")
            
            print(f"     Progress: {tokyo_high.exploration_progress}%")
    
    # Demonstrate world events
    print(f"\n🌟 World Events:")
    
    # Trigger a world event
    from world_building import WorldEventType
    event = world_manager.trigger_world_event(
        WorldEventType.CURSE_OUTBREAK, 
        explorer.level, 
        explorer.reputation
    )
    
    if event:
        print(f"   📰 {event.name}")
        print(f"   📝 {event.description}")
        
        # Player responds to event
        response = "investigate"
        result = event.process_player_response(response, explorer)
        print(f"   ✅ Response: {result['message']}")
        
        celebrate("achievement", "World event completed!")


def demo_journal_system():
    """Demonstrate comprehensive journal system."""
    print("\n📖 JOURNAL SYSTEM DEMO".center(50))
    audio_visual.play_sound_track(SoundTrack.PEACEFUL)
    
    journal = GameJournal()
    
    # Create and add a quest
    demo_quest = Quest(
        "demo_quest",
        "Master the Enhanced Features",
        "Learn about all the new systems in the enhanced RPG.",
        [
            "Try the stamina system",
            "Complete a stealth mission", 
            "Explore world locations",
            "Craft an item"
        ],
        {"experience": 200, "reputation": 30}
    )
    
    demo_quest.start_quest()
    journal.add_quest(demo_quest)
    
    print(f"\n📋 Active Quest: {demo_quest.get_status_summary()}")
    
    # Complete some objectives
    for i in range(2):
        journal.update_quest_progress("demo_quest", i)
        updated_quest = journal.get_quest("demo_quest")
        print(f"   ✅ Objective {i+1} completed!")
        print(f"   📊 Progress: {updated_quest.progress:.0f}%")
    
    # Add character relationships
    characters_to_add = [
        ("Gojo Satoru", "Your mysterious and powerful teacher"),
        ("Yuji Itadori", "Cheerful and determined classmate"),
        ("Megumi Fushiguro", "Serious and strategic ally")
    ]
    
    print(f"\n👥 Character Relationships:")
    for name, description in characters_to_add:
        character = journal.add_character(name, description)
        
        # Simulate relationship changes
        change = random.randint(10, 25)
        journal.update_character_relationship(name, change, "Worked well together in training")
        
        character = journal.get_character(name)
        print(f"   • {name}: {character.get_relationship_status()}")
    
    # Add lore entries
    lore_entries = [
        ("Cursed Energy Basics", "Negative emotions manifest as cursed energy", "fundamentals"),
        ("Tokyo Jujutsu High History", "Founded to train the next generation of sorcerers", "locations"),
        ("Special Grade Curses", "The most dangerous class of cursed spirits", "threats")
    ]
    
    print(f"\n📚 Lore Discovered:")
    for title, content, category in lore_entries:
        journal.add_lore_entry(title, content, category)
        print(f"   • {title} ({category})")
    
    # Show journal summary
    print(f"\n📊 Journal Summary:")
    print(journal.get_journal_summary())


def demo_customization_system():
    """Demonstrate character customization and crafting."""
    print("\n⚙️ CUSTOMIZATION SYSTEM DEMO".center(50))
    audio_visual.play_sound_track(SoundTrack.PEACEFUL)
    
    customization = CharacterCustomization()
    
    print(f"\n👕 Starting Equipment:")
    print(customization.equipment.get_equipment_summary())
    
    # Demonstrate crafting
    print(f"\n🔨 Crafting Demo:")
    
    # Add some materials to inventory
    materials = [
        ("wood", 5),
        ("metal_ore", 3), 
        ("cursed_crystal", 2),
        ("cloth", 4)
    ]
    
    print(f"   📦 Adding materials to inventory:")
    for material, quantity in materials:
        # Create dummy material items
        from customization_system import Item, ItemType, ItemRarity
        material_item = Item(material.title(), f"Crafting material: {material}", 
                           ItemType.MATERIAL, ItemRarity.COMMON)
        
        customization.inventory.add_item(material_item, quantity)
        print(f"     • {material.title()}: {quantity}")
    
    print(f"\n   {customization.inventory.get_capacity_info()}")
    
    # Add crafting tools
    customization.crafting.add_tool("crafting_bench")
    print(f"   🔧 Added crafting bench")
    
    # Show available recipes
    available_recipes = customization.crafting.get_available_recipes()
    print(f"\n   📋 Available Recipes:")
    for recipe_name in available_recipes[:3]:  # Show first 3
        recipe_info = customization.crafting.get_recipe_info(recipe_name)
        if recipe_info:
            print(f"     • {recipe_info['result']}")
            print(f"       Materials: {recipe_info['materials']}")
            print(f"       Success Rate: {recipe_info['success_rate']}%")
    
    # Craft an item
    if available_recipes:
        recipe_to_craft = available_recipes[0]
        print(f"\n   🔨 Crafting {recipe_to_craft}...")
        
        result = customization.crafting.craft_item(recipe_to_craft, customization.inventory)
        if result['success']:
            celebrate("achievement", f"Crafted {result['item'].name}!")
            print(f"       📊 Item Stats: {result['item'].stats}")
        else:
            print(f"       ❌ Crafting failed: {result['message']}")
    
    # Show character customization summary
    print(f"\n📊 Customization Summary:")
    print(customization.get_customization_summary())


def demo_audio_visual_system():
    """Demonstrate audio-visual enhancements."""
    print("\n🎭 AUDIO-VISUAL SYSTEM DEMO".center(50))
    
    # Demonstrate different moods
    print(f"\n🎵 Music System Demo:")
    
    moods = [
        (SoundTrack.PEACEFUL, "Peaceful exploration"),
        (SoundTrack.TENSE, "Building tension"),
        (SoundTrack.COMBAT, "Intense battle"),
        (SoundTrack.VICTORY, "Triumphant success")
    ]
    
    for track, description in moods:
        audio_visual.play_sound_track(track)
        print(f"   🎵 {description}: {audio_visual.get_current_mood_description()}")
        time.sleep(0.5)
    
    # Demonstrate visual effects
    print(f"\n✨ Visual Effects Demo:")
    
    effects = [
        (VisualEffect.CURSED_ENERGY, "Channeling cursed energy"),
        (VisualEffect.TECHNIQUE_CAST, "Casting powerful technique"),
        (VisualEffect.IMPACT, "Devastating impact"),
        (VisualEffect.TRANSFORMATION, "Character transformation")
    ]
    
    for effect, description in effects:
        print(f"   {description}:")
        audio_visual.play_visual_effect(effect, 0.5, "")
        time.sleep(0.5)
    
    # Demonstrate framed content
    print(f"\n🖼️ Enhanced UI Demo:")
    
    # Chapter transition
    audio_visual.display_chapter_transition(1, "The Journey Begins")
    
    # Character introduction
    audio_visual.display_character_introduction("Satoru Gojo", "The Strongest Sorcerer")
    
    # Technique showcase
    audio_visual.display_technique_showcase(
        "Domain Expansion: Infinite Void",
        "A domain that bombards the target with infinite information"
    )


def main():
    """Run the complete enhanced demo."""
    demo_title()
    
    # Run all demos in sequence
    print("\n🚀 Starting comprehensive demo...\n")
    
    # Character creation and systems
    player = demo_character_creation()
    time.sleep(1)
    
    demo_stamina_system(player)
    time.sleep(1)
    
    demo_enhanced_combat(player)
    time.sleep(1)
    
    demo_gameplay_modes()
    time.sleep(1)
    
    demo_world_building()
    time.sleep(1)
    
    demo_journal_system()
    time.sleep(1)
    
    demo_customization_system()
    time.sleep(1)
    
    demo_audio_visual_system()
    
    # Final celebration
    print("\n" + "=" * 80)
    celebrate("achievement", "Enhanced RPG Demo Complete!")
    print("=" * 80)
    print("🌟 All enhanced features demonstrated successfully!")
    print("🎮 The Jujutsu Kaisen RPG is now a truly immersive experience!")
    print("🏯 Ready for epic adventures in the world of Jujutsu Sorcery!")
    print("=" * 80)


if __name__ == "__main__":
    main()