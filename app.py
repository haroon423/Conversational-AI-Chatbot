
import streamlit as st
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Streamlit App
st.title("AI Chatbot")

st.write("Ask me anything!")

# User input
user_input = st.text_input("Your question:", "")

if user_input:
    # Tokenize input and generate a response
    inputs = tokenizer([user_input], return_tensors="pt")
    reply_ids = model.generate(**inputs)
    bot_reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

    # Display bot response
    st.write(f"**Bot**: {bot_reply}")
