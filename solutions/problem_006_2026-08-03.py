"""
Problem #6
Date: 2026-08-03
Task: Write a Python implementation of a binary search algorithm with clear comments.


# Define a function for binary search
def binary_search(array, target):
    # Initialize two pointers, one at the start and one at the end of the array
    left = 0
    right = len(array) - 1
    
    # Continue searching while the two pointers haven't crossed each other
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the target is found at the middle index, return it
        if array[mid] == target:
            return mid
        
        # If the target is less than the middle element, move the right pointer
        elif array[mid] > target:
            right = mid - 1
        
        # If the target is greater than the middle element, move the left pointer
        else:
            left = mid + 1
    
    # If the target is not found, return -1
    return -1

# Define a main function with a working example
def main():
    # Create a sorted array
    array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    
    # Define a target value to search for
    target = 23
    
    # Call the binary search function
    result = binary_search(array, target)
    
    # Print the result
    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the array.")

# Run the main function
if __name__ == "__main__":
    main()
