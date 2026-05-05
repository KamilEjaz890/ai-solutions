"""
Problem #6
Date: 2026-05-05
Task: Write a Python implementation of a binary search algorithm with clear comments.


# Define a function for binary search
def binary_search(arr, target):
    # Initialize two pointers, one at the start and one at the end of the array
    left = 0
    right = len(arr) - 1
    
    # Continue searching while the two pointers haven't crossed each other
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the target is found at the middle index, return the index
        if arr[mid] == target:
            return mid
        # If the target is less than the middle element, move the right pointer
        elif arr[mid] > target:
            right = mid - 1
        # If the target is greater than the middle element, move the left pointer
        else:
            left = mid + 1
    
    # If the target is not found, return -1
    return -1

# Define a main function to test the binary search
def main():
    # Create a sorted array
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    
    # Set a target value to search for
    target = 23
    
    # Call the binary search function and store the result
    result = binary_search(arr, target)
    
    # Print the result
    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the array.")

# Call the main function
if __name__ == "__main__":
    main()
