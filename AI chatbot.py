import nltk
from nltk.chat.util import Chat, reflections

# Define pairs (Pattern, Response)
pairs = [
    ["hi|hello", ["Hello!", "Hi there!"]],
    ["how are you?", ["I'm doing great, thank you!"]],
    ["what is your name?", ["I am a chatbot created with Python."]],
    ["quit", ["Goodbye!"]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)
print("Chatbot: Hello! Type 'quit' to exit.")
chatbot.converse()