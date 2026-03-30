# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Smarter Scheduling

PawPal+ includes the following intelligent scheduling features:

- **Sort by time or priority** — tasks are automatically ordered for a clean daily view
- **Filter by status** — view only incomplete tasks to focus on what's left
- **Conflict detection** — warns you when two tasks are scheduled at the same time
- **Recurring tasks** — daily/weekly/monthly tasks automatically reschedule after completion

## Testing PawPal+

Run the test suite with:

python -m pytest

### What the tests cover:
- Task completion: verifies mark_completed() correctly updates status
- Task addition: verifies adding a task increases the pet's task count
- Sorting: verifies tasks are returned in chronological order
- Conflict detection: verifies the scheduler flags two tasks at the same time
- Recurring tasks: verifies a completed daily task generates a new one for the next day

### Confidence Level: ⭐⭐⭐⭐
All 5 tests pass. Edge cases like duplicate recurring tasks and timezone 
handling would be the next things to test.