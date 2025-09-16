"""
Emotional Moments and CT Awakening System

Manages pivotal emotional beats, CT awakenings, and character development moments
that create impactful narrative experiences.
"""

from typing import Dict, List, Any, Optional
from character import Player, Trait, CursedTechnique
import random


class EmotionalMoment:
    """Represents a pivotal emotional moment in the story."""
    
    def __init__(self, name: str, trigger_condition: Dict[str, Any], 
                 emotional_scene: str, consequences: Dict[str, Any]):
        self.name = name
        self.trigger_condition = trigger_condition
        self.emotional_scene = emotional_scene
        self.consequences = consequences
        self.has_occurred = False


class CTAwakening:
    """Represents a Cursed Technique awakening with emotional backstory."""
    
    def __init__(self, technique_name: str, awakening_trigger: Dict[str, Any],
                 backstory: str, awakening_scene: str, new_abilities: List[str]):
        self.technique_name = technique_name
        self.awakening_trigger = awakening_trigger
        self.backstory = backstory
        self.awakening_scene = awakening_scene
        self.new_abilities = new_abilities
        self.awakened = False


class EmotionalMomentManager:
    """Manages emotional moments, CT awakenings, and character development."""
    
    def __init__(self):
        self.emotional_moments = {}
        self.ct_awakenings = {}
        self.character_memories = []
        self._initialize_emotional_moments()
        self._initialize_ct_awakenings()
    
    def _initialize_emotional_moments(self):
        """Initialize pivotal emotional moments."""
        
        # First loss - emotional growth
        self.emotional_moments["first_loss"] = EmotionalMoment(
            "The Weight of Failure",
            {"trigger": "combat_defeat", "min_chapter": 3},
            """
🌧️ As you lie defeated, memories flood your mind. The faces of those you couldn't save, 
the weakness you felt when it mattered most. Your hands tremble not from injury, but from 
the crushing realization that strength alone isn't enough.

"Why... why wasn't I strong enough?" you whisper to yourself.

In this moment of despair, you remember why you became a sorcerer. Not for glory or power, 
but to protect those who cannot protect themselves. The pain in your heart burns brighter 
than any physical wound.

This failure... it will define you. But how?
            """,
            {
                "trait_changes": {Trait.DETERMINED: 15, Trait.COMPASSIONATE: 10},
                "unlocks": ["inner_resolve_technique"],
                "emotional_flag": "experienced_first_loss"
            }
        )
        
        # Friendship bond moment
        self.emotional_moments["true_friendship"] = EmotionalMoment(
            "Bonds Beyond Words",
            {"trigger": "high_relationship", "npc": "yuji", "threshold": 70},
            """
🌟 Under the moonlight after a difficult mission, you and Yuji sit in comfortable silence. 
The weight of what you've both seen and experienced hangs in the air, but so does something 
else - an unbreakable bond forged through shared trials.

"You know," Yuji says quietly, "when I thought I was going to lose you back there... 
I realized something. You're not just my teammate. You're my brother."

The words hit you harder than any cursed technique. In this world of curses and death, 
true friendship is the rarest treasure of all.

"Brother," you reply, and the word carries the weight of an unbreakable vow.
            """,
            {
                "trait_changes": {Trait.PROTECTIVE: 20, Trait.COMPASSIONATE: 10},
                "unlocks": ["brotherhood_technique", "shared_resolve"],
                "relationship_bonus": {"yuji": 20},
                "emotional_flag": "brotherhood_with_yuji"
            }
        )
        
        # Sacrifice moment
        self.emotional_moments["moment_of_sacrifice"] = EmotionalMoment(
            "The Price of Protection",
            {"trigger": "protect_ally", "damage_taken": 50},
            """
💔 Pain shoots through your body as you take the devastating blow meant for your friend. 
Blood runs down your face, your vision blurs, but your resolve only grows stronger.

"Why did you do that?!" they cry out, catching you as you stumble.

"Because..." you gasp, looking into their terrified eyes, "because you're worth protecting. 
Everyone is worth protecting. That's what it means to be a sorcerer."

In this moment of sacrifice, you understand the true meaning of strength. It's not about 
how much damage you can deal - it's about how much you're willing to endure for others.
            """,
            {
                "trait_changes": {Trait.PROTECTIVE: 25, Trait.COMPASSIONATE: 15},
                "unlocks": ["guardian_spirit_technique", "sacrificial_barrier"],
                "emotional_flag": "made_great_sacrifice"
            }
        )
        
        # Rage and loss moment
        self.emotional_moments["awakening_rage"] = EmotionalMoment(
            "The Fire of Vengeance",
            {"trigger": "npc_injured", "npc": "any", "severity": "critical"},
            """
🔥 Rage. Pure, unbridled rage courses through your veins as you see your friend lying 
motionless. The curse responsible stands over them, grinning with malevolent satisfaction.

"No... NO!" you scream, cursed energy erupting from your body like a volcano. The very 
air around you begins to distort from the intensity of your emotions.

"I'll make you pay for this. I'LL MAKE YOU ALL PAY!"

Your friends have never seen you like this. Raw power, driven by grief and fury, 
transforms you into something fearsome. In this moment, you touch a darkness within 
yourself that both terrifies and empowers you.
            """,
            {
                "trait_changes": {Trait.AGGRESSIVE: 30, Trait.RECKLESS: 15, Trait.PROTECTIVE: 10},
                "unlocks": ["berserker_mode", "vengeful_strike"],
                "emotional_flag": "experienced_awakening_rage"
            }
        )
    
    def _initialize_ct_awakenings(self):
        """Initialize Cursed Technique awakenings with emotional backstories."""
        
        # Black Flash awakening
        self.ct_awakenings["black_flash"] = CTAwakening(
            "Black Flash",
            {"min_level": 8, "required_traits": [Trait.FOCUSED], "emotional_state": "determined"},
            """
💫 BACKSTORY: The Memory of Helplessness

Years ago, before you became a sorcerer, you watched helplessly as a curse attacked 
your childhood friend. You were weak, untrained, powerless. That feeling of helplessness 
has haunted you ever since.

Now, in this critical moment, that same feeling threatens to overwhelm you. But this time 
is different. This time, you have the power to act. This time, you won't be helpless.

"I refuse to be weak again," you whisper, remembering your friend's face.
            """,
            """
⚡ AWAKENING: The Perfect Moment

Time seems to slow as you recall every moment of training, every drop of sweat, every 
ounce of determination that brought you to this point. Your cursed energy flows with 
perfect precision, synchronized with your very heartbeat.

The memory of your powerless past fuels your focused present. As your fist connects, 
cursed energy impacts within 0.000001 seconds - the perfect Black Flash.

🌟 "This is the difference between who I was... and who I've become!"

The technique isn't just about timing or power - it's about the perfect harmony between 
memory, emotion, and will. You have awakened the Black Flash!
            """,
            ["black_flash", "focused_strike", "memory_resonance"]
        )
        
        # Domain Expansion awakening
        self.ct_awakenings["domain_expansion"] = CTAwakening(
            "Domain Expansion: Memories of Resolve",
            {"min_level": 20, "emotional_flags": ["experienced_first_loss", "made_great_sacrifice"], 
             "required_traits": [Trait.DETERMINED, Trait.PROTECTIVE]},
            """
🌌 BACKSTORY: The Culmination of Growth

Every choice you've made, every sacrifice you've endured, every friend you've protected - 
all of it has led to this moment. The memories of your journey play before your eyes 
like fragments of a broken mirror, each reflecting a piece of who you've become.

Your first defeat taught you humility. Your sacrifices taught you the value of others. 
Your bonds taught you that strength comes from connection, not isolation.

"All of my experiences... all of my growth... everything I am..."
            """,
            """
🌐 AWAKENING: Domain Expansion - Memories of Resolve

"Domain Expansion: Memories of Resolve!"

The world transforms around you. This isn't just a manifestation of cursed energy - 
it's a manifestation of your very soul. Every important moment of your journey materializes 
in the domain: your first day at the school, your first victory, your first loss, the 
faces of everyone you've fought to protect.

Within this domain, you and your allies are strengthened by the weight of shared memories, 
while enemies are overwhelmed by the emotional intensity of your resolve.

🌟 "This domain isn't just my power - it's the power of everyone who believed in me!"

You have achieved the ultimate expression of your cursed technique!
            """,
            ["domain_expansion_memories", "memory_manipulation", "resolve_amplification", "emotional_resonance"]
        )
        
        # Wukong awakening (unique to the character's journey)
        self.ct_awakenings["wukong_mastery"] = CTAwakening(
            "Seventy-Two Transformations Mastery",
            {"min_level": 15, "technique_experience": "wukong_technique", "emotional_state": "balanced"},
            """
🐒 BACKSTORY: The Monkey King's Wisdom

In dreams, you've walked with the legendary Monkey King. He showed you that true strength 
isn't about overpowering your enemies - it's about adapting, growing, and finding creative 
solutions to impossible problems.

"Strength without wisdom is just destruction," the Monkey King told you. "But wisdom 
without strength is just philosophy. You must become both."

You remember his mischievous grin as he added, "And don't forget to have fun while doing it!"
            """,
            """
🌟 AWAKENING: The True Nature of Change

Suddenly, you understand. The Seventy-Two Transformations isn't about changing your body - 
it's about changing your perspective, your approach, your very essence to meet any challenge.

Your cursed energy flows like water, adapting to any container. Like the wind, you become 
everywhere and nowhere. Like fire, you burn away the impossible to reveal the possible.

🐒 "I am not bound by what I was, only by what I choose to become!"

The Monkey King's laughter echoes in your mind as you achieve true mastery. You can now 
transform not just your technique, but your entire approach to any situation!
            """,
            ["adaptive_transformation", "wisdom_of_change", "mischievous_flexibility", "infinite_possibility"]
        )
    
    def check_emotional_triggers(self, game_state, recent_events: List[str]) -> Optional[EmotionalMoment]:
        """Check if any emotional moments should be triggered."""
        for moment_name, moment in self.emotional_moments.items():
            if moment.has_occurred:
                continue
            
            if self._evaluate_trigger(moment.trigger_condition, game_state, recent_events):
                moment.has_occurred = True
                return moment
        
        return None
    
    def check_ct_awakening_triggers(self, player: Player, game_state, emotional_state: str) -> Optional[CTAwakening]:
        """Check if any CT awakenings should be triggered."""
        for awakening_name, awakening in self.ct_awakenings.items():
            if awakening.awakened:
                continue
            
            if self._evaluate_ct_trigger(awakening.awakening_trigger, player, game_state, emotional_state):
                awakening.awakened = True
                return awakening
        
        return None
    
    def _evaluate_trigger(self, condition: Dict[str, Any], game_state, recent_events: List[str]) -> bool:
        """Evaluate if an emotional moment trigger condition is met."""
        trigger = condition.get("trigger")
        
        if trigger == "combat_defeat" and "combat_defeat" in recent_events:
            return game_state.current_chapter >= condition.get("min_chapter", 1)
        
        elif trigger == "high_relationship":
            npc = condition.get("npc")
            threshold = condition.get("threshold", 70)
            return game_state.get_relationship(npc) >= threshold
        
        elif trigger == "protect_ally" and "protected_ally" in recent_events:
            return True  # Additional damage check would be done in combat system
        
        elif trigger == "npc_injured" and "npc_injured" in recent_events:
            return True
        
        return False
    
    def _evaluate_ct_trigger(self, condition: Dict[str, Any], player: Player, game_state, emotional_state: str) -> bool:
        """Evaluate if a CT awakening trigger condition is met."""
        # Level requirement
        if player.level < condition.get("min_level", 1):
            return False
        
        # Trait requirements
        required_traits = condition.get("required_traits", [])
        player_traits = player.get_dominant_traits()
        if not all(trait in player_traits for trait in required_traits):
            return False
        
        # Emotional state requirement
        required_state = condition.get("emotional_state")
        if required_state and emotional_state != required_state:
            return False
        
        # Emotional flags requirement
        required_flags = condition.get("emotional_flags", [])
        for flag in required_flags:
            if not game_state.get_story_flag(flag, False):
                return False
        
        # Technique experience requirement
        required_technique = condition.get("technique_experience")
        if required_technique:
            has_technique = any(t.name.lower().replace(" ", "_") == required_technique 
                              for t in player.techniques)
            if not has_technique:
                return False
        
        return True
    
    def apply_emotional_moment(self, moment: EmotionalMoment, player: Player, game_state) -> Dict[str, Any]:
        """Apply the effects of an emotional moment."""
        print(f"\n🌟 EMOTIONAL MOMENT: {moment.name}")
        print("=" * 60)
        print(moment.emotional_scene)
        print("=" * 60)
        
        consequences = moment.consequences
        result = {"moment_name": moment.name, "effects": []}
        
        # Apply trait changes
        if "trait_changes" in consequences:
            for trait, change in consequences["trait_changes"].items():
                old_value = player.traits[trait]
                player.modify_trait(trait, change)
                new_value = player.traits[trait]
                print(f"\n💫 {trait.value}: {old_value} → {new_value} (+{change})")
                result["effects"].append(f"{trait.value} increased by {change}")
        
        # Apply relationship bonuses
        if "relationship_bonus" in consequences:
            for npc, bonus in consequences["relationship_bonus"].items():
                game_state.update_relationship(npc, bonus)
                print(f"\n💕 Relationship with {npc.title()}: +{bonus}")
                result["effects"].append(f"Relationship with {npc} increased by {bonus}")
        
        # Set emotional flags
        if "emotional_flag" in consequences:
            flag = consequences["emotional_flag"]
            game_state.add_story_flag(flag, True)
            print(f"\n🏁 Emotional milestone achieved: {flag}")
            result["effects"].append(f"Emotional milestone: {flag}")
        
        # Unlock new abilities/techniques
        if "unlocks" in consequences:
            for unlock in consequences["unlocks"]:
                game_state.add_story_flag(f"unlocked_{unlock}", True)
                print(f"\n🔓 New ability unlocked: {unlock.replace('_', ' ').title()}")
                result["effects"].append(f"Unlocked: {unlock}")
        
        input("\nPress Enter to continue...")
        return result
    
    def apply_ct_awakening(self, awakening: CTAwakening, player: Player, game_state) -> Dict[str, Any]:
        """Apply the effects of a CT awakening."""
        print(f"\n🌟 CURSED TECHNIQUE AWAKENING")
        print("=" * 70)
        print(awakening.backstory)
        print("\n" + "=" * 70)
        input("Press Enter to continue to the awakening...")
        print("\n" + "=" * 70)
        print(awakening.awakening_scene)
        print("=" * 70)
        
        result = {"technique_name": awakening.technique_name, "new_abilities": []}
        
        # Unlock new abilities
        for ability in awakening.new_abilities:
            game_state.add_story_flag(f"awakened_{ability}", True)
            game_state.unlock_technique(ability)
            print(f"\n✨ New ability awakened: {ability.replace('_', ' ').title()}")
            result["new_abilities"].append(ability)
        
        # Grant significant experience for the awakening
        experience_gain = 100 + (player.level * 10)
        player.gain_experience(experience_gain)
        print(f"\n⭐ Gained {experience_gain} experience from awakening!")
        
        # Set awakening flag
        game_state.add_story_flag(f"ct_awakened_{awakening.technique_name.lower().replace(' ', '_')}", True)
        
        input("\nPress Enter to continue...")
        return result
    
    def get_emotional_state(self, player: Player, recent_events: List[str]) -> str:
        """Determine the player's current emotional state based on traits and recent events."""
        dominant_traits = player.get_dominant_traits()
        
        if "combat_victory" in recent_events and Trait.DETERMINED in dominant_traits:
            return "determined"
        elif "protected_ally" in recent_events and Trait.PROTECTIVE in dominant_traits:
            return "protective"
        elif "made_sacrifice" in recent_events:
            return "noble"
        elif "combat_defeat" in recent_events:
            return "desperate"
        elif len([t for t in dominant_traits if t in [Trait.COMPASSIONATE, Trait.PROTECTIVE, Trait.FOCUSED]]) >= 2:
            return "balanced"
        elif Trait.AGGRESSIVE in dominant_traits and Trait.RECKLESS in dominant_traits:
            return "fierce"
        else:
            return "neutral"


def get_emotional_moment_manager() -> EmotionalMomentManager:
    """Get the global emotional moment manager instance."""
    return EmotionalMomentManager()