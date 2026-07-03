"""
Problem #5
Date: 2026-07-03
Task: Write a Python script that reads a list of numbers and plots a bar chart using matplotlib.


# Import the necessary libraries
import matplotlib.pyplot as plt

# Define a function to plot a bar chart
def plot_bar_chart(numbers, labels):
    """
    Plots a bar chart using the given numbers and labels.
    
    Args:
        numbers (list): A list of numbers to plot.
        labels (list): A list of labels for the numbers.
    """
    # Check if the lengths of numbers and labels are equal
    if len(numbers) != len(labels):
        raise ValueError("The lengths of numbers and labels must be equal")

    # Create a bar chart
    plt.bar(labels, numbers)

    # Add title and labels
    plt.title('Bar Chart')
    plt.xlabel('Labels')
    plt.ylabel('Numbers')

    # Display the plot
    plt.show()

# Define a main function
def main():
    # Example usage
    numbers = [10, 20, 15, 30, 25]
    labels = ['A', 'B', 'C', 'D', 'E']

    # Plot the bar chart
    plot_bar_chart(numbers, labels)

# Run the main function
if __name__ == "__main__":
    main()
