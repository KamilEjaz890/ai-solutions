"""
Problem #5
Date: 2026-05-14
Task: Write a Python script that reads a list of numbers and plots a bar chart using matplotlib.


# Import the necessary libraries
import matplotlib.pyplot as plt

# Define a function to plot a bar chart
def plot_bar_chart(numbers, labels=None):
    """
    Plots a bar chart using the given numbers and labels.
    
    Args:
        numbers (list): A list of numbers to plot.
        labels (list, optional): A list of labels for the numbers. Defaults to None.
    """
    
    # Check if labels are provided, if not, use default labels (1, 2, 3, etc.)
    if labels is None:
        # Generate default labels
        labels = [f"Number {i+1}" for i in range(len(numbers))]
    
    # Check if the number of labels matches the number of numbers
    if len(labels) != len(numbers):
        raise ValueError("The number of labels must match the number of numbers")
    
    # Create the bar chart
    plt.bar(labels, numbers)
    
    # Add title and labels
    plt.title("Bar Chart Example")
    plt.xlabel("Labels")
    plt.ylabel("Numbers")
    
    # Show the plot
    plt.show()

# Working example
if __name__ == "__main__":
    # Define a list of numbers
    numbers = [10, 20, 30, 40, 50]
    
    # Define a list of labels
    labels = ["A", "B", "C", "D", "E"]
    
    # Plot the bar chart
    plot_bar_chart(numbers, labels)
