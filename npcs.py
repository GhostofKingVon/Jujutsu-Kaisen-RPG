"""
NPC Interaction and Relationship System

Manages NPCs, relationship dynamics, dialogue, and special abilities unlocked
through character bonds.
"""

from typing import Dict, List, Any, Optional
from character import Trait
import random


class NPC:
    """Represents an NPC with personality, relationships, and dialogue."""
    
    def __init__(self, name: str, personality_traits: List[str], 
                 dialogue_options: Dict[str, List[str]], 
                 special_abilities: Dict[int, str]):
        self.name = name
        self.personality_traits = personality_traits
        self.dialogue_options = dialogue_options  # Different dialogue based on relationship
        self.special_abilities = special_abilities  # Unlocked at relationship thresholds
        self.current_relationship = 0
        self.unlocked_abilities = []
        self.interaction_count = 0
        self.last_interaction_chapter = 0
    
    def get_dialogue(self, relationship_level: int, context: str = "casual") -> str:
        """Get appropriate dialogue based on relationship level."""
        if relationship_level >= 80:
            level = "close_friend"
        elif relationship_level >= 60:
            level = "good_friend"
        elif relationship_level >= 40:
            level = "friend"
        elif relationship_level >= 20:
            level = "acquaintance"
        elif relationship_level >= 0:
            level = "neutral"
        else:
            level = "dislike"
        
        dialogue_list = self.dialogue_options.get(f"{level}_{context}", 
                                                 self.dialogue_options.get(level, 
                                                 ["..."]))
        return random.choice(dialogue_list)
    
    def check_ability_unlock(self, relationship_level: int) -> List[str]:
        """Check if any new abilities are unlocked at current relationship level."""
        new_abilities = []
        
        for threshold, ability in self.special_abilities.items():
            if relationship_level >= threshold and ability not in self.unlocked_abilities:
                self.unlocked_abilities.append(ability)
                new_abilities.append(ability)
        
        return new_abilities


