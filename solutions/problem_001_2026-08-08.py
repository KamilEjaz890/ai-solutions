"""
Problem #1
Date: 2026-08-08
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
    # Calculate the squared differences from the mean for each element
    squared_diffs = np.square(array - mean)
    # Calculate the variance by taking the mean of the squared differences
    variance = calculate_mean(squared_diffs)
    return variance

# Define a function to calculate the covariance between two arrays
def calculate_covariance(x, y):
    # Calculate the mean of both arrays
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    # Calculate the product of the differences from the mean for each pair of elements
    products = (x - mean_x) * (y - mean_y)
    # Calculate the covariance by taking the mean of the products
    covariance = calculate_mean(products)
    return covariance

# Define a function to perform linear regression
def linear_regression(x, y):
    # Calculate the mean of the input and output arrays
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    
    # Calculate the variance of the input array
    variance_x = calculate_variance(x)
    
    # Calculate the covariance between the input and output arrays
    covariance_xy = calculate_covariance(x, y)
    
    # Calculate the slope (beta1) using the formula: beta1 = cov(x, y) / var(x)
    slope = covariance_xy / variance_x
    
    # Calculate the intercept (beta0) using the formula: beta0 = mean(y) - beta1 * mean(x)
    intercept = mean_y - slope * mean_x
    
    return slope, intercept

# Define a function to make predictions using a linear regression model
def make_prediction(slope, intercept, x):
    # Calculate the predicted output using the formula: y = beta0 + beta1 * x
    prediction = intercept + slope * x
    return prediction

# Example usage:
if __name__ == "__main__":
    # Generate some sample data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 7, 11])
    
    # Perform linear regression
    slope, intercept = linear_regression(x, y)
    print(f"Slope: {slope}, Intercept: {intercept}")
    
    # Make a prediction
    prediction = make_prediction(slope, intercept, 6)
    print(f"Predicted output for x = 6: {prediction}")
