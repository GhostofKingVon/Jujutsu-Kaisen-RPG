# Jujutsu Kaisen RPG

A turn-based RPG built in Python following the Jujutsu Kaisen manga storyline with player choice-driven narrative, strategic combat, and character relationship dynamics.

## 🎮 Game Features

### Enhanced Character Creation System
- **Comprehensive Backgrounds**: Choose from 6 detailed backgrounds (Ordinary Student, Sorcerer Family, Curse Victim, etc.)
- **Personality Assessment**: 4-question personality test that determines your character's core traits
- **Appearance Customization**: Hair color, eye color, height, and build options
- **Starting Relationships**: Choose which NPCs you want to form closer bonds with initially
- **Trait Integration**: Background and personality choices affect your starting abilities and relationships

### Sukuna (Megumi's Body) Storyline
- **King of Curses**: Encounter Sukuna possessing Megumi's body with unique powers and ancient knowledge
- **Branching Dialogue**: Multiple interaction paths (communication, combat, retreat) with distinct consequences
- **Ancient Techniques**: Learn forbidden jujutsu techniques from Sukuna himself
- **Moral Choices**: Balance gaining power from Sukuna while maintaining your moral compass
- **Story Integration**: Sukuna's presence affects the main storyline and relationships with other characters

### Story-Driven Progression System
- **Natural Technique Learning**: Unlock abilities through meaningful story events rather than just leveling
- **Context-Aware Growth**: Techniques learned reflect your choices and relationships
- **Multiple Learning Paths**: Gain techniques through training with NPCs, story discoveries, or moral decisions
- **Balanced Progression**: Experience and power growth tied to narrative progression

### Comprehensive Side Quest System
- **Character-Specific Quests**: Deep side quests for each major NPC (Megumi, Yuji, Todo, Gojo, etc.)
- **Relationship Requirements**: Quests unlock based on your bond level with specific characters
- **Multiple Objectives**: Each quest has several steps that develop character relationships
- **Meaningful Rewards**: Gain unique techniques, stat bonuses, and character development through quests

### Turn-Based Combat System
- **Combat Actions**: Attack, use cursed techniques (CTs), dodge, guard, or flee
- **Dodge Mechanics**: Prepare to dodge incoming attacks and trigger counters
- **Ultra Instinct System**: Special transformation abilities that enhance dodge chance and counter damage
- **Multi-Phase Boss Battles**: Bosses transition through phases with unique abilities and taunts
- **Strategic Elements**: Status effects, cooldowns, and energy management

### Story and Exploration
- **Canon Storyline**: Follows the Jujutsu Kaisen manga with player choice deviations
- **Branching Narrative**: Decisions affect story progression and character relationships
- **Exploration System**: Interact with environments, discover secrets, and find items
- **Multiple Locations**: Tokyo Jujutsu High, Kyoto School, Shibuya District, and more

### Character Traits and Evolution
- **Dynamic Traits**: Compassionate, Focused, Aggressive, Protective, Analytical, Reckless, Determined, Cautious
- **Trait Evolution**: Traits change based on player decisions and actions
- **Personality Impact**: Dominant traits affect dialogue options, relationship compatibility, and available techniques

### Enhanced NPC Interaction System
- **Deep Character Development**: Extensive dialogue trees with context-specific responses
- **Dynamic Relationships**: NPCs react differently based on your relationship level and recent actions
- **Multiple Interaction Types**: Casual conversation, training sessions, mission coordination
- **Character Growth**: NPCs evolve and change based on your shared experiences

### Cursed Techniques and Abilities
- **Canon Techniques**: Black Flash, Limitless series, Divine Dogs, Boogie Woogie, and more
- **Original Techniques**: Wukong techniques, Ultra Instinct abilities, and unique combinations
- **Story-Based Learning**: Unlock new abilities through character bonds and story events
- **Ancient Knowledge**: Learn forbidden techniques from Sukuna and other powerful entities
- **Domain Expansions**: Ultimate techniques available through deep character development

### Relationship System
- **Enhanced NPCs**: Yuji, Megumi, Nobara, Todo, Gojo, Sukuna, and other canon characters
- **Relationship Levels**: From strangers to unbreakable bonds with detailed progression
- **Team Combinations**: Unlock special combo attacks through strong friendships
- **Personality Compatibility**: Shared traits improve relationship growth
- **Quest Integration**: Relationships unlock unique side quests and story paths

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- No additional dependencies required (uses only standard library)

### Installation
1. Clone the repository
2. Navigate to the game directory
3. Run the game:
   ```bash
   python3 main.py
   ```

### Quick Demo
To see all systems in action without playing:
```bash
python3 demo.py
```

## 📁 File Structure

