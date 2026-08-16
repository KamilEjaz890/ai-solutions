"""
Problem #9
Date: 2026-08-16
Task: Write a Python function that implements the Fibonacci sequence three different ways.


# Define a function to generate the Fibonacci sequence using recursion
def fibonacci_recursive(n):
    # Base cases: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: return the sum of the two preceding numbers
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Define a function to generate the Fibonacci sequence using iteration
def fibonacci_iterative(n):
    # Initialize the first two numbers in the sequence
    a, b = 0, 1
    # Initialize an empty list to store the sequence
    sequence = []
    # Generate the sequence up to the nth number
    for _ in range(n+1):
        # Append the current number to the sequence
        sequence.append(a)
        # Update the current numbers for the next iteration
        a, b = b, a + b
    # Return the sequence
    return sequence

# Define a function to generate the Fibonacci sequence using memoization
def fibonacci_memoized(n, memo={}):
    # Base cases: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Check if the result is already in the memo dictionary
    elif n in memo:
        return memo[n]
    # If not, calculate the result and store it in the memo dictionary
    else:
        result = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
        memo[n] = result
        return result

# Example usage:
if __name__ == "__main__":
    n = 10
    print("Fibonacci sequence using recursion:")
    print([fibonacci_recursive(i) for i in range(n+1)])
    print("Fibonacci sequence using iteration:")
    print(fibonacci_iterative(n))
    print("Fibonacci sequence using memoization:")
    print([fibonacci_memoized(i) for i in range(n+1)])
