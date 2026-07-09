"""
Problem #1
Date: 2026-07-09
Task: Write a Python function that implements linear regression from scratch using only numpy. Include comments.


# Import the numpy library for numerical operations
import numpy as np

# Define a function to calculate the mean of an array
def calculate_mean(array):
    # Calculate the sum of all elements in the array
    total = np.sum(array)
    # Calculate the mean by dividing the sum by the number of elements
    mean = total / len(array)
    return mean

# Define a function to calculate the variance of an array
def calculate_variance(array):
    # Calculate the mean of the array
    mean = calculate_mean(array)
    # Calculate the squared differences from the mean
    squared_diffs = np.square(array - mean)
    # Calculate the variance by taking the mean of the squared differences
    variance = calculate_mean(squared_diffs)
    return variance

# Define a function to calculate the covariance between two arrays
def calculate_covariance(x, y):
    # Calculate the mean of x and y
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    # Calculate the differences from the means
    diff_x = x - mean_x
    diff_y = y - mean_y
    # Calculate the covariance by taking the mean of the product of the differences
    covariance = calculate_mean(diff_x * diff_y)
    return covariance

# Define a function to perform linear regression
def linear_regression(x, y):
    # Calculate the mean of x and y
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    # Calculate the variance of x and the covariance between x and y
    variance_x = calculate_variance(x)
    covariance_xy = calculate_covariance(x, y)
    # Calculate the slope (beta1) and intercept (beta0) of the regression line
    beta1 = covariance_xy / variance_x
    beta0 = mean_y - beta1 * mean_x
    return beta0, beta1

# Define a function to make predictions using the linear regression model
def make_prediction(x, beta0, beta1):
    # Calculate the predicted y value using the regression equation
    y_pred = beta0 + beta1 * x
    return y_pred

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    x = np.random.rand(100)
    y = 2 * x + np.random.randn(100) / 10

    # Perform linear regression
    beta0, beta1 = linear_regression(x, y)
    print(f"Regression equation: y = {beta0:.2f} + {beta1:.2f}x")

    # Make a prediction
    x_pred = 0.5
    y_pred = make_prediction(x_pred, beta0, beta1)
    print(f"Predicted y value for x = {x_pred}: {y_pred:.2f}")
