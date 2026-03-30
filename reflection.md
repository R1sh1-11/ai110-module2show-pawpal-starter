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

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
