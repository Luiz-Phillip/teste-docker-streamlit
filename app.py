import streamlit as st


# Set page title
st.set_page_config(page_title="My Streamlit App")

# Add a title to the app
st.title("Welcome to My Streamlit App")

# Add a text input for user's name
user_name = st.text_input("Enter your name")

# Display a personalized greeting
if user_name:
    st.write(f"Hello, {user_name}! Welcome to the app.")

# Add a sidebar
st.sidebar.header("Options")

# Add a selectbox to the sidebar
option = st.sidebar.selectbox(
    "Choose a visualization",
    ("Bar Chart", "Line Chart", "Scatter Plot")
)

# Display the selected option
st.write(f"You selected: {option}")

# Placeholder for future visualizations
st.write("Visualization will be added here based on your selection.")

# Add a button
if st.button("Click me!"):
    st.balloons()
