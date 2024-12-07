import streamlit as st
import requests


# Set up the main page layout
st.title('One-Day Tour Planning Assistant')

# User login placeholder (for simplicity, using a simple text input)
user_name = st.text_input("Enter your username")

if user_name:
    st.success(f"Welcome, {user_name}!")

    # Collect user preferences
    city = st.text_input("Which city would you like to explore?")
    start_time = st.time_input("What time do you want to start your tour?")
    end_time = st.time_input("What time do you want to end your tour?")
    budget = st.number_input("Enter your budget for the day ($)", min_value=10)
    interests = st.multiselect("Select your interests", ["Culture", "Adventure", "Food", "Shopping", "Nature"])

    # Submit button to send data to the backend
    if st.button("Plan My Trip"):
        payload = {
            "user_name": user_name,
            "city": city,
            "start_time": str(start_time),
            "end_time": str(end_time),
            "budget": budget,
            "interests": interests
        }
        response = requests.post("http://127.0.0.1:8000/generate_itinerary", json=payload)

        
        if response.status_code == 200:
            itinerary = response.json()
            st.subheader("Your Itinerary")
            for i, stop in enumerate(itinerary.get("stops", []), 1):
                st.write(f"{i}. {stop}")
        else:
            st.error("Failed to generate the itinerary. Please try again.")
