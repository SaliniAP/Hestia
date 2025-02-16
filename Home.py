import streamlit as st
import datetime

st.set_page_config(page_title = "Hestia")
st.title(":green[Hestia] ")
st.write("_Your planet tamagotchi!_")
placeholder = st.empty()
with placeholder.container():
    st.image("planet.png")
st.sidebar.success("Select A Page 👆")
#st.sidebar.success("Select a page above ☝️ to navigate.")

if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'
    st.session_state.journal = 'collapsed'

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

if "tasks" not in st.session_state:
    st.session_state.tasks = []



def toggle_sidebar_todo():
    st.session_state.sidebar_state = not st.session_state.sidebar_state

def toggle_sidebar_journal():
    st.session_state.journal = not st.session_state.journal


# Sidebar content (only shown when sidebar_state is True)
if st.button("To-Do List", help = "Open your daily to-do list"):
    toggle_sidebar_todo()

if st.session_state.sidebar_state:
    with st.sidebar:
        st.write("### To-Do")
        st.write("This is your daily to-do list. Add items by pressing checkbox and cross off items by clicking the box. Your planet will heal with every item you cross off <3")
        
        
        text_input = st.text_input(
            "What's something on your mind 👇",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder="Enter an item here",
            )
        
        if text_input:  # Ensure input is not empty
            st.session_state.tasks.append({"task": text_input, "completed": False})
        

        st.subheader("Your Tasks:")
        if st.session_state.tasks:
            for index, task in enumerate(st.session_state.tasks):
                # Checkbox for task completion
                completed = st.checkbox(task["task"], value=task["completed"], key=f"task_{index}")
                # Update task status
                st.session_state.tasks[index]["completed"] = completed
                with placeholder.container():
                    st.image("flowerplanet.png")
            # Button to remove completed tasks
        if st.button("Remove Completed Tasks"):
            st.session_state.tasks = [task for task in st.session_state.tasks if not task["completed"]]
            st.rerun()
            
        
        st.button("Close To-Do List", on_click=toggle_sidebar_todo)


## Planet health
st.write("Your planet's health")
metric1, metric2, metric3 = st.columns(3)
metric1.metric(label="Health", value="50", delta="1")
metric2.metric(label="To-Do Items", value = str(len(st.session_state.tasks)), delta="1")
metric3.metric(label="Journal Entries", value=str(len(st.session_state.passages)), delta='1')
