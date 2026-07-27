"""
Problem #9
Date: 2026-07-27
Task: Write a Python function that implements the Fibonacci sequence three different ways.


# Define a function to calculate the Fibonacci sequence using recursion
def fibonacci_recursive(n):
    # Base cases: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: calculate the nth Fibonacci number as the sum of the two preceding ones
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Define a function to calculate the Fibonacci sequence using iteration
def fibonacci_iterative(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # If n is 0, return 0
    if n == 0:
        return a
    # If n is 1, return 1
    elif n == 1:
        return b
    # Calculate the nth Fibonacci number iteratively
    for _ in range(2, n+1):
        # Update a and b to the next two Fibonacci numbers
        a, b = b, a + b
    # Return the nth Fibonacci number
    return b

# Define a function to calculate the Fibonacci sequence using memoization
def fibonacci_memoized(n, memo={}):
    # Base cases: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # If the nth Fibonacci number is already in the memo dictionary, return it
    elif n in memo:
        return memo[n]
    # Otherwise, calculate the nth Fibonacci number and store it in the memo dictionary
    else:
        result = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
        memo[n] = result
        return result

# Test the functions with an example
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci number at position {n} (recursive): {fibonacci_recursive(n)}")
    print(f"Fibonacci number at position {n} (iterative): {fibonacci_iterative(n)}")
    print(f"Fibonacci number at position {n} (memoized): {fibonacci_memoized(n)}")
