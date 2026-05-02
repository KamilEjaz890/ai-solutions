"""
Problem #3
Date: 2026-05-02
Task: Write a Python script that builds a simple chatbot using if/else logic and a dictionary of responses.


# Import the required libraries
import random

# Define a dictionary of responses for the chatbot
# The keys are the user inputs and the values are the chatbot responses
responses = {
    'hello': ['Hi, how are you?', 'Hello! What can I do for you?', 'Hey, how can I assist you today?'],
    'how are you': ['I\'m doing great, thanks for asking!', 'I\'m good, thanks!', 'I\'m just a chatbot, I don\'t have feelings, but thanks for asking!'],
    'what is your name': ['My name is ChatBot!', 'I\'m an AI chatbot, I don\'t have a personal name.', 'You can call me CB for short!'],
    'default': ['I didn\'t understand that. Can you please rephrase?', 'Sorry, I\'m not sure what you mean.', 'Can you please ask something else?']
}

# Define a function to get the chatbot response
def get_response(user_input):
    # Convert the user input to lowercase for case-insensitive comparison
    user_input = user_input.lower()
    
    # Check if the user input is in the responses dictionary
    if user_input in responses:
        # If it is, return a random response from the list of responses
        return random.choice(responses[user_input])
    else:
        # If it's not, return a random default response
        return random.choice(responses['default'])

# Define a main function to run the chatbot
def main():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    
    # Run the chatbot in an infinite loop until the user types 'quit'
    while True:
        user_input = input("You: ")
        
        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        
        # Get the chatbot response and print it
        print("ChatBot:", get_response(user_input))

# Run the main function
if __name__ == "__main__":
    main()
