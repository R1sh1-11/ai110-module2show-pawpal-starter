from pawpal_system import Owner, Pet, Task, Scheduler, Frequency
from datetime import datetime, timedelta

def make_task(desc, hour, priority=1, frequency=Frequency.DAILY):
    return Task(desc, datetime(2025, 1, 1, hour, 0), timedelta(minutes=30), priority, frequency)

def test_mark_complete():
    task = make_task("Walk", 8)
    task.mark_completed()
    assert task.completed == True

def test_add_task_increases_count():
    pet = Pet("Buddy", "Dog", 3)
    task = make_task("Feed", 8)
    pet.add_task(task)
    assert len(pet.get_tasks()) == 1

def test_sort_by_time():
    owner = Owner("Alex")
    pet = Pet("Buddy", "Dog", 3)
    owner.add_pet(pet)
    pet.add_task(make_task("Evening feed", 18))
    pet.add_task(make_task("Morning walk", 8))
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_tasks("time")
    assert sorted_tasks[0].time.hour == 8
    assert sorted_tasks[1].time.hour == 18

def test_conflict_detection():
    owner = Owner("Alex")
    pet = Pet("Buddy", "Dog", 3)
    owner.add_pet(pet)
    pet.add_task(make_task("Walk", 8))
    pet.add_task(make_task("Vet", 8))
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) == 1

def test_recurring_task():
    owner = Owner("Alex")
    pet = Pet("Buddy", "Dog", 3)
    owner.add_pet(pet)
    task = make_task("Walk", 8, frequency=Frequency.DAILY)
    pet.add_task(task)
    task.mark_completed()
    scheduler = Scheduler(owner)
    scheduler.schedule_recurring_tasks()
    assert len(pet.get_tasks()) == 2