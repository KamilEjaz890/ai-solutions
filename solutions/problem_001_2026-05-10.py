"""
Problem #1
Date: 2026-05-10
Task: Write a Python function that implements linear regression from scratch using only numpy. Include comments.


# Import the numpy library, which provides support for large, multi-dimensional arrays and matrices
import numpy as np

# Define a function to calculate the mean of an array
def calculate_mean(array):
    # Calculate the sum of all elements in the array
    total = np.sum(array)
    # Calculate the mean by dividing the sum by the number of elements
    mean = total / len(array)
    return mean

# Define a function to calculate the coefficients (slope and intercept) of the linear regression line
def calculate_coefficients(x, y):
    # Calculate the mean of x and y
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)

    # Calculate the deviations from the mean for x and y
    deviations_x = x - mean_x
    deviations_y = y - mean_y

    # Calculate the slope (beta1) using the formula: beta1 = Σ[(xi - mean_x)(yi - mean_y)] / Σ(xi - mean_x)^2
    numerator = np.sum(deviations_x * deviations_y)
    denominator = np.sum(deviations_x ** 2)
    beta1 = numerator / denominator

    # Calculate the intercept (beta0) using the formula: beta0 = mean_y - beta1 * mean_x
    beta0 = mean_y - beta1 * mean_x

    return beta0, beta1

# Define a function to predict y values using the linear regression model
def predict(x, beta0, beta1):
    # Calculate the predicted y values using the formula: y = beta0 + beta1 * x
    y_pred = beta0 + beta1 * x
    return y_pred

# Define a function to calculate the cost (mean squared error) of the linear regression model
def calculate_cost(y, y_pred):
    # Calculate the differences between actual and predicted y values
    differences = y - y_pred
    # Calculate the mean squared error
    cost = np.mean(differences ** 2)
    return cost

# Example usage:
if __name__ == "__main__":
    # Generate some sample data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 7, 11])

    # Calculate the coefficients (slope and intercept) of the linear regression line
    beta0, beta1 = calculate_coefficients(x, y)
    print(f"Intercept (beta0): {beta0}, Slope (beta1): {beta1}")

    # Predict y values using the linear regression model
    y_pred = predict(x, beta0, beta1)
    print(f"Predicted y values: {y_pred}")

    # Calculate the cost (mean squared error) of the linear regression model
    cost = calculate_cost(y, y_pred)
    print(f"Mean Squared Error (cost): {cost}")
