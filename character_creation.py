"""
Enhanced Character Creation System

Provides expanded character customization including appearance, personality,
backstory, starting techniques, and morality system following the Jujutsu Kaisen universe.
"""

from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
from character import Player, Trait, CursedTechnique
import random


class Appearance:
    """Character appearance options."""
    
    def __init__(self):
        self.hair_color = ""
        self.eye_color = ""
        self.height = ""
        self.build = ""
        self.distinguishing_features = ""
    
    def to_dict(self) -> Dict[str, str]:
        return {
            'hair_color': self.hair_color,
            'eye_color': self.eye_color,
            'height': self.height,
            'build': self.build,
            'distinguishing_features': self.distinguishing_features
        }


class Background(Enum):
    """Character background origins."""
    TOKYO_NATIVE = "tokyo_native"
    COUNTRYSIDE_FAMILY = "countryside_family" 
    CURSE_VICTIM_SURVIVOR = "curse_victim_survivor"
    SORCERER_FAMILY = "sorcerer_family"
    ORDINARY_AWAKENING = "ordinary_awakening"
    TRAGIC_INCIDENT = "tragic_incident"


class MoralitySystem:
    """Tracks player morality affecting relationships and story outcomes."""
    
    def __init__(self):
        self.altruism = 50  # 0-100, affects helping others
        self.pragmatism = 50  # 0-100, affects practical vs idealistic choices
        self.justice = 50  # 0-100, affects rule-following vs doing what's right
        self.mercy = 50  # 0-100, affects sparing enemies vs finishing them
        
    def modify_morality(self, aspect: str, change: int):
        """Modify a morality aspect."""
        current = getattr(self, aspect, 50)
        setattr(self, aspect, max(0, min(100, current + change)))
    
    def get_alignment(self) -> str:
        """Get character's moral alignment based on values."""
        if self.altruism >= 70 and self.justice >= 70:
            return "Heroic"
        elif self.altruism >= 70 and self.pragmatism >= 70:
            return "Pragmatic Hero"
        elif self.pragmatism >= 70 and self.justice <= 30:
            return "Anti-Hero"
        elif self.mercy <= 30 and self.justice <= 30:
            return "Dark"
        else:
            return "Balanced"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'altruism': self.altruism,
            'pragmatism': self.pragmatism,
            'justice': self.justice,
            'mercy': self.mercy,
            'alignment': self.get_alignment()
        }


class StartingTechnique:
    """Represents a starting cursed technique choice."""
    
    def __init__(self, name: str, technique: CursedTechnique, description: str, 
                 progression_path: List[str], requirements: Dict[str, Any] = None):
        self.name = name
        self.technique = technique
        self.description = description
        self.progression_path = progression_path  # Future techniques in this line
        self.requirements = requirements or {}  # Prerequisites for this choice


