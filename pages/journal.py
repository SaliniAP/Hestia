import streamlit as st
import datetime


if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

if "passages" not in st.session_state:
    st.session_state.passages = []

st.sidebar.success("Check on your planet 👆")

st.title("📔 Personal Journal")
st.write("This is your digital diary. You can view and edit all of your entries here.")


def save_entry(entry_text):
    if entry_text:
        st.toast("Journal entry saved!")
        entry = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "text": entry_text,
            }

        st.session_state.journal_entries.append(entry)
        st.success("Journal entry saved!")
        st.sidebar.success("Go to 'journal' to see your entries.")

text_input = st.text_input(
            "Start today's entry",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder="Start entry",
            )
 
if st.button("Create Entry"):
    with st.container():
        
        if text_input:  # Ensure input is not empty
            st.session_state.passages.append({"date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "text": text_input})
         

if "passages" not in st.session_state or not st.session_state.passages:
    st.info("No journal entries yet. Start writing!")
else:
    for index, entry in enumerate(reversed(st.session_state.passages)):  # Show newest first
        with st.expander(f"📅 {entry['date']}"):
            st.write(entry["text"])
            
            # Button to delete a specific entry
            if st.button("🗑️ Delete", key=f"delete_{index}"):
                del st.session_state.passages[len(st.session_state.passages) - 1 - index]
                st.rerun()