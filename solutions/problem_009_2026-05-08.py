"""
Problem #9
Date: 2026-05-08
Task: Write a Python function that implements the Fibonacci sequence three different ways.


# Method 1: Recursive Fibonacci function
def fibonacci_recursive(n):
    # Base cases: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: call the function with n-1 and n-2
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Method 2: Iterative Fibonacci function
def fibonacci_iterative(n):
    # Initialize the first two numbers in the sequence
    a, b = 0, 1
    # If n is 0, return 0
    if n == 0:
        return a
    # If n is 1, return 1
    elif n == 1:
        return b
    # Iterate from 2 to n (inclusive)
    for _ in range(2, n+1):
        # Update a and b to the next two numbers in the sequence
        a, b = b, a + b
    # Return the nth number in the sequence
    return b

# Method 3: Memoized Fibonacci function
def fibonacci_memoized(n, memo={}):
    # Base cases: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # If n is already in the memo dictionary, return its value
    elif n in memo:
        return memo[n]
    # Otherwise, calculate the nth number and store it in the memo dictionary
    else:
        result = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
        memo[n] = result
        return result

# Example usage:
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci({n}) using recursive method: {fibonacci_recursive(n)}")
    print(f"Fibonacci({n}) using iterative method: {fibonacci_iterative(n)}")
    print(f"Fibonacci({n}) using memoized method: {fibonacci_memoized(n)}")
