"""
Problem #9
Date: 2026-05-28
Task: Write a Python function that implements the Fibonacci sequence three different ways.


# Define a function to calculate the Fibonacci sequence using recursion
def fibonacci_recursive(n):
    # Base cases: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: return the sum of the two preceding numbers
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Define a function to calculate the Fibonacci sequence using iteration
def fibonacci_iterative(n):
    # Initialize the first two numbers in the sequence
    a, b = 0, 1
    # If n is 0, return 0
    if n == 0:
        return a
    # If n is 1, return 1
    elif n == 1:
        return b
    # Iterate from 2 to n (inclusive) to calculate the sequence
    for _ in range(2, n+1):
        # Update a and b to the next two numbers in the sequence
        a, b = b, a + b
    # Return the nth number in the sequence
    return b

# Define a function to calculate the Fibonacci sequence using memoization
def fibonacci_memoization(n, memo = {}):
    # Base cases: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # If the result is already in the memo dictionary, return it
    elif n in memo:
        return memo[n]
    # Otherwise, calculate the result and store it in the memo dictionary
    else:
        result = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
        memo[n] = result
        return result

# Test the functions with an example
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci number at position {n} (recursive): {fibonacci_recursive(n)}")
    print(f"Fibonacci number at position {n} (iterative): {fibonacci_iterative(n)}")
    print(f"Fibonacci number at position {n} (memoization): {fibonacci_memoization(n)}")
