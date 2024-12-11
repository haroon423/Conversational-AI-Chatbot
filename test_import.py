from chatbot import generate_response  # Import the function from chatbot.py

def test_generate_response():
    # Test the chatbot's response
    response = generate_response("Hello, how are you?")
    assert isinstance(response, str)
    assert response != ""
