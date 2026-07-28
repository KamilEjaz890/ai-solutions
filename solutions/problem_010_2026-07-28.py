"""
Problem #10
Date: 2026-07-28
Task: Write a Python script that simulates a basic neural network forward pass using only numpy.


# Import the numpy library for numerical operations
import numpy as np

# Define a function to perform the sigmoid activation function
def sigmoid(x):
    # The sigmoid function maps any real number to a value between 0 and 1
    return 1 / (1 + np.exp(-x))

# Define a function to perform the ReLU activation function
def relu(x):
    # The ReLU function returns 0 for negative numbers and the number itself for positive numbers
    return np.maximum(x, 0)

# Define a class to represent a basic neural network layer
class NeuralNetworkLayer:
    def __init__(self, input_size, output_size):
        # Initialize the layer with random weights and biases
        self.weights = np.random.rand(input_size, output_size)
        self.biases = np.random.rand(1, output_size)

    def forward_pass(self, inputs):
        # Perform the forward pass by multiplying the inputs with the weights and adding the biases
        linear_output = np.dot(inputs, self.weights) + self.biases
        # Apply the sigmoid activation function to the linear output
        return sigmoid(linear_output)

# Define a class to represent a neural network with multiple layers
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize the neural network with two layers: input to hidden and hidden to output
        self.layer1 = NeuralNetworkLayer(input_size, hidden_size)
        self.layer2 = NeuralNetworkLayer(hidden_size, output_size)

    def forward_pass(self, inputs):
        # Perform the forward pass through the first layer
        hidden_layer_output = self.layer1.forward_pass(inputs)
        # Apply the ReLU activation function to the hidden layer output
        hidden_layer_output = relu(hidden_layer_output)
        # Perform the forward pass through the second layer
        output_layer_output = self.layer2.forward_pass(hidden_layer_output)
        return output_layer_output

# Create a neural network with 2 input neurons, 2 hidden neurons, and 1 output neuron
nn = NeuralNetwork(2, 2, 1)

# Create a sample input
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Perform the forward pass
outputs = nn.forward_pass(inputs)

# Print the outputs
print(outputs)
