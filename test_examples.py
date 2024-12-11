import unittest
from chatbot import generate_response  # Import your chatbot's function/module

class TestChatbot(unittest.TestCase):
    def test_generate_response(self):
        user_input = "Hello, how are you?"
        response = generate_response(user_input)
        self.assertIsInstance(response, str)
        self.assertNotEqual(response.strip(), "")

    def test_empty_input(self):
        user_input = ""
        response = generate_response(user_input)
        self.assertEqual(response, "Please say something!")  # Adjust based on your implementation

if __name__ == '__main__':
    unittest.main()
