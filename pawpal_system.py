import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Tuple, Dict, Literal


class Frequency(Enum):
    ONCE = "once"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


@dataclass
class Task:
    description: str
    time: datetime
    duration: timedelta
    priority: int
    frequency: Frequency
    completed: bool = False
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def mark_completed(self) -> None:
        self.completed = True

    def mark_pending(self) -> None:
        self.completed = False

    def is_overdue(self) -> bool:
        return (not self.completed) and (self.time < datetime.now())


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        for existing in list(self.tasks):
            if existing.task_id == task.task_id:
                self.tasks.remove(existing)
                return

    def get_tasks(self) -> List[Task]:
        return self.tasks


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        for existing in list(self.pets):
            if existing is pet or existing.name == pet.name:
                self.pets.remove(existing)
                return

    def get_pets(self) -> List[Pet]:
        return self.pets


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_tasks(self, criteria: Literal["time", "priority"]) -> List[Task]:
        tasks = self.get_all_tasks()
        if criteria == "time":
            return sorted(tasks, key=lambda t: t.time)
        if criteria == "priority":
            return sorted(tasks, key=lambda t: t.priority)
        return tasks

    def filter_tasks(self, criteria: Dict[str, object]) -> List[Task]:
        tasks = self.get_all_tasks()
        if "completed" in criteria:
            tasks = [t for t in tasks if t.completed == bool(criteria["completed"])]
        if "pet_name" in criteria:
            pet_name = criteria["pet_name"]
            tasks = [t for t in tasks if any(p.name == pet_name and t in p.tasks for p in self.owner.pets)]
        return tasks

    def detect_conflicts(self) -> List[Tuple[Task, Task]]:
        tasks = sorted(self.get_all_tasks(), key=lambda t: t.time)
        conflicts: List[Tuple[Task, Task]] = []
        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                if tasks[i].time == tasks[j].time:
                    conflicts.append((tasks[i], tasks[j]))
                else:
                    break
        return conflicts

    def schedule_recurring_tasks(self) -> None:
        for pet in self.owner.pets:
            for task in list(pet.tasks):
                if task.completed and task.frequency != Frequency.ONCE:
                    if task.frequency == Frequency.DAILY:
                        next_time = task.time + timedelta(days=1)
                    elif task.frequency == Frequency.WEEKLY:
                        next_time = task.time + timedelta(weeks=1)
                    elif task.frequency == Frequency.MONTHLY:
                        next_time = task.time + timedelta(days=30)
                    else:
                        continue

                    new_task = Task(
                        description=task.description,
                        time=next_time,
                        duration=task.duration,
                        priority=task.priority,
                        frequency=task.frequency,
                        completed=False,
                    )
                    pet.add_task(new_task)

    def get_all_tasks(self) -> List[Task]:
        all_tasks: List[Task] = []
        for pet in self.owner.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks