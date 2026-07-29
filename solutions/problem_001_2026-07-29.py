"""
Problem #1
Date: 2026-07-29
Task: Write a Python function that implements linear regression from scratch using only numpy. Include comments.


# Import the numpy library for numerical operations
import numpy as np

# Define a function to calculate the mean of a given array
def calculate_mean(array):
    # Calculate the sum of all elements in the array
    total = np.sum(array)
    # Calculate the mean by dividing the sum by the number of elements
    mean = total / len(array)
    return mean

# Define a function to calculate the variance of a given array
def calculate_variance(array):
    # Calculate the mean of the array
    mean = calculate_mean(array)
    # Calculate the squared differences from the mean for each element
    squared_diffs = np.square(array - mean)
    # Calculate the variance by taking the mean of the squared differences
    variance = calculate_mean(squared_diffs)
    return variance

# Define a function to calculate the covariance between two arrays
def calculate_covariance(array1, array2):
    # Calculate the mean of each array
    mean1 = calculate_mean(array1)
    mean2 = calculate_mean(array2)
    # Calculate the differences from the mean for each element in both arrays
    diff1 = array1 - mean1
    diff2 = array2 - mean2
    # Calculate the covariance by taking the mean of the product of the differences
    covariance = calculate_mean(diff1 * diff2)
    return covariance

# Define a function to perform linear regression
def linear_regression(x, y):
    # Calculate the coefficients (slope and intercept) using the formulae
    # slope = covariance(x, y) / variance(x)
    # intercept = mean(y) - slope * mean(x)
    slope = calculate_covariance(x, y) / calculate_variance(x)
    intercept = calculate_mean(y) - slope * calculate_mean(x)
    return slope, intercept

# Define a function to make predictions using the linear regression model
def make_prediction(x, slope, intercept):
    # Calculate the predicted value using the formula: y = slope * x + intercept
    prediction = slope * x + intercept
    return prediction

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 7, 11])

    # Perform linear regression
    slope, intercept = linear_regression(x, y)
    print("Slope:", slope)
    print("Intercept:", intercept)

    # Make a prediction
    x_new = 6
    prediction = make_prediction(x_new, slope, intercept)
    print("Predicted value for x =", x_new, ":", prediction)
