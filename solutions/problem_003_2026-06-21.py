"""
Problem #3
Date: 2026-06-21
Task: Write a Python script that builds a simple chatbot using if/else logic and a dictionary of responses.


# Import the required libraries
import random

# Define a dictionary of responses for the chatbot
# This dictionary maps user inputs to possible chatbot responses
responses = {
    'hello': ['Hi, how are you?', 'Hello! What can I do for you?', 'Hey, how can I help you today?'],
    'how are you': ['I\'m doing great, thanks for asking!', 'I\'m good, thanks!', 'I\'m just a chatbot, I don\'t have feelings, but thanks for asking!'],
    'what is your name': ['My name is ChatBot!', 'I\'m an AI assistant, but you can call me ChatBot!', 'You can call me ChatBot, nice to meet you!'],
    'default': ['Sorry, I didn\'t understand that.', 'Can you please rephrase?', 'I\'m not sure what you mean.']
}

# Define a function to get the chatbot's response
def get_response(user_input):
    # Convert the user's input to lowercase to make the chatbot case-insensitive
    user_input = user_input.lower()
    
    # Check if the user's input is in the dictionary of responses
    if user_input in responses:
        # If the input is in the dictionary, return a random response
        return random.choice(responses[user_input])
    else:
        # If the input is not in the dictionary, return a default response
        return random.choice(responses['default'])

# Define a function to run the chatbot
def run_chatbot():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    
    # Run the chatbot in an infinite loop until the user types 'quit'
    while True:
        user_input = input("You: ")
        
        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        
        # Get the chatbot's response and print it
        print("ChatBot:", get_response(user_input))

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
