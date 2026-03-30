from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional, Tuple, Dict

class Frequency(Enum):
    ONCE = "once"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    # add more as needed

@dataclass
class Task:
    description: str
    time: datetime
    duration: timedelta
    priority: int
    frequency: Frequency
    completed: bool = False

    def mark_completed(self) -> None:
        pass

    def mark_pending(self) -> None:
        pass

    def is_overdue(self) -> bool:
        pass

@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet: Pet) -> None:
        pass

    def get_pets(self) -> List[Pet]:
        pass

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_tasks(self, criteria: str) -> List[Task]:
        pass

    def filter_tasks(self, criteria: Dict[str, object]) -> List[Task]:
        pass

    def detect_conflicts(self) -> List[Tuple[Task, Task]]:
        pass

    def schedule_recurring_tasks(self) -> None:
        pass

    def get_all_tasks(self) -> List[Task]:
        pass