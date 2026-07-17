"""
Problem #9
Date: 2026-07-17
Task: Write a Python function that implements the Fibonacci sequence three different ways.


# Method 1: Recursive Fibonacci
def fibonacci_recursive(n):
    # Base cases: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: call fibonacci_recursive with n-1 and n-2
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Method 2: Iterative Fibonacci
def fibonacci_iterative(n):
    # Initialize variables to store the last two Fibonacci numbers
    a, b = 0, 1
    # If n is 0, return 0
    if n == 0:
        return 0
    # Iterate from 2 to n (inclusive)
    for _ in range(2, n+1):
        # Update a and b to the next two Fibonacci numbers
        a, b = b, a + b
    # Return the nth Fibonacci number
    return b

# Method 3: Memoized Fibonacci (using a dictionary to store previously computed values)
def fibonacci_memoized(n, memo={}):
    # Base cases: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # If n is already in the memo dictionary, return its value
    elif n in memo:
        return memo[n]
    # Otherwise, compute the nth Fibonacci number and store it in the memo dictionary
    else:
        result = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
        memo[n] = result
        return result

# Example usage:
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci number at position {n} (recursive): {fibonacci_recursive(n)}")
    print(f"Fibonacci number at position {n} (iterative): {fibonacci_iterative(n)}")
    print(f"Fibonacci number at position {n} (memoized): {fibonacci_memoized(n)}")
