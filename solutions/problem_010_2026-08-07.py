"""
Problem #10
Date: 2026-08-07
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

# Define a basic neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize the weights and biases for the layers
        self.weights1 = np.random.rand(input_size, hidden_size)
        self.bias1 = np.zeros((1, hidden_size))
        self.weights2 = np.random.rand(hidden_size, output_size)
        self.bias2 = np.zeros((1, output_size))

    def forward_pass(self, inputs):
        # Compute the output of the first layer
        hidden_layer = sigmoid(np.dot(inputs, self.weights1) + self.bias1)
        
        # Compute the output of the second layer
        output_layer = sigmoid(np.dot(hidden_layer, self.weights2) + self.bias2)
        
        return output_layer

# Define a basic neural network class with ReLU activation
class NeuralNetworkReLU:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize the weights and biases for the layers
        self.weights1 = np.random.rand(input_size, hidden_size)
        self.bias1 = np.zeros((1, hidden_size))
        self.weights2 = np.random.rand(hidden_size, output_size)
        self.bias2 = np.zeros((1, output_size))

    def forward_pass(self, inputs):
        # Compute the output of the first layer with ReLU activation
        hidden_layer = relu(np.dot(inputs, self.weights1) + self.bias1)
        
        # Compute the output of the second layer with sigmoid activation
        output_layer = sigmoid(np.dot(hidden_layer, self.weights2) + self.bias2)
        
        return output_layer

# Working example
if __name__ == "__main__":
    # Create a neural network with 2 input neurons, 2 hidden neurons, and 1 output neuron
    nn = NeuralNetwork(2, 2, 1)
    
    # Create a neural network with ReLU activation
    nn_relu = NeuralNetworkReLU(2, 2, 1)
    
    # Define the input values
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    
    # Perform the forward pass
    outputs = nn.forward_pass(inputs)
    outputs_relu = nn_relu.forward_pass(inputs)
    
    # Print the outputs
    print("Sigmoid Activation Outputs:")
    print(outputs)
    print("ReLU Activation Outputs:")
    print(outputs_relu)
