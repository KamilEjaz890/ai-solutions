"""
Problem #5
Date: 2026-06-13
Task: Write a Python script that reads a list of numbers and plots a bar chart using matplotlib.


# Import the necessary libraries
import matplotlib.pyplot as plt

# Define a function to plot a bar chart
def plot_bar_chart(numbers, labels=None):
    """
    Plots a bar chart using matplotlib.

    Args:
        numbers (list): A list of numbers to plot.
        labels (list, optional): A list of labels for the numbers. Defaults to None.
    """
    # Check if labels are provided, if not, use default labels
    if labels is None:
        labels = [f"Number {i+1}" for i in range(len(numbers))]

    # Check if the lengths of numbers and labels match
    if len(numbers) != len(labels):
        raise ValueError("The lengths of numbers and labels must match")

    # Create the bar chart
    plt.bar(labels, numbers)

    # Add title and labels
    plt.title("Bar Chart of Numbers")
    plt.xlabel("Labels")
    plt.ylabel("Values")

    # Show the plot
    plt.show()

# Example usage
if __name__ == "__main__":
    # Define a list of numbers
    numbers = [10, 20, 30, 40, 50]

    # Define a list of labels
    labels = ["A", "B", "C", "D", "E"]

    # Plot the bar chart
    plot_bar_chart(numbers, labels)
