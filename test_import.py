import sys
sys.path.append(".")

from src.chatbot import generate_response  # If chatbot.py is in the 'src' folder
print(generate_response("Test"))
