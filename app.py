import streamlit as st
from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler, Frequency

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# --- Session State Setup ---
if "owner" not in st.session_state:
    st.session_state.owner = None
if "scheduler" not in st.session_state:
    st.session_state.scheduler = None

# --- Step 1: Owner + Pet Info ---
st.subheader("👤 Owner & Pet Info")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
age = st.number_input("Pet age", min_value=0, max_value=30, value=3)

if st.button("Save Owner & Pet"):
    pet = Pet(name=pet_name, species=species, age=age)
    owner = Owner(name=owner_name)
    owner.add_pet(pet)
    st.session_state.owner = owner
    st.session_state.scheduler = Scheduler(owner)
    st.success(f"Saved! {owner_name} and {pet_name} are ready.")

st.divider()

# --- Step 2: Add Tasks ---
st.subheader("📋 Add a Task")

if st.session_state.owner is None:
    st.info("Save your owner and pet info first.")
else:
    col1, col2 = st.columns(2)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col2:
        priority = st.number_input("Priority (1=high)", min_value=1, max_value=5, value=1)
        freq = st.selectbox("Frequency", ["once", "daily", "weekly", "monthly"])
        task_hour = st.slider("Hour of day", 0, 23, 8)

    if st.button("Add Task"):
        freq_map = {
            "once": Frequency.ONCE,
            "daily": Frequency.DAILY,
            "weekly": Frequency.WEEKLY,
            "monthly": Frequency.MONTHLY,
        }
        task = Task(
            description=task_title,
            time=datetime.now().replace(hour=task_hour, minute=0, second=0, microsecond=0),
            duration=timedelta(minutes=int(duration)),
            priority=int(priority),
            frequency=freq_map[freq],
        )
        # Add to first pet
        pet = st.session_state.owner.get_pets()[0]
        pet.add_task(task)
        st.success(f"Added task: {task_title} at {task_hour:02d}:00")

st.divider()

# --- Step 3: Generate Schedule ---
st.subheader("📅 Today's Schedule")

if st.session_state.scheduler is None:
    st.info("Save your owner and pet info first.")
else:
    scheduler = st.session_state.scheduler
    all_tasks = scheduler.get_all_tasks()

    if not all_tasks:
        st.info("No tasks yet. Add some above!")
    else:
        if st.button("Generate Schedule"):
            sorted_tasks = scheduler.sort_tasks("time")
            conflicts = scheduler.detect_conflicts()

            st.markdown("### Sorted by Time")
            table_data = [
                {
                    "Time": t.time.strftime("%H:%M"),
                    "Task": t.description,
                    "Duration": f"{int(t.duration.total_seconds() // 60)} min",
                    "Priority": t.priority,
                    "Frequency": t.frequency.value,
                    "Done": "✅" if t.completed else "❌",
                }
                for t in sorted_tasks
            ]
            st.table(table_data)

            if conflicts:
                st.warning(f"⚠️ {len(conflicts)} conflict(s) detected:")
                for t1, t2 in conflicts:
                    st.warning(f"'{t1.description}' and '{t2.description}' both at {t1.time.strftime('%H:%M')}")
            else:
                st.success("✅ No scheduling conflicts!")