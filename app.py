
import streamlit as st
from chatbot import generate_response  # Import the function from chatbot.py

# Streamlit App
st.title("AI Chatbot")

st.write("Ask me anything!")

# User input
user_input = st.text_input("Your question:", "")

if user_input:
    # Generate a response from the chatbot
    bot_reply = generate_response(user_input)
    # Display bot response
    st.write(f"**Bot**: {bot_reply}")

    # Display bot response
    st.write(f"**Bot**: {bot_reply}")
