"""
Problem #1
Date: 2026-06-09
Task: Write a Python function that implements linear regression from scratch using only numpy. Include comments.


# Import the numpy library for numerical operations
import numpy as np

# Define a function to calculate the cost (mean squared error) of the model
def calculate_cost(X, y, theta):
    # Calculate the predicted values using the current theta values
    predictions = np.dot(X, theta)
    
    # Calculate the mean squared error between predictions and actual values
    cost = (1 / (2 * len(y))) * np.sum(np.square(predictions - y))
    
    return cost

# Define a function to perform gradient descent to optimize theta values
def gradient_descent(X, y, theta, alpha, num_iterations):
    # Initialize a list to store the cost at each iteration
    costs = []
    
    # Perform gradient descent for the specified number of iterations
    for _ in range(num_iterations):
        # Calculate the predicted values using the current theta values
        predictions = np.dot(X, theta)
        
        # Calculate the gradient of the cost function with respect to theta
        gradient = (1 / len(y)) * np.dot(X.T, (predictions - y))
        
        # Update theta values using the gradient and learning rate
        theta = theta - alpha * gradient
        
        # Calculate the cost at the current iteration
        cost = calculate_cost(X, y, theta)
        
        # Append the cost to the list
        costs.append(cost)
    
    return theta, costs

# Define a function to implement linear regression from scratch
def linear_regression(X, y, alpha=0.01, num_iterations=1000):
    # Add a column of ones to X for the bias term
    X = np.hstack((np.ones((X.shape[0], 1)), X))
    
    # Initialize theta values to zero
    theta = np.zeros(X.shape[1])
    
    # Perform gradient descent to optimize theta values
    theta, costs = gradient_descent(X, y, theta, alpha, num_iterations)
    
    return theta, costs

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 3, 5, 7, 11])
    
    # Perform linear regression
    theta, costs = linear_regression(X, y)
    
    # Print the optimized theta values
    print("Optimized theta values:", theta)
    
    # Print the predicted values
    predicted_values = np.dot(np.hstack((np.ones((X.shape[0], 1)), X)), theta)
    print("Predicted values:", predicted_values)
