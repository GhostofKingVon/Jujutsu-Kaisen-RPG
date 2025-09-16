"""
Enhanced NPC System - Manga Characters

Detailed interactions with canonical Jujutsu Kaisen characters including 
personality-based dialogue, relationship consequences, and technique learning.
"""

from typing import Dict, List, Any, Optional, Tuple
from character import Trait
import random


class MangaNPC:
    """Enhanced NPC class for manga characters with deeper personality and interactions."""
    
    def __init__(self, name: str, personality_traits: List[str], 
                 background: str, cursed_technique: str,
                 dialogue_tree: Dict[str, Any],
                 teaching_abilities: List[str] = None,
                 relationship_effects: Dict[int, str] = None):
        self.name = name
        self.personality_traits = personality_traits
        self.background = background
        self.cursed_technique = cursed_technique
        self.dialogue_tree = dialogue_tree
        self.teaching_abilities = teaching_abilities or []
        self.relationship_effects = relationship_effects or {}
        
        # Relationship tracking
        self.current_relationship = 0
        self.interaction_count = 0
        self.last_interaction_chapter = 0
        self.unlocked_teachings = []
        self.personal_story_unlocked = False
        
        # Situational states
        self.current_mood = "neutral"
        self.story_context = "daily_life"
    
    def get_dialogue(self, relationship_level: int, context: str = "casual", 
                    player_traits: List[Trait] = None) -> Dict[str, Any]:
        """Get contextual dialogue based on relationship, situation, and player traits."""
        
        # Determine relationship category
        rel_category = self._get_relationship_category(relationship_level)
        
        # Get base dialogue options
        dialogue_key = f"{rel_category}_{context}"
        if dialogue_key not in self.dialogue_tree:
            dialogue_key = rel_category
        
        base_dialogues = self.dialogue_tree.get(dialogue_key, ["..."])
        
        # Personality compatibility effects
        compatibility_bonus = self._calculate_compatibility(player_traits or [])
        
        # Select appropriate dialogue
        selected_dialogue = random.choice(base_dialogues)
        
        # Add personality-based reactions
        reaction = self._get_personality_reaction(context, compatibility_bonus)
        
        return {
            "dialogue": selected_dialogue,
            "reaction": reaction,
            "relationship_change": self._calculate_relationship_change(context, compatibility_bonus),
            "special_event": self._check_special_events(relationship_level, context)
        }
    
    def _get_relationship_category(self, level: int) -> str:
        """Convert numerical relationship to category."""
        if level >= 80:
            return "unbreakable_bond"
        elif level >= 60:
            return "close_friend"
        elif level >= 40:
            return "good_friend"
        elif level >= 20:
            return "friend"
        elif level >= 10:
            return "acquaintance"
        elif level >= 0:
            return "neutral"
        else:
            return "dislike"
    
    def _calculate_compatibility(self, player_traits: List[Trait]) -> int:
        """Calculate personality compatibility bonus."""
        compatibility = 0
        player_trait_names = [trait.value.lower() for trait in player_traits]
        
        for trait in self.personality_traits:
            if trait.lower() in player_trait_names:
                compatibility += 10
        
        return compatibility
    
    def _get_personality_reaction(self, context: str, compatibility: int) -> str:
        """Get personality-based reaction."""
        if compatibility > 20:
            return "very_positive"
        elif compatibility > 10:
            return "positive"
        elif compatibility < -10:
            return "negative"
        else:
            return "neutral"
    
    def _calculate_relationship_change(self, context: str, compatibility: int) -> int:
        """Calculate how much relationship should change."""
        base_change = {
            "casual": 2,
            "combat": 5,
            "training": 3,
            "personal": 8,
            "crisis": 10
        }.get(context, 2)
        
        # Apply compatibility modifier
        modifier = compatibility // 10
        return base_change + modifier
    
    def _check_special_events(self, relationship_level: int, context: str) -> Optional[str]:
        """Check if any special events should trigger."""
        # Personal story unlock
        if relationship_level >= 50 and not self.personal_story_unlocked:
            self.personal_story_unlocked = True
            return "personal_story"
        
        # Teaching opportunities
        for threshold in [30, 60, 80]:
            if relationship_level >= threshold and threshold not in [int(t.split('_')[0]) for t in self.unlocked_teachings]:
                return f"teaching_opportunity_{threshold}"
        
        return None
    
    def can_teach_technique(self, technique_name: str, relationship_level: int) -> bool:
        """Check if NPC can teach a specific technique."""
        return (technique_name in self.teaching_abilities and 
                relationship_level >= 40)