```
Jujutsu-Kaisen-RPG/
├── main.py              # Main game entry point and game loop
├── game_state.py        # Game state management and save/load system
├── character.py         # Character classes, traits, and progression
├── character_creation.py # Enhanced character creation system
├── combat.py            # Turn-based combat system with strategic elements
├── cursed_techniques.py # Cursed technique library and effects
├── story.py             # Story progression and exploration system
├── npcs.py              # NPC interactions and relationship management
├── side_quests.py       # Comprehensive side quest system
├── demo.py              # Original demonstration script
├── enhanced_demo.py     # Demonstration of all new features
└── README.md            # This file
```

## 🎯 Core Systems

### Character System (`character.py`)
- **Player Class**: Level progression, trait evolution, technique learning
- **Enemy Class**: AI behavior patterns, multi-phase capabilities
- **Trait System**: 8 distinct personality traits affecting gameplay
- **Technique Management**: Cursed energy costs, cooldowns, and effects

### Combat System (`combat.py`)
- **Turn-Based**: Strategic action selection with consequences
- **Dodge/Counter**: Timing-based defensive mechanics
- **Status Effects**: Buffs, debuffs, and ongoing effects
- **Transformation**: Special modes like "Ultra Instinct Monkey"

### Story System (`story.py`)
- **Scene Management**: Structured narrative with branching paths
- **Choice Consequences**: Immediate and long-term effects of decisions
- **Exploration**: Location-based discovery and interaction
- **Character Development**: Story choices shape personality traits

### Relationship System (`npcs.py`)
- **Dynamic Dialogue**: Conversation changes based on relationship level
- **Ability Unlocking**: Special techniques through strong bonds
- **Team Combinations**: Powerful combo attacks with trusted allies
- **Personality Matching**: Compatibility affects relationship growth

### Technique System (`cursed_techniques.py`)
- **Comprehensive Library**: 30+ techniques from canon and original content
- **Progressive Unlocking**: Level and trait-based availability
- **Special Effects**: Unique mechanics for different technique types
- **Domain Expansions**: Ultimate abilities for advanced players

## 🎲 Gameplay Flow

1. **Enhanced Character Creation**: Comprehensive character building with backgrounds, personality assessment, appearance customization, and relationship preferences
2. **Story Progression**: Make choices that shape your personality, relationships, and available story paths
3. **Side Quest System**: Engage in character-specific quests that deepen relationships and unlock unique content
4. **Combat Encounters**: Strategic turn-based battles with cursed spirits and enhanced enemies
5. **Story-Driven Growth**: Gain experience and unlock techniques through meaningful story events and character bonds
6. **Relationship Building**: Interact with NPCs through multiple contexts (casual, training, missions) to unlock special abilities
7. **Sukuna Encounters**: Navigate complex interactions with the King of Curses and make crucial moral decisions
8. **Story Branches**: Experience dramatically different outcomes based on your character development and choices

## 🔧 Customization and Extension

The modular design allows for easy expansion:

- **New Techniques**: Add to `cursed_techniques.py` technique library or implement story-based learning in `character.py`
- **Additional NPCs**: Extend the NPC system in `npcs.py` with new characters and relationship dynamics
- **Story Content**: Add new scenes and choices in `story.py`, including complex branching narratives
- **Side Quests**: Create new character development quests in `side_quests.py`
- **Combat Mechanics**: Enhance the combat system in `combat.py` with new enemy types and abilities
- **Character Backgrounds**: Add new backgrounds and personality options in `character_creation.py`

### Testing New Features
Run the comprehensive demo to see all enhancements:
```bash
python3 enhanced_demo.py
```

## 💾 Save System

- **Automatic Saves**: Progress saved every 5 chapters
- **Manual Saves**: Save anytime from the game menu
- **Persistent Data**: Character stats, relationships, story progress, and inventory
- **Cross-Session**: Resume your adventure exactly where you left off

## 🎨 Sample Gameplay

```
=== MAIN MENU ===
1. New Game
2. Load Game
3. Exit

Enter your choice (1-3): 1

=== NEW GAME ===
Creating your sorcerer...
Enter your character's name: Akira

Welcome, Akira!
Your journey as a Jujutsu Sorcerer begins...

📖 Arrival at Tokyo Jujutsu High
==================================================
You arrive at Tokyo Jujutsu High as a new first-year student...

What would you like to do?
1. Help the injured student immediately
2. Assess the situation carefully first
3. Charge in to fight the curse immediately
```

## 🤝 Contributing

This is a foundational implementation designed for expansion. Feel free to:
- Add new cursed techniques and abilities
- Expand the story with additional scenes and choices
- Implement new NPCs and relationship dynamics
- Enhance combat mechanics and status effects

## 📜 License

This project is for educational and entertainment purposes, inspired by the Jujutsu Kaisen manga and anime series.