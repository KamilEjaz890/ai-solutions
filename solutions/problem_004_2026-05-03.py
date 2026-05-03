"""
Problem #4
Date: 2026-05-03
Task: Write a Python function that implements bubble sort and explains how it works step by step.


# Define a function to implement bubble sort
def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Iterate over the array from the first element to the second last element
    for i in range(n - 1):
        # Initialize a flag to check if any swaps were made in the current iteration
        swapped = False
        
        # Iterate over the array from the first element to the (n - i - 1)th element
        for j in range(n - i - 1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to True
                swapped = True
        
        # If no swaps were made in the current iteration, the array is already sorted
        if not swapped:
            break
    
    # Return the sorted array
    return arr

# Define a main function to test the bubble sort function
def main():
    # Create an example array
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    # Print the original array
    print("Original array:", arr)
    
    # Sort the array using bubble sort
    sorted_arr = bubble_sort(arr)
    
    # Print the sorted array
    print("Sorted array:", sorted_arr)

# Call the main function
if __name__ == "__main__":
    main()
