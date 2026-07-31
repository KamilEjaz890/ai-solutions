"""
Problem #3
Date: 2026-07-31
Task: Write a Python script that builds a simple chatbot using if/else logic and a dictionary of responses.


# Import the required libraries
import random

# Define a dictionary to store the chatbot's responses
# The keys are the user's input and the values are the chatbot's responses
responses = {
    'hello': ['Hi, how are you?', 'Hello! What can I do for you?', 'Hey, what\'s up?'],
    'how are you': ['I\'m doing great, thanks!', 'I\'m good, thanks for asking!', 'I\'m just a chatbot, I don\'t have feelings, but thanks for asking!'],
    'what is your name': ['My name is ChatBot!', 'I\'m an AI chatbot, I don\'t have a personal name.', 'You can call me Bot!'],
    'default': ['I didn\'t understand that.', 'Can you please rephrase?', 'Sorry, I\'m not sure what you mean.']
}

# Define a function to get the chatbot's response
def get_response(user_input):
    # Convert the user's input to lowercase to make the chatbot case-insensitive
    user_input = user_input.lower()
    
    # Check if the user's input is in the responses dictionary
    if user_input in responses:
        # If the input is in the dictionary, return a random response
        return random.choice(responses[user_input])
    else:
        # If the input is not in the dictionary, return a default response
        return random.choice(responses['default'])

# Define a function to start the chat
def start_chat():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    
    # Start an infinite loop to keep the chat going
    while True:
        # Get the user's input
        user_input = input("You: ")
        
        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Get the chatbot's response and print it
        print("ChatBot: ", get_response(user_input))

# Start the chat
start_chat()
