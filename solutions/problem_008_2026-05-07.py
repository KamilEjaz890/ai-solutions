"""
Problem #8
Date: 2026-05-07
Task: Write a Python script that generates a simple quiz game with 5 AI-related questions.


# Import the required libraries
import random

# Define a dictionary to store the quiz questions, options, and answers
quiz_questions = {
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
    "What is the primary goal of natural language processing?": {
        "A": "To enable computers to understand human language",
        "B": "To enable humans to understand computer language",
        "C": "To improve computer vision",
        "D": "To develop expert systems",
        "Answer": "A"
    },
    "Which of the following is an application of computer vision?": {
        "A": "Image recognition",
        "B": "Object detection",
        "C": "Facial recognition",
        "D": "All of the above",
        "Answer": "D"
    },
    "What is the term for a computer system that can mimic human conversation?": {
        "A": "Chatbot",
        "B": "Virtual assistant",
        "C": "Robot",
        "D": "All of the above",
        "Answer": "A"
    }
}

# Define a function to run the quiz game
def run_quiz():
    # Initialize the score to 0
    score = 0
    
    # Iterate over each question in the quiz questions dictionary
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
            print("Correct answer!\n")
            score += 1
        else:
            print(f"Incorrect answer. The correct answer is {options['Answer']}.\n")
    
    # Print the final score
    print(f"Quiz finished! Your final score is {score} out of {len(quiz_questions)}")

# Run the quiz game
if __name__ == "__main__":
    run_quiz()
