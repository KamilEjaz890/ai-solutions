"""
Problem #1
Date: 2026-04-30
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
def calculate_covariance(array1, array2):
    # Calculate the mean of the first array
    mean1 = calculate_mean(array1)
    # Calculate the mean of the second array
    mean2 = calculate_mean(array2)
    # Calculate the differences from the means
    diff1 = array1 - mean1
    diff2 = array2 - mean2
    # Calculate the covariance by taking the mean of the product of the differences
    covariance = calculate_mean(diff1 * diff2)
    return covariance

# Define a function to perform linear regression
def linear_regression(x, y):
    # Calculate the mean of the x and y arrays
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    
    # Calculate the deviations from the means
    dev_x = x - mean_x
    dev_y = y - mean_y
    
    # Calculate the slope (beta1) using the covariance and variance
    beta1 = calculate_covariance(x, y) / calculate_variance(x)
    
    # Calculate the intercept (beta0)
    beta0 = mean_y - beta1 * mean_x
    
    return beta0, beta1

# Define a function to make predictions using the linear regression model
def make_prediction(x, beta0, beta1):
    # Calculate the predicted y value using the linear regression equation
    y_pred = beta0 + beta1 * x
    return y_pred

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    x = np.random.rand(100)
    y = 2 * x + 1 + np.random.randn(100) / 10
    
    # Perform linear regression
    beta0, beta1 = linear_regression(x, y)
    print(f"Intercept (beta0): {beta0}, Slope (beta1): {beta1}")
    
    # Make a prediction
    x_new = 0.5
    y_pred = make_prediction(x_new, beta0, beta1)
    print(f"Predicted y value for x = {x_new}: {y_pred}")
