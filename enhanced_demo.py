#!/usr/bin/env python3
"""
Enhanced demo script showcasing the new emotional moments and cutscene systems.
"""

from character import Player, Enemy, Trait, CursedTechnique
from combat import CombatSystem
from game_state import GameState
from story import StoryManager
from npcs import NPCManager
from cursed_techniques import TechniqueLibrary
from emotional_moments import get_emotional_moment_manager
from cutscenes import get_cutscene_manager


def demo_emotional_moments():
    """Demonstrate the emotional moments system."""
    print("=== EMOTIONAL MOMENTS SYSTEM DEMO ===")
    
    emotion_manager = get_emotional_moment_manager()
    game_state = GameState()
    player = Player("Demo Hero")
    player.modify_trait(Trait.COMPASSIONATE, 70)
    player.modify_trait(Trait.DETERMINED, 65)
    game_state.set_player(player)
    
    # Simulate high relationship with Yuji
    game_state.update_relationship("yuji", 75)
    
    # Check for emotional moment trigger
    recent_events = ["high_relationship"]
    emotional_moment = emotion_manager.check_emotional_triggers(game_state, recent_events)
    
    if emotional_moment:
        print(f"🌟 Triggered emotional moment: {emotional_moment.name}")
        print("(In actual gameplay, this would show the full cutscene)")
    else:
        print("No emotional moments triggered (this is normal for demo)")
    
    print()


def demo_cutscenes():
    """Demonstrate the cutscene system."""
    print("=== CUTSCENE SYSTEM DEMO ===")
    
    cutscene_manager = get_cutscene_manager()
    
    # Play a short cutscene
    print("Playing opening cutscene (fast mode)...")
    cutscene_manager.play_cutscene("opening", fast_mode=True)
    
    # Show dramatic transitions
    print("\nDemonstrating dramatic transitions:")
    cutscene_manager.show_dramatic_transition("technique_success")
    cutscene_manager.show_dramatic_transition("emotional_breakthrough")
    
    # Show technique animation
    print("\nDemonstrating technique animation:")
    cutscene_manager.create_technique_animation("Black Flash", "Demo Hero", "Test Enemy")
    
    print()


def demo_enhanced_combat():
    """Demonstrate enhanced combat with dramatic elements."""
    print("=== ENHANCED COMBAT DEMO ===")
    
    player = Player("Enhanced Demo")
    player.level = 10
    player.gain_experience(0)  # Trigger technique learning
    
    # Add a special technique
    from cursed_techniques import TechniqueLibrary
    tech_lib = TechniqueLibrary()
    black_flash = tech_lib.get_technique("black_flash")
    if black_flash:
        player.add_technique(black_flash)
    
    enemy = Enemy("Demo Boss", 100, 50)
    enemy.max_phases = 2
    enemy.phase_transition_messages = ["The boss gets serious!"]
    
    combat = CombatSystem()
    
    print(f"Combat setup: {player.name} vs {enemy.name}")
    print(f"Player has enhanced techniques: {[t.name for t in player.techniques]}")
    print("(Enhanced combat includes dramatic moments, technique animations, and emotional beats)")
    
    print()


def demo_enhanced_story():
    """Demonstrate enhanced story system."""
    print("=== ENHANCED STORY SYSTEM DEMO ===")
    
    game_state = GameState()
    player = Player("Story Hero")
    player.modify_trait(Trait.FOCUSED, 70)
    game_state.set_player(player)
    
    story_manager = StoryManager()
    story_manager.start_story(game_state)
    
    print(f"Current story scene: {story_manager.current_scene}")
    print("Enhanced story includes:")
    print("- Emotional moment triggers")
    print("- CT awakening sequences")
    print("- Dynamic cutscenes")
    print("- Dramatic story beats")
    
    # Add some recent events
    story_manager.add_recent_event("combat_victory")
    story_manager.add_recent_event("protected_ally")
    
    print(f"Recent events tracked: {story_manager.recent_events}")
    
    print()


def demo_ct_awakenings():
    """Demonstrate CT awakening system."""
    print("=== CT AWAKENING SYSTEM DEMO ===")
    
    emotion_manager = get_emotional_moment_manager()
    game_state = GameState()
    player = Player("Awakening Demo")
    player.level = 15
    player.modify_trait(Trait.FOCUSED, 80)
    player.modify_trait(Trait.DETERMINED, 75)
    
    # Add some emotional flags that might trigger awakenings
    game_state.add_story_flag("experienced_first_loss", True)
    game_state.add_story_flag("made_great_sacrifice", True)
    
    game_state.set_player(player)
    
    # Check for CT awakening
    emotional_state = emotion_manager.get_emotional_state(player, ["combat_victory"])
    ct_awakening = emotion_manager.check_ct_awakening_triggers(player, game_state, emotional_state)
    
    if ct_awakening:
        print(f"🌟 CT Awakening ready: {ct_awakening.technique_name}")
        print("(In actual gameplay, this would show the full awakening sequence)")
    else:
        print("No CT awakenings ready (this is normal - awakenings have strict requirements)")
    
    print(f"Player emotional state: {emotional_state}")
    print(f"Player dominant traits: {[t.value for t in player.get_dominant_traits()]}")
    
    print()


def main():
    """Run all enhanced system demonstrations."""
    print("🌟 JUJUTSU KAISEN RPG - ENHANCED SYSTEM DEMONSTRATIONS")
    print("=" * 80)
    
    demo_emotional_moments()
    demo_cutscenes()
    demo_enhanced_combat()
    demo_enhanced_story()
    demo_ct_awakenings()
    
    print("=" * 80)
    print("🎉 All enhanced systems demonstrated successfully!")
    print("✨ New features include:")
    print("  • Emotional moments with character development")
    print("  • CT awakenings with backstories")
    print("  • Cinematic cutscenes and dramatic transitions")
    print("  • Enhanced combat with mid-battle drama")
    print("  • Deeper story progression with emotional beats")
    print("\nRun 'python3 main.py' to experience the enhanced game!")


if __name__ == "__main__":
    main()