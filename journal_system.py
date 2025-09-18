"""
In-Game Journal System

Tracks quests, lore, character relationships, and player progress.
Provides a comprehensive record of the player's journey.
"""

from typing import Dict, List, Any, Optional
from enum import Enum
from datetime import datetime
import json


class QuestStatus(Enum):
    """Status of quests in the journal."""
    NOT_STARTED = "not_started"
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"
    ABANDONED = "abandoned"


class JournalEntryType(Enum):
    """Types of journal entries."""
    QUEST = "quest"
    LORE = "lore"
    CHARACTER = "character"
    EVENT = "event"
    LOCATION = "location"
    TECHNIQUE = "technique"
    ACHIEVEMENT = "achievement"


class Quest:
    """Individual quest or mission."""
    
    def __init__(self, quest_id: str, title: str, description: str, 
                 objectives: List[str], rewards: Dict[str, Any]):
        self.quest_id = quest_id
        self.title = title
        self.description = description
        self.objectives = objectives
        self.rewards = rewards
        self.status = QuestStatus.NOT_STARTED
        self.progress = 0  # 0-100%
        self.completed_objectives = []
        self.started_date = None
        self.completed_date = None
        self.notes = []
        self.related_npcs = []
        self.related_locations = []
    
    def start_quest(self):
        """Start the quest."""
        self.status = QuestStatus.ACTIVE
        self.started_date = datetime.now()
    
    def complete_objective(self, objective_index: int):
        """Mark an objective as completed."""
        if 0 <= objective_index < len(self.objectives):
            if objective_index not in self.completed_objectives:
                self.completed_objectives.append(objective_index)
                self.progress = (len(self.completed_objectives) / len(self.objectives)) * 100
                
                # Auto-complete quest if all objectives done
                if len(self.completed_objectives) == len(self.objectives):
                    self.complete_quest()
    
    def complete_quest(self):
        """Mark the quest as completed."""
        self.status = QuestStatus.COMPLETED
        self.completed_date = datetime.now()
        self.progress = 100
    
    def fail_quest(self, reason: str = ""):
        """Mark the quest as failed."""
        self.status = QuestStatus.FAILED
        if reason:
            self.notes.append(f"Quest failed: {reason}")
    
    def add_note(self, note: str):
        """Add a note to the quest."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.notes.append(f"[{timestamp}] {note}")
    
    def get_status_summary(self) -> str:
        """Get a summary of quest status."""
        status_emoji = {
            QuestStatus.NOT_STARTED: "⚪",
            QuestStatus.ACTIVE: "🔵",
            QuestStatus.COMPLETED: "✅",
            QuestStatus.FAILED: "❌",
            QuestStatus.ABANDONED: "⚫"
        }
        
        emoji = status_emoji.get(self.status, "❓")
        progress_text = f" ({self.progress:.0f}%)" if self.status == QuestStatus.ACTIVE else ""
        
        return f"{emoji} {self.title}{progress_text}"


class CharacterEntry:
    """Character relationship and information entry."""
    
    def __init__(self, name: str, initial_description: str):
        self.name = name
        self.description = initial_description
        self.relationship_level = 0
        self.relationship_history = []
        self.personality_notes = []
        self.techniques_observed = []
        self.dialogue_history = []
        self.significant_events = []
        self.first_met_date = datetime.now()
        self.last_interaction_date = datetime.now()
    
    def update_relationship(self, change: int, reason: str):
        """Update relationship level with reason."""
        old_level = self.relationship_level
        self.relationship_level += change
        self.relationship_level = max(-100, min(100, self.relationship_level))
        
        entry = {
            "date": datetime.now(),
            "change": change,
            "reason": reason,
            "new_level": self.relationship_level
        }
        self.relationship_history.append(entry)
        self.last_interaction_date = datetime.now()
    
    def add_dialogue(self, dialogue: str, context: str = ""):
        """Record dialogue with this character."""
        entry = {
            "date": datetime.now(),
            "dialogue": dialogue,
            "context": context
        }
        self.dialogue_history.append(entry)
    
    def observe_technique(self, technique_name: str, description: str):
        """Record observation of character's technique."""
        if technique_name not in [t["name"] for t in self.techniques_observed]:
            self.techniques_observed.append({
                "name": technique_name,
                "description": description,
                "observed_date": datetime.now()
            })
    
    def add_personality_note(self, note: str):
        """Add a personality observation."""
        self.personality_notes.append({
            "note": note,
            "date": datetime.now()
        })
    
    def record_significant_event(self, event: str):
        """Record a significant event involving this character."""
        self.significant_events.append({
            "event": event,
            "date": datetime.now()
        })
    
    def get_relationship_status(self) -> str:
        """Get relationship status description."""
        level = self.relationship_level
        
        if level >= 80:
            return "🤝 Close Ally"
        elif level >= 60:
            return "😊 Good Friend"
        elif level >= 40:
            return "👋 Friend"
        elif level >= 20:
            return "🙂 Acquaintance"
        elif level >= 0:
            return "😐 Neutral"
        elif level >= -20:
            return "😒 Dislike"
        elif level >= -40:
            return "😠 Antagonistic"
        else:
            return "⚔️ Enemy"


