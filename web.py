# Import necessary modules
import streamlit as st
import functions

# Load existing todos from file
todos = functions.get_todos()

# Function to add a new todo
def add_todo():
    # Get the new todo from the text input
    todo = st.session_state['new_todo'] + "\n"
    # Add the new todo to the list
    todos.append(todo)
    # Write the updated list back to the file
    functions.write_todos(todos)

# Display an image
st.image(image="fulllogo.png", width=300)
# Display the title of the app
st.title("PHUC'S TODO APP")
# Display a subheader
st.subheader("This is my todo app")
# Display a text
st.write("This app is to increase your productivity!")

# Loop through the todos
for index, todo in enumerate(todos):
    # Create a checkbox for each todo
    checkbox = st.checkbox(todo, key=todo)
    # If the checkbox is checked
    if checkbox:
        # Remove the todo from the list
        todos.pop(index)
        # Write the updated list back to the file
        functions.write_todos(todos)
        # Remove the checkbox from the session state
        del st.session_state[todo]
        # Rerun the app to update the display
        st.rerun()

# Create a text input for adding new todos
st.text_input(label="New Todo", placeholder="Add new todo...", on_change=add_todo, key='new_todo')
# Add a footer
st.markdown('---')
st.markdown('**Camera Application** developed with ❤️ by [Phuc Le](https://github.com/phucleit96)')