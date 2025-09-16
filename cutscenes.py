"""
Cutscene and Dramatic Moment System

Manages cutscenes, dramatic transitions, and cinematic storytelling moments
to enhance the narrative experience of the Jujutsu Kaisen RPG.
"""

from typing import Dict, List, Any, Optional
import random
import time


class CutsceneFrame:
    """Represents a single frame/moment in a cutscene."""
    
    def __init__(self, text: str, duration: float = 2.0, effects: List[str] = None):
        self.text = text
        self.duration = duration  # Seconds to display
        self.effects = effects or []  # Visual effects like "fade", "flash", etc.


class Cutscene:
    """Represents a complete cutscene with multiple frames."""
    
    def __init__(self, name: str, frames: List[CutsceneFrame], 
                 music_cue: str = None, skippable: bool = True):
        self.name = name
        self.frames = frames
        self.music_cue = music_cue
        self.skippable = skippable


class CutsceneManager:
    """Manages cutscenes and dramatic storytelling moments."""
    
    def __init__(self):
        self.cutscenes = {}
        self.dramatic_transitions = {}
        self._initialize_cutscenes()
        self._initialize_dramatic_transitions()
    
    def _initialize_cutscenes(self):
        """Initialize all cutscenes in the game."""
        
        # Opening cutscene
        opening_frames = [
            CutsceneFrame(
                "🌸 Tokyo, Japan - Autumn 2018",
                3.0, ["fade_in"]
            ),
            CutsceneFrame(
                "The world of Jujutsu Sorcery exists hidden from ordinary people...",
                4.0
            ),
            CutsceneFrame(
                "Where curses born from human emotions threaten innocent lives...",
                4.0
            ),
            CutsceneFrame(
                "And brave sorcerers stand as humanity's secret guardians.",
                4.0
            ),
            CutsceneFrame(
                "⛩️ Tokyo Jujutsu High School",
                3.0, ["location_reveal"]
            ),
            CutsceneFrame(
                "Your journey begins here...",
                2.0, ["fade_out"]
            )
        ]
        
        self.cutscenes["opening"] = Cutscene(
            "Opening", opening_frames, "epic_orchestral", False
        )
        
        # First technique awakening
        technique_awakening_frames = [
            CutsceneFrame(
                "💫 Something stirs deep within your soul...",
                3.0, ["mystical_glow"]
            ),
            CutsceneFrame(
                "Memories of ancient power flow through your consciousness...",
                4.0
            ),
            CutsceneFrame(
                "⚡ Your cursed energy resonates with a frequency you've never felt before!",
                3.0, ["energy_surge"]
            ),
            CutsceneFrame(
                "🌟 A new technique awakens within you!",
                2.0, ["bright_flash"]
            )
        ]
        
        self.cutscenes["first_technique_awakening"] = Cutscene(
            "First Technique Awakening", technique_awakening_frames, "mystical_ambient"
        )
        
        # Domain expansion first use
        domain_expansion_frames = [
            CutsceneFrame(
                "🌌 The very fabric of reality bends to your will...",
                4.0, ["reality_distortion"]
            ),
            CutsceneFrame(
                "Space itself becomes your canvas...",
                3.0
            ),
            CutsceneFrame(
                "Time slows as your inner world manifests...",
                4.0, ["time_slow"]
            ),
            CutsceneFrame(
                "🌐 'Domain Expansion...'",
                2.0, ["dramatic_pause"]
            ),
            CutsceneFrame(
                "🌟 The ultimate expression of your cursed technique erupts forth!",
                3.0, ["domain_burst"]
            )
        ]
        
        self.cutscenes["domain_expansion_first"] = Cutscene(
            "First Domain Expansion", domain_expansion_frames, "epic_crescendo", False
        )
        
        # Shibuya incident introduction
        shibuya_intro_frames = [
            CutsceneFrame(
                "🌃 Shibuya District - Halloween Night",
                3.0, ["night_atmosphere"]
            ),
            CutsceneFrame(
                "The busiest intersection in the world falls silent...",
                4.0
            ),
            CutsceneFrame(
                "Cursed energy thick enough to taste fills the air...",
                4.0, ["ominous_energy"]
            ),
            CutsceneFrame(
                "👹 Something ancient and malevolent stirs in the shadows...",
                4.0
            ),
            CutsceneFrame(
                "⚠️ This night will change everything.",
                3.0, ["warning_flash"]
            )
        ]
        
        self.cutscenes["shibuya_incident_intro"] = Cutscene(
            "Shibuya Incident Introduction", shibuya_intro_frames, "dark_tension"
        )
        
        # Final boss preparation
        final_boss_prep_frames = [
            CutsceneFrame(
                "💀 The final confrontation approaches...",
                3.0, ["dark_energy"]
            ),
            CutsceneFrame(
                "Everything you've learned, everyone you've grown close to...",
                4.0
            ),
            CutsceneFrame(
                "All of it has led to this moment.",
                3.0
            ),
            CutsceneFrame(
                "🔥 Your friends stand beside you, ready to face the ultimate evil.",
                4.0, ["ally_gathering"]
            ),
            CutsceneFrame(
                "⚔️ 'Let's finish this... together!'",
                2.0, ["battle_cry"]
            )
        ]
        
        self.cutscenes["final_boss_preparation"] = Cutscene(
            "Final Boss Preparation", final_boss_prep_frames, "heroic_resolve"
        )
    
    def _initialize_dramatic_transitions(self):
        """Initialize dramatic scene transitions."""
        
        self.dramatic_transitions = {
            "technique_success": [
                "⚡ Power courses through your being!",
                "🌟 Your technique flows with perfect precision!",
                "💫 Cursed energy resonates in perfect harmony!",
                "✨ Your will manifests as raw power!"
            ],
            
            "technique_failure": [
                "💥 Your cursed energy falters at the crucial moment!",
                "😤 The technique slips through your grasp!",
                "⚠️ Something went wrong with the energy flow!",
                "💔 Your concentration breaks under pressure!"
            ],
            
            "boss_phase_transition": [
                "🔥 The enemy's aura suddenly intensifies!",
                "⚡ 'You think this is my full power?! You're mistaken!'",
                "💀 'Time to get serious... prepare yourself!'",
                "🌪️ The very air around them begins to distort!"
            ],
            
            "ally_support": [
                "💪 'We're with you! Don't give up!'",
                "🤝 'Our bonds make us stronger!'",
                "⭐ 'Together, we can overcome anything!'",
                "🔥 'This is what friendship means!'"
            ],
            
            "emotional_breakthrough": [
                "💭 A flood of memories washes over you...",
                "💝 You remember why you fight...",
                "🌈 Your resolve crystallizes into pure determination!",
                "⚡ Emotional energy transforms into cursed power!"
            ],
            
            "victory_moment": [
                "🎉 'We did it! We actually did it!'",
                "🌟 Victory tastes sweeter when shared with friends!",
                "💪 'That's the power of working together!'",
                "😊 'I'm proud to fight alongside you all!'"
            ],
            
            "sacrifice_moment": [
                "💔 'I won't let you hurt my friends!'",
                "🛡️ 'This is what it means to protect others!'",
                "💪 'Some things are worth any price!'",
                "⭐ 'If my sacrifice saves everyone else...'"
            ]
        }
    
    def play_cutscene(self, cutscene_name: str, fast_mode: bool = False) -> bool:
        """Play a cutscene. Returns True if completed, False if skipped."""
        if cutscene_name not in self.cutscenes:
            print(f"Cutscene '{cutscene_name}' not found.")
            return False
        
        cutscene = self.cutscenes[cutscene_name]
        
        print(f"\n🎬 {cutscene.name}")
        print("=" * 60)
        
        if cutscene.music_cue:
            print(f"♪ Now playing: {cutscene.music_cue.replace('_', ' ').title()}")
        
        if cutscene.skippable and not fast_mode:
            print("(Press Enter to continue, 's' to skip)")
        
        for i, frame in enumerate(cutscene.frames):
            if not fast_mode:
                # Check for skip input (simplified for demo)
                user_input = input(f"\n{frame.text}\n> ").strip().lower()
                if user_input == 's' and cutscene.skippable:
                    print("Cutscene skipped.")
                    return False
            else:
                print(f"\n{frame.text}")
                time.sleep(0.5)  # Brief pause in fast mode
        
        print("\n" + "=" * 60)
        return True
    
    def show_dramatic_transition(self, transition_type: str, custom_message: str = None) -> str:
        """Show a dramatic transition message."""
        if custom_message:
            message = custom_message
        elif transition_type in self.dramatic_transitions:
            message = random.choice(self.dramatic_transitions[transition_type])
        else:
            message = "⚡ Something dramatic happens!"
        
        print(f"\n{'='*20} DRAMATIC MOMENT {'='*20}")
        print(f"{message}")
        print("=" * 60)
        
        return message
    
    def create_technique_animation(self, technique_name: str, user_name: str, 
                                 target_name: str = None, success: bool = True) -> str:
        """Create an animated description of technique usage."""
        animations = {
            "black_flash": [
                f"⚡ {user_name} focuses their cursed energy to a single point...",
                f"💫 Time seems to slow as they prepare the perfect strike...",
                f"🌟 Their fist glows with concentrated power...",
                f"💥 BLACK FLASH! The impact resonates through reality itself!"
            ],
            
            "domain_expansion": [
                f"🌌 {user_name} raises their hands to the sky...",
                f"🌀 Reality begins to bend and warp around them...",
                f"⚡ 'Domain Expansion...'",
                f"🌐 Their inner world manifests, overwhelming everything!"
            ],
            
            "shadow_clone": [
                f"👤 {user_name} weaves cursed energy through the shadows...",
                f"🌑 Darkness responds to their call...",
                f"👥 From the shadows, a perfect duplicate emerges!"
            ],
            
            "wukong_technique": [
                f"🐒 {user_name} channels the wisdom of the Monkey King...",
                f"⚡ Ancient power flows through their movements...",
                f"🌟 They move with impossible agility and grace!",
                f"💫 The legendary technique manifests in perfect form!"
            ]
        }
        
        # Get animation for specific technique or use generic
        technique_key = technique_name.lower().replace(" ", "_")
        if technique_key in animations:
            frames = animations[technique_key]
        else:
            frames = [
                f"⚡ {user_name} channels their cursed energy...",
                f"🌟 Power builds as they prepare their technique...",
                f"💫 {technique_name} activates with incredible force!"
            ]
        
        # Play animation
        print(f"\n🎭 TECHNIQUE ANIMATION: {technique_name}")
        print("-" * 50)
        
        for frame in frames:
            print(frame)
            time.sleep(1.5)  # Dramatic pause between frames
        
        if target_name:
            if success:
                impact_message = f"💥 The technique strikes {target_name} with devastating effect!"
            else:
                impact_message = f"💨 {target_name} manages to avoid the technique!"
            print(impact_message)
            time.sleep(1.0)
        
        print("-" * 50)
        return technique_name
    
    def create_boss_phase_transition(self, boss_name: str, phase: int, 
                                   transition_message: str = None) -> str:
        """Create a dramatic boss phase transition."""
        if not transition_message:
            transition_message = random.choice(self.dramatic_transitions["boss_phase_transition"])
        
        print(f"\n🔥 BOSS PHASE TRANSITION 🔥")
        print("=" * 60)
        print(f"💀 {boss_name} - Phase {phase}")
        print("-" * 60)
        print(transition_message)
        print("=" * 60)
        
        # Phase-specific effects
        if phase == 2:
            print("⚡ Their cursed energy doubles in intensity!")
            print("🌪️ The very air begins to distort from their power!")
        elif phase == 3:
            print("💀 This is their true form!")
            print("🌋 Reality itself seems to bend to their will!")
        elif phase >= 4:
            print("⚠️ WARNING: MAXIMUM POWER DETECTED!")
            print("🚨 All previous limits have been shattered!")
        
        print("=" * 60)
        input("Press Enter to continue...")
        
        return transition_message
    
    def create_emotional_cutscene(self, emotion_type: str, character_name: str, 
                                context: str = "") -> str:
        """Create a dynamic emotional cutscene based on the situation."""
        emotional_frames = {
            "determination": [
                f"💪 {character_name} clenches their fists with resolve...",
                f"🔥 'I won't give up! Not now, not ever!'",
                f"⚡ Their cursed energy flares with renewed purpose!",
                f"🌟 Determination burns brighter than any flame!"
            ],
            
            "friendship": [
                f"🤝 {character_name} looks at their companions...",
                f"💫 'We've come so far together...'",
                f"❤️ 'I'm grateful to have friends like you!'",
                f"🌈 The bonds between them glow with warm energy!"
            ],
            
            "sacrifice": [
                f"💔 {character_name} steps forward, knowing the cost...",
                f"🛡️ 'Someone has to protect what matters most...'",
                f"⭐ 'If this is what it takes, then I'll gladly pay the price!'",
                f"🌟 Their noble spirit shines brighter than any star!"
            ],
            
            "awakening": [
                f"💫 Something deep within {character_name} stirs...",
                f"⚡ Power beyond imagination courses through them!",
                f"🌟 'I finally understand... this is who I'm meant to be!'",
                f"✨ They have awakened to their true potential!"
            ]
        }
        
        frames = emotional_frames.get(emotion_type, [
            f"💭 {character_name} experiences a powerful emotion...",
            f"🌟 This moment will define their future...",
            f"⚡ Something important has changed within them..."
        ])
        
        print(f"\n💝 EMOTIONAL MOMENT: {emotion_type.title()}")
        print("=" * 60)
        
        if context:
            print(f"📖 Context: {context}")
            print("-" * 60)
        
        for frame in frames:
            print(frame)
            time.sleep(2.0)
        
        print("=" * 60)
        input("Press Enter to continue...")
        
        return emotion_type
    
    def get_combat_taunts(self, character_name: str, situation: str) -> List[str]:
        """Get appropriate combat taunts for different situations."""
        taunts = {
            "opening": [
                f"Come on! Show me what you've got!",
                f"I won't hold back - and neither should you!",
                f"Let's see if you can keep up with me!",
                f"This is going to be fun!"
            ],
            
            "winning": [
                f"Is that really your best effort?",
                f"I'm just getting warmed up!",
                f"You'll have to do better than that!",
                f"Come on, show me your real power!"
            ],
            
            "losing": [
                f"I'm not done yet!",
                f"This isn't over!",
                f"I won't give up that easily!",
                f"Time to get serious!"
            ],
            
            "final_attack": [
                f"This ends now!",
                f"Here's everything I've got!",
                f"For everyone I care about!",
                f"This is my final technique!"
            ]
        }
        
        return taunts.get(situation, ["Let's finish this!"])
    
    def create_team_combo_cutscene(self, participants: List[str], combo_name: str) -> str:
        """Create a cutscene for team combination attacks."""
        print(f"\n🌟 TEAM COMBINATION TECHNIQUE 🌟")
        print("=" * 70)
        print(f"✨ {combo_name}")
        print("=" * 70)
        
        # Opening frame
        print(f"🤝 {participants[0]} and {participants[1]} exchange a knowing look...")
        time.sleep(2.0)
        
        print(f"💫 'Our hearts beat as one!'")
        time.sleep(2.0)
        
        print(f"⚡ Their cursed energy synchronizes perfectly!")
        time.sleep(2.0)
        
        print(f"🌟 '{combo_name}!'")
        time.sleep(2.0)
        
        print(f"💥 The combined technique erupts with incredible power!")
        time.sleep(2.0)
        
        print("=" * 70)
        input("Press Enter to continue...")
        
        return combo_name


def get_cutscene_manager() -> CutsceneManager:
    """Get the global cutscene manager instance."""
    return CutsceneManager()