import streamlit as st
import datetime

st.title("Hestia ~")
st.write("Your planet tamagotchi!")


if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'
    st.session_state.journal = 'collapsed'

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

def toggle_sidebar_todo():
    st.session_state.sidebar_state = not st.session_state.sidebar_state

def toggle_sidebar_journal():
    st.session_state.journal = not st.session_state.journal

def new_journal():
    st.text_area("Write your journal entry:")


object_list = []
print (f"object_list:{object_list}")
print (f"type:{type(object_list)}")
# Sidebar content (only shown when sidebar_state is True)
left, right = st.columns(2)
with left:
    if st.button("To-Do List", help = "Open your daily to-do list"):
        toggle_sidebar_todo()
with right:
    if st.button("Journal Entry", help = "Open your journal"):
        toggle_sidebar_journal()

if st.session_state.sidebar_state:
    with st.sidebar:
        st.write("### To-Do")
        st.write("This is your daily to-do list. Add items by pressing checkbox and cross off items by clicking the box. Your planet will heal with every item you cross off <3")
        
        
        text_input = st.text_input(
            "Enter some text 👇",
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
            # Button to remove completed tasks
            if st.button("Remove Completed Tasks"):
                st.session_state.tasks = [task for task in st.session_state.tasks if not task["completed"]]
                st.rerun()
            
        
        st.button("Close To-Do List", on_click=toggle_sidebar_todo)
    
if st.session_state.journal:
    with st.sidebar:
        st.write("### Journal")
        st.write("This is your journal. You can add journal entries by pressing New Entry. More entries will allow your planet to thrive!")
        
        st.button("New Entry", on_click=new_journal)


        st.button("Close Journal", on_click=toggle_sidebar_journal)