class LoreEntry:
    """Lore and world-building information entry."""
    
    def __init__(self, title: str, content: str, category: str):
        self.title = title
        self.content = content
        self.category = category
        self.discovered_date = datetime.now()
        self.related_locations = []
        self.related_characters = []
        self.related_quests = []
        self.importance_level = "normal"  # low, normal, high, critical
        self.tags = []
    
    def add_relation(self, relation_type: str, relation_id: str):
        """Add a relation to other journal entries."""
        if relation_type == "location":
            if relation_id not in self.related_locations:
                self.related_locations.append(relation_id)
        elif relation_type == "character":
            if relation_id not in self.related_characters:
                self.related_characters.append(relation_id)
        elif relation_type == "quest":
            if relation_id not in self.related_quests:
                self.related_quests.append(relation_id)
    
    def add_tag(self, tag: str):
        """Add a tag for categorization."""
        if tag not in self.tags:
            self.tags.append(tag)


class GameJournal:
    """Main journal system managing all entries."""
    
    def __init__(self):
        self.quests: Dict[str, Quest] = {}
        self.characters: Dict[str, CharacterEntry] = {}
        self.lore_entries: Dict[str, LoreEntry] = {}
        self.locations_visited: Dict[str, Dict[str, Any]] = {}
        self.techniques_learned: Dict[str, Dict[str, Any]] = {}
        self.achievements: List[Dict[str, Any]] = []
        self.daily_entries: List[Dict[str, Any]] = []
        self.statistics = {
            "start_date": datetime.now(),
            "play_time": 0,
            "battles_won": 0,
            "battles_lost": 0,
            "locations_discovered": 0,
            "techniques_mastered": 0,
            "relationships_formed": 0
        }
    
    def add_quest(self, quest: Quest):
        """Add a new quest to the journal."""
        self.quests[quest.quest_id] = quest
    
    def get_quest(self, quest_id: str) -> Optional[Quest]:
        """Get a quest by ID."""
        return self.quests.get(quest_id)
    
    def update_quest_progress(self, quest_id: str, objective_index: int):
        """Update progress on a quest objective."""
        quest = self.get_quest(quest_id)
        if quest:
            quest.complete_objective(objective_index)
            return True
        return False
    
    def add_character(self, name: str, description: str) -> CharacterEntry:
        """Add a new character entry."""
        if name not in self.characters:
            self.characters[name] = CharacterEntry(name, description)
            self.statistics["relationships_formed"] += 1
        return self.characters[name]
    
    def get_character(self, name: str) -> Optional[CharacterEntry]:
        """Get a character entry."""
        return self.characters.get(name)
    
    def update_character_relationship(self, name: str, change: int, reason: str):
        """Update relationship with a character."""
        character = self.get_character(name)
        if character:
            character.update_relationship(change, reason)
        else:
            # Create new character entry
            character = self.add_character(name, "Encountered character")
            character.update_relationship(change, reason)
    
    def add_lore_entry(self, title: str, content: str, category: str) -> LoreEntry:
        """Add a new lore entry."""
        entry_id = title.lower().replace(" ", "_")
        if entry_id not in self.lore_entries:
            self.lore_entries[entry_id] = LoreEntry(title, content, category)
        return self.lore_entries[entry_id]
    
    def visit_location(self, location_name: str, description: str):
        """Record visiting a location."""
        if location_name not in self.locations_visited:
            self.locations_visited[location_name] = {
                "first_visit": datetime.now(),
                "description": description,
                "visit_count": 1,
                "discoveries": [],
                "last_visit": datetime.now()
            }
            self.statistics["locations_discovered"] += 1
        else:
            self.locations_visited[location_name]["visit_count"] += 1
            self.locations_visited[location_name]["last_visit"] = datetime.now()
    
    def learn_technique(self, technique_name: str, description: str, source: str):
        """Record learning a new technique."""
        if technique_name not in self.techniques_learned:
            self.techniques_learned[technique_name] = {
                "learned_date": datetime.now(),
                "description": description,
                "source": source,
                "times_used": 0,
                "effectiveness": []
            }
            self.statistics["techniques_mastered"] += 1
    
    def use_technique(self, technique_name: str, effectiveness: int):
        """Record using a technique."""
        if technique_name in self.techniques_learned:
            self.techniques_learned[technique_name]["times_used"] += 1
            self.techniques_learned[technique_name]["effectiveness"].append(effectiveness)
    
    def add_achievement(self, title: str, description: str, category: str = "general"):
        """Add an achievement."""
        achievement = {
            "title": title,
            "description": description,
            "category": category,
            "earned_date": datetime.now()
        }
        self.achievements.append(achievement)
    
    def record_battle_result(self, won: bool, enemy_name: str, techniques_used: List[str]):
        """Record the result of a battle."""
        if won:
            self.statistics["battles_won"] += 1
        else:
            self.statistics["battles_lost"] += 1
        
        # Add daily entry
        self.add_daily_entry(
            "battle",
            f"{'Victory against' if won else 'Defeat by'} {enemy_name}",
            {"techniques_used": techniques_used, "result": "victory" if won else "defeat"}
        )
    
    def add_daily_entry(self, entry_type: str, summary: str, details: Dict[str, Any] = None):
        """Add a daily journal entry."""
        entry = {
            "date": datetime.now(),
            "type": entry_type,
            "summary": summary,
            "details": details or {}
        }
        self.daily_entries.append(entry)
    
    def get_active_quests(self) -> List[Quest]:
        """Get all active quests."""
        return [quest for quest in self.quests.values() if quest.status == QuestStatus.ACTIVE]
    
    def get_completed_quests(self) -> List[Quest]:
        """Get all completed quests."""
        return [quest for quest in self.quests.values() if quest.status == QuestStatus.COMPLETED]
    
    def get_recent_entries(self, days: int = 7) -> List[Dict[str, Any]]:
        """Get recent daily entries."""
        cutoff_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        cutoff_date = cutoff_date.replace(day=cutoff_date.day - days)
        
        return [entry for entry in self.daily_entries if entry["date"] >= cutoff_date]
    
    def search_journal(self, query: str) -> Dict[str, List[Any]]:
        """Search through journal entries."""
        results = {
            "quests": [],
            "characters": [],
            "lore": [],
            "locations": [],
            "techniques": [],
            "daily_entries": []
        }
        
        query_lower = query.lower()
        
        # Search quests
        for quest in self.quests.values():
            if (query_lower in quest.title.lower() or 
                query_lower in quest.description.lower() or
                any(query_lower in obj.lower() for obj in quest.objectives)):
                results["quests"].append(quest)
        
        # Search characters
        for character in self.characters.values():
            if (query_lower in character.name.lower() or
                query_lower in character.description.lower() or
                any(query_lower in note["note"].lower() for note in character.personality_notes)):
                results["characters"].append(character)
        
        # Search lore
        for lore in self.lore_entries.values():
            if (query_lower in lore.title.lower() or
                query_lower in lore.content.lower() or
                query_lower in lore.category.lower()):
                results["lore"].append(lore)
        
        # Search locations
        for location_name, location_data in self.locations_visited.items():
            if query_lower in location_name.lower() or query_lower in location_data["description"].lower():
                results["locations"].append((location_name, location_data))
        
        # Search techniques
        for technique_name, technique_data in self.techniques_learned.items():
            if query_lower in technique_name.lower() or query_lower in technique_data["description"].lower():
                results["techniques"].append((technique_name, technique_data))
        
        # Search daily entries
        for entry in self.daily_entries:
            if query_lower in entry["summary"].lower():
                results["daily_entries"].append(entry)
        
        return results
    
    def get_journal_summary(self) -> str:
        """Get a summary of journal contents."""
        active_quests = len(self.get_active_quests())
        completed_quests = len(self.get_completed_quests())
        
        summary_lines = [
            f"📊 Journal Summary",
            f"Active Quests: {active_quests}",
            f"Completed Quests: {completed_quests}",
            f"Characters Met: {len(self.characters)}",
            f"Lore Entries: {len(self.lore_entries)}",
            f"Locations Visited: {len(self.locations_visited)}",
            f"Techniques Learned: {len(self.techniques_learned)}",
            f"Achievements: {len(self.achievements)}",
            f"Battles Won: {self.statistics['battles_won']}",
            f"Battles Lost: {self.statistics['battles_lost']}"
        ]
        
        return "\n".join(summary_lines)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert journal to dictionary for saving."""
        return {
            "quests": {
                qid: {
                    "quest_id": q.quest_id,
                    "title": q.title,
                    "description": q.description,
                    "objectives": q.objectives,
                    "rewards": q.rewards,
                    "status": q.status.value,
                    "progress": q.progress,
                    "completed_objectives": q.completed_objectives,
                    "started_date": q.started_date.isoformat() if q.started_date else None,
                    "completed_date": q.completed_date.isoformat() if q.completed_date else None,
                    "notes": q.notes,
                    "related_npcs": q.related_npcs,
                    "related_locations": q.related_locations
                }
                for qid, q in self.quests.items()
            },
            "characters": {
                name: {
                    "name": c.name,
                    "description": c.description,
                    "relationship_level": c.relationship_level,
                    "relationship_history": [
                        {**h, "date": h["date"].isoformat()}
                        for h in c.relationship_history
                    ],
                    "personality_notes": [
                        {**n, "date": n["date"].isoformat()}
                        for n in c.personality_notes
                    ],
                    "techniques_observed": [
                        {**t, "observed_date": t["observed_date"].isoformat()}
                        for t in c.techniques_observed
                    ],
                    "dialogue_history": [
                        {**d, "date": d["date"].isoformat()}
                        for d in c.dialogue_history
                    ],
                    "significant_events": [
                        {**e, "date": e["date"].isoformat()}
                        for e in c.significant_events
                    ],
                    "first_met_date": c.first_met_date.isoformat(),
                    "last_interaction_date": c.last_interaction_date.isoformat()
                }
                for name, c in self.characters.items()
            },
            "lore_entries": {
                lid: {
                    "title": l.title,
                    "content": l.content,
                    "category": l.category,
                    "discovered_date": l.discovered_date.isoformat(),
                    "related_locations": l.related_locations,
                    "related_characters": l.related_characters,
                    "related_quests": l.related_quests,
                    "importance_level": l.importance_level,
                    "tags": l.tags
                }
                for lid, l in self.lore_entries.items()
            },
            "locations_visited": {
                name: {
                    **data,
                    "first_visit": data["first_visit"].isoformat(),
                    "last_visit": data["last_visit"].isoformat()
                }
                for name, data in self.locations_visited.items()
            },
            "techniques_learned": {
                name: {
                    **data,
                    "learned_date": data["learned_date"].isoformat()
                }
                for name, data in self.techniques_learned.items()
            },
            "achievements": [
                {**a, "earned_date": a["earned_date"].isoformat()}
                for a in self.achievements
            ],
            "daily_entries": [
                {**e, "date": e["date"].isoformat()}
                for e in self.daily_entries
            ],
            "statistics": {
                **self.statistics,
                "start_date": self.statistics["start_date"].isoformat()
            }
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'GameJournal':
        """Create journal from dictionary data."""
        journal = cls()
        
        # Load quests
        for qid, q_data in data.get("quests", {}).items():
            quest = Quest(
                q_data["quest_id"],
                q_data["title"],
                q_data["description"],
                q_data["objectives"],
                q_data["rewards"]
            )
            quest.status = QuestStatus(q_data["status"])
            quest.progress = q_data["progress"]
            quest.completed_objectives = q_data["completed_objectives"]
            quest.started_date = datetime.fromisoformat(q_data["started_date"]) if q_data["started_date"] else None
            quest.completed_date = datetime.fromisoformat(q_data["completed_date"]) if q_data["completed_date"] else None
            quest.notes = q_data["notes"]
            quest.related_npcs = q_data["related_npcs"]
            quest.related_locations = q_data["related_locations"]
            journal.quests[qid] = quest
        
        # Load characters (simplified for brevity - full implementation would restore all fields)
        for name, c_data in data.get("characters", {}).items():
            character = CharacterEntry(c_data["name"], c_data["description"])
            character.relationship_level = c_data["relationship_level"]
            # Restore other fields...
            journal.characters[name] = character
        
        # Load other data structures similarly...
        
        return journal