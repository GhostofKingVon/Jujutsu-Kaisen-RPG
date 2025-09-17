# Jujutsu Kaisen RPG

A turn-based RPG built in Python following the Jujutsu Kaisen manga storyline with player choice-driven narrative, strategic combat, and character relationship dynamics.

## 🎮 Game Features

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

### Cursed Techniques and Abilities
- **Canon Techniques**: Black Flash, Limitless series, Divine Dogs, Boogie Woogie, and more
- **Original Techniques**: Wukong techniques, Ultra Instinct abilities, and unique combinations
- **Technique Progression**: Unlock new abilities through leveling, relationships, and story progress
- **Domain Expansions**: Ultimate techniques available at high levels

### Relationship System
- **Dynamic NPCs**: Yuji, Megumi, Nobara, Todo, Gojo, and other canon characters
- **Relationship Levels**: From strangers to unbreakable bonds
- **Team Combinations**: Unlock special combo attacks through strong friendships
- **Personality Compatibility**: Shared traits improve relationship growth

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
├── combat.py            # Turn-based combat system with strategic elements
├── cursed_techniques.py # Cursed technique library and effects
├── story.py             # Story progression and exploration system (dynamic arc loader)
├── story1.py            # Arc 1: Introduction Arc - Tokyo Jujutsu High Beginnings
├── story2.py            # Arc 2: Vs. Mahito/Junpei Arc - The Nature of Humanity
├── story3.py            # Arc 3: Kyoto Exchange Event Arc - Rivalry and Growth
├── npcs.py              # NPC interactions and relationship management
├── demo.py              # Demonstration script for all systems
├── story_demo.py        # Expanded story system demonstration
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

### Story System (`story.py` + Arc Files)
- **Dynamic Arc Loading**: Modular story system with separate files for each major arc
- **Rich Branching Narratives**: 30+ detailed scenes with multiple paths and outcomes
- **Character Development**: Deep relationship building and trait-based story progression
- **Multiple Endings**: Different outcomes based on player choices and character growth
- **Replayability**: Extensive branching paths encourage multiple playthroughs

**Available Story Arcs:**
- **Arc 1**: Introduction Arc - Arrival at Tokyo Jujutsu High (9 scenes)
- **Arc 2**: Vs. Mahito/Junpei Arc - The Nature of Humanity (11 scenes)  
- **Arc 3**: Kyoto Exchange Event Arc - Rivalry and Growth (10 scenes)

Each arc contains 700-900+ lines of detailed storytelling with:
- Multiple investigation and interaction approaches
- Complex moral choices with meaningful consequences
- Character specialization paths (combat, support, healing)
- Relationship dynamics that influence story progression
- Optional side content and exploration sequences

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

1. **Character Creation**: Name your sorcerer and begin at Tokyo Jujutsu High
2. **Story Progression**: Make choices that shape your personality and relationships
3. **Combat Encounters**: Strategic turn-based battles with cursed spirits
4. **Character Growth**: Gain experience, level up, and unlock new abilities
5. **Relationship Building**: Interact with NPCs to unlock special abilities
6. **Story Branches**: Experience different outcomes based on your choices

## 🔧 Customization and Extension

The modular design allows for easy expansion:

- **New Techniques**: Add to `cursed_techniques.py` technique library
- **Additional NPCs**: Extend the NPC system in `npcs.py`
- **Story Content**: Add new scenes and arcs by creating new story files (story4.py, story5.py, etc.)
- **Combat Mechanics**: Enhance the combat system in `combat.py`
- **Character Development**: Expand trait systems and progression mechanics

**Story Arc Development**: The new modular story system makes it easy to add new arcs:
1. Create a new story file (e.g., `story4.py`)
2. Implement the `get_arc4_scenes()` function returning a scene dictionary
3. The system will automatically load and integrate the new content

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