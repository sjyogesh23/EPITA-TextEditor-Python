import streamlit as st
import os

st.set_page_config(
    page_title="Text Editor",
    layout="wide"
)


if 'content' not in st.session_state:
    st.session_state.content = ""
if 'filename' not in st.session_state:
    st.session_state.filename = "Untitled"

def get_lines():
    if st.session_state.content:
        return st.session_state.content.split("\n")
    return []

def update_content(lines):
    st.session_state.content = "\n".join(lines)

st.sidebar.header("Actions")
action = st.sidebar.radio(
    "Choose Action", 
    ["View / Reset", "Add Line", "Modify Line", "Delete Line", "Save File", "Load File"]
)

st.sidebar.markdown("---")

if action == "Add Line":
    st.sidebar.subheader("Add a new line")
    lines = get_lines()
    
    line_no = st.sidebar.number_input("Line number:", min_value=0, max_value=len(lines), value=len(lines))
    new_text = st.sidebar.text_input("New line:")
    
    if st.sidebar.button("Add Line"):
        if line_no >= len(lines):
            lines.append(new_text)
        else:
            lines.insert(line_no, new_text)
        update_content(lines)
        st.success(f"Line added at index {line_no}")
        st.rerun()

elif action == "Modify Line":
    st.sidebar.subheader("Modify a line")
    lines = get_lines()
    
    if not lines:
        st.sidebar.warning("File is empty.")
    else:
        line_no = st.sidebar.number_input("Line number:", min_value=0, max_value=len(lines)-1, value=0)
        current_text = lines[line_no] if lines else ""
        new_text = st.sidebar.text_input("New text:", value=current_text)
        
        if st.sidebar.button("Update Line"):
            lines[line_no] = new_text
            update_content(lines)
            st.success(f"Line {line_no} updated")
            st.rerun()

elif action == "Delete Line":
    st.sidebar.subheader("Delete a line")
    lines = get_lines()
    
    if not lines:
        st.sidebar.warning("File is empty.")
    else:
        line_no = st.sidebar.number_input("Line number:", min_value=0, max_value=len(lines)-1, value=0)
        
        if st.sidebar.button("Delete Line"):
            del lines[line_no]
            update_content(lines)
            st.warning(f"Line {line_no} deleted")
            st.rerun()

elif action == "Save File":
    st.sidebar.subheader("Save")
    save_name = st.sidebar.text_input("Filename:", value=st.session_state.filename)
    
    if st.sidebar.button("Save"):
        if not save_name:
            st.sidebar.error("Filename cannot be empty.")
        else:
            try:
                with open(save_name, "w") as f:
                    f.write(st.session_state.content)
                st.session_state.filename = save_name
                st.sidebar.success(f"Saved to {save_name}")
            except OSError as e:
                st.sidebar.error(f"Error saving: {e}")

elif action == "Load File":
    st.sidebar.subheader("Load File")
    load_name = st.sidebar.text_input("Filename:")
    
    if st.sidebar.button("Load"):
        if not os.path.exists(load_name):
            st.sidebar.error("File not found.")
        else:
            try:
                with open(load_name, "r") as f:
                    st.session_state.content = f.read()
                st.session_state.filename = load_name
                st.sidebar.success(f"Loaded {load_name}")
                st.rerun()
            except Exception as e:
                st.sidebar.error(f"Error: {e}")

elif action == "View / Reset":
    if st.sidebar.button("Clear Editor"):
        st.session_state.content = ""
        st.session_state.filename = "Untitled"
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.caption("(c) 2025 Yogesh Sankaranarayanan Jayanthi")


st.title(f"{st.session_state.filename}")
st.markdown("---")

lines = get_lines()

if not lines or (len(lines) == 1 and lines[0] == ""):
    st.info("File is not there ! Either Load a file or insert lines.")
else:
    for i, line in enumerate(lines):
        c1, c2 = st.columns([2,50]) 
        with c1:
            st.write(f"{i} )")
        with c2:
            st.write(line)