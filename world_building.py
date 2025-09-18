"""
Enhanced World Building System

Expands the in-game world with more locations, hidden areas, interactive elements,
world events, and rich lore content.
"""

from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
import random
from datetime import datetime


class LocationType(Enum):
    """Types of locations in the world."""
    SCHOOL = "school"
    URBAN = "urban"
    SHRINE = "shrine"
    FOREST = "forest"
    UNDERGROUND = "underground"
    DOMAIN = "domain"
    HIDDEN = "hidden"


class WorldEventType(Enum):
    """Types of world events that can occur."""
    CURSE_OUTBREAK = "curse_outbreak"
    RIVAL_CHALLENGE = "rival_challenge"
    ALLIANCE_OFFER = "alliance_offer"
    ANCIENT_DISCOVERY = "ancient_discovery"
    POLITICAL_SHIFT = "political_shift"
    NATURAL_PHENOMENON = "natural_phenomenon"


class Location:
    """Enhanced location with interactive elements and secrets."""
    
    def __init__(self, name: str, description: str, location_type: LocationType):
        self.name = name
        self.description = description
        self.location_type = location_type
        self.areas: Dict[str, Dict[str, Any]] = {}
        self.npcs: List[str] = []
        self.secrets: List[Dict[str, Any]] = []
        self.artifacts: List[Dict[str, Any]] = []
        self.environmental_effects: List[str] = []
        self.accessibility_requirements: Dict[str, Any] = {}
        self.visited = False
        self.exploration_progress = 0  # 0-100%
        self.hidden_areas_found = []
        self.lore_fragments = []
    
    def add_area(self, area_name: str, area_data: Dict[str, Any]):
        """Add a sub-area to this location."""
        self.areas[area_name] = area_data
    
    def add_secret(self, secret_type: str, content: Dict[str, Any]):
        """Add a secret to be discovered."""
        secret = {
            "type": secret_type,
            "content": content,
            "discovered": False,
            "requirements": content.get("requirements", {})
        }
        self.secrets.append(secret)
    
    def discover_secret(self, secret_index: int) -> Optional[Dict[str, Any]]:
        """Discover a secret if requirements are met."""
        if 0 <= secret_index < len(self.secrets):
            secret = self.secrets[secret_index]
            if not secret["discovered"]:
                secret["discovered"] = True
                return secret["content"]
        return None
    
    def add_artifact(self, name: str, description: str, power: str, rarity: str):
        """Add a discoverable artifact."""
        artifact = {
            "name": name,
            "description": description,
            "power": power,
            "rarity": rarity,
            "discovered": False
        }
        self.artifacts.append(artifact)
    
    def explore_area(self, area_name: str, character_traits: List) -> Dict[str, Any]:
        """Explore a specific area of the location."""
        if area_name not in self.areas:
            return {"success": False, "message": "Area not found"}
        
        area = self.areas[area_name]
        
        # Check if exploration reveals something new
        discovery_chance = 30
        
        # Trait bonuses for exploration
        from character import Trait
        for trait in character_traits:
            if trait == Trait.ANALYTICAL:
                discovery_chance += 20
            elif trait == Trait.CAUTIOUS:
                discovery_chance += 15
            elif trait == Trait.FOCUSED:
                discovery_chance += 10
        
        results = {"success": True, "discoveries": [], "experience": 10}
        
        if random.randint(1, 100) <= discovery_chance:
            # Found something!
            discovery_type = random.choice(["lore", "item", "secret_passage", "npc_interaction"])
            
            if discovery_type == "lore":
                lore_fragment = self._generate_lore_fragment()
                self.lore_fragments.append(lore_fragment)
                results["discoveries"].append({"type": "lore", "content": lore_fragment})
            
            elif discovery_type == "item":
                item = self._generate_random_item()
                results["discoveries"].append({"type": "item", "content": item})
            
            elif discovery_type == "secret_passage":
                if area_name not in self.hidden_areas_found:
                    self.hidden_areas_found.append(area_name)
                    results["discoveries"].append({"type": "secret_passage", "area": area_name})
            
            elif discovery_type == "npc_interaction":
                npc = self._generate_random_encounter()
                results["discoveries"].append({"type": "encounter", "content": npc})
        
        self.exploration_progress = min(100, self.exploration_progress + 5)
        results["exploration_progress"] = self.exploration_progress
        
        return results
    
    def _generate_lore_fragment(self) -> Dict[str, Any]:
        """Generate a lore fragment for discovery."""
        lore_fragments = {
            LocationType.SCHOOL: [
                {"title": "School History", "content": "Ancient wards protect this institution from the strongest curses."},
                {"title": "Student Records", "content": "Many legendary sorcerers once walked these halls."},
                {"title": "Hidden Teachings", "content": "Secret techniques are taught to only the most promising students."}
            ],
            LocationType.URBAN: [
                {"title": "City Legends", "content": "This district was once the site of a great curse battle."},
                {"title": "Urban Spirits", "content": "Modern curses adapt to technology in unexpected ways."},
                {"title": "Hidden Shrines", "content": "Ancient protection symbols still ward certain buildings."}
            ],
            LocationType.SHRINE: [
                {"title": "Sacred History", "content": "This shrine has been protecting the area for over 1000 years."},
                {"title": "Ritual Knowledge", "content": "Specific ceremonies can enhance cursed energy flow."},
                {"title": "Divine Protection", "content": "The kami of this place watches over worthy sorcerers."}
            ],
            LocationType.UNDERGROUND: [
                {"title": "Hidden Networks", "content": "These tunnels connect to many important locations."},
                {"title": "Ancient Seals", "content": "Powerful curses were once imprisoned here."},
                {"title": "Lost Civilization", "content": "Pre-modern sorcerers built these chambers for training."}
            ]
        }
        
        fragments = lore_fragments.get(self.location_type, [{"title": "Mystery", "content": "Strange energies linger here."}])
        return random.choice(fragments)
    
    def _generate_random_item(self) -> Dict[str, Any]:
        """Generate a random item discovery."""
        items = [
            {"name": "Cursed Tool Fragment", "description": "A piece of a broken cursed tool", "value": "crafting"},
            {"name": "Ancient Scroll", "description": "Contains hints about forgotten techniques", "value": "knowledge"},
            {"name": "Spirit Charm", "description": "Provides minor protection against curses", "value": "protection"},
            {"name": "Energy Crystal", "description": "Restores cursed energy when used", "value": "recovery"},
            {"name": "Historical Document", "description": "Reveals secrets about this location", "value": "lore"}
        ]
        return random.choice(items)
    
    def _generate_random_encounter(self) -> Dict[str, Any]:
        """Generate a random NPC encounter."""
        encounters = [
            {"name": "Wandering Monk", "type": "wisdom", "dialogue": "The path of enlightenment requires understanding both light and shadow."},
            {"name": "Former Student", "type": "information", "dialogue": "I remember when this place was different... more dangerous."},
            {"name": "Spirit Guardian", "type": "challenge", "dialogue": "Prove your worth to proceed further."},
            {"name": "Local Historian", "type": "lore", "dialogue": "Let me tell you about the true history of this place..."}
        ]
        return random.choice(encounters)


class WorldEvent:
    """Dynamic world events that evolve based on player decisions."""
    
    def __init__(self, event_type: WorldEventType, name: str, description: str, duration: int):
        self.event_type = event_type
        self.name = name
        self.description = description
        self.duration = duration  # Days the event lasts
        self.start_date = datetime.now()
        self.is_active = True
        self.player_responses = []
        self.consequences = []
        self.affected_locations = []
        self.reputation_changes = {}
    
    def add_consequence(self, description: str, effect: Dict[str, Any]):
        """Add a consequence of player actions during this event."""
        consequence = {
            "description": description,
            "effect": effect,
            "timestamp": datetime.now()
        }
        self.consequences.append(consequence)
    
    def process_player_response(self, response: str, character) -> Dict[str, Any]:
        """Process player response to the event."""
        self.player_responses.append(response)
        
        # Event-specific response handling
        if self.event_type == WorldEventType.CURSE_OUTBREAK:
            return self._handle_curse_outbreak_response(response, character)
        elif self.event_type == WorldEventType.RIVAL_CHALLENGE:
            return self._handle_rival_challenge_response(response, character)
        elif self.event_type == WorldEventType.ALLIANCE_OFFER:
            return self._handle_alliance_offer_response(response, character)
        # Add more event types as needed
        
        return {"success": True, "message": "Response recorded"}
    
    def _handle_curse_outbreak_response(self, response: str, character) -> Dict[str, Any]:
        """Handle response to curse outbreak event."""
        if response == "investigate":
            character.update_reputation("jujutsu_society", 5)
            character.update_morality("help_innocent", 1)
            self.add_consequence("Investigated the outbreak", {"experience": 50, "reputation": 5})
            return {"success": True, "message": "Your investigation helps contain the outbreak"}
        
        elif response == "evacuate_civilians":
            character.update_reputation("civilians", 10)
            character.update_morality("help_innocent", 2)
            self.add_consequence("Saved civilians", {"experience": 30, "reputation": 10})
            return {"success": True, "message": "Civilians safely evacuated"}
        
        elif response == "ignore":
            character.update_reputation("jujutsu_society", -5)
            character.update_morality("harm_innocent", 1)
            self.add_consequence("Ignored the crisis", {"reputation": -5})
            return {"success": False, "message": "The situation worsens without intervention"}
        
        return {"success": True, "message": "Response recorded"}
    
    def _handle_rival_challenge_response(self, response: str, character) -> Dict[str, Any]:
        """Handle response to rival challenge."""
        if response == "accept_honorably":
            character.update_morality("uphold_justice", 1)
            return {"success": True, "message": "An honorable duel is arranged", "combat": True}
        
        elif response == "decline_respectfully":
            character.update_morality("show_mercy", 1)
            return {"success": True, "message": "Your restraint is noted"}
        
        elif response == "provoke":
            character.update_morality("seek_revenge", 1)
            return {"success": True, "message": "The rivalry intensifies", "combat": True, "difficulty": "hard"}
        
        return {"success": True, "message": "Response recorded"}
    
    def _handle_alliance_offer_response(self, response: str, character) -> Dict[str, Any]:
        """Handle response to alliance offer."""
        if response == "accept":
            character.update_morality("uphold_justice", 1)
            character.update_reputation("students", 10)
            return {"success": True, "message": "Alliance formed successfully", "alliance": True}
        
        elif response == "negotiate":
            character.update_morality("follow_rules", 1)
            return {"success": True, "message": "Terms under negotiation", "pending": True}
        
        elif response == "decline":
            return {"success": True, "message": "Alliance declined"}
        
        return {"success": True, "message": "Response recorded"}


