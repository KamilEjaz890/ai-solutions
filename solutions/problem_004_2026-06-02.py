"""
Problem #4
Date: 2026-06-02
Task: Write a Python function that implements bubble sort and explains how it works step by step.


# Define a function to implement bubble sort
def bubble_sort(arr):
    # Get the length of the input array
    n = len(arr)
    
    # Iterate over the array from the first element to the second last element
    for i in range(n - 1):
        # Initialize a flag to track if any swaps were made in the current iteration
        swapped = False
        
        # Iterate over the array from the first element to the (n - i - 1)th element
        for j in range(n - i - 1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to True to indicate that a swap was made
                swapped = True
        
        # If no swaps were made in the current iteration, the array is already sorted
        if not swapped:
            break
    
    # Return the sorted array
    return arr

# Example usage:
if __name__ == "__main__":
    # Define an example array
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    # Print the original array
    print("Original array:", arr)
    
    # Sort the array using bubble sort
    sorted_arr = bubble_sort(arr)
    
    # Print the sorted array
    print("Sorted array:", sorted_arr)
