from pawpal_system import Owner, Pet, Task, Scheduler, Frequency
from datetime import datetime, timedelta

# Setup
owner = Owner("Alex")
dog = Pet("Buddy", "Dog", 3)
cat = Pet("Whiskers", "Cat", 5)
owner.add_pet(dog)
owner.add_pet(cat)

# Add tasks
dog.add_task(Task("Morning walk", datetime(2025, 1, 1, 8, 0), timedelta(minutes=30), priority=1, frequency=Frequency.DAILY))
dog.add_task(Task("Evening feed", datetime(2025, 1, 1, 18, 0), timedelta(minutes=15), priority=2, frequency=Frequency.DAILY))
cat.add_task(Task("Give medication", datetime(2025, 1, 1, 9, 0), timedelta(minutes=5), priority=1, frequency=Frequency.DAILY))

# Conflict test - same time as morning walk
dog.add_task(Task("Vet appointment", datetime(2025, 1, 1, 8, 0), timedelta(minutes=60), priority=1, frequency=Frequency.ONCE))

# Print sorted schedule
scheduler = Scheduler(owner)
print("=== Today's Schedule ===")
for task in scheduler.sort_tasks("time"):
    print(f"{task.time.strftime('%H:%M')} | {task.description} | Priority: {task.priority}")

# Print conflicts
print("\n=== Conflicts ===")
for t1, t2 in scheduler.detect_conflicts():
    print(f"CONFLICT: '{t1.description}' and '{t2.description}' both at {t1.time.strftime('%H:%M')}")