#!/usr/bin/env python3
"""
Enhanced Jujutsu Kaisen RPG Demo

Demonstrates all the new features including enhanced character creation,
Sukuna storylines, side quests, and improved progression systems.
"""

from character_creation import CharacterCreationManager, Background
from character import Player, Trait
from game_state import GameState
from story import StoryManager
from side_quests import SideQuestManager
from npcs import NPCManager
import time


def demo_enhanced_character_creation():
    """Demo the enhanced character creation system."""
    print("=" * 60)
    print("           ENHANCED CHARACTER CREATION DEMO")
    print("=" * 60)
    
    # Simulate character creation choices
    creator = CharacterCreationManager()
    
    print("🎭 Creating a character with Sorcerer Family background...")
    player = Player("Akira Zenin")
    
    # Apply background bonuses manually for demo
    bg_bonuses = creator.background_bonuses[Background.SORCERER_FAMILY]
    for trait, value in bg_bonuses["traits"].items():
        player.modify_trait(trait, value)
    
    for npc, value in bg_bonuses["relationships"].items():
        player.relationships[npc] = value
    
    # Simulate appearance choices
    player.appearance = {
        "hair_color": "Black",
        "eye_color": "Blue", 
        "height": "Tall",
        "build": "Athletic"
    }
    player.background = Background.SORCERER_FAMILY
    
    print(f"✅ Character Created: {player.name}")
    print(f"Background: {player.background.value}")
    print(f"Appearance: {player.appearance['height']}, {player.appearance['build']} build")
    print(f"           {player.appearance['hair_color']} hair, {player.appearance['eye_color']} eyes")
    print(f"Dominant Traits: {[trait.value for trait in player.get_dominant_traits()]}")
    print(f"Starting Relationships: {player.relationships}")
    print()
    
    return player


def demo_sukuna_storyline():
    """Demo the Sukuna storyline integration."""
    print("=" * 60)
    print("           SUKUNA STORYLINE DEMO")
    print("=" * 60)
    
    story_manager = StoryManager()
    game_state = GameState()
    player = Player("Demo Player")
    game_state.set_player(player)
    
    print("👹 Sukuna (in Megumi's body) has been added to the story!")
    print("Available Sukuna scenes:")
    
    sukuna_scenes = [
        "sukuna_first_encounter",
        "sukuna_dialogue", 
        "sukuna_teaching_moment",
        "sukuna_reveals_plans"
    ]
    
    for scene_id in sukuna_scenes:
        if scene_id in story_manager.story_scenes:
            scene = story_manager.story_scenes[scene_id]
            print(f"  📖 {scene.title}")
            print(f"     Location: {scene.location}")
            print(f"     Choices: {len(scene.choices)}")
    
    print("\n💫 Sukuna relationship system:")
    npc_manager = NPCManager()
    sukuna_npc = npc_manager.get_npc("sukuna")
    
    print(f"  Name: {sukuna_npc.name}")
    print(f"  Personality: {sukuna_npc.personality_traits}")
    print(f"  Special Abilities: {len(sukuna_npc.special_abilities)} unlockable")
    
    # Demo dialogue at different relationship levels
    print(f"\n  Sample Dialogue (Neutral): \"{sukuna_npc.get_dialogue(0)}\"")
    print(f"  Sample Dialogue (Friend): \"{sukuna_npc.get_dialogue(60)}\"")
    print()


def demo_side_quests():
    """Demo the side quest system."""
    print("=" * 60)
    print("           SIDE QUEST SYSTEM DEMO")
    print("=" * 60)
    
    quest_manager = SideQuestManager()
    game_state = GameState()
    player = Player("Quest Demo")
    
    # Set up player to meet quest requirements
    player.level = 5
    player.modify_trait(Trait.FOCUSED, 70)
    game_state.set_player(player)
    game_state.update_relationship("megumi", 50)
    game_state.update_relationship("yuji", 35)
    game_state.add_story_flag("met_sukuna", True)
    
    print("🎯 Available Side Quests:")
    available_quests = quest_manager.get_available_quests(game_state)
    
    for quest in available_quests:
        print(f"  📋 {quest.title}")
        print(f"     Given by: {quest.npc_giver.title()}")
        print(f"     Objectives: {len(quest.objectives)}")
        print(f"     Requirements: Min relationship {quest.requirements.get('min_relationship', 0)}")
        print()
    
    # Demo starting a quest
    if available_quests:
        demo_quest = available_quests[0]
        print(f"🎬 Starting quest: {demo_quest.title}")
        success = quest_manager.start_quest(demo_quest.quest_id, game_state)
        print(f"   Status: {'Started!' if success else 'Failed to start'}")
        
        if success:
            print(f"   Objectives:")
            for i, obj in enumerate(demo_quest.objectives, 1):
                print(f"     {i}. {obj}")
    print()


def demo_story_driven_progression():
    """Demo the story-driven progression system."""
    print("=" * 60)
    print("           STORY-DRIVEN PROGRESSION DEMO")
    print("=" * 60)
    
    player = Player("Progression Demo")
    print(f"🧙 Starting Character: {player.name}")
    print(f"   Level: {player.level}")
    print(f"   Techniques: {[t.name for t in player.techniques]}")
    print(f"   Max Cursed Energy: {player.max_cursed_energy}")
    print()
    
    print("📚 Learning techniques through story events...")
    
    # Demo story-based technique learning
    story_techniques = [
        ("Sukuna's Insight", "Learned from the King of Curses"),
        ("Shadow Mastery", "Mastered through training with Megumi"),
        ("Bond of Friendship", "Unlocked through deep relationships")
    ]
    
    for technique_name, context in story_techniques:
        success = player.learn_story_technique(technique_name, context)
        if success:
            print(f"   ✨ Learned: {technique_name}")
            print(f"      Context: {context}")
    
    print(f"\n🎯 Updated Character:")
    print(f"   Techniques: {[t.name for t in player.techniques]}")
    print()


def demo_enhanced_npc_interactions():
    """Demo enhanced NPC interactions."""
    print("=" * 60)
    print("           ENHANCED NPC INTERACTIONS DEMO")
    print("=" * 60)
    
    npc_manager = NPCManager()
    game_state = GameState()
    player = Player("Social Demo")
    game_state.set_player(player)
    
    npcs_to_demo = ["yuji", "megumi", "sukuna"]
    
    for npc_name in npcs_to_demo:
        npc = npc_manager.get_npc(npc_name)
        if npc:
            print(f"💬 {npc.name}")
            print(f"   Personality: {', '.join(npc.personality_traits)}")
            
            # Demo dialogue at different relationship levels
            relationship_levels = [0, 30, 60, 90]
            level_names = ["Neutral", "Acquaintance", "Good Friend", "Close Friend"]
            
            for level, name in zip(relationship_levels, level_names):
                dialogue = npc.get_dialogue(level)
                print(f"   {name}: \"{dialogue}\"")
            
            print(f"   Unlockable Abilities: {len(npc.special_abilities)}")
            print()


def main():
    """Run all enhancement demos."""
    print("🎮 JUJUTSU KAISEN RPG - ENHANCEMENT DEMONSTRATIONS")
    print("=" * 80)
    print("Showcasing all new features and improvements...")
    print()
    
    time.sleep(1)
    
    # Demo each enhancement
    demo_enhanced_character_creation()
    time.sleep(1)
    
    demo_sukuna_storyline()
    time.sleep(1)
    
    demo_side_quests()
    time.sleep(1)
    
    demo_story_driven_progression()
    time.sleep(1)
    
    demo_enhanced_npc_interactions()
    
    print("=" * 80)
    print("🎉 ALL ENHANCEMENTS DEMONSTRATED SUCCESSFULLY!")
    print()
    print("Key Improvements Implemented:")
    print("✅ Enhanced Character Creation (backgrounds, personality, appearance)")
    print("✅ Sukuna (Megumi's Body) Storyline Integration")
    print("✅ Comprehensive Side Quest System")
    print("✅ Story-Driven Technique Progression")
    print("✅ Enhanced NPC Interactions & Dialogue")
    print("✅ Dynamic Relationship-Based Content")
    print()
    print("🎯 Ready to play! Run 'python3 main.py' to start your adventure!")
    print("=" * 80)


if __name__ == "__main__":
    main()