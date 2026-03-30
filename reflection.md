# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The three core user actions I identified are:
- Enter owner and pet info — the user provides basic details about themselves and their pet
- Add and edit care tasks — the user creates tasks like walks, feeding, or meds 
  with a duration and priority
- Generate a daily schedule — the app produces a planned schedule based on 
  constraints and priorities and explains why it chose that plan

I designed four classes:
- Owner: holds the user's name and manages a list of Pet objects
- Pet: holds a pet's name, species, and age, and manages a list of Task objects
- Task: represents a single care activity with a description, time, duration, 
  priority, frequency, and completion status. Uses a unique task_id for identity.
- Scheduler: takes an Owner and handles all smart logic — sorting, filtering, 
  conflict detection, and recurring task scheduling


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, two changes were made after an AI review of the skeleton:

1. Added a task_id field (uuid) to Task so tasks can be reliably identified, 
   compared, and removed without ambiguity.
2. Changed sort_tasks() to use Literal["time", "priority"] instead of a plain 
   string to prevent invalid inputs and make the API clearer.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers two main constraints: time (when a task is scheduled) and priority (how important it is). I decided time mattered most for daily scheduling since a pet owner needs to know what to do and when. Priority is used as a secondary sort to break ties and help the owner focus on critical tasks like medication over optional ones like enrichment.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

My scheduler only detects exact time conflicts rather than overlapping 
durations. This is a reasonable tradeoff for simplicity and most pet care 
tasks are scheduled at distinct times and exact conflicts are the most 
common real-world mistake to catch.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI for design brainstorming (generating the UML diagram), scaffolding class skeletons, implementing method logic, generating tests, and debugging failing tests. The most helpful prompts were specific ones that referenced my actual file using #file:pawpal_system.py. Asking AI to explain why a test was failing rather than just asking it to fix it also helped me understand the code better.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

I rejected the AI's suggestion to keep the if next_time > now check in schedule_recurring_tasks(). The AI added it to avoid scheduling tasks in the past, but it broke the recurring task test since the test used a fixed past date. I removed it after understanding why the test was failing and confirmed all 5 tests passed after the change.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested five behaviors:

Task completion: mark_completed() correctly flips the completed flag
Task addition: adding a task increases the pet's task count
Sorting: tasks are returned in chronological order
Conflict detection: the scheduler correctly flags two tasks at the same time
Recurring tasks: a completed daily task generates a new task for the following day

These tests matter because they cover the core scheduling behaviors the app depends on. If any of these break, the schedule output would be wrong or misleading.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

All 5 tests pass. I would next test edge cases like a pet with no tasks, duplicate recurring tasks being created on repeated calls, and tasks that span midnight causing false conflict detection.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The CLI-first workflow worked really well. Testing the logic in main.py before connecting it to Streamlit meant the UI integration was smooth and I already knew the backend was solid before touching app.py.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would add the ability to mark tasks complete directly in the UI and trigger recurring task scheduling from there. Right now the recurring logic only runs when called manually in code, not from the app itself.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

AI is great at scaffolding and boilerplate but you still need to understand your own code to catch bugs. The failing recurring task test was caused by an AI assumption that seemed reasonable but didn't fit the actual use case. Being the lead architect means reviewing and questioning what AI generates, not just accepting it.