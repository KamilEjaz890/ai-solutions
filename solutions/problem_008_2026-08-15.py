"""
Problem #8
Date: 2026-08-15
Task: Write a Python script that generates a simple quiz game with 5 AI-related questions.


# Import the required libraries
import random

# Define a dictionary with AI-related questions, options, and answers
ai_questions = {
    "What does AI stand for?": {
        "A": "Artificial Intelligence",
        "B": "Advanced Intelligence",
        "C": "Augmented Intelligence",
        "D": "Acquired Intelligence",
        "answer": "A"
    },
    "Which of the following is a type of machine learning?": {
        "A": "Deep Learning",
        "B": "Natural Language Processing",
        "C": "Computer Vision",
        "D": "All of the above",
        "answer": "D"
    },
    "What is the term for a computer system that can simulate human conversation?": {
        "A": "Chatbot",
        "B": "Virtual Assistant",
        "C": "Robot",
        "D": "Artificial Intelligence",
        "answer": "A"
    },
    "Which programming language is commonly used for AI development?": {
        "A": "Python",
        "B": "Java",
        "C": "C++",
        "D": "JavaScript",
        "answer": "A"
    },
    "What is the term for a computer system that can learn from data without being explicitly programmed?": {
        "A": "Machine Learning",
        "B": "Deep Learning",
        "C": "Natural Language Processing",
        "D": "Computer Vision",
        "answer": "A"
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
            if option != "answer":
                print(f"{option}: {value}")
        
        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, D): ")
        
        # Check if the user's answer is correct
        if user_answer.upper() == options["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer is {options['answer']}.\n")
    
    # Print the final score
    print(f"Quiz complete! Your final score is {score} out of {len(ai_questions)}")

# Run the quiz game
if __name__ == "__main__":
    run_quiz()
