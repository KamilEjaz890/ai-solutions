"""
Problem #8
Date: 2026-08-05
Task: Write a Python script that generates a simple quiz game with 5 AI-related questions.


# Import the required libraries
import random

# Define a dictionary with questions, options, and answers
quiz_questions = {
    "What does AI stand for?": {
        "A": "Artificial Intelligence",
        "B": "Artificial Instinct",
        "C": "Artificial Insight",
        "D": "Artificial Imagination",
        "Answer": "A"
    },
    "Which of the following is a type of machine learning?": {
        "A": "Deep Learning",
        "B": "Supervised Learning",
        "C": "Unsupervised Learning",
        "D": "All of the above",
        "Answer": "D"
    },
    "What is the term for a computer program that can have a conversation with a human?": {
        "A": "Chatbot",
        "B": "Robot",
        "C": "AI Assistant",
        "D": "Virtual Assistant",
        "Answer": "A"
    },
    "Which of the following is an application of natural language processing?": {
        "A": "Speech Recognition",
        "B": "Sentiment Analysis",
        "C": "Language Translation",
        "D": "All of the above",
        "Answer": "D"
    },
    "What is the term for a neural network with multiple layers?": {
        "A": "Deep Neural Network",
        "B": "Shallow Neural Network",
        "C": "Wide Neural Network",
        "D": "Narrow Neural Network",
        "Answer": "A"
    }
}

# Function to run the quiz game
def run_quiz():
    # Initialize the score
    score = 0
    
    # Iterate over each question in the quiz
    for question, options in quiz_questions.items():
        # Print the question and options
        print(question)
        for option, value in options.items():
            if option != "Answer":
                print(f"{option}: {value}")
        
        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, D): ")
        
        # Check if the user's answer is correct
        if user_answer.upper() == options["Answer"]:
            print("Correct answer!\n")
            score += 1
        else:
            print(f"Incorrect answer. The correct answer is {options['Answer']}.\n")
    
    # Print the final score
    print(f"Quiz completed! Your final score is {score} out of {len(quiz_questions)}")

# Run the quiz game
if __name__ == "__main__":
    run_quiz()
