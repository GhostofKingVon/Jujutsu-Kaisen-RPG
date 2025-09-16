# Jujutsu Kaisen RPG

A comprehensive turn-based RPG built in Python following the Jujutsu Kaisen manga storyline with enhanced character creation, strategic combat, deep character relationships, and a dynamic morality system.

## 🎮 Enhanced Game Features

### Advanced Character Creation System
- **Detailed Appearance Customization**: Hair color, eye color, height, build, and distinguishing features
- **Background Selection**: Choose from 6 different origins that affect your story and relationships
- **Personality Trait Selection**: Pick 3 dominant traits from 8 options that shape your character
- **Starting Cursed Technique**: Select from multiple technique paths with unique progression routes
- **Morality System**: Dynamic alignment based on choices affecting relationships and story outcomes

### Turn-Based Combat System
- **Combat Actions**: Attack, use cursed techniques (CTs), dodge, guard, or flee
- **Dodge Mechanics**: Prepare to dodge incoming attacks and trigger counters
- **Ultra Instinct System**: Special transformation abilities that enhance dodge chance and counter damage
- **Multi-Phase Boss Battles**: Bosses transition through phases with unique abilities and taunts
- **Strategic Elements**: Status effects, cooldowns, and energy management
- **Enhanced Combat**: Dynamic dialogue, emotional cutscenes, and environmental interactions

### Manga-Accurate Story System
- **Canon Storyline**: Follows major Jujutsu Kaisen manga arcs with player choice deviations
- **Story Arcs**: Introduction → Fearsome Womb → Kyoto Goodwill Event → Shibuya Incident → Culling Game
- **Branching Narrative**: Decisions affect story progression and character relationships
- **Character Development Moments**: Key scenes from the manga with player involvement
- **Major Battles**: Canonical fights with dramatic story impact

### Enhanced Character Interactions
- **6 Major NPCs**: Yuji, Megumi, Nobara, Gojo, Sukuna, and Todo with deep personality systems
- **Dynamic Dialogue**: Conversation changes based on relationship level and player traits
- **Relationship Consequences**: Strong bonds unlock special abilities and story branches
- **Personality Compatibility**: Shared traits improve relationship growth rates
- **Teaching System**: Learn techniques from NPCs based on relationship strength

### Expanded Cursed Techniques System (42+ Techniques)
- **Canon Technique Lines**: 
  - Yuji Line: Divergent Fist → Black Flash mastery
  - Megumi Line: Ten Shadows with all shikigami
  - Gojo Line: Limitless techniques including Hollow Purple
  - Nobara Line: Straw Doll technique and Resonance
  - Inumaki Line: Cursed Speech variations
- **Domain Expansions**: Ultimate techniques for advanced players
- **Original Techniques**: Wukong-inspired abilities and Ultra Instinct transformations
- **Reverse Cursed Technique**: Healing abilities for advanced sorcerers
- **Technique Progression**: Unlock advanced abilities through story progress and relationships

### Morality and Choice System
- **Four Morality Aspects**: Altruism, Pragmatism, Justice, and Mercy
- **Dynamic Alignment**: Character alignment evolves based on choices
- **Choice Consequences**: Immediate and long-term effects on story and relationships
- **Ending Variations**: Multiple story outcomes based on moral choices

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

### Enhanced Demo
To see all enhanced systems in action without playing:
```bash
python3 enhanced_demo.py
```

## 📁 Enhanced File Structure

```
Jujutsu-Kaisen-RPG/
├── main.py                    # Main game entry point with enhanced features
├── character_creation.py      # NEW: Advanced character creation system
├── manga_story.py            # NEW: Manga-accurate story progression
├── enhanced_npcs.py          # NEW: Deep NPC personality system
├── story_enhanced.py         # Enhanced story management
├── game_state.py             # Game state management and save/load system
├── character.py              # Enhanced character classes with new attributes
├── combat.py                 # Turn-based combat with enhanced mechanics
├── cursed_techniques.py      # Expanded technique library (42+ techniques)
├── story.py                  # Original story system (backup)
├── npcs.py                   # Original NPC system (backup)
├── enhanced_demo.py          # NEW: Comprehensive feature demonstration
├── demo.py                   # Original system demonstration
└── README.md                 # This enhanced documentation
```

## 🎯 Enhanced Core Systems

### Character Creation System (`character_creation.py`)
- **CharacterCreator**: Interactive character creation with all customization options
- **MoralitySystem**: Dynamic morality tracking affecting story outcomes
- **Background Origins**: Six different backstories affecting starting relationships
- **Appearance System**: Detailed physical customization options
- **Starting Technique Selection**: Multiple cursed technique paths with progression

### Enhanced Story System (`manga_story.py`, `story_enhanced.py`)
- **MangaStoryManager**: Manga-accurate story progression with major arcs
- **Choice Consequences**: Advanced consequence system affecting multiple game aspects
- **Character Development**: Key manga moments integrated with player choices
- **Story Branches**: Multiple paths based on player decisions and morality

### Enhanced NPC System (`enhanced_npcs.py`)
- **MangaNPC**: Deep personality-based NPC interactions
- **Relationship Effects**: Unlockable abilities and story content through bonds
- **Teaching System**: Learn canonical techniques from appropriate characters
- **Personality Compatibility**: Relationship growth based on shared traits

