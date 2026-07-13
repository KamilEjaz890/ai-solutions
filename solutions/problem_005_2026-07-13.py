"""
Problem #5
Date: 2026-07-13
Task: Write a Python script that reads a list of numbers and plots a bar chart using matplotlib.


# Import the necessary libraries: matplotlib for plotting and numpy for numerical operations
import matplotlib.pyplot as plt
import numpy as np

# Define a function to plot a bar chart
def plot_bar_chart(numbers, labels):
    """
    Plots a bar chart using the given numbers and labels.
    
    Args:
        numbers (list): A list of numbers to plot.
        labels (list): A list of labels corresponding to the numbers.
    """
    # Check if the lengths of numbers and labels match
    if len(numbers) != len(labels):
        raise ValueError("The lengths of numbers and labels must match.")

    # Create a range of x values for the bars
    x = np.arange(len(numbers))

    # Create the bar chart
    plt.bar(x, numbers)

    # Set the labels for the x-axis
    plt.xticks(x, labels)

    # Set the title and labels for the axes
    plt.title("Bar Chart")
    plt.xlabel("Labels")
    plt.ylabel("Values")

    # Show the plot
    plt.show()

# Example usage
if __name__ == "__main__":
    # Define a list of numbers and labels
    numbers = [10, 20, 15, 30, 25]
    labels = ["A", "B", "C", "D", "E"]

    # Plot the bar chart
    plot_bar_chart(numbers, labels)
