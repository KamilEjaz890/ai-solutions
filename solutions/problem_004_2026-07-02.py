"""
Problem #4
Date: 2026-07-02
Task: Write a Python function that implements bubble sort and explains how it works step by step.


# Define a function called bubble_sort that takes a list as input
def bubble_sort(nums):
    # Get the length of the input list
    n = len(nums)
    
    # Iterate over the list n-1 times (since the last element will be in place after n-1 passes)
    for i in range(n-1):
        # Initialize a flag to track if any swaps were made in the current pass
        swapped = False
        
        # Iterate over the list from the first element to the (n-i-1)th element
        for j in range(n-i-1):
            # If the current element is greater than the next element, swap them
            if nums[j] > nums[j+1]:
                # Swap the elements
                nums[j], nums[j+1] = nums[j+1], nums[j]
                # Set the flag to True to indicate that a swap was made
                swapped = True
        
        # If no swaps were made in the current pass, the list is already sorted
        if not swapped:
            break
    
    # Return the sorted list
    return nums

# Example usage:
if __name__ == "__main__":
    # Define a list of numbers
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    # Print the original list
    print("Original list:", numbers)
    
    # Sort the list using bubble sort
    sorted_numbers = bubble_sort(numbers)
    
    # Print the sorted list
    print("Sorted list:", sorted_numbers)
