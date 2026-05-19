"""
Problem #10
Date: 2026-05-19
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

# Define a function to perform a basic neural network forward pass
def neural_network_forward_pass(inputs, weights1, weights2, bias1, bias2):
    # Calculate the output of the first layer using the weights and bias
    hidden_layer = sigmoid(np.dot(inputs, weights1) + bias1)
    
    # Calculate the output of the second layer using the weights and bias
    output_layer = sigmoid(np.dot(hidden_layer, weights2) + bias2)
    
    # Return the output of the neural network
    return output_layer

# Define a function to perform a neural network forward pass with ReLU activation
def neural_network_forward_pass_relu(inputs, weights1, weights2, bias1, bias2):
    # Calculate the output of the first layer using the weights and bias
    hidden_layer = relu(np.dot(inputs, weights1) + bias1)
    
    # Calculate the output of the second layer using the weights and bias
    output_layer = sigmoid(np.dot(hidden_layer, weights2) + bias2)
    
    # Return the output of the neural network
    return output_layer

# Working example
if __name__ == "__main__":
    # Define the inputs to the neural network
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

    # Define the weights and biases for the neural network
    weights1 = np.array([[1, 1], [1, 1]])
    weights2 = np.array([[1], [1]])
    bias1 = np.array([0, 0])
    bias2 = np.array([0])

    # Perform the neural network forward pass
    output = neural_network_forward_pass(inputs, weights1, weights2, bias1, bias2)
    output_relu = neural_network_forward_pass_relu(inputs, weights1, weights2, bias1, bias2)

    # Print the output of the neural network
    print("Neural Network Output (Sigmoid):")
    print(output)
    print("Neural Network Output (ReLU):")
    print(output_relu)
