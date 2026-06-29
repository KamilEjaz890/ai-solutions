"""
Problem #1
Date: 2026-06-29
Task: Write a Python function that implements linear regression from scratch using only numpy. Include comments.


# Import the numpy library for numerical operations
import numpy as np

# Define a class for Linear Regression
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
        # Get the number of samples and features in the training data
        num_samples, num_features = X.shape
        
        # Initialize the weights and bias if not already initialized
        if self.weights is None:
            self.weights = np.zeros(num_features)
        if self.bias is None:
            self.bias = 0
        
        # Gradient Descent algorithm to optimize the weights and bias
        for _ in range(self.num_iterations):
            # Predict the output using the current weights and bias
            y_predicted = np.dot(X, self.weights) + self.bias
            
            # Calculate the gradients of the loss function with respect to the weights and bias
            dw = (1 / num_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / num_samples) * np.sum(y_predicted - y)
            
            # Update the weights and bias using the gradients and learning rate
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    # Method to predict the output for the given input
    def predict(self, X):
        # Predict the output using the optimized weights and bias
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted

# Example usage of the Linear Regression model
if __name__ == "__main__":
    # Generate some sample data
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 3, 5, 7, 11])

    # Create an instance of the Linear Regression model
    model = LinearRegression()

    # Fit the model to the training data
    model.fit(X, y)

    # Predict the output for some input
    input_data = np.array([[6]])
    predicted_output = model.predict(input_data)

    # Print the predicted output
    print("Predicted output:", predicted_output)
