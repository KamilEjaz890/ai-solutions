"""
Problem #8
Date: 2026-04-27
Task: Write a Python script that generates a simple quiz game with 5 AI-related questions.


# Import the required libraries
import random

# Define a class for the quiz game
class QuizGame:
    def __init__(self):
        # Initialize the quiz questions and answers
        self.questions = {
            "What does AI stand for?": "Artificial Intelligence",
            "Which of the following is a type of machine learning?": "Supervised Learning",
            "What is the term for a computer system that can think and learn like a human?": "Artificial Intelligence",
            "What is the name of the popular AI chatbot developed by Meta?": "LLaMA",
            "What is the term for a computer system that can understand and generate human-like language?": "Natural Language Processing"
        }
        # Define the options for each question
        self.options = {
            "What does AI stand for?": ["Artificial Intelligence", "Advanced Intelligence", "Augmented Intelligence", "Acquired Intelligence"],
            "Which of the following is a type of machine learning?": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "None of the above"],
            "What is the term for a computer system that can think and learn like a human?": ["Artificial Intelligence", "Machine Learning", "Deep Learning", "Natural Language Processing"],
            "What is the name of the popular AI chatbot developed by Meta?": ["LLaMA", "ChatGPT", "Bard", "None of the above"],
            "What is the term for a computer system that can understand and generate human-like language?": ["Natural Language Processing", "Machine Learning", "Deep Learning", "Artificial Intelligence"]
        }

    # Method to play the quiz game
    def play(self):
        # Initialize the score
        score = 0
        # Iterate over each question
        for question, answer in self.questions.items():
            # Print the question and options
            print(f"\nQuestion: {question}")
            print("Options:")
            for i, option in enumerate(self.options[question]):
                print(f"{i+1}. {option}")
            # Get the user's response
            response = input("Enter the number of your answer: ")
            # Check if the response is correct
            if self.options[question][int(response) - 1] == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {answer}.")
        # Print the final score
        print(f"\nQuiz complete! Your final score is {score} out of {len(self.questions)}")

# Create an instance of the quiz game and play it
if __name__ == "__main__":
    quiz = QuizGame()
    quiz.play()