class EnhancedNPCManager:
    """Manages enhanced manga character NPCs."""
    
    def __init__(self):
        self.npcs = {}
        self._initialize_manga_characters()
    
    def _initialize_manga_characters(self):
        """Initialize all major manga characters."""
        
        # Yuji Itadori - The Protagonist's Heart
        self.npcs["yuji"] = MangaNPC(
            name="Yuji Itadori",
            personality_traits=["compassionate", "determined", "optimistic", "protective", "empathetic"],
            background="Former regular student who became Sukuna's vessel to save others",
            cursed_technique="Superhuman Physical Abilities + Sukuna's Techniques",
            dialogue_tree={
                "neutral": [
                    "Hey! I'm Yuji Itadori. Nice to meet you!",
                    "Are you a new sorcerer? Welcome to this crazy world!",
                    "Don't worry, we'll figure this curse stuff out together!"
                ],
                "friend": [
                    "You're really getting the hang of this! I'm proud of you.",
                    "Want to grab some food? Fighting curses works up an appetite!",
                    "I love how you never give up, no matter how tough things get."
                ],
                "close_friend": [
                    "You're someone I can always count on. Thank you for that.",
                    "Together, we can save everyone! I truly believe that.",
                    "Your strength gives me hope, even in the darkest times."
                ],
                "unbreakable_bond": [
                    "You're like family to me. I'd face any curse to protect you.",
                    "Our bond transcends life and death. Nothing can break us apart!",
                    "With you by my side, I feel like we can change the world."
                ],
                "friend_combat": [
                    "Let's show them what teamwork looks like!",
                    "I've got your back! Trust in our bond!"
                ],
                "close_friend_combat": [
                    "Our hearts beat as one! Let's do this!",
                    "This is our strength - the power to protect others!"
                ],
                "personal": [
                    "Sometimes I wonder if I'm strong enough to carry Sukuna's burden...",
                    "Every life we save makes it all worth it, you know?",
                    "I'm scared of what Sukuna might do, but I won't give up."
                ]
            },
            teaching_abilities=["divergent_fist", "black_flash", "physical_enhancement"],
            relationship_effects={
                30: "Yuji shares training tips for physical enhancement",
                60: "Yuji teaches basics of Black Flash technique",
                80: "Unlocks combination attacks with Yuji"
            }
        )
        
        # Megumi Fushiguro - The Strategic Thinker
        self.npcs["megumi"] = MangaNPC(
            name="Megumi Fushiguro",
            personality_traits=["analytical", "reserved", "strategic", "loyal", "introspective"],
            background="Heir to the Zenin clan who chose his own path",
            cursed_technique="Ten Shadows Technique",
            dialogue_tree={
                "neutral": [
                    "I'm Megumi Fushiguro. Let's work efficiently together.",
                    "Focus on understanding your technique's fundamentals.",
                    "This world isn't kind to the unprepared."
                ],
                "friend": [
                    "Your analytical approach is commendable.",
                    "I respect how you handle difficult situations.",
                    "You've proven yourself more capable than most."
                ],
                "close_friend": [
                    "I trust your judgment completely.",
                    "Your growth has been remarkable to witness.",
                    "You understand the weight of our responsibilities."
                ],
                "unbreakable_bond": [
                    "You're one of the few people I trust with my life.",
                    "Our strategies work because we truly understand each other.",
                    "I'll stand with you against any threat, no matter the cost."
                ],
                "friend_combat": [
                    "Let's coordinate our attacks strategically.",
                    "Your positioning is perfect. I'll support you."
                ],
                "personal": [
                    "I sometimes wonder if I'm holding everyone back...",
                    "The Ten Shadows technique... it's both a gift and a burden.",
                    "I chose this path to save my sister. I can't fail."
                ]
            },
            teaching_abilities=["shadow_manipulation", "strategic_thinking", "shikigami_basics"],
            relationship_effects={
                30: "Megumi shares tactical combat knowledge",
                60: "Megumi teaches shadow manipulation basics",
                80: "Unlocks advanced Ten Shadows training"
            }
        )
        
        # Nobara Kugisaki - The Confident Fighter
        self.npcs["nobara"] = MangaNPC(
            name="Nobara Kugisaki",
            personality_traits=["confident", "fierce", "loyal", "fashion-conscious", "stubborn"],
            background="Country girl who came to Tokyo to prove herself",
            cursed_technique="Straw Doll Technique",
            dialogue_tree={
                "neutral": [
                    "I'm Nobara Kugisaki. Don't expect me to go easy on you!",
                    "You better keep up with me if we're working together.",
                    "I didn't come to Tokyo to babysit newbies."
                ],
                "friend": [
                    "Not bad! You might actually be worth my time.",
                    "Your style is starting to grow on me.",
                    "Okay, I admit it - you're pretty cool."
                ],
                "close_friend": [
                    "You're one of the few people who really gets me.",
                    "I'd fight any curse for you - and look good doing it!",
                    "We make an unstoppable team, don't we?"
                ],
                "unbreakable_bond": [
                    "You're stuck with me for life now - lucky you!",
                    "Together we'll show everyone what real strength looks like!",
                    "My nail techniques and your skills? Unbeatable combination!"
                ],
                "friend_combat": [
                    "Let's show them how it's done!",
                    "Follow my lead - I've got this!"
                ],
                "personal": [
                    "Sometimes I miss the countryside... but don't tell anyone I said that.",
                    "I came to Tokyo to be someone important. I won't settle for less.",
                    "People think I'm just a country bumpkin, but I'll prove them wrong."
                ]
            },
            teaching_abilities=["straw_doll_technique", "nail_techniques", "confidence_building"],
            relationship_effects={
                30: "Nobara gives fashion and confidence advice",
                60: "Nobara teaches Straw Doll technique basics",
                80: "Unlocks advanced resonance techniques"
            }
        )
        
        # Satoru Gojo - The Strongest
        self.npcs["gojo"] = MangaNPC(
            name="Satoru Gojo",
            personality_traits=["confident", "playful", "powerful", "protective", "unconventional"],
            background="The strongest jujutsu sorcerer and teacher",
            cursed_technique="Limitless + Six Eyes",
            dialogue_tree={
                "neutral": [
                    "Yo! I'm Gojo-sensei, your impossibly handsome teacher!",
                    "Ready to learn from the strongest? You're in for a treat!",
                    "Don't worry, I'll make sure you don't die... probably."
                ],
                "friend": [
                    "You're showing real promise! I'm impressed.",
                    "Keep this up and you might actually be worth my time!",
                    "Your potential is... interesting. Very interesting."
                ],
                "close_friend": [
                    "You remind me of myself at your age - terrifying thought!",
                    "I see great things in your future, kid.",
                    "You've got what it takes to change this world."
                ],
                "unbreakable_bond": [
                    "You're like the student I always hoped to have.",
                    "Together, we can reshape the jujutsu world!",
                    "I trust you with my students - that's the highest honor I can give."
                ],
                "friend_combat": [
                    "Watch and learn from the master!",
                    "Try to keep up with me!"
                ],
                "personal": [
                    "Being the strongest is... lonely sometimes.",
                    "I fight so my students can have a better world than I did.",
                    "The weight of everyone's expectations... it's heavier than you'd think."
                ]
            },
            teaching_abilities=["limitless_basics", "infinity_theory", "advanced_combat"],
            relationship_effects={
                40: "Gojo shares basic Limitless theory",
                70: "Gojo provides advanced technique training",
                90: "Gojo considers you his successor"
            }
        )
        
        # Sukuna - The King of Curses
        self.npcs["sukuna"] = MangaNPC(
            name="Ryomen Sukuna",
            personality_traits=["sadistic", "powerful", "ancient", "prideful", "calculating"],
            background="The legendary King of Curses from 1000 years ago",
            cursed_technique="Cleave, Dismantle, Fire techniques",
            dialogue_tree={
                "neutral": [
                    "A mere insect dares to address me?",
                    "How amusing... another weak sorcerer.",
                    "You bore me already."
                ],
                "acquaintance": [
                    "Hmm, you're slightly less pathetic than the others.",
                    "Your cursed energy has a... distinct flavor.",
                    "Perhaps you're worth a few moments of my attention."
                ],
                "friend": [  # Sukuna doesn't really have "friends"
                    "You continue to surprise me, mortal.",
                    "Your strength grows... interesting.",
                    "I acknowledge your existence."
                ],
                "close_friend": [
                    "You amuse me more than most insects.",
                    "Perhaps when I reclaim my full power, I'll spare you.",
                    "Your potential... it intrigues the King of Curses."
                ],
                "combat": [
                    "Finally, some entertainment!",
                    "Let me show you true power!",
                    "Kneel before the King of Curses!"
                ],
                "personal": [
                    "This vessel... it constrains my true magnificence.",
                    "One day, I will reclaim my throne.",
                    "The age of humans is ending. My age will begin anew."
                ]
            },
            teaching_abilities=["curse_knowledge", "domain_theory", "ancient_techniques"],
            relationship_effects={
                20: "Sukuna shares ancient curse knowledge",
                50: "Sukuna teaches basic Domain theory", 
                80: "Sukuna considers making a binding vow"
            }
        )
        
        # Aoi Todo - The Eccentric Powerhouse
        self.npcs["todo"] = MangaNPC(
            name="Aoi Todo",
            personality_traits=["eccentric", "powerful", "passionate", "loyal", "unpredictable"],
            background="Third-year Kyoto student obsessed with strength and his 'type'",
            cursed_technique="Boogie Woogie",
            dialogue_tree={
                "neutral": [
                    "What's your type in women? Answer me!",
                    "Show me your strength! I'll judge if you're worthy!",
                    "A sorcerer without passion is just a walking corpse!"
                ],
                "friend": [
                    "My brother! You understand what true strength means!",
                    "Your passion burns as bright as mine!",
                    "Together we are unstoppable!"
                ],
                "close_friend": [
                    "You are my brother in arms and in spirit!",
                    "Our friendship transcends schools and rivalry!",
                    "Let's reach even greater heights together!"
                ],
                "unbreakable_bond": [
                    "My best friend! My brother! My equal!",
                    "Our bond is stronger than any cursed technique!",
                    "We'll become legends together!"
                ],
                "friend_combat": [
                    "Let's show them the power of true friendship!",
                    "Switching places in 3... 2... 1!"
                ],
                "personal": [
                    "Strength without heart is meaningless.",
                    "I fight for those who can't fight for themselves.",
                    "My technique lets me be everywhere I'm needed most."
                ]
            },
            teaching_abilities=["boogie_woogie", "combat_passion", "friendship_power"],
            relationship_effects={
                30: "Todo teaches combat enthusiasm",
                60: "Todo shares Boogie Woogie techniques",
                80: "Todo considers you his best friend forever"
            }
        )
    
    def get_npc(self, name: str) -> Optional[MangaNPC]:
        """Get an NPC by name."""
        return self.npcs.get(name.lower())
    
    def interact_with_npc(self, npc_name: str, player, context: str = "casual") -> Dict[str, Any]:
        """Handle interaction with an NPC."""
        npc = self.get_npc(npc_name)
        if not npc:
            return {"error": "NPC not found"}
        
        # Get current relationship level
        current_relationship = getattr(player, 'relationships', {}).get(npc_name.lower(), 0)
        
        # Get player's dominant traits
        player_traits = getattr(player, 'dominant_traits', [])
        
        # Get dialogue and effects
        interaction_result = npc.get_dialogue(current_relationship, context, player_traits)
        
        # Update interaction count
        npc.interaction_count += 1
        
        # Apply relationship change
        if hasattr(player, 'relationships'):
            old_relationship = player.relationships.get(npc_name.lower(), 0)
            new_relationship = old_relationship + interaction_result['relationship_change']
            player.relationships[npc_name.lower()] = max(-100, min(100, new_relationship))
            
            # Check for new abilities or events
            new_abilities = []
            for threshold, ability in npc.relationship_effects.items():
                if new_relationship >= threshold and old_relationship < threshold:
                    new_abilities.append(ability)
            
            interaction_result['new_abilities'] = new_abilities
        
        return interaction_result
    
    def get_available_teachers(self, player) -> List[Tuple[str, List[str]]]:
        """Get list of NPCs who can teach the player techniques."""
        available_teachers = []
        
        for npc_name, npc in self.npcs.items():
            relationship = getattr(player, 'relationships', {}).get(npc_name, 0)
            teachable_techniques = []
            
            for technique in npc.teaching_abilities:
                if npc.can_teach_technique(technique, relationship):
                    teachable_techniques.append(technique)
            
            if teachable_techniques:
                available_teachers.append((npc.name, teachable_techniques))
        
        return available_teachers
    
    def check_special_events(self, player, current_chapter: int) -> List[Dict[str, Any]]:
        """Check for special events triggered by relationships or story progress."""
        special_events = []
        
        for npc_name, npc in self.npcs.items():
            relationship = getattr(player, 'relationships', {}).get(npc_name, 0)
            
            # Check for personal story unlocks
            if relationship >= 50 and not npc.personal_story_unlocked:
                special_events.append({
                    "type": "personal_story",
                    "npc": npc.name,
                    "title": f"{npc.name}'s Personal Story",
                    "description": f"Your close relationship with {npc.name} unlocks their personal story."
                })
                npc.personal_story_unlocked = True
            
            # Check for technique teaching opportunities
            for threshold in [30, 60, 80]:
                if (relationship >= threshold and 
                    f"taught_{threshold}" not in npc.unlocked_teachings):
                    
                    special_events.append({
                        "type": "technique_teaching",
                        "npc": npc.name,
                        "threshold": threshold,
                        "techniques": npc.teaching_abilities
                    })
                    npc.unlocked_teachings.append(f"taught_{threshold}")
        
        return special_events