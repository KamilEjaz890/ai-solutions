"""
Problem #1
Date: 2026-05-30
Task: Write a Python function that implements linear regression from scratch using only numpy. Include comments.


# Import the numpy library for numerical operations
import numpy as np

# Define a class for linear regression
class LinearRegression:
    # Constructor to initialize the model
    def __init__(self, learning_rate=0.001, num_iterations=1000):
        # Initialize the learning rate and number of iterations
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        # Initialize the weights and bias to zero
        self.weights = None
        self.bias = None

    # Method to fit the model to the training data
    def fit(self, X, y):
        # Get the number of samples and features
        num_samples, num_features = X.shape
        # Initialize the weights and bias
        self.weights = np.zeros(num_features)
        self.bias = 0

        # Gradient descent algorithm to optimize the weights and bias
        for _ in range(self.num_iterations):
            # Calculate the predicted values
            y_predicted = np.dot(X, self.weights) + self.bias
            # Calculate the gradients
            dw = (1 / num_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / num_samples) * np.sum(y_predicted - y)
            # Update the weights and bias
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    # Method to make predictions
    def predict(self, X):
        # Calculate the predicted values
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted

# Example usage
if __name__ == "__main__":
    # Create a sample dataset
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 3, 5, 7, 11])

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(X, y)

    # Make predictions
    predictions = model.predict(X)

    # Print the predictions
    print("Predictions:", predictions)
