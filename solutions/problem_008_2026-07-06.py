"""
Problem #8
Date: 2026-07-06
Task: Write a Python script that generates a simple quiz game with 5 AI-related questions.


# Import the required libraries
import random

# Define a dictionary with questions, options, and answers
quiz_questions = {
    "What does AI stand for?": {
        "A": "Artificial Intelligence",
        "B": "Advanced Informatics",
        "C": "Automated Innovation",
        "D": "Augmented Insight",
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
        "A": "Self-driving cars",
        "B": "Facial recognition",
        "C": "Object detection",
        "D": "All of the above",
        "Answer": "D"
    },
    "What is the term for a computer system that can mimic human conversation?": {
        "A": "Chatbot",
        "B": "Virtual assistant",
        "C": "Conversational AI",
        "D": "All of the above",
        "Answer": "D"
    }
}

# Function to run the quiz
def run_quiz(questions):
    # Initialize the score
    score = 0
    
    # Iterate over each question in the quiz
    for question, options in questions.items():
        # Print the question and options
        print(question)
        for option, value in options.items():
            if option != "Answer":
                print(f"{option}: {value}")
        
        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, D): ")
        
        # Check if the user's answer is correct
        if user_answer.upper() == options["Answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {options['Answer']}.\n")
    
    # Print the final score
    print(f"Quiz complete! Your final score is {score} out of {len(questions)}")

# Run the quiz with the defined questions
if __name__ == "__main__":
    run_quiz(quiz_questions)
