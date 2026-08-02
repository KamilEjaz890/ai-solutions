"""
Problem #5
Date: 2026-08-02
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
    
    # Check if labels are provided, if not, use a range of numbers as labels
    if labels is None:
        labels = range(len(numbers))
    
    # Create the bar chart
    plt.bar(labels, numbers)
    
    # Set the title and labels for the chart
    plt.title('Bar Chart Example')
    plt.xlabel('Labels')
    plt.ylabel('Values')
    
    # Show the chart
    plt.show()

# Define a main function to test the plot_bar_chart function
def main():
    # Example list of numbers
    numbers = [10, 20, 15, 30, 25]
    
    # Example list of labels
    labels = ['A', 'B', 'C', 'D', 'E']
    
    # Call the plot_bar_chart function with the example data
    plot_bar_chart(numbers, labels)

# Call the main function
if __name__ == "__main__":
    main()
