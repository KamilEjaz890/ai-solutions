"""
Problem #3
Date: 2026-06-11
Task: Write a Python script that builds a simple chatbot using if/else logic and a dictionary of responses.


# Import the required libraries
import random

# Define a dictionary of responses for the chatbot
# The keys are the user's input, and the values are the chatbot's responses
responses = {
    'hello': ['Hi, how are you?', 'Hello! What can I do for you?', 'Hey, how\'s it going?'],
    'how are you': ['I\'m doing great, thanks!', 'I\'m good, thanks for asking!', 'I\'m just a chatbot, I don\'t have feelings, but thanks for asking!'],
    'what is your name': ['My name is ChatBot!', 'I\'m an AI, I don\'t have a personal name.', 'You can call me CB for short!'],
    'default': ['I didn\'t understand that.', 'Can you please rephrase?', 'Sorry, I\'m not sure what you mean.']
}

# Define a function to get the chatbot's response
def get_response(user_input):
    # Convert the user's input to lowercase to make the chatbot case-insensitive
    user_input = user_input.lower()
    
    # Check if the user's input is in the dictionary of responses
    if user_input in responses:
        # If it is, return a random response from the list of responses
        return random.choice(responses[user_input])
    else:
        # If it's not, return a default response
        return random.choice(responses['default'])

# Define a main function to run the chatbot
def main():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    
    # Run the chatbot in a loop until the user types 'quit'
    while True:
        # Get the user's input
        user_input = input("You: ")
        
        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Get the chatbot's response
        response = get_response(user_input)
        
        # Print the chatbot's response
        print("ChatBot: ", response)

# Run the main function
if __name__ == "__main__":
    main()
