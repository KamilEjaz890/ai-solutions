"""
Problem #7
Date: 2026-08-04
Task: Write a Python function that counts word frequency in a text and shows the top 10 words.


# Import the required libraries
from collections import Counter
import re

# Function to count word frequency in a text
def count_word_frequency(text):
    # Convert the text to lower case to ensure the word count is case-insensitive
    text = text.lower()
    
    # Remove punctuation and special characters from the text
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    word_frequency = Counter(words)
    
    # Return the top 10 most common words
    return word_frequency.most_common(10)

# Function to print the word frequency
def print_word_frequency(word_frequency):
    # Print the word frequency in a readable format
    print("Word Frequency:")
    for word, frequency in word_frequency:
        print(f"{word}: {frequency}")

# Main function
def main():
    # Example text
    text = "This is an example sentence. This sentence is just an example. This example is used to demonstrate the word frequency count."
    
    # Count the word frequency
    word_frequency = count_word_frequency(text)
    
    # Print the word frequency
    print_word_frequency(word_frequency)

# Run the main function
if __name__ == "__main__":
    main()