### Expanded Technique System (`cursed_techniques.py`)
- **42+ Techniques**: Comprehensive library from basic to Domain Expansion level
- **Canon Accuracy**: Techniques from major manga characters with proper mechanics
- **Progression Paths**: Logical advancement through related technique families
- **Special Mechanics**: Unique effects for different technique types

## 🎲 Enhanced Gameplay Flow

1. **Advanced Character Creation**: Customize appearance, select background, choose personality traits, and pick starting technique
2. **Manga Story Progression**: Experience key events from the Jujutsu Kaisen manga with your personal influence
3. **Deep Character Interactions**: Build relationships with canonical characters through personality-based interactions
4. **Strategic Combat**: Enhanced turn-based battles with emotional story beats and dynamic dialogue
5. **Moral Choices**: Make decisions that shape your character's alignment and affect story outcomes
6. **Technique Mastery**: Progress through canonical technique lines by building relationships and making story choices
7. **Multiple Endings**: Experience different story conclusions based on relationships, morality, and choices

## 🔧 Customization and Extension

The enhanced modular design allows for extensive expansion:

- **New Techniques**: Add to the comprehensive technique library with proper progression paths
- **Additional NPCs**: Extend the personality-based NPC system with new characters
- **Story Content**: Add new manga arcs or original story branches
- **Combat Mechanics**: Enhance battle system with new special abilities
- **Character Backgrounds**: Create new origin stories with unique effects

## 💾 Enhanced Save System

- **Comprehensive Data**: Saves appearance, background, morality, relationships, and technique progress
- **Story Progress**: Maintains manga arc progression and choice consequences
- **Character Development**: Preserves personality evolution and NPC relationship states
- **Cross-Session Continuity**: Resume with all enhanced features intact

## 🎨 Sample Enhanced Gameplay

```
=== ENHANCED CHARACTER CREATION ===
Creating your unique Jujutsu Sorcerer...

Enter your character's name: Akira

--- APPEARANCE CUSTOMIZATION ---
Choose your hair color:
1. Black  2. Brown  3. Blonde  4. White
5. Red    6. Blue   7. Pink    8. Green

--- CHARACTER BACKGROUND ---
Choose your origin story:
1. Tokyo Native - Born and raised in Tokyo, familiar with urban curse activity
2. Countryside Family - From a rural sorcerer family with traditional techniques
3. Curse Victim Survivor - Survived a curse attack, awakening your abilities
4. Sorcerer Family Legacy - Born into a prominent sorcerer family
5. Ordinary Awakening - Regular person who suddenly developed cursed energy
6. Tragic Incident - Lost loved ones to curses, driving your desire for power

--- PERSONALITY TRAITS ---
Choose 3 dominant traits:
1. Compassionate - Deeply caring for others, even enemies
2. Focused - Maintains concentration and strategic thinking
3. Aggressive - Direct confrontation and overwhelming force
4. Protective - Shields others from harm at personal cost
5. Analytical - Studies situations and enemies methodically
6. Reckless - Acts on instinct without considering consequences
7. Determined - Never gives up, pushes through adversity
8. Cautious - Careful planning and risk assessment

--- STARTING CURSED TECHNIQUE ---
Choose your initial technique path:
1. Divergent Fist Path - Master delayed cursed energy leading to Black Flash
2. Ten Shadows Path - Control shadows and summon shikigami
3. Cursed Speech Path - Develop reality-altering vocal techniques
4. Construction Path - Master cursed tool creation and manipulation
5. Pure Energy Path - Shape raw cursed energy into unique techniques
```

## 🌟 New Features Highlights

### Character Creation Enhancements
- **Visual Customization**: Complete appearance control
- **Meaningful Backgrounds**: 6 origins affecting gameplay
- **Personality Selection**: Traits that actually impact story
- **Technique Paths**: Starting choice affects entire progression
- **Morality Foundation**: Alignment system from character creation

### Story Integration
- **Manga Accuracy**: Follows official storyline with player agency
- **Character Moments**: Experience key development scenes
- **Choice Impact**: Decisions have lasting consequences
- **Relationship Depth**: Build meaningful bonds with canonical characters

### Combat Evolution
- **Enhanced Mechanics**: More strategic and story-integrated
- **Emotional Beats**: Technique awakenings with dramatic impact
- **Dynamic Dialogue**: Characters react based on relationships
- **Environmental Integration**: Location affects combat options

### Technique Mastery
- **42+ Techniques**: Comprehensive canonical and original abilities
- **Logical Progression**: Techniques build upon each other
- **Relationship Unlocks**: Learn from appropriate mentors
- **Domain Expansions**: Ultimate techniques for masters

## 🤝 Contributing

This enhanced implementation provides a solid foundation for further expansion. Feel free to:
- Add new manga arcs and story content
- Expand the technique library with additional canonical abilities
- Implement new NPCs with the personality-based interaction system
- Create additional character backgrounds and their unique effects
- Enhance combat mechanics with new strategic elements

## 📜 License

This project is for educational and entertainment purposes, inspired by the Jujutsu Kaisen manga and anime series by Gege Akutami.