"""
Problem #10
Date: 2026-05-29
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

# Define a class to represent a neural network layer
class NeuralNetworkLayer:
    # Initialize the layer with the number of inputs, the number of neurons, and the activation function
    def __init__(self, num_inputs, num_neurons, activation_function):
        # Initialize the weights randomly with a small value
        self.weights = np.random.rand(num_inputs, num_neurons) * 0.1
        # Initialize the biases to zero
        self.biases = np.zeros((1, num_neurons))
        # Store the activation function
        self.activation_function = activation_function

    # Define a method to perform the forward pass through the layer
    def forward(self, inputs):
        # Calculate the weighted sum of the inputs and weights, and add the biases
        weighted_sum = np.dot(inputs, self.weights) + self.biases
        # Apply the activation function to the weighted sum
        if self.activation_function == 'sigmoid':
            return sigmoid(weighted_sum)
        elif self.activation_function == 'relu':
            return relu(weighted_sum)
        else:
            raise ValueError("Invalid activation function")

# Define a class to represent the neural network
class NeuralNetwork:
    # Initialize the neural network with the number of inputs, the number of hidden neurons, and the number of outputs
    def __init__(self, num_inputs, num_hidden, num_outputs):
        # Create the hidden layer
        self.hidden_layer = NeuralNetworkLayer(num_inputs, num_hidden, 'relu')
        # Create the output layer
        self.output_layer = NeuralNetworkLayer(num_hidden, num_outputs, 'sigmoid')

    # Define a method to perform the forward pass through the neural network
    def forward(self, inputs):
        # Perform the forward pass through the hidden layer
        hidden_outputs = self.hidden_layer.forward(inputs)
        # Perform the forward pass through the output layer
        output = self.output_layer.forward(hidden_outputs)
        return output

# Create a neural network with 2 inputs, 2 hidden neurons, and 1 output
neural_network = NeuralNetwork(2, 2, 1)

# Create an input array
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Perform the forward pass through the neural network
outputs = neural_network.forward(inputs)

# Print the outputs
print(outputs)
