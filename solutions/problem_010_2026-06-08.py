"""
Problem #10
Date: 2026-06-08
Task: Write a Python script that simulates a basic neural network forward pass using only numpy.


# Import the numpy library for numerical operations
import numpy as np

# Define a function to compute the sigmoid activation function
def sigmoid(x):
    # The sigmoid function maps any real number to a value between 0 and 1
    return 1 / (1 + np.exp(-x))

# Define a function to compute the ReLU activation function
def relu(x):
    # The ReLU function maps all negative numbers to 0 and all positive numbers to themselves
    return np.maximum(x, 0)

# Define a NeuralNetwork class to encapsulate the neural network's properties and methods
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize the weights and biases for the neural network
        # Weights are initialized with random values, and biases are initialized with zeros
        self.weights1 = np.random.rand(input_size, hidden_size)
        self.weights2 = np.random.rand(hidden_size, output_size)
        self.bias1 = np.zeros((1, hidden_size))
        self.bias2 = np.zeros((1, output_size))

    def forward_pass(self, inputs):
        # Compute the output of the first layer (hidden layer) using the sigmoid activation function
        hidden_layer = sigmoid(np.dot(inputs, self.weights1) + self.bias1)
        
        # Compute the output of the second layer (output layer) using the ReLU activation function
        output_layer = relu(np.dot(hidden_layer, self.weights2) + self.bias2)
        
        # Return the output of the neural network
        return output_layer

# Create an instance of the NeuralNetwork class
nn = NeuralNetwork(2, 2, 1)

# Define input values for the neural network
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Perform a forward pass through the neural network
outputs = nn.forward_pass(inputs)

# Print the output of the neural network
print(outputs)
