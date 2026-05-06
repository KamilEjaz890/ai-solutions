"""
Problem #7
Date: 2026-05-06
Task: Write a Python function that counts word frequency in a text and shows the top 10 words.


# Import the required libraries
from collections import Counter
import re

# Function to count word frequency in a text
def count_word_frequency(text):
    # Convert the text to lower case
    text = text.lower()
    
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    word_frequency = Counter(words)
    
    # Get the top 10 most common words
    top_10_words = word_frequency.most_common(10)
    
    return top_10_words

# Function to print the top 10 words
def print_top_10_words(top_10_words):
    # Print the top 10 words
    print("Top 10 Words:")
    for i, (word, frequency) in enumerate(top_10_words):
        print(f"{i+1}. {word}: {frequency}")

# Main function
def main():
    # Example text
    text = "This is a sample text. This text is just a sample. The sample text is used to demonstrate the word frequency counter."
    
    # Count the word frequency
    top_10_words = count_word_frequency(text)
    
    # Print the top 10 words
    print_top_10_words(top_10_words)

# Run the main function
if __name__ == "__main__":
    main()