class CharacterCreator:
    """Enhanced character creation system."""
    
    def __init__(self):
        self.starting_techniques = self._initialize_starting_techniques()
        self.backgrounds = self._initialize_backgrounds()
        
    def create_character(self) -> Player:
        """Interactive character creation process."""
        print("\n" + "=" * 60)
        print("           JUJUTSU SORCERER CREATION")
        print("=" * 60)
        print("Welcome to Tokyo Jujutsu High!")
        print("Let's create your unique sorcerer...")
        
        # Basic info
        name = self._get_character_name()
        
        # Appearance
        appearance = self._customize_appearance()
        
        # Background
        background = self._choose_background()
        
        # Personality traits
        personality_traits = self._select_personality_traits()
        
        # Starting cursed technique
        starting_technique = self._choose_starting_technique()
        
        # Create the player
        player = Player(name)
        
        # Apply customizations
        player.appearance = appearance
        player.background = background
        player.morality = MoralitySystem()
        
        # Apply background effects
        self._apply_background_effects(player, background)
        
        # Set personality traits
        for trait, value in personality_traits.items():
            player.modify_trait(trait, value)
        
        # Add starting technique
        if starting_technique:
            player.add_technique(starting_technique.technique)
            player.technique_progression_path = starting_technique.progression_path
        
        # Display creation summary
        self._display_character_summary(player)
        
        return player
    
    def _get_character_name(self) -> str:
        """Get character name from player."""
        while True:
            name = input("\nEnter your sorcerer's name: ").strip()
            if name:
                return name
            print("Please enter a valid name.")
    
    def _customize_appearance(self) -> Appearance:
        """Interactive appearance customization."""
        print("\n--- APPEARANCE CUSTOMIZATION ---")
        appearance = Appearance()
        
        print("\nChoose your hair color:")
        hair_options = ["Black", "Brown", "Blonde", "White", "Red", "Blue", "Pink", "Green"]
        for i, option in enumerate(hair_options, 1):
            print(f"{i}. {option}")
        
        choice = self._get_choice(len(hair_options))
        appearance.hair_color = hair_options[choice - 1]
        
        print("\nChoose your eye color:")
        eye_options = ["Brown", "Black", "Blue", "Green", "Hazel", "Gray", "Red", "Golden"]
        for i, option in enumerate(eye_options, 1):
            print(f"{i}. {option}")
        
        choice = self._get_choice(len(eye_options))
        appearance.eye_color = eye_options[choice - 1]
        
        print("\nChoose your height:")
        height_options = ["Short (5'0\"-5'4\")", "Average (5'5\"-5'8\")", "Tall (5'9\"-6'2\")", "Very Tall (6'3\"+)"]
        for i, option in enumerate(height_options, 1):
            print(f"{i}. {option}")
        
        choice = self._get_choice(len(height_options))
        appearance.height = height_options[choice - 1]
        
        print("\nChoose your build:")
        build_options = ["Lean", "Athletic", "Muscular", "Stocky", "Petite"]
        for i, option in enumerate(build_options, 1):
            print(f"{i}. {option}")
        
        choice = self._get_choice(len(build_options))
        appearance.build = build_options[choice - 1]
        
        # Optional distinguishing features
        print("\nAny distinguishing features? (scars, tattoos, etc.) [Enter to skip]:")
        features = input("> ").strip()
        appearance.distinguishing_features = features
        
        return appearance
    
    def _choose_background(self) -> Background:
        """Choose character background."""
        print("\n--- CHARACTER BACKGROUND ---")
        print("Your origin story affects starting relationships and abilities:")
        
        backgrounds = [
            ("Tokyo Native", "Born and raised in Tokyo, familiar with urban curse activity"),
            ("Countryside Family", "From a rural sorcerer family with traditional techniques"),
            ("Curse Victim Survivor", "Survived a curse attack, awakening your abilities"),
            ("Sorcerer Family Legacy", "Born into a prominent sorcerer family with expectations"),
            ("Ordinary Awakening", "Regular person who suddenly developed cursed energy"),
            ("Tragic Incident", "Lost loved ones to curses, driving your desire for power")
        ]
        
        for i, (name, desc) in enumerate(backgrounds, 1):
            print(f"{i}. {name}")
            print(f"   {desc}")
        
        choice = self._get_choice(len(backgrounds))
        return list(Background)[choice - 1]
    
    def _select_personality_traits(self) -> Dict[Trait, int]:
        """Select dominant personality traits."""
        print("\n--- PERSONALITY TRAITS ---")
        print("Choose 3 dominant traits that define your character:")
        
        trait_descriptions = {
            Trait.COMPASSIONATE: "Deeply caring for others, even enemies",
            Trait.FOCUSED: "Maintains concentration and strategic thinking",
            Trait.AGGRESSIVE: "Direct confrontation and overwhelming force",
            Trait.PROTECTIVE: "Shields others from harm at personal cost",
            Trait.ANALYTICAL: "Studies situations and enemies methodically",
            Trait.RECKLESS: "Acts on instinct without considering consequences",
            Trait.DETERMINED: "Never gives up, pushes through adversity",
            Trait.CAUTIOUS: "Careful planning and risk assessment"
        }
        
        available_traits = list(Trait)
        selected_traits = {}
        
        for selection in range(3):
            print(f"\nSelect trait #{selection + 1}:")
            for i, trait in enumerate(available_traits, 1):
                print(f"{i}. {trait.value} - {trait_descriptions[trait]}")
            
            choice = self._get_choice(len(available_traits))
            chosen_trait = available_traits[choice - 1]
            
            # Higher value for first trait, medium for second, lower for third
            trait_value = [70, 55, 40][selection]
            selected_traits[chosen_trait] = trait_value
            
            # Remove chosen trait from available options
            available_traits.remove(chosen_trait)
        
        return selected_traits
    
    def _choose_starting_technique(self) -> Optional[StartingTechnique]:
        """Choose starting cursed technique."""
        print("\n--- STARTING CURSED TECHNIQUE ---")
        print("Choose your initial cursed technique:")
        
        techniques = list(self.starting_techniques.values())
        
        for i, tech in enumerate(techniques, 1):
            print(f"{i}. {tech.name}")
            print(f"   {tech.description}")
            print(f"   Progression: {' → '.join(tech.progression_path[:3])}...")
        
        print(f"{len(techniques) + 1}. Random Assignment (Let fate decide)")
        
        choice = self._get_choice(len(techniques) + 1)
        
        if choice == len(techniques) + 1:
            return random.choice(techniques)
        else:
            return techniques[choice - 1]
    
    def _apply_background_effects(self, player: Player, background: Background):
        """Apply background-specific effects to the player."""
        if background == Background.TOKYO_NATIVE:
            player.morality.pragmatism += 10
            # Starting relationship bonus with Tokyo students
            
        elif background == Background.COUNTRYSIDE_FAMILY:
            player.morality.justice += 15
            # Bonus to traditional technique learning
            
        elif background == Background.CURSE_VICTIM_SURVIVOR:
            player.morality.mercy -= 10
            player.modify_trait(Trait.DETERMINED, 20)
            # Fear resistance bonus
            
        elif background == Background.SORCERER_FAMILY:
            player.max_cursed_energy += 20
            player.cursed_energy += 20
            # Higher expectations, pressure
            
        elif background == Background.ORDINARY_AWAKENING:
            player.morality.altruism += 15
            # Unique perspective bonuses
            
        elif background == Background.TRAGIC_INCIDENT:
            player.morality.justice += 20
            player.modify_trait(Trait.PROTECTIVE, 25)
            # Bonus damage against curses
    
    def _initialize_starting_techniques(self) -> Dict[str, StartingTechnique]:
        """Initialize available starting techniques."""
        techniques = {}
        
        # Divergent Fist lineage (Yuji-inspired)
        divergent_fist = CursedTechnique(
            "Divergent Fist",
            damage=30,
            cost=15,
            description="A delayed cursed energy impact following your physical strike.",
            technique_type="offensive",
            cooldown=1
        )
        techniques["divergent_fist"] = StartingTechnique(
            "Divergent Fist Path",
            divergent_fist,
            "Master the art of delayed cursed energy, leading to Black Flash mastery",
            ["Divergent Fist", "Enhanced Strikes", "Black Flash", "Perfect Black Flash"]
        )
        
        # Ten Shadows foundation (Megumi-inspired)
        shadow_manipulation = CursedTechnique(
            "Shadow Manifestation", 
            damage=25,
            cost=20,
            description="Manifest simple shadow constructs for offense and defense.",
            technique_type="utility",
            cooldown=2
        )
        techniques["shadow_manifestation"] = StartingTechnique(
            "Ten Shadows Path",
            shadow_manipulation,
            "Control shadows and summon shikigami, potentially unlocking the Ten Shadows Technique",
            ["Shadow Manifestation", "Divine Dogs", "Nue", "Great Serpent", "Max Elephant"]
        )
        
        # Cursed Speech foundation (Inumaki-inspired)
        minor_speech = CursedTechnique(
            "Compelling Word",
            damage=20,
            cost=25,
            description="Speak a single word with cursed energy to compel weak actions.",
            technique_type="utility",
            cooldown=3
        )
        techniques["compelling_word"] = StartingTechnique(
            "Cursed Speech Path",
            minor_speech,
            "Develop the power of cursed speech, affecting reality through words",
            ["Compelling Word", "Command Voice", "Cursed Speech", "Reality Alteration"]
        )
        
        # Construction technique (inspired by Nobara)
        tool_enhancement = CursedTechnique(
            "Tool Enhancement",
            damage=28,
            cost=18,
            description="Enhance weapons and tools with cursed energy.",
            technique_type="offensive",
            cooldown=1
        )
        techniques["tool_enhancement"] = StartingTechnique(
            "Construction Path", 
            tool_enhancement,
            "Master cursed tool creation and manipulation",
            ["Tool Enhancement", "Cursed Constructs", "Straw Doll Technique", "Resonance"]
        )
        
        # Original: Energy Manipulation
        pure_energy = CursedTechnique(
            "Cursed Energy Shaping",
            damage=35,
            cost=22,
            description="Shape raw cursed energy into various offensive forms.",
            technique_type="offensive",
            cooldown=2
        )
        techniques["energy_shaping"] = StartingTechnique(
            "Pure Energy Path",
            pure_energy,
            "Master raw cursed energy manipulation and create unique techniques",
            ["Energy Shaping", "Energy Blasts", "Energy Shields", "Energy Domain"]
        )
        
        return techniques
    
    def _initialize_backgrounds(self) -> Dict[Background, Dict[str, Any]]:
        """Initialize background information and effects."""
        return {
            Background.TOKYO_NATIVE: {
                "description": "Born and raised in Tokyo, you're familiar with the urban curse environment.",
                "starting_relationships": {"yuji": 5, "nobara": 5},
                "special_knowledge": ["tokyo_geography", "urban_curses"],
                "morality_effects": {"pragmatism": 10}
            },
            Background.COUNTRYSIDE_FAMILY: {
                "description": "From a rural sorcerer family with traditional techniques.",
                "starting_relationships": {"megumi": 10},
                "special_knowledge": ["traditional_techniques", "family_history"],
                "morality_effects": {"justice": 15}
            },
            # ... other backgrounds would be defined here
        }
    
    def _get_choice(self, max_choice: int) -> int:
        """Get and validate user choice."""
        while True:
            try:
                choice = int(input(f"\nEnter your choice (1-{max_choice}): "))
                if 1 <= choice <= max_choice:
                    return choice
                else:
                    print(f"Please enter a number between 1 and {max_choice}.")
            except ValueError:
                print("Please enter a valid number.")
    
    def _display_character_summary(self, player: Player):
        """Display complete character creation summary."""
        print("\n" + "=" * 60)
        print("           CHARACTER CREATION COMPLETE")
        print("=" * 60)
        print(f"Name: {player.name}")
        print(f"Appearance: {player.appearance.hair_color} hair, {player.appearance.eye_color} eyes")
        print(f"           {player.appearance.height}, {player.appearance.build} build")
        if player.appearance.distinguishing_features:
            print(f"           {player.appearance.distinguishing_features}")
        
        print(f"\nBackground: {player.background.value.replace('_', ' ').title()}")
        
        print(f"\nDominant Traits:")
        for trait in player.get_dominant_traits():
            print(f"  • {trait.value}")
        
        print(f"\nMoral Alignment: {player.morality.get_alignment()}")
        
        if hasattr(player, 'technique_progression_path'):
            print(f"\nTechnique Path: {player.technique_progression_path[0]}")
        
        print(f"\nStarting Stats:")
        print(f"  HP: {player.hp}/{player.max_hp}")
        print(f"  Cursed Energy: {player.cursed_energy}/{player.max_cursed_energy}")
        print(f"  Level: {player.level}")
        
        print("\n" + "=" * 60)
        input("Press Enter to begin your journey at Tokyo Jujutsu High...")