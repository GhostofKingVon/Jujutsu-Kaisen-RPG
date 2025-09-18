"""
Audio-Visual Enhancement System

Provides dynamic soundtracks, visual effects, and immersive feedback
for the enhanced RPG experience.
"""

import os
import random
import time
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum


class SoundTrack(Enum):
    """Different music tracks for various situations."""
    MAIN_MENU = "main_menu"
    PEACEFUL = "peaceful"
    TENSE = "tense"
    COMBAT = "combat"
    BOSS_BATTLE = "boss_battle"
    VICTORY = "victory"
    DEFEAT = "defeat"
    EXPLORATION = "exploration"
    STEALTH = "stealth"
    INVESTIGATION = "investigation"
    EMOTIONAL = "emotional"
    TRANSFORMATION = "transformation"


class VisualEffect(Enum):
    """Visual effects for different actions."""
    CURSED_ENERGY = "cursed_energy"
    TECHNIQUE_CAST = "technique_cast"
    IMPACT = "impact"
    DODGE = "dodge"
    COUNTER = "counter"
    TRANSFORMATION = "transformation"
    LEVEL_UP = "level_up"
    DISCOVERY = "discovery"
    DAMAGE = "damage"
    HEALING = "healing"


class AudioVisualSystem:
    """Manages audio-visual feedback and immersion."""
    
    def __init__(self):
        self.current_track = SoundTrack.MAIN_MENU
        self.audio_enabled = True
        self.visual_effects_enabled = True
        self.dynamic_music = True
        self.effect_intensity = "normal"  # minimal, normal, intense
        
        # Track music for mood management
        self.mood_stack = []
        self.music_transition_time = 2
        
        # Visual effect library
        self.effect_library = self._initialize_effects()
        
        # Sound descriptions (since we can't play actual audio)
        self.sound_descriptions = self._initialize_sound_descriptions()
    
    def _initialize_effects(self) -> Dict[VisualEffect, Dict[str, List[str]]]:
        """Initialize visual effect library."""
        return {
            VisualEffect.CURSED_ENERGY: {
                "minimal": ["⚡", "✨", "💫"],
                "normal": ["⚡ ✨ ⚡", "✨ 💫 ✨", "💫 ⚡ 💫"],
                "intense": ["⚡✨💫⚡✨", "✨⚡💫✨⚡", "💫✨⚡💫✨"]
            },
            VisualEffect.TECHNIQUE_CAST: {
                "minimal": ["🌟", "💥", "🔥"],
                "normal": ["🌟 💥 🌟", "💥 🔥 💥", "🔥 🌟 🔥"],
                "intense": ["🌟💥🔥🌟💥", "💥🔥🌟💥🔥", "🔥🌟💥🔥🌟"]
            },
            VisualEffect.IMPACT: {
                "minimal": ["💥", "💢", "💨"],
                "normal": ["💥 💢 💥", "💢 💨 💢", "💨 💥 💨"],
                "intense": ["💥💢💨💥💢", "💢💨💥💢💨", "💨💥💢💨💥"]
            },
            VisualEffect.DODGE: {
                "minimal": ["💨", "🌪️", "💫"],
                "normal": ["💨 🌪️ 💨", "🌪️ 💫 🌪️", "💫 💨 💫"],
                "intense": ["💨🌪️💫💨🌪️", "🌪️💫💨🌪️💫", "💫💨🌪️💫💨"]
            },
            VisualEffect.TRANSFORMATION: {
                "minimal": ["✨", "🌟", "💫"],
                "normal": ["✨ 🌟 ✨", "🌟 💫 🌟", "💫 ✨ 💫"],
                "intense": ["✨🌟💫✨🌟", "🌟💫✨🌟💫", "💫✨🌟💫✨"]
            },
            VisualEffect.LEVEL_UP: {
                "minimal": ["🎉", "⭐", "🌟"],
                "normal": ["🎉 ⭐ 🎉", "⭐ 🌟 ⭐", "🌟 🎉 🌟"],
                "intense": ["🎉⭐🌟🎉⭐", "⭐🌟🎉⭐🌟", "🌟🎉⭐🌟🎉"]
            },
            VisualEffect.DISCOVERY: {
                "minimal": ["🔍", "💎", "📜"],
                "normal": ["🔍 💎 🔍", "💎 📜 💎", "📜 🔍 📜"],
                "intense": ["🔍💎📜🔍💎", "💎📜🔍💎📜", "📜🔍💎📜🔍"]
            }
        }
    
    def _initialize_sound_descriptions(self) -> Dict[SoundTrack, Dict[str, str]]:
        """Initialize sound track descriptions."""
        return {
            SoundTrack.MAIN_MENU: {
                "description": "Mystical orchestral theme with traditional Japanese instruments",
                "mood": "welcoming and mysterious"
            },
            SoundTrack.PEACEFUL: {
                "description": "Gentle piano with soft strings and nature sounds",
                "mood": "calm and serene"
            },
            SoundTrack.TENSE: {
                "description": "Low strings with gradually building percussion",
                "mood": "suspenseful and foreboding"
            },
            SoundTrack.COMBAT: {
                "description": "Fast-paced orchestral with intense percussion and electronic elements",
                "mood": "energetic and focused"
            },
            SoundTrack.BOSS_BATTLE: {
                "description": "Epic orchestral with choir, heavy drums, and dramatic brass",
                "mood": "epic and challenging"
            },
            SoundTrack.VICTORY: {
                "description": "Triumphant fanfare with soaring melodies",
                "mood": "celebratory and uplifting"
            },
            SoundTrack.STEALTH: {
                "description": "Minimal ambient sounds with subtle tension",
                "mood": "focused and cautious"
            },
            SoundTrack.INVESTIGATION: {
                "description": "Thoughtful piano with mysterious ambient layers",
                "mood": "contemplative and curious"
            },
            SoundTrack.TRANSFORMATION: {
                "description": "Powerful orchestral surge with ethereal choir",
                "mood": "transcendent and empowering"
            }
        }
    
    def play_sound_track(self, track: SoundTrack, force_change: bool = False):
        """Change background music track."""
        if not self.audio_enabled:
            return
        
        if self.current_track == track and not force_change:
            return
        
        old_track = self.current_track
        self.current_track = track
        
        if self.dynamic_music:
            self._display_music_transition(old_track, track)
    
    def _display_music_transition(self, old_track: SoundTrack, new_track: SoundTrack):
        """Display music transition notification."""
        if old_track == new_track:
            return
        
        old_desc = self.sound_descriptions.get(old_track, {}).get("description", "music")
        new_desc = self.sound_descriptions.get(new_track, {}).get("description", "music")
        
        print(f"\n🎵 Music transitions from {old_desc}")
        print(f"   to {new_desc}")
    
    def push_mood(self, track: SoundTrack):
        """Push current mood and switch to new track (for temporary changes)."""
        self.mood_stack.append(self.current_track)
        self.play_sound_track(track)
    
    def pop_mood(self):
        """Return to previous mood."""
        if self.mood_stack:
            previous_track = self.mood_stack.pop()
            self.play_sound_track(previous_track)
    
    def play_visual_effect(self, effect: VisualEffect, duration: float = 1.0, message: str = ""):
        """Display visual effect."""
        if not self.visual_effects_enabled:
            return
        
        if effect not in self.effect_library:
            return
        
        effects = self.effect_library[effect][self.effect_intensity]
        chosen_effect = random.choice(effects)
        
        # Display effect with optional message
        if message:
            print(f"\n{chosen_effect} {message} {chosen_effect}")
        else:
            print(f"\n{chosen_effect}")
        
        # Simulate duration for effect timing
        if duration > 0:
            time.sleep(min(duration, 0.5))  # Cap sleep time for responsiveness
    
    def combat_sequence_effects(self, action_type: str, character_name: str, 
                               target_name: str = "", damage: int = 0):
        """Play appropriate effects for combat actions."""
        effects_map = {
            "attack": (VisualEffect.IMPACT, f"{character_name} strikes!"),
            "technique": (VisualEffect.TECHNIQUE_CAST, f"{character_name} channels cursed energy!"),
            "dodge": (VisualEffect.DODGE, f"{character_name} evades gracefully!"),
            "counter": (VisualEffect.IMPACT, f"{character_name} counters!"),
            "transform": (VisualEffect.TRANSFORMATION, f"{character_name} transforms!"),
            "victory": (VisualEffect.LEVEL_UP, f"{character_name} emerges victorious!"),
            "defeat": (VisualEffect.DAMAGE, f"{character_name} falls...")
        }
        
        if action_type in effects_map:
            effect, message = effects_map[action_type]
            self.play_visual_effect(effect, 1.0, message)
        
        # Add damage-specific effects
        if damage > 0:
            if damage >= 50:
                self.play_visual_effect(VisualEffect.IMPACT, 0.5, "CRITICAL HIT!")
            elif damage >= 30:
                self.play_visual_effect(VisualEffect.IMPACT, 0.3, "Heavy damage!")
    
    def story_sequence_effects(self, scene_type: str, emotional_weight: str = "normal"):
        """Play effects for story sequences."""
        scene_effects = {
            "discovery": (VisualEffect.DISCOVERY, SoundTrack.EXPLORATION),
            "revelation": (VisualEffect.CURSED_ENERGY, SoundTrack.EMOTIONAL),
            "tension": (None, SoundTrack.TENSE),
            "peaceful": (None, SoundTrack.PEACEFUL),
            "dramatic": (VisualEffect.TECHNIQUE_CAST, SoundTrack.EMOTIONAL)
        }
        
        if scene_type in scene_effects:
            effect, track = scene_effects[scene_type]
            
            # Set mood music
            self.push_mood(track)
            
            # Play visual effect if specified
            if effect:
                self.play_visual_effect(effect, 1.5)
    
    def create_ascii_art_frame(self, content: str, width: int = 60, 
                              style: str = "normal") -> str:
        """Create framed ASCII art for important moments."""
        styles = {
            "normal": {"top": "=", "side": "|"},
            "fancy": {"top": "★", "side": "║"},
            "combat": {"top": "⚔", "side": "│"},
            "magic": {"top": "✦", "side": "┃"}
        }
        
        frame_chars = styles.get(style, styles["normal"])
        top_char = frame_chars["top"]
        side_char = frame_chars["side"]
        
        # Create frame
        top_line = top_char * width
        bottom_line = top_char * width
        
        # Split content into lines and center
        lines = content.split('\n')
        framed_lines = [top_line]
        
        for line in lines:
            padding = (width - len(line) - 4) // 2
            framed_line = f"{side_char} {' ' * padding}{line}{' ' * (width - len(line) - padding - 4)} {side_char}"
            framed_lines.append(framed_line)
        
        framed_lines.append(bottom_line)
        
        return '\n'.join(framed_lines)
    
    def display_chapter_transition(self, chapter_number: int, chapter_title: str):
        """Display chapter transition with effects."""
        self.push_mood(SoundTrack.EMOTIONAL)
        
        content = f"CHAPTER {chapter_number}\n{chapter_title}"
        framed_content = self.create_ascii_art_frame(content, 50, "fancy")
        
        print("\n" + framed_content)
        self.play_visual_effect(VisualEffect.DISCOVERY, 2.0)
        
        time.sleep(1)
        self.pop_mood()
    
    def display_character_introduction(self, character_name: str, title: str = ""):
        """Display character introduction with effects."""
        content = f"{character_name}"
        if title:
            content += f"\n{title}"
        
        framed_content = self.create_ascii_art_frame(content, 40, "normal")
        
        print(f"\n{framed_content}")
        self.play_visual_effect(VisualEffect.CURSED_ENERGY, 1.0)
    
    def display_technique_showcase(self, technique_name: str, description: str):
        """Display technique with dramatic effects."""
        content = f"✦ {technique_name} ✦\n{description}"
        framed_content = self.create_ascii_art_frame(content, 60, "magic")
        
        print(f"\n{framed_content}")
        self.play_visual_effect(VisualEffect.TECHNIQUE_CAST, 2.0)
    
    def create_progress_bar(self, current: int, maximum: int, width: int = 20, 
                           filled_char: str = "█", empty_char: str = "░") -> str:
        """Create visual progress bar."""
        percentage = current / maximum if maximum > 0 else 0
        filled_length = int(width * percentage)
        
        bar = filled_char * filled_length + empty_char * (width - filled_length)
        return f"[{bar}] {current}/{maximum} ({percentage:.1%})"
    
    def display_status_with_bars(self, character_name: str, hp: Tuple[int, int], 
                                ce: Tuple[int, int], stamina: Tuple[int, int] = None):
        """Display character status with visual bars."""
        print(f"\n👤 {character_name}")
        print(f"❤️  HP: {self.create_progress_bar(hp[0], hp[1])}")
        print(f"⚡ CE: {self.create_progress_bar(ce[0], ce[1])}")
        
        if stamina:
            print(f"💪 Stamina: {self.create_progress_bar(stamina[0], stamina[1])}")
    
    def celebration_sequence(self, event_type: str, details: str = ""):
        """Play celebration sequence for achievements."""
        self.push_mood(SoundTrack.VICTORY)
        
        celebrations = {
            "level_up": "🎉 LEVEL UP! 🎉",
            "quest_complete": "✅ QUEST COMPLETE! ✅",
            "achievement": "🏆 ACHIEVEMENT UNLOCKED! 🏆",
            "discovery": "🔍 NEW DISCOVERY! 🔍",
            "relationship": "🤝 RELATIONSHIP MILESTONE! 🤝"
        }
        
        celebration_text = celebrations.get(event_type, "🌟 SUCCESS! 🌟")
        
        if details:
            content = f"{celebration_text}\n{details}"
        else:
            content = celebration_text
        
        framed_content = self.create_ascii_art_frame(content, 50, "fancy")
        
        print(f"\n{framed_content}")
        self.play_visual_effect(VisualEffect.LEVEL_UP, 2.0)
        
        time.sleep(1)
        self.pop_mood()
    
    def set_effect_intensity(self, intensity: str):
        """Set visual effect intensity."""
        if intensity in ["minimal", "normal", "intense"]:
            self.effect_intensity = intensity
    
    def toggle_audio(self):
        """Toggle audio on/off."""
        self.audio_enabled = not self.audio_enabled
        status = "enabled" if self.audio_enabled else "disabled"
        print(f"🔊 Audio {status}")
    
    def toggle_visual_effects(self):
        """Toggle visual effects on/off."""
        self.visual_effects_enabled = not self.visual_effects_enabled
        status = "enabled" if self.visual_effects_enabled else "disabled"
        print(f"✨ Visual effects {status}")
    
    def get_current_mood_description(self) -> str:
        """Get description of current audio mood."""
        track_info = self.sound_descriptions.get(self.current_track, {})
        return track_info.get("mood", "neutral")


# Global audio-visual system instance
audio_visual = AudioVisualSystem()


def play_effect(effect: VisualEffect, message: str = "", duration: float = 1.0):
    """Convenience function to play visual effect."""
    audio_visual.play_visual_effect(effect, duration, message)


def set_mood(track: SoundTrack):
    """Convenience function to set mood."""
    audio_visual.play_sound_track(track)


def combat_effect(action: str, character: str, target: str = "", damage: int = 0):
    """Convenience function for combat effects."""
    audio_visual.combat_sequence_effects(action, character, target, damage)


def celebrate(event_type: str, details: str = ""):
    """Convenience function for celebrations."""
    audio_visual.celebration_sequence(event_type, details)