"""
Problem #8
Date: 2026-07-16
Task: Write a Python script that generates a simple quiz game with 5 AI-related questions.


# Import the required libraries
import random

# Define a dictionary to store the quiz questions, options, and answers
quiz_questions = {
    "What does AI stand for?": {
        "A": "Artificial Intelligence",
        "B": "Artificial Innovations",
        "C": "Advanced Innovations",
        "D": "Advanced Intelligence",
        "Answer": "A"
    },
    "Which of the following is a type of machine learning?": {
        "A": "Deep Learning",
        "B": "Natural Language Processing",
        "C": "Computer Vision",
        "D": "All of the above",
        "Answer": "D"
    },
    "What is the term for a computer program that can have a conversation with a human?": {
        "A": "Chatbot",
        "B": "Virtual Assistant",
        "C": "Robot",
        "D": "AI Model",
        "Answer": "A"
    },
    "Which of the following is a benefit of using AI in business?": {
        "A": "Increased labor costs",
        "B": "Improved customer service",
        "C": "Reduced efficiency",
        "D": "Decreased productivity",
        "Answer": "B"
    },
    "What is the term for the process of training an AI model on a large dataset?": {
        "A": "Supervised learning",
        "B": "Unsupervised learning",
        "C": "Reinforcement learning",
        "D": "Data training",
        "Answer": "A"
    }
}

# Define a function to run the quiz
def run_quiz():
    # Initialize the score to 0
    score = 0
    
    # Loop through each question in the quiz
    for question, options in quiz_questions.items():
        # Print the question and options
        print(question)
        for option, value in options.items():
            if option != "Answer":
                print(f"{option}: {value}")
        
        # Ask the user for their answer
        user_answer = input("Enter your answer (A, B, C, D): ")
        
        # Check if the user's answer is correct
        if user_answer.upper() == options["Answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {options['Answer']}.\n")
    
    # Print the final score
    print(f"Quiz complete! Your final score is {score} out of {len(quiz_questions)}")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
