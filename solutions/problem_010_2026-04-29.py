"""
Problem #10
Date: 2026-04-29
Task: Write a Python script that simulates a basic neural network forward pass using only numpy.


# Import the numpy library for numerical operations
import numpy as np

# Define a function to perform the sigmoid activation function
def sigmoid(x):
    # The sigmoid function maps any real number to a value between 0 and 1
    return 1 / (1 + np.exp(-x))

# Define a function to perform the ReLU activation function
def relu(x):
    # The ReLU function returns 0 for any negative input and the input itself for any positive input
    return np.maximum(x, 0)

# Define a NeuralNetwork class to encapsulate the neural network's properties and methods
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize the weights and biases for the layers
        self.weights1 = np.random.rand(input_size, hidden_size)
        self.weights2 = np.random.rand(hidden_size, output_size)
        self.bias1 = np.zeros((1, hidden_size))
        self.bias2 = np.zeros((1, output_size))

    def forward_pass(self, inputs):
        # Perform the forward pass through the neural network
        # First, calculate the output of the hidden layer
        hidden_layer = sigmoid(np.dot(inputs, self.weights1) + self.bias1)
        
        # Then, calculate the output of the output layer
        output_layer = sigmoid(np.dot(hidden_layer, self.weights2) + self.bias2)
        
        return output_layer

# Create a NeuralNetwork instance with 2 input neurons, 2 hidden neurons, and 1 output neuron
nn = NeuralNetwork(2, 2, 1)

# Create a sample input
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Perform the forward pass
output = nn.forward_pass(inputs)

# Print the output
print(output)
