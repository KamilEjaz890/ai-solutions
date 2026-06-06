"""
Problem #8
Date: 2026-06-06
Task: Write a Python script that generates a simple quiz game with 5 AI-related questions.


# Import the required libraries
import random

# Define a dictionary with AI-related questions, options, and answers
ai_questions = {
    "What does AI stand for?": {
        "A": "Artificial Intelligence",
        "B": "Artificial Insight",
        "C": "Artificial Imagination",
        "D": "Artificial Innovation",
        "Answer": "A"
    },
    "Which of the following is a type of machine learning?": {
        "A": "Deep Learning",
        "B": "Natural Language Processing",
        "C": "Computer Vision",
        "D": "All of the above",
        "Answer": "D"
    },
    "What is the term for a computer system that can think and learn like a human?": {
        "A": "Artificial General Intelligence",
        "B": "Artificial Narrow Intelligence",
        "C": "Artificial Super Intelligence",
        "D": "Artificial Intelligence",
        "Answer": "A"
    },
    "Which programming language is commonly used for AI development?": {
        "A": "Python",
        "B": "Java",
        "C": "C++",
        "D": "All of the above",
        "Answer": "D"
    },
    "What is the term for a set of data used to train a machine learning model?": {
        "A": "Training Data",
        "B": "Testing Data",
        "C": "Validation Data",
        "D": "Dataset",
        "Answer": "A"
    }
}

# Define a function to run the quiz game
def run_quiz():
    # Initialize the score
    score = 0
    
    # Iterate over each question in the dictionary
    for question, options in ai_questions.items():
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
    print(f"Quiz complete! Your final score is {score} out of {len(ai_questions)}")

# Run the quiz game
if __name__ == "__main__":
    run_quiz()
