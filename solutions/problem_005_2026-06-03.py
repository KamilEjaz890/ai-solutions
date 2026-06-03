"""
Problem #5
Date: 2026-06-03
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
    
    # Check if labels are provided, if not, use default labels
    if labels is None:
        # Generate default labels as numbers from 1 to n
        labels = [f'Number {i+1}' for i in range(len(numbers))]
    
    # Check if the number of labels matches the number of numbers
    if len(numbers) != len(labels):
        raise ValueError("The number of labels must match the number of numbers")
    
    # Create the bar chart
    plt.bar(labels, numbers)
    
    # Add title and labels
    plt.title('Bar Chart of Numbers')
    plt.xlabel('Labels')
    plt.ylabel('Values')
    
    # Show the plot
    plt.show()

# Example usage
if __name__ == "__main__":
    # Define a list of numbers
    numbers = [10, 20, 15, 30, 25]
    
    # Define a list of labels
    labels = ['A', 'B', 'C', 'D', 'E']
    
    # Call the function to plot the bar chart
    plot_bar_chart(numbers, labels)
