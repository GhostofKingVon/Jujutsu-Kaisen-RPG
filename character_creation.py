"""
Enhanced Character Creation System

Provides a comprehensive character creation experience with backgrounds,
traits, relationships, and customization options.
"""

from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
from character import Player, Trait
import random


class Background(Enum):
    """Character background options that affect starting stats and story."""
    ORDINARY_STUDENT = "Ordinary Student"
    SORCERER_FAMILY = "Sorcerer Family"
    CURSE_VICTIM = "Curse Victim Survivor"
    ATHLETE = "Former Athlete"
    SCHOLAR = "Academic Prodigy"
    DELINQUENT = "Reformed Delinquent"


class Appearance:
    """Character appearance options."""
    
    HAIR_COLORS = ["Black", "Brown", "Blonde", "White", "Blue", "Pink", "Red"]
    EYE_COLORS = ["Brown", "Black", "Blue", "Green", "Gray", "Amber", "Violet"]
    HEIGHT_OPTIONS = ["Short", "Average", "Tall", "Very Tall"]
    BUILD_OPTIONS = ["Slim", "Average", "Athletic", "Stocky", "Muscular"]


class CharacterCreationManager:
    """Manages the enhanced character creation process."""
    
    def __init__(self):
        self.background_bonuses = {
            Background.ORDINARY_STUDENT: {
                "traits": {Trait.COMPASSIONATE: 20, Trait.DETERMINED: 15},
                "relationships": {"yuji": 10},
                "description": "You lived a normal life until cursed spirits entered your world."
            },
            Background.SORCERER_FAMILY: {
                "traits": {Trait.FOCUSED: 25, Trait.ANALYTICAL: 20},
                "relationships": {"megumi": 15, "gojo": 5},
                "description": "Born into a family of sorcerers, you understand the jujutsu world."
            },
            Background.CURSE_VICTIM: {
                "traits": {Trait.PROTECTIVE: 25, Trait.CAUTIOUS: 15},
                "relationships": {"nanami": 10},
                "description": "You survived a curse attack that changed your life forever."
            },
            Background.ATHLETE: {
                "traits": {Trait.AGGRESSIVE: 20, Trait.DETERMINED: 25},
                "relationships": {"todo": 15},
                "description": "Your athletic background gives you exceptional physical capabilities."
            },
            Background.SCHOLAR: {
                "traits": {Trait.ANALYTICAL: 30, Trait.FOCUSED: 20},
                "relationships": {"ino": 10},
                "description": "Your academic excellence helps you understand cursed energy theory."
            },
            Background.DELINQUENT: {
                "traits": {Trait.RECKLESS: 20, Trait.AGGRESSIVE: 20},
                "relationships": {"sukuna": 5},
                "description": "Your troubled past made you tough and street-smart."
            }
        }
    
    def create_character(self) -> Player:
        """Run the complete character creation process."""
        print("\n" + "="*60)
        print("           CHARACTER CREATION")
        print("="*60)
        print("Welcome to the world of Jujutsu Sorcerers!")
        print("Let's create your unique character...")
        print()
        
        # Step 1: Basic Information
        name = self._get_character_name()
        
        # Step 2: Background Selection
        background = self._select_background()
        
        # Step 3: Personality Assessment
        personality_traits = self._personality_assessment()
        
        # Step 4: Appearance Customization
        appearance = self._customize_appearance()
        
        # Step 5: Relationship Preferences
        relationship_prefs = self._relationship_preferences()
        
        # Step 6: Final Confirmation
        player = self._create_player_with_choices(
            name, background, personality_traits, appearance, relationship_prefs
        )
        
        self._display_character_summary(player, background, appearance)
        
        return player
    
    def _get_character_name(self) -> str:
        """Get the character's name."""
        print("=== BASIC INFORMATION ===")
        while True:
            name = input("Enter your character's name: ").strip()
            if name and len(name) >= 2:
                print(f"Nice to meet you, {name}!")
                return name
            print("Please enter a valid name (at least 2 characters).")
    
    def _select_background(self) -> Background:
        """Let player select their character's background."""
        print("\n=== BACKGROUND ===")
        print("Your background shapes who you are and how you came to jujutsu sorcery.")
        print()
        
        backgrounds = list(Background)
        for i, bg in enumerate(backgrounds, 1):
            description = self.background_bonuses[bg]["description"]
            print(f"{i}. {bg.value}")
            print(f"   {description}")
            print()
        
        while True:
            try:
                choice = int(input(f"Choose your background (1-{len(backgrounds)}): "))
                if 1 <= choice <= len(backgrounds):
                    selected_bg = backgrounds[choice - 1]
                    print(f"You chose: {selected_bg.value}")
                    return selected_bg
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    def _personality_assessment(self) -> Dict[Trait, int]:
        """Conduct personality assessment through questions."""
        print("\n=== PERSONALITY ASSESSMENT ===")
        print("Answer these questions to determine your character's personality.")
        print()
        
        trait_scores = {trait: 0 for trait in Trait}
        
        questions = [
            {
                "question": "You see a weak curse threatening civilians. What's your first instinct?",
                "answers": [
                    ("Immediately rush to protect them", {Trait.PROTECTIVE: 15, Trait.COMPASSIONATE: 10}),
                    ("Quickly analyze the situation first", {Trait.ANALYTICAL: 15, Trait.CAUTIOUS: 10}),
                    ("Charge in with full force", {Trait.AGGRESSIVE: 15, Trait.RECKLESS: 10}),
                    ("Focus and plan the perfect strike", {Trait.FOCUSED: 15, Trait.DETERMINED: 10})
                ]
            },
            {
                "question": "Your friend is in danger during a mission. How do you respond?",
                "answers": [
                    ("Risk everything to save them", {Trait.PROTECTIVE: 20, Trait.RECKLESS: 10}),
                    ("Find the safest way to help", {Trait.CAUTIOUS: 15, Trait.COMPASSIONATE: 15}),
                    ("Stay focused on the mission", {Trait.FOCUSED: 20, Trait.ANALYTICAL: 10}),
                    ("Never give up until they're safe", {Trait.DETERMINED: 20, Trait.PROTECTIVE: 10})
                ]
            },
            {
                "question": "How do you prefer to approach challenges?",
                "answers": [
                    ("Head-on with determination", {Trait.AGGRESSIVE: 15, Trait.DETERMINED: 15}),
                    ("Carefully and methodically", {Trait.ANALYTICAL: 20, Trait.CAUTIOUS: 10}),
                    ("With compassion for all involved", {Trait.COMPASSIONATE: 20, Trait.PROTECTIVE: 10}),
                    ("With laser focus", {Trait.FOCUSED: 20, Trait.DETERMINED: 10})
                ]
            },
            {
                "question": "What drives you to become stronger?",
                "answers": [
                    ("To protect those I care about", {Trait.PROTECTIVE: 25, Trait.COMPASSIONATE: 15}),
                    ("To understand the truth", {Trait.ANALYTICAL: 20, Trait.FOCUSED: 20}),
                    ("To prove myself", {Trait.DETERMINED: 20, Trait.AGGRESSIVE: 15}),
                    ("To help anyone in need", {Trait.COMPASSIONATE: 25, Trait.PROTECTIVE: 10})
                ]
            }
        ]
        
        for q_data in questions:
            print(f"Q: {q_data['question']}")
            answers = q_data['answers']
            
            for i, (answer_text, _) in enumerate(answers, 1):
                print(f"   {i}. {answer_text}")
            print()
            
            while True:
                try:
                    choice = int(input(f"Your answer (1-{len(answers)}): "))
                    if 1 <= choice <= len(answers):
                        traits_to_add = answers[choice - 1][1]
                        for trait, points in traits_to_add.items():
                            trait_scores[trait] += points
                        print(f"You chose: {answers[choice - 1][0]}")
                        print()
                        break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")
        
        return trait_scores
    
    def _customize_appearance(self) -> Dict[str, str]:
        """Let player customize character appearance."""
        print("\n=== APPEARANCE CUSTOMIZATION ===")
        print("Customize your character's appearance.")
        print()
        
        appearance = {}
        
        # Hair color
        print("Hair colors:", ", ".join(f"{i+1}. {color}" for i, color in enumerate(Appearance.HAIR_COLORS)))
        while True:
            try:
                choice = int(input(f"Choose hair color (1-{len(Appearance.HAIR_COLORS)}): "))
                if 1 <= choice <= len(Appearance.HAIR_COLORS):
                    appearance["hair_color"] = Appearance.HAIR_COLORS[choice - 1]
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Eye color
        print("Eye colors:", ", ".join(f"{i+1}. {color}" for i, color in enumerate(Appearance.EYE_COLORS)))
        while True:
            try:
                choice = int(input(f"Choose eye color (1-{len(Appearance.EYE_COLORS)}): "))
                if 1 <= choice <= len(Appearance.EYE_COLORS):
                    appearance["eye_color"] = Appearance.EYE_COLORS[choice - 1]
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Height
        print("Height options:", ", ".join(f"{i+1}. {height}" for i, height in enumerate(Appearance.HEIGHT_OPTIONS)))
        while True:
            try:
                choice = int(input(f"Choose height (1-{len(Appearance.HEIGHT_OPTIONS)}): "))
                if 1 <= choice <= len(Appearance.HEIGHT_OPTIONS):
                    appearance["height"] = Appearance.HEIGHT_OPTIONS[choice - 1]
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Build
        print("Build options:", ", ".join(f"{i+1}. {build}" for i, build in enumerate(Appearance.BUILD_OPTIONS)))
        while True:
            try:
                choice = int(input(f"Choose build (1-{len(Appearance.BUILD_OPTIONS)}): "))
                if 1 <= choice <= len(Appearance.BUILD_OPTIONS):
                    appearance["build"] = Appearance.BUILD_OPTIONS[choice - 1]
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
        
        return appearance
    
    def _relationship_preferences(self) -> Dict[str, int]:
        """Let player set initial relationship preferences."""
        print("\n=== RELATIONSHIP PREFERENCES ===")
        print("Who are you most interested in getting to know? (This affects starting relationships)")
        print()
        
        npc_options = [
            ("Yuji Itadori", "The determined vessel of Sukuna"),
            ("Megumi Fushiguro", "The serious strategist with shadow techniques"),
            ("Nobara Kugisaki", "The confident girl from the countryside"),
            ("Satoru Gojo", "The strongest sorcerer and eccentric teacher"),
            ("Nanami Kento", "The professional grade 1 sorcerer"),
            ("Aoi Todo", "The powerful student from Kyoto School")
        ]
        
        for i, (name, description) in enumerate(npc_options, 1):
            print(f"{i}. {name} - {description}")
        
        print()
        relationships = {}
        
        while True:
            try:
                choice = int(input(f"Choose someone to start with a closer bond (1-{len(npc_options)}): "))
                if 1 <= choice <= len(npc_options):
                    selected_npc = npc_options[choice - 1][0].lower().split()[0]  # Get first name
                    relationships[selected_npc] = 15
                    print(f"You chose to start with a closer relationship to {npc_options[choice - 1][0]}.")
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
        
        return relationships
    
    def _create_player_with_choices(self, name: str, background: Background, 
                                  personality_traits: Dict[Trait, int], 
                                  appearance: Dict[str, str],
                                  relationship_prefs: Dict[str, int]) -> Player:
        """Create the player character with all customization choices."""
        player = Player(name)
        
        # Apply background bonuses
        bg_bonuses = self.background_bonuses[background]
        for trait, value in bg_bonuses["traits"].items():
            player.modify_trait(trait, value)
        
        for npc, value in bg_bonuses["relationships"].items():
            player.relationships[npc] = value
        
        # Apply personality assessment results
        for trait, value in personality_traits.items():
            player.modify_trait(trait, value)
        
        # Apply relationship preferences
        for npc, value in relationship_prefs.items():
            player.relationships[npc] = player.relationships.get(npc, 0) + value
        
        # Store character info for later reference
        player.background = background
        player.appearance = appearance
        
        return player
    
    def _display_character_summary(self, player: Player, background: Background, 
                                 appearance: Dict[str, str]):
        """Display the final character summary."""
        print("\n" + "="*60)
        print("           CHARACTER SUMMARY")
        print("="*60)
        print(f"Name: {player.name}")
        print(f"Background: {background.value}")
        print(f"Appearance: {appearance['height']}, {appearance['build']} build")
        print(f"           {appearance['hair_color']} hair, {appearance['eye_color']} eyes")
        print()
        print("Dominant Traits:")
        for trait in player.get_dominant_traits():
            print(f"  • {trait.value}")
        print()
        print("Starting Relationships:")
        for npc, value in player.relationships.items():
            if value > 0:
                print(f"  • {npc.title()}: {value}")
        print()
        print("Your journey as a Jujutsu Sorcerer begins...")
        print("="*60)
        
        input("\nPress Enter to continue...")