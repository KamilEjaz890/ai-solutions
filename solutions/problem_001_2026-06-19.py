"""
Problem #1
Date: 2026-06-19
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
        # Initialize the coefficients (weights and bias)
        self.weights = None
        self.bias = None

    # Method to fit the model to the training data
    def fit(self, X, y):
        # Get the number of samples and features
        num_samples, num_features = X.shape
        
        # Initialize the coefficients (weights and bias) with zeros
        self.weights = np.zeros(num_features)
        self.bias = 0

        # Gradient Descent algorithm to optimize the coefficients
        for _ in range(self.num_iterations):
            # Calculate the predicted values
            y_predicted = np.dot(X, self.weights) + self.bias
            
            # Calculate the gradients of the loss function with respect to the coefficients
            dw = (1 / num_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / num_samples) * np.sum(y_predicted - y)

            # Update the coefficients using the gradients and learning rate
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    # Method to make predictions using the trained model
    def predict(self, X):
        # Calculate the predicted values using the trained coefficients
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([2, 3, 5, 7])

    # Create an instance of the Linear Regression model
    model = LinearRegression()

    # Train the model using the sample data
    model.fit(X, y)

    # Make predictions using the trained model
    predictions = model.predict(X)

    # Print the predictions
    print("Predictions: ", predictions)
