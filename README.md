# Jujutsu Kaisen RPG

A turn-based RPG built in Python following the Jujutsu Kaisen manga storyline with player choice-driven narrative, strategic combat, and character relationship dynamics.

## 🎮 Game Features

### Enhanced Combat System
- **Combat Actions**: Attack, use cursed techniques (CTs), dodge, guard, or flee
- **Combo System**: Chain successful attacks for increasing damage multipliers (up to 3x)
- **Ultimate Techniques**: Powerful moves based on character traits, charged through combat
- **Environmental Combat**: 5 terrain types with tactical interactions and bonus effects
- **Dodge & Counter**: Prepare to dodge incoming attacks and trigger devastating counters
- **Ultra Instinct System**: Special transformation abilities that enhance dodge chance and counter damage
- **Multi-Phase Boss Battles**: Bosses transition through phases with unique abilities and taunts
- **Strategic Elements**: Status effects, cooldowns, and energy management

### Advanced Technique System
- **Technique Mastery**: 5-level progression system improving damage and reducing costs
- **Skill Trees**: Trait-based technique unlocks with prerequisites and upgrade paths
- **Canon Techniques**: Black Flash, Limitless series, Divine Dogs, Boogie Woogie, and more
- **Original Techniques**: Wukong techniques, Ultra Instinct abilities, and unique combinations
- **Technique Fusion**: Advanced combinations unlocked through mastery and relationships
- **Domain Fragments**: Partial domain abilities available at high levels

### Character Development & Progression
- **Dynamic Traits**: Compassionate, Focused, Aggressive, Protective, Analytical, Reckless, Determined, Cautious
- **Trait Evolution**: Traits change based on player decisions and actions throughout the story
- **Personal Missions**: Character-specific questlines that explore backstories and motivations
- **Skill Point System**: Earned through leveling, spent on technique upgrades and new abilities
- **Character Backstory Events**: Interactive narrative events that shape character development
- **Personality Impact**: Dominant traits affect dialogue options, relationship compatibility, and available techniques

### Enhanced Exploration & Discovery
- **Interactive Environments**: Hidden areas, secret training grounds, and spiritual encounters
- **Character Backstory Discovery**: Uncover family history, past trauma, and hidden talents
- **Technique Knowledge**: Find ancient scrolls and training notes that provide gameplay benefits
- **Spiritual Encounters**: Meet benevolent spirits that offer wisdom and character growth
- **Memorial Sites**: Discover locations that honor fallen sorcerers and provide permanent bonuses

### Story and Exploration
- **Canon Storyline**: Follows the Jujutsu Kaisen manga with player choice deviations
- **Branching Narrative**: Decisions affect story progression and character relationships
- **Enhanced Exploration**: Discover hidden paths, collectibles, puzzles, and character development events
- **Multiple Locations**: Tokyo Jujutsu High, Kyoto School, Shibuya District, and secret areas

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
├── story.py             # Story progression and exploration system
├── npcs.py              # NPC interactions and relationship management
├── demo.py              # Demonstration script for all systems
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

## 🎲 Enhanced Gameplay Flow

1. **Character Creation**: Name your sorcerer and begin at Tokyo Jujutsu High
2. **Story Progression**: Make choices that shape your personality and relationships
3. **Combat Encounters**: Strategic turn-based battles with enhanced mechanics
   - Build combos for increasing damage
   - Charge ultimate techniques through successful actions
   - Use environmental interactions tactically
4. **Character Development**: Multi-layered progression system
   - Gain experience and skill points through various activities
   - Master techniques through repeated use
   - Unlock new abilities based on traits and relationships
5. **Personal Missions**: Complete character-specific questlines
   - Explore your character's backstory and motivations
   - Unlock unique abilities and story content
6. **Relationship Building**: Interact with NPCs to unlock special abilities and team techniques
7. **Enhanced Exploration**: Discover hidden areas and character development opportunities
8. **Story Branches**: Experience different outcomes based on your choices and character development

## 🌟 New Features Highlight

### Enhanced Combat Mechanics
- **Combo System**: Chain up to 3 successful actions for 44% damage bonus
- **Ultimate Techniques**: 8 trait-based ultimate moves with unique effects
- **Environmental Combat**: 5 terrain types (Forest, Urban, Shrine, Underground, Rooftop)
- **Tactical Positioning**: Use destructible objects, natural energy, and elevation

### Advanced Character Progression
- **Technique Mastery**: 5-level progression improving damage (+100%) and efficiency (-40% cost)
- **Skill Trees**: 10+ new techniques unlocked through traits and relationships
- **Personal Missions**: 6+ character-specific questlines with meaningful rewards
- **Character Development Events**: Interactive backstory exploration affecting growth

### Quality of Life Improvements
- **Character Development Menu**: Accessible in-game interface for managing progression
- **Enhanced Save System**: Preserves all new progression data
- **Comprehensive Demo**: `enhanced_demo.py` showcases all new features
- **Integrated Systems**: All enhancements work seamlessly with existing gameplay

## 🔧 Customization and Extension

The modular design allows for easy expansion:

- **New Techniques**: Add to `cursed_techniques.py` technique library or character skill trees
- **Additional NPCs**: Extend the NPC system in `npcs.py` with new relationship mechanics
- **Story Content**: Add new scenes, choices, and personal missions in `story.py`
- **Combat Mechanics**: Enhance the combat system in `combat.py` with new environmental effects
- **Character Development**: Extend trait-based progression and backstory events

## 🎮 Running the Enhanced Demo

Experience all the new features:

```bash
python3 enhanced_demo.py
```

This comprehensive demo showcases:
- Enhanced combat with combos and ultimates
- Technique mastery and skill tree systems
- Character development and personal missions
- Enhanced exploration features
- Integrated system demonstration

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