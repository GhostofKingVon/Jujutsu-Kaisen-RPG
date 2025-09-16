"""
Arc 2: Vs. Mahito/Junpei Arc

Covers the encounter with Mahito and the tragic story of Junpei:
- First encounter with special grade curse Mahito
- Meeting Junpei Yoshino and his struggles
- Understanding the darker side of curses and human nature
- Making difficult moral choices
- Potential to save or lose Junpei based on player decisions
"""

from typing import Dict, Any
from character import Trait, Enemy
from .base_arc import BaseStoryArc, StoryChoice, StoryScene


class MahitoJunpeiArc(BaseStoryArc):
    """Second arc focusing on Mahito and Junpei's story."""
    
    def __init__(self):
        super().__init__("Vs. Mahito/Junpei Arc", 2)
    
    def initialize_arc(self):
        """Initialize all scenes for the Mahito/Junpei Arc."""
        
        # Arc starting scene
        self.add_scene("start", StoryScene(
            "Strange Reports",
            """Reports have been coming in about unusual cursed spirit activity in a local 
high school. Students have been found dead under mysterious circumstances, their bodies 
grotesquely transformed. The pattern suggests the work of a special grade cursed spirit.

Nanami-sensei briefs your team on the mission while Gojo is away on other business.

"This isn't like the training exercises," Nanami warns. "A special grade curse is far 
beyond what you've faced. Your job is to investigate and gather intelligence, not to 
engage directly."

As you approach the school, you sense an overwhelming malevolent presence.""",
            [
                StoryChoice(
                    "Suggest splitting up to cover more ground",
                    {
                        "traits": {Trait.ANALYTICAL: 5, Trait.CAUTIOUS: 5},
                        "story_flags": {"strategic_approach": True},
                        "next_scene": "investigation_split"
                    }
                ),
                StoryChoice(
                    "Insist the team stays together for safety",
                    {
                        "traits": {Trait.PROTECTIVE: 10, Trait.CAUTIOUS: 5},
                        "story_flags": {"safety_first": True},
                        "next_scene": "investigation_together"
                    }
                ),
                StoryChoice(
                    "Volunteer to investigate the most dangerous area alone",
                    {
                        "traits": {Trait.DETERMINED: 10, Trait.RECKLESS: 5},
                        "story_flags": {"solo_volunteer": True},
                        "next_scene": "investigation_solo"
                    }
                )
            ],
            "Cursed High School - Entrance"
        ))
        
        # Investigation outcomes lead to meeting Junpei
        self.add_scene("investigation_together", StoryScene(
            "A Lonely Figure",
            """Moving through the school as a group, you discover evidence of the curse's 
handiwork - twisted bodies and an overwhelming aura of hatred. As you investigate the 
rooftop, you encounter a solitary student sitting alone.

The boy appears to be around your age, with dark hair covering his eyes. He doesn't 
seem surprised to see you, despite your arrival being unusual.

"You're not students here," he observes quietly. "You're like those others who can see 
things that aren't supposed to exist, aren't you?"

This must be Junpei Yoshino. You can sense cursed energy around him, but it feels... 
different. Almost familiar.""",
            [
                StoryChoice(
                    "Approach him calmly and introduce yourself",
                    {
                        "traits": {Trait.COMPASSIONATE: 10},
                        "relationships": {"junpei": 15},
                        "story_flags": {"gentle_approach": True},
                        "next_scene": "junpei_introduction"
                    }
                ),
                StoryChoice(
                    "Question him about the strange deaths",
                    {
                        "traits": {Trait.ANALYTICAL: 10},
                        "relationships": {"junpei": 5},
                        "story_flags": {"direct_questioning": True},
                        "next_scene": "junpei_interrogation"
                    }
                ),
                StoryChoice(
                    "Warn him about the danger and tell him to leave",
                    {
                        "traits": {Trait.PROTECTIVE: 10},
                        "relationships": {"junpei": 10},
                        "story_flags": {"protective_warning": True},
                        "next_scene": "junpei_warning"
                    }
                )
            ],
            "Cursed High School - Rooftop"
        ))
        
        # Junpei introduction scene
        self.add_scene("junpei_introduction", StoryScene(
            "Understanding Junpei",
            """You sit down near Junpei, keeping a respectful distance. Your gentle approach 
seems to surprise him - it's clear he's not used to kindness from his peers.

"I'm not used to people being... nice," Junpei admits. "This school is full of bullies 
and fake people. But recently, I met someone who understood. Someone who showed me that 
people who hurt others deserve what they get."

His words send a chill down your spine. The cursed energy around him is growing stronger, 
and you realize he's been influenced by something - or someone - dangerous.

"His name is Mahito," Junpei continues. "He taught me that curses are more honest than 
humans. They don't pretend to be something they're not.""",
            [
                StoryChoice(
                    "Try to convince him that Mahito is manipulating him",
                    {
                        "traits": {Trait.COMPASSIONATE: 5, Trait.DETERMINED: 5},
                        "relationships": {"junpei": 10},
                        "story_flags": {"attempted_persuasion": True},
                        "next_scene": "persuasion_attempt"
                    }
                ),
                StoryChoice(
                    "Ask him to tell you more about Mahito",
                    {
                        "traits": {Trait.ANALYTICAL: 10},
                        "relationships": {"junpei": 5},
                        "story_flags": {"gathering_intel": True},
                        "next_scene": "mahito_information"
                    }
                ),
                StoryChoice(
                    "Share your own experiences with loneliness and bullying",
                    {
                        "traits": {Trait.COMPASSIONATE: 15},
                        "relationships": {"junpei": 20},
                        "story_flags": {"emotional_connection": True},
                        "next_scene": "emotional_bond"
                    }
                )
            ],
            "Cursed High School - Rooftop"
        ))
        
        # Emotional bond scene - key for saving Junpei
        self.add_scene("emotional_bond", StoryScene(
            "A Moment of Connection",
            """You share your own struggles and the pain of feeling isolated. Junpei's eyes 
widen with recognition - someone finally understands his suffering without judgment.

"You... you really get it," he whispers. "I thought I was the only one who felt this 
empty. Mahito said that all humans are cruel, but you're..."

Suddenly, the air grows thick with malevolent cursed energy. A grotesque figure emerges 
from the shadows - Mahito himself, his patchwork appearance and stitched smile making 
your skin crawl.

"My, my," Mahito says with false cheer. "It seems Junpei has made a new friend. How 
delightfully human of him."

Your emotional connection with Junpei may be the key to saving him from Mahito's influence.""",
            [
                StoryChoice(
                    "Stand protectively in front of Junpei",
                    {
                        "traits": {Trait.PROTECTIVE: 15, Trait.DETERMINED: 10},
                        "relationships": {"junpei": 25},
                        "story_flags": {"protected_junpei": True},
                        "next_scene": "protective_stance"
                    }
                ),
                StoryChoice(
                    "Challenge Mahito directly",
                    {
                        "traits": {Trait.AGGRESSIVE: 10, Trait.RECKLESS: 5},
                        "story_flags": {"challenged_mahito": True},
                        "combat": True,
                        "enemy": "mahito_first_encounter",
                        "next_scene": "mahito_first_battle"
                    }
                ),
                StoryChoice(
                    "Try to appeal to Junpei's humanity",
                    {
                        "traits": {Trait.COMPASSIONATE: 15},
                        "relationships": {"junpei": 20},
                        "story_flags": {"appeal_to_humanity": True},
                        "next_scene": "humanity_appeal"
                    }
                )
            ],
            "Cursed High School - Rooftop"
        ))
        
        # Key branching point - saving Junpei
        self.add_scene("protective_stance", StoryScene(
            "The Power of Human Connection",
            """Your protective stance triggers something in Junpei. For the first time in months, 
someone is willing to stand up for him without expecting anything in return.

"No," Junpei says suddenly, his voice growing stronger. "Mahito, this person isn't like 
the others. They showed me that not all humans are cruel."

Mahito's smile wavers slightly. "Junpei, you're being naive. Humans will always—"

"You're wrong!" Junpei interrupts, stepping beside you. "I felt real kindness just now. 
Something you said was impossible."

The cursed energy around Junpei begins to stabilize. Your connection has given him the 
strength to resist Mahito's influence.""",
            [
                StoryChoice(
                    "Encourage Junpei to fight alongside you",
                    {
                        "traits": {Trait.DETERMINED: 10},
                        "relationships": {"junpei": 30},
                        "story_flags": {"junpei_ally": True},
                        "ally": "junpei",
                        "next_scene": "junpei_redemption"
                    }
                ),
                StoryChoice(
                    "Tell Junpei to escape while you fight Mahito",
                    {
                        "traits": {Trait.PROTECTIVE: 15, Trait.RECKLESS: 5},
                        "relationships": {"junpei": 25},
                        "story_flags": {"junpei_escaped": True},
                        "combat": True,
                        "enemy": "mahito_enraged",
                        "next_scene": "solo_mahito_fight"
                    }
                )
            ],
            "Cursed High School - Rooftop"
        ))
        
        # Junpei redemption path
        self.add_scene("junpei_redemption", StoryScene(
            "Fighting Together",
            """With Junpei fighting alongside you, Mahito realizes his manipulation has failed. 
The special grade curse's expression shifts from amusement to genuine anger.

"Impossible," Mahito snarls. "Humans are selfish creatures. You're just pretending to 
care about him!"

But Junpei's newfound resolve proves Mahito wrong. Together, you manage to drive off 
the special grade curse, though you know this isn't the last you'll see of him.

"Thank you," Junpei says afterward. "You saved me from becoming something monstrous. 
I want to learn to use my cursed energy to protect people like you did for me."

Your choice to show genuine compassion has saved Junpei and gained a powerful ally.""",
            [
                StoryChoice(
                    "Invite Junpei to join Tokyo Jujutsu High",
                    {
                        "traits": {Trait.COMPASSIONATE: 10},
                        "relationships": {"junpei": 35, "gojo": 10},
                        "story_flags": {"junpei_saved": True, "new_student": True},
                        "achievements": ["Saved Junpei"],
                        "experience": 200,
                        "next_scene": "arc_completion_good"
                    }
                )
            ],
            "Cursed High School - Rooftop"
        ))
        
        # Alternative darker path
        self.add_scene("mahito_manipulation", StoryScene(
            "Mahito's Victory",
            """Without a strong enough connection to counter Mahito's influence, Junpei falls 
deeper under the special grade curse's control. You watch in horror as his humanity 
slips away, replaced by the cold logic of curse thinking.

"You see?" Mahito says triumphantly. "This is what humans truly are beneath their masks. 
Junpei understands now that curses are more honest than your species."

Junpei's transformation into a curse user becomes complete. Your failure to reach him 
in time has created a powerful enemy and given Mahito a victory in his war against humanity.

This tragic outcome will haunt you and affect your relationships with others who learn 
of what happened.""",
            [
                StoryChoice(
                    "Vow to stop Mahito and save others from this fate",
                    {
                        "traits": {Trait.DETERMINED: 15, Trait.PROTECTIVE: 10},
                        "story_flags": {"junpei_lost": True, "mahito_enemy": True},
                        "relationships": {"yuji": -5, "megumi": -5, "nobara": -5},
                        "experience": 100,
                        "next_scene": "arc_completion_tragic"
                    }
                )
            ],
            "Cursed High School - Rooftop"
        ))
        
        # Arc completion scenes
        self.add_scene("arc_completion_good", StoryScene(
            "A Life Saved",
            """Returning to Tokyo Jujutsu High with Junpei, you report the encounter with 
Mahito to the faculty. Gojo is particularly interested in your success in saving Junpei 
from the special grade curse's influence.

"Impressive," Gojo says. "Mahito is one of the most dangerous curses we've encountered. 
His ability to manipulate human souls makes him extremely difficult to counter. But you 
found a way - through genuine human connection."

Junpei begins his training as a jujutsu sorcerer, frequently expressing his gratitude 
for your intervention. Your compassionate choice has not only saved a life but gained 
a loyal friend and ally for the battles ahead.""",
            [
                StoryChoice(
                    "Prepare for future encounters with Mahito",
                    {
                        "story_flags": {"prepared_for_mahito": True},
                        "next_arc": 3,
                        "next_scene": "start"
                    }
                )
            ],
            "Tokyo Jujutsu High - Faculty Office"
        ))
        
        self.add_scene("arc_completion_tragic", StoryScene(
            "The Weight of Failure",
            """The loss of Junpei weighs heavily on everyone at Tokyo Jujutsu High. Your 
teammates struggle with the knowledge that they were unable to save him, and you can 
see the doubt in their eyes.

"These things happen," Gojo tries to console you. "Mahito is extremely dangerous, and 
Junpei was already too far under his influence. Don't blame yourself."

But you do blame yourself. The knowledge that a different choice might have saved Junpei 
haunts your dreams. This failure strengthens your resolve but also introduces a darkness 
that will influence your future decisions.""",
            [
                StoryChoice(
                    "Channel your guilt into determination to save others",
                    {
                        "traits": {Trait.DETERMINED: 20},
                        "story_flags": {"guilt_driven": True},
                        "next_arc": 3,
                        "next_scene": "start"
                    }
                )
            ],
            "Tokyo Jujutsu High - Your Dormitory"
        ))
    
    def create_enemy(self, enemy_type: str, player_level: int) -> Enemy:
        """Create arc-specific enemies."""
        if enemy_type == "mahito_first_encounter":
            enemy = Enemy("Mahito (First Encounter)", 250, 120, "special")
            enemy.ai_pattern = "cunning"
            enemy.special_abilities = ["idle_transfiguration", "soul_manipulation"]
            enemy.weaknesses = ["strong_resolve", "human_connection"]
        elif enemy_type == "mahito_enraged":
            enemy = Enemy("Mahito (Enraged)", 300, 150, "special")
            enemy.ai_pattern = "aggressive"
            enemy.special_abilities = ["idle_transfiguration", "soul_manipulation", "domain_expansion"]
        else:
            return super().create_enemy(enemy_type, player_level)
        
        # Mahito is special grade - don't scale normally
        enemy.level = max(player_level + 3, 10)  # Always stronger than player
        return enemy