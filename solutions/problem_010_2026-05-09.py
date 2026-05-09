"""
Problem #10
Date: 2026-05-09
Task: Write a Python script that simulates a basic neural network forward pass using only numpy.


# Import the numpy library for numerical computations
import numpy as np

# Define a function to compute the sigmoid activation function
def sigmoid(x):
    # The sigmoid function maps any real number to a value between 0 and 1
    return 1 / (1 + np.exp(-x))

# Define a function to compute the ReLU activation function
def relu(x):
    # The ReLU function maps all negative numbers to 0 and all non-negative numbers to themselves
    return np.maximum(x, 0)

# Define a NeuralNetwork class to simulate a basic neural network
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize the weights and biases for the layers
        self.weights1 = np.random.rand(input_size, hidden_size)
        self.weights2 = np.random.rand(hidden_size, output_size)
        self.bias1 = np.zeros((1, hidden_size))
        self.bias2 = np.zeros((1, output_size))

    def forward_pass(self, inputs):
        # Compute the output of the first layer using the sigmoid activation function
        hidden_layer = sigmoid(np.dot(inputs, self.weights1) + self.bias1)
        
        # Compute the output of the second layer using the ReLU activation function
        output_layer = relu(np.dot(hidden_layer, self.weights2) + self.bias2)
        
        return output_layer

# Create a NeuralNetwork instance with 2 input neurons, 2 hidden neurons, and 1 output neuron
nn = NeuralNetwork(2, 2, 1)

# Create a sample input
inputs = np.array([[0.5, 0.3]])

# Perform a forward pass through the network
output = nn.forward_pass(inputs)

# Print the output of the network
print("Output:", output)