class NPCManager:
    """Manages all NPCs and their interactions."""
    
    def __init__(self):
        self.npcs = {}
        self._initialize_npcs()
    
    def _initialize_npcs(self):
        """Initialize all NPCs with their characteristics."""
        
        # Yuji Itadori
        self.npcs["yuji"] = NPC(
            "Yuji Itadori",
            ["compassionate", "determined", "friendly", "protective"],
            {
                "neutral": [
                    "Hey there! I'm Yuji. Nice to meet you!",
                    "Are you a new student? Welcome to the school!",
                    "This place can be pretty intense, but you'll get used to it.",
                    "Want to hear about the time I fought a special grade curse?",
                    "Gojo-sensei says I'm getting stronger every day!"
                ],
                "acquaintance": [
                    "Hey! How's your training going?",
                    "Want to grab some food later? I know a great place!",
                    "I've been working on my cursed energy control. It's tough!",
                    "Your technique is really cool! Can you teach me sometime?",
                    "Fushiguro's been helping me with strategy. You should join us!"
                ],
                "friend": [
                    "You're getting really strong! I'm impressed.",
                    "Thanks for always having my back in fights.",
                    "We make a pretty good team, don't we?",
                    "I love how passionate you are about protecting people.",
                    "Sometimes I think about what Sukuna would say... but with friends like you, I don't worry."
                ],
                "good_friend": [
                    "I'm really glad we became friends. You're someone I can count on.",
                    "Your determination reminds me why I became a sorcerer.",
                    "Let's protect people together!",
                    "You understand what it's like to carry something heavy, don't you?",
                    "When I'm around you, I remember what it feels like to just be... normal."
                ],
                "close_friend": [
                    "You're like family to me. I'd do anything to protect you.",
                    "Together, we can face any curse that comes our way!",
                    "I believe in you completely. Let's save everyone we can!",
                    "Promise me something - if Sukuna ever takes over completely, you'll stop me.",
                    "You make me believe that even someone like me can make a difference."
                ],
                "neutral_training": [
                    "Physical training is my specialty! Want to spar?",
                    "I learned this move from watching movies. Surprisingly effective!",
                    "Let's focus on building your core strength first."
                ],
                "friend_training": [
                    "I'll share some techniques Todo taught me!",
                    "Your form is getting much better. Keep it up!",
                    "Training with friends makes everything more fun!"
                ],
                "neutral_mission": [
                    "Stay close and watch my back, okay?",
                    "Remember - saving people comes first, everything else second.",
                    "I've got a good feeling about this mission!"
                ],
                "friend_mission": [
                    "With you here, I know we can handle anything!",
                    "Let's show these curses what real teamwork looks like!",
                    "I trust you completely. Let's save everyone!"
                ],
                "neutral_combat": [
                    "Let's work together on this one!",
                    "I'll cover your back!"
                ],
                "friend_combat": [
                    "We've got this! Just like we practiced!",
                    "Trust me, I won't let anything happen to you!"
                ],
                "close_friend_combat": [
                    "Our bond makes us stronger! Let's show them our power!",
                    "We fight as one! Nothing can stop us!"
                ]
            },
            {
                20: "Teamwork Boost - Increased damage when fighting alongside Yuji",
                50: "Encouraging Presence - Yuji's presence restores cursed energy",
                80: "Unbreakable Bond - Can perform combination techniques with Yuji"
            }
        )
        
        # Megumi Fushiguro
        self.npcs["megumi"] = NPC(
            "Megumi Fushiguro",
            ["analytical", "reserved", "strategic", "loyal"],
            {
                "neutral": [
                    "I'm Megumi Fushiguro. Let's work well together.",
                    "Focus on your training. This isn't a game.",
                    "Understanding your cursed technique is crucial.",
                    "The Ten Shadows Technique requires constant vigilance.",
                    "Every mission is a life-or-death situation. Remember that."
                ],
                "acquaintance": [
                    "Your technique has potential. Keep refining it.",
                    "Strategy is just as important as power.",
                    "You're more capable than I initially thought.",
                    "I've noticed you adapt quickly to new situations.",
                    "Your cursed energy control is improving steadily."
                ],
                "friend": [
                    "I respect your dedication to improvement.",
                    "Your analytical approach is impressive.",
                    "I can rely on you in difficult situations.",
                    "You remind me why teamwork matters in this job.",
                    "I appreciate having someone who thinks before acting."
                ],
                "good_friend": [
                    "You understand the weight of our responsibilities.",
                    "Your growth has been remarkable to witness.",
                    "I'm glad to have someone like you as an ally.",
                    "Sometimes I wonder if my shadows would accept you...",
                    "You've become someone I genuinely care about."
                ],
                "close_friend": [
                    "You're one of the few people I trust completely.",
                    "Our strategies work because we understand each other.",
                    "I'll always have your back, no matter what.",
                    "My shadows respond to you almost as well as they do to me.",
                    "If something ever happens to me... protect the others."
                ],
                "neutral_training": [
                    "Shadow techniques require perfect emotional control.",
                    "Let me show you proper stance for summoning.",
                    "Your foundation needs work before advanced techniques."
                ],
                "friend_training": [
                    "I'll share some shadow manipulation secrets with you.",
                    "Watch carefully - this technique saved my life once.",
                    "Your progress makes teaching worthwhile."
                ],
                "neutral_mission": [
                    "Stick to the plan. Improvisation leads to casualties.",
                    "I'll handle reconnaissance. You focus on support.",
                    "Keep your cursed energy signature low."
                ],
                "friend_mission": [
                    "I trust your judgment on this one.",
                    "Let's coordinate our techniques for maximum impact.",
                    "With you here, I feel more confident about success."
                ],
                "friend_combat": [
                    "Let's use the strategy we discussed.",
                    "I'll create an opening for you."
                ],
                "close_friend_combat": [
                    "Execute plan Delta. You know what to do.",
                    "Our synchronized attacks are flawless."
                ]
            },
            {
                25: "Strategic Insight - Megumi shares enemy weaknesses",
                55: "Shadow Support - Megumi's shadows can assist in battle",
                85: "Perfect Synchronization - Unlock dual shadow techniques"
            }
        )
        
        # Nobara Kugisaki
        self.npcs["nobara"] = NPC(
            "Nobara Kugisaki",
            ["confident", "aggressive", "fashionable", "fierce"],
            {
                "neutral": [
                    "I'm Nobara Kugisaki. Don't get in my way.",
                    "You better be strong enough to keep up.",
                    "This isn't about making friends, it's about exorcising curses."
                ],
                "acquaintance": [
                    "You're not completely hopeless, I guess.",
                    "Your fighting style is... adequate.",
                    "Maybe you won't be dead weight after all."
                ],
                "friend": [
                    "You've got guts. I like that.",
                    "We should go shopping sometime. You need better clothes.",
                    "Your combat skills are actually pretty impressive."
                ],
                "good_friend": [
                    "You're one of the few people here I actually respect.",
                    "Thanks for always being honest with me.",
                    "Let's crush some curses together!"
                ],
                "close_friend": [
                    "You're my best friend, and that means everything to me.",
                    "I'd trust you with my life in any situation.",
                    "We're going to be the strongest duo ever!"
                ],
                "friend_combat": [
                    "Let's show them what we're made of!",
                    "I'll hit them high, you hit them low!"
                ],
                "close_friend_combat": [
                    "Time to unleash our signature combo!",
                    "They don't stand a chance against us!"
                ]
            },
            {
                30: "Fierce Determination - Nobara's presence increases critical hit chance",
                60: "Straw Doll Assistance - Nobara can mark enemies for extra damage",
                90: "Unbreakable Trust - Can perform devastating combination attacks"
            }
        )
        
        # Aoi Todo
        self.npcs["todo"] = NPC(
            "Aoi Todo",
            ["passionate", "strong", "eccentric", "mentor"],
            {
                "neutral": [
                    "What's your type of woman?",
                    "You look weak. Prove me wrong.",
                    "Strength isn't just about power."
                ],
                "acquaintance": [
                    "You have potential, but you need more passion!",
                    "Your cursed energy flow could be better.",
                    "Show me your fighting spirit!"
                ],
                "friend": [
                    "My brother! You understand what it means to fight!",
                    "Your passion burns bright! I respect that!",
                    "Let's train together and become stronger!"
                ],
                "good_friend": [
                    "You're a true warrior, my brother!",
                    "Your dedication to strength inspires me!",
                    "We share the same burning spirit!"
                ],
                "close_friend": [
                    "You are my brother in every sense! We fight as one!",
                    "Your spirit and mine are connected beyond words!",
                    "Together, we are unstoppable!"
                ],
                "friend_combat": [
                    "My brother! Let's show them real power!",
                    "Our fighting spirits will crush any opponent!"
                ],
                "close_friend_combat": [
                    "Brother! Time for our ultimate technique!",
                    "Our bond transcends ordinary teamwork!"
                ]
            },
            {
                35: "Brotherhood Boost - Todo's training increases physical power",
                65: "Boogie Woogie Support - Todo can switch enemy positions",
                95: "Soul Connection - Unlock the ultimate brotherhood technique"
            }
        )
        
        # Satoru Gojo
        self.npcs["gojo"] = NPC(
            "Satoru Gojo",
            ["charismatic", "powerful", "carefree", "protective"],
            {
                "neutral": [
                    "Oh, a new student! Welcome to the school!",
                    "Don't worry, you're in good hands with me as your teacher.",
                    "Cursed spirits don't stand a chance against my students."
                ],
                "acquaintance": [
                    "You're showing good progress in your training.",
                    "Remember, technique is everything in jujutsu.",
                    "Your potential is quite interesting."
                ],
                "friend": [
                    "You're becoming quite the impressive sorcerer!",
                    "I'm proud of how far you've come.",
                    "You have the makings of someone truly special."
                ],
                "good_friend": [
                    "You remind me of myself when I was younger.",
                    "Your growth has exceeded my expectations.",
                    "I believe you could become one of the strongest."
                ],
                "close_friend": [
                    "You're like the student I always hoped to teach.",
                    "Your potential rivals even the most gifted sorcerers.",
                    "I'll always be here to guide you, no matter what."
                ]
            },
            {
                40: "Master's Guidance - Gojo provides advanced training tips",
                70: "Limitless Insights - Learn advanced cursed energy manipulation",
                100: "Special Grade Potential - Unlock hidden power within yourself"
            }
        )
        
        # Ryomen Sukuna (in Megumi's body)
        self.npcs["sukuna"] = NPC(
            "Ryomen Sukuna",
            ["malevolent", "powerful", "ancient", "cunning", "arrogant"],
            {
                "neutral": [
                    "Interesting... You dare approach me?",
                    "Another weak sorcerer seeks my attention.",
                    "Do you comprehend who stands before you?",
                    "Your cursed energy is... amusing."
                ],
                "dislike": [
                    "You disgust me with your weakness.",
                    "Begone from my sight, insect.",
                    "Your very existence offends me.",
                    "I have no time for pathetic worms like you."
                ],
                "acquaintance": [
                    "You show promise... for a modern sorcerer.",
                    "Your technique has caught my interest.",
                    "Perhaps you're not entirely worthless.",
                    "I acknowledge your... potential."
                ],
                "friend": [
                    "You have earned a measure of my respect.",
                    "Your power grows... impressive for this era.",
                    "Few have shown such understanding of true strength.",
                    "You begin to comprehend the nature of cursed energy."
                ],
                "good_friend": [
                    "You possess the spirit of a true sorcerer.",
                    "Your evolution has been... entertaining to observe.",
                    "Perhaps this body has found a worthy ally.",
                    "Your cursed techniques show remarkable finesse."
                ],
                "close_friend": [
                    "You have transcended the limitations of your generation.",
                    "In you, I see echoes of the Golden Age of Jujutsu.",
                    "Your power approaches something worthy of my acknowledgment.",
                    "Together, we could reshape this world of sorcery."
                ],
                "neutral_combat": [
                    "Witness the power of the King of Curses!",
                    "I'll show you what true malevolence looks like!",
                    "Prepare yourself for divine techniques!"
                ],
                "friend_combat": [
                    "Fight alongside me, worthy one!",
                    "Let us demonstrate our combined might!",
                    "Your techniques complement my power well!"
                ],
                "close_friend_combat": [
                    "Together, we are unstoppable!",
                    "Our bond transcends the boundaries of vessel and curse!",
                    "Witness the pinnacle of jujutsu sorcery!"
                ]
            },
            {
                25: "Malevolent Insight - Sukuna reveals enemy weaknesses",
                50: "Cursed Energy Mastery - Enhanced technique power",
                75: "Divine Techniques - Access to ancient cursed methods",
                100: "King's Authority - Ultimate power sharing with Sukuna"
            }
        )
    
    def get_npc(self, name: str) -> Optional[NPC]:
        """Get an NPC by name."""
        return self.npcs.get(name.lower())
    
    def interact_with_npc(self, npc_name: str, game_state, interaction_type: str = "casual") -> Dict[str, Any]:
        """Handle interaction with an NPC."""
        npc = self.get_npc(npc_name)
        if not npc:
            return {"error": f"NPC {npc_name} not found"}
        
        current_relationship = game_state.get_relationship(npc_name)
        npc.current_relationship = current_relationship
        
        # Get dialogue
        dialogue = npc.get_dialogue(current_relationship, interaction_type)
        
        # Process interaction effects
        result = {
            "dialogue": dialogue,
            "npc": npc.name,
            "relationship_change": 0,
            "unlocked_abilities": []
        }
        
        # Increase relationship based on interaction type and compatibility
        if interaction_type == "casual":
            relationship_gain = self._calculate_relationship_gain(npc, game_state.player)
        elif interaction_type == "combat":
            relationship_gain = relationship_gain * 2  # Combat bonding is stronger
        elif interaction_type == "training":
            relationship_gain = relationship_gain * 1.5
        else:
            relationship_gain = 1
        
        # Apply relationship change
        game_state.update_relationship(npc_name, relationship_gain)
        result["relationship_change"] = relationship_gain
        
        # Check for newly unlocked abilities
        new_relationship = game_state.get_relationship(npc_name)
        unlocked = npc.check_ability_unlock(new_relationship)
        result["unlocked_abilities"] = unlocked
        
        # Update interaction tracking
        npc.interaction_count += 1
        npc.last_interaction_chapter = game_state.current_chapter
        
        return result
    
    def _calculate_relationship_gain(self, npc: NPC, player) -> int:
        """Calculate relationship gain based on personality compatibility."""
        base_gain = random.randint(1, 3)
        
        # Check personality compatibility
        player_traits = [trait.value.lower() for trait in player.get_dominant_traits()]
        compatible_traits = set(player_traits) & set(npc.personality_traits)
        
        # Bonus for compatible personalities
        compatibility_bonus = len(compatible_traits)
        
        return base_gain + compatibility_bonus
    
    def get_available_npcs(self, location: str) -> List[str]:
        """Get list of NPCs available at a specific location."""
        location_npcs = {
            "tokyo jujutsu high": ["yuji", "megumi", "nobara", "gojo"],
            "kyoto jujutsu high": ["todo", "mai", "noritoshi"],
            "shibuya": ["yuji", "megumi", "nobara"],  # During Shibuya incident
            "training grounds": ["yuji", "megumi", "nobara", "todo"],
        }
        
        # Default to all NPCs if location not specified
        available = []
        for key, npcs in location_npcs.items():
            if key.lower() in location.lower():
                available.extend(npcs)
        
        return list(set(available)) if available else ["yuji", "megumi", "nobara"]
    
    def get_relationship_status(self, npc_name: str, relationship_level: int) -> str:
        """Get a descriptive relationship status."""
        if relationship_level >= 90:
            return "Soul Mates / Brothers-in-Arms"
        elif relationship_level >= 80:
            return "Unbreakable Bond"
        elif relationship_level >= 70:
            return "Best Friends"
        elif relationship_level >= 60:
            return "Close Friends"
        elif relationship_level >= 50:
            return "Good Friends"
        elif relationship_level >= 40:
            return "Friends"
        elif relationship_level >= 30:
            return "Friendly Acquaintances"
        elif relationship_level >= 20:
            return "Acquaintances"
        elif relationship_level >= 10:
            return "Neutral"
        elif relationship_level >= 0:
            return "Distant"
        else:
            return "Dislike"
    
    def check_team_combo_availability(self, player_relationships: Dict[str, int]) -> List[str]:
        """Check which team combination techniques are available."""
        available_combos = []
        
        # Yuji + Player combos
        if player_relationships.get("yuji", 0) >= 80:
            available_combos.append("Black Flash Synchronization")
        
        # Megumi + Player combos
        if player_relationships.get("megumi", 0) >= 85:
            available_combos.append("Shadow Technique Fusion")
        
        # Nobara + Player combos
        if player_relationships.get("nobara", 0) >= 90:
            available_combos.append("Resonance Destruction")
        
        # Todo + Player combos
        if player_relationships.get("todo", 0) >= 95:
            available_combos.append("Brotherhood Ultimate Strike")
        
        # Triple combinations
        yuji_rel = player_relationships.get("yuji", 0)
        megumi_rel = player_relationships.get("megumi", 0)
        nobara_rel = player_relationships.get("nobara", 0)
        
        if yuji_rel >= 70 and megumi_rel >= 70 and nobara_rel >= 70:
            available_combos.append("First Year Trinity Strike")
        
        return available_combos
    
    def execute_team_combo(self, combo_name: str, participants: List[str]) -> Dict[str, Any]:
        """Execute a team combination technique."""
        combo_effects = {
            "Black Flash Synchronization": {
                "damage_multiplier": 2.5,
                "description": "You and Yuji synchronize your cursed energy for a devastating Black Flash!",
                "special_effect": "guaranteed_critical"
            },
            "Shadow Technique Fusion": {
                "damage_multiplier": 2.2,
                "description": "Your techniques merge with Megumi's shadows for a perfect combination attack!",
                "special_effect": "ignore_defenses"
            },
            "Resonance Destruction": {
                "damage_multiplier": 2.8,
                "description": "You and Nobara create a resonance that destroys enemies from within!",
                "special_effect": "true_damage"
            },
            "Brotherhood Ultimate Strike": {
                "damage_multiplier": 3.0,
                "description": "You and Todo unleash the power of true brotherhood!",
                "special_effect": "massive_knockback"
            },
            "First Year Trinity Strike": {
                "damage_multiplier": 3.5,
                "description": "The first years combine their power in perfect harmony!",
                "special_effect": "area_damage"
            }
        }
        
        return combo_effects.get(combo_name, {
            "damage_multiplier": 1.5,
            "description": "A powerful combination attack!",
            "special_effect": "team_boost"
        })


def get_npc_manager() -> NPCManager:
    """Get the global NPC manager instance."""
    return NPCManager()