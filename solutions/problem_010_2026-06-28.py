"""
Problem #10
Date: 2026-06-28
Task: Write a Python script that simulates a basic neural network forward pass using only numpy.


# Import the numpy library for numerical operations
import numpy as np

# Define a function to perform sigmoid activation
def sigmoid(x):
    # The sigmoid function maps any real number to a value between 0 and 1
    return 1 / (1 + np.exp(-x))

# Define a function to perform ReLU activation
def relu(x):
    # The ReLU function maps all negative numbers to 0 and all positive numbers to themselves
    return np.maximum(x, 0)

# Define a NeuralNetwork class
class NeuralNetwork:
    # Initialize the neural network with input size, hidden size, and output size
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases for the layers
        self.weights1 = np.random.rand(input_size, hidden_size)
        self.weights2 = np.random.rand(hidden_size, output_size)
        self.bias1 = np.zeros((1, hidden_size))
        self.bias2 = np.zeros((1, output_size))

    # Define a method to perform the forward pass
    def forward(self, inputs):
        # Calculate the output of the first layer using the weights, biases, and ReLU activation
        hidden_layer = relu(np.dot(inputs, self.weights1) + self.bias1)
        
        # Calculate the output of the second layer using the weights, biases, and sigmoid activation
        output_layer = sigmoid(np.dot(hidden_layer, self.weights2) + self.bias2)
        
        # Return the output of the neural network
        return output_layer

# Create a neural network with 2 inputs, 2 hidden units, and 1 output
nn = NeuralNetwork(2, 2, 1)

# Create an input array
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Perform the forward pass
outputs = nn.forward(inputs)

# Print the outputs
print(outputs)