class LoreLibrary:
    """Comprehensive lore and world-building content."""
    
    def __init__(self):
        self.artifacts = {}
        self.historical_events = {}
        self.character_backgrounds = {}
        self.world_mysteries = {}
        self.discovered_lore = []
        self._initialize_lore()
    
    def _initialize_lore(self):
        """Initialize the lore library with rich content."""
        # Artifacts
        self.artifacts = {
            "ancient_seal": {
                "name": "Ancient Binding Seal",
                "description": "A powerful seal used to contain the strongest curses",
                "history": "Created by master sorcerers 500 years ago during the Great Curse War",
                "power": "Can temporarily bind Grade 1 curses",
                "location_hint": "Hidden in the depths of Tokyo Jujutsu High"
            },
            "founders_scroll": {
                "name": "Founder's Teaching Scroll",
                "description": "Contains the original principles of Jujutsu Sorcery",
                "history": "Written by the founder of modern Jujutsu education",
                "power": "Grants insight into advanced techniques",
                "location_hint": "Sealed in the main library's secret section"
            },
            "monkey_kings_staff": {
                "name": "Replica of the Monkey King's Staff",
                "description": "A cursed tool inspired by the legendary Ruyi Jingu Bang",
                "history": "Crafted by a sorcerer who studied ancient Chinese legends",
                "power": "Extends and contracts at will, devastating reach",
                "location_hint": "Lost in the underground training chambers"
            }
        }
        
        # Historical Events
        self.historical_events = {
            "great_curse_war": {
                "name": "The Great Curse War",
                "period": "500 years ago",
                "description": "A devastating conflict between sorcerers and an army of special grade curses",
                "key_figures": ["Master Tengen", "Ancient Clan Leaders"],
                "outcome": "Sorcerers victory, but at great cost",
                "lasting_effects": "Established modern Jujutsu hierarchy and barrier techniques"
            },
            "meiji_restoration_curses": {
                "name": "Meiji Era Curse Surge",
                "period": "1868-1912",
                "description": "Rapid modernization led to new types of curses emerging",
                "key_figures": ["Modernist Sorcerers", "Traditional Clan Elders"],
                "outcome": "Adaptation of ancient techniques to modern world",
                "lasting_effects": "Foundation of current sorcerer education system"
            }
        }
        
        # World Mysteries
        self.world_mysteries = {
            "vanishing_sorcerers": {
                "name": "The Vanishing Sorcerers",
                "description": "Several powerful sorcerers disappeared without a trace 20 years ago",
                "clues": ["Last seen investigating ancient curse sites", "Left behind cryptic messages"],
                "theories": ["Discovered something too dangerous", "Transported to another realm"],
                "investigation_status": "Open"
            },
            "origin_of_curses": {
                "name": "The True Origin of Cursed Spirits",
                "description": "Despite common knowledge, the true origin of curses remains mysterious",
                "clues": ["Ancient texts suggest curses existed before human emotions", "Pre-historic curse sites"],
                "theories": ["Primordial entities", "Interdimensional beings", "Natural world phenomena"],
                "investigation_status": "Highly classified"
            }
        }
    
    def discover_lore(self, lore_type: str, lore_id: str) -> Optional[Dict[str, Any]]:
        """Discover a piece of lore."""
        lore_libraries = {
            "artifact": self.artifacts,
            "event": self.historical_events,
            "mystery": self.world_mysteries
        }
        
        if lore_type in lore_libraries and lore_id in lore_libraries[lore_type]:
            lore_piece = lore_libraries[lore_type][lore_id]
            
            discovery_entry = {
                "type": lore_type,
                "id": lore_id,
                "content": lore_piece,
                "discovered_date": datetime.now()
            }
            
            self.discovered_lore.append(discovery_entry)
            return lore_piece
        
        return None
    
    def get_lore_summary(self) -> str:
        """Get a summary of discovered lore."""
        if not self.discovered_lore:
            return "No lore discovered yet. Explore the world to uncover its secrets."
        
        summary = []
        for category in ["artifact", "event", "mystery"]:
            category_lore = [l for l in self.discovered_lore if l["type"] == category]
            if category_lore:
                summary.append(f"{category.title()}s discovered: {len(category_lore)}")
        
        return " | ".join(summary)


