"""
Problem #3
Date: 2026-06-01
Task: Write a Python script that builds a simple chatbot using if/else logic and a dictionary of responses.


# Import the required libraries
import random

# Define a dictionary of responses for the chatbot
# This dictionary maps user inputs to possible chatbot responses
responses = {
    'hello': ['Hi, how are you?', 'Hello! How can I help you?', 'Hey, what\'s up?'],
    'how are you': ['I\'m doing great, thanks!', 'I\'m good, thanks for asking!', 'I\'m just a chatbot, I don\'t have feelings, but thanks for asking!'],
    'what is your name': ['My name is ChatBot', 'I\'m an AI assistant, you can call me ChatBot', 'You can call me CB for short'],
    'default': ['Sorry, I didn\'t understand that', 'Can you please rephrase?', 'I\'m not sure what you mean']
}

# Define a function to get the chatbot response
def get_response(user_input):
    # Convert the user input to lowercase for case-insensitive comparison
    user_input = user_input.lower()
    
    # Check if the user input matches any of the keys in the responses dictionary
    for key in responses:
        if key in user_input:
            # If a match is found, return a random response from the corresponding list
            return random.choice(responses[key])
    
    # If no match is found, return a default response
    return random.choice(responses['default'])

# Define a main function to run the chatbot
def main():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    
    # Run the chatbot in a loop until the user types 'quit'
    while True:
        user_input = input("You: ")
        
        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Get the chatbot response and print it
        print("ChatBot: ", get_response(user_input))

# Run the main function
if __name__ == "__main__":
    main()
