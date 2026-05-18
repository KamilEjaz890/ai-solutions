"""
Problem #9
Date: 2026-05-18
Task: Write a Python function that implements the Fibonacci sequence three different ways.


# Define a function to calculate the Fibonacci sequence using recursion
def fibonacci_recursive(n):
    # Base cases for the recursion
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Define a function to calculate the Fibonacci sequence using iteration
def fibonacci_iterative(n):
    # Initialize the first two numbers in the sequence
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    # Calculate the rest of the sequence
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Define a function to calculate the Fibonacci sequence using memoization
def fibonacci_memoization(n, memo={}):
    # Base cases for the recursion
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # Check if the result is already in the memo dictionary
    elif n in memo:
        return memo[n]
    # If not, calculate the result and store it in the memo dictionary
    else:
        result = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
        memo[n] = result
        return result

# Test the functions
print("Fibonacci Recursive:", fibonacci_recursive(10))
print("Fibonacci Iterative:", fibonacci_iterative(10))
print("Fibonacci Memoization:", fibonacci_memoization(10))
