"""
Problem #8
Date: 2026-05-17
Task: Write a Python script that generates a simple quiz game with 5 AI-related questions.


# Import the required modules
import random

# Define a dictionary with questions, options, and answers
quiz_questions = {
    "What does AI stand for?": {
        "A": "Artificial Intelligence",
        "B": "Augmented Intelligence",
        "C": "Applied Intelligence",
        "D": "Automated Intelligence",
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
    "Which of the following is an application of AI in healthcare?": {
        "A": "Medical Diagnosis",
        "B": "Personalized Medicine",
        "C": "Medical Imaging Analysis",
        "D": "All of the above",
        "Answer": "D"
    },
    "What is the term for a type of AI that can learn from experience and improve its performance over time?": {
        "A": "Supervised Learning",
        "B": "Unsupervised Learning",
        "C": "Reinforcement Learning",
        "D": "Deep Learning",
        "Answer": "C"
    }
}

# Function to run the quiz
def run_quiz(questions):
    # Initialize the score
    score = 0
    
    # Iterate over each question
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
            print("Correct answer!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer is {options['Answer']}.\n")
    
    # Print the final score
    print(f"Quiz finished! Your final score is {score} out of {len(questions)}")

# Run the quiz with the defined questions
if __name__ == "__main__":
    run_quiz(quiz_questions)