class WorldManager:
    """Manages the overall world state, events, and progression."""
    
    def __init__(self):
        self.locations: Dict[str, Location] = {}
        self.active_events: List[WorldEvent] = []
        self.completed_events: List[WorldEvent] = []
        self.lore_library = LoreLibrary()
        self.world_state = {}
        self.day_count = 1
        
        self._initialize_world()
    
    def _initialize_world(self):
        """Initialize the world with enhanced locations."""
        # Tokyo Jujutsu High (Enhanced)
        tokyo_high = Location("Tokyo Jujutsu High", 
                            "Premier institution for training Jujutsu Sorcerers", 
                            LocationType.SCHOOL)
        
        tokyo_high.add_area("hidden_library", {
            "description": "Secret library containing forbidden knowledge",
            "requirements": {"trait": "analytical", "level": 10},
            "secrets": ["ancient_techniques", "curse_origins"]
        })
        
        tokyo_high.add_area("underground_training", {
            "description": "Secret training chambers beneath the school",
            "requirements": {"relationship": {"gojo": 50}},
            "secrets": ["legendary_weapons", "master_techniques"]
        })
        
        tokyo_high.add_secret("hidden_passage", {
            "description": "A secret passage connecting to underground Tokyo",
            "requirements": {"exploration": 75},
            "reward": {"location_access": "underground_tokyo"}
        })
        
        self.locations["tokyo_jujutsu_high"] = tokyo_high
        
        # Shibuya District (Enhanced)
        shibuya = Location("Shibuya District", 
                         "Dense urban area prone to curse manifestations", 
                         LocationType.URBAN)
        
        shibuya.add_area("abandoned_subway", {
            "description": "Abandoned subway tunnels filled with curses",
            "requirements": {"level": 15},
            "secrets": ["curse_nest", "ancient_artifacts"]
        })
        
        shibuya.add_area("rooftop_network", {
            "description": "Network of rooftops offering strategic advantages",
            "requirements": {"trait": "focused"},
            "secrets": ["observation_points", "escape_routes"]
        })
        
        self.locations["shibuya_district"] = shibuya
        
        # New Locations
        # Hidden Shrine
        hidden_shrine = Location("Tengu Mountain Shrine", 
                                "Ancient shrine protected by supernatural guardians", 
                                LocationType.SHRINE)
        
        hidden_shrine.add_area("inner_sanctum", {
            "description": "Sacred space where time flows differently",
            "requirements": {"moral_alignment": "good", "level": 20},
            "secrets": ["time_manipulation", "divine_techniques"]
        })
        
        self.locations["tengu_shrine"] = hidden_shrine
        
        # Underground Network
        underground = Location("Underground Tokyo", 
                             "Vast network of tunnels and hidden chambers", 
                             LocationType.UNDERGROUND)
        
        underground.add_area("ancient_chambers", {
            "description": "Pre-modern training and ritual chambers",
            "requirements": {"lore_knowledge": 5},
            "secrets": ["ancient_seals", "forgotten_techniques"]
        })
        
        self.locations["underground_tokyo"] = underground
    
    def trigger_world_event(self, event_type: WorldEventType, 
                           player_level: int, player_reputation: Dict[str, int]) -> Optional[WorldEvent]:
        """Trigger a world event based on game state."""
        event_templates = {
            WorldEventType.CURSE_OUTBREAK: {
                "name": "Curse Outbreak in Residential District",
                "description": "Multiple curses have appeared simultaneously in a civilian area",
                "duration": 3,
                "level_requirement": 5
            },
            WorldEventType.RIVAL_CHALLENGE: {
                "name": "Challenge from Kyoto School",
                "description": "A rival student from Kyoto School has issued a formal challenge",
                "duration": 1,
                "level_requirement": 10
            },
            WorldEventType.ALLIANCE_OFFER: {
                "name": "Proposal for Inter-School Alliance",
                "description": "Tokyo and Kyoto schools consider forming a stronger alliance",
                "duration": 7,
                "level_requirement": 15
            }
        }
        
        if event_type in event_templates:
            template = event_templates[event_type]
            
            # Check if player meets requirements
            if player_level >= template["level_requirement"]:
                event = WorldEvent(event_type, template["name"], 
                                 template["description"], template["duration"])
                
                self.active_events.append(event)
                return event
        
        return None
    
    def advance_day(self):
        """Advance world state by one day."""
        self.day_count += 1
        
        # Process active events
        events_to_complete = []
        for event in self.active_events:
            event.duration -= 1
            if event.duration <= 0:
                event.is_active = False
                events_to_complete.append(event)
        
        # Move completed events
        for event in events_to_complete:
            self.active_events.remove(event)
            self.completed_events.append(event)
        
        # Chance for new events
        if random.randint(1, 100) <= 15:  # 15% chance per day
            self._generate_random_event()
    
    def _generate_random_event(self):
        """Generate a random world event."""
        event_types = list(WorldEventType)
        event_type = random.choice(event_types)
        
        # Generate based on current world state
        # This is a simplified version - could be much more complex
        if event_type == WorldEventType.CURSE_OUTBREAK:
            return self.trigger_world_event(event_type, 1, {})
    
    def get_world_status(self) -> Dict[str, Any]:
        """Get current world status summary."""
        return {
            "day": self.day_count,
            "active_events": len(self.active_events),
            "locations_discovered": len([l for l in self.locations.values() if l.visited]),
            "total_locations": len(self.locations),
            "lore_pieces": len(self.lore_library.discovered_lore)
        }