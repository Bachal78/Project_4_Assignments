import random  # Importing random module to generate random numbers
import time    # Importing time module to measure performance of functions

# -------------------------------------------
# Naive Search Function: O(n) time complexity
# -------------------------------------------
def naive_search(l, target):
    # Loop through each index and value in list l
    for i in range(len(l)):
        if l[i] == target:  # Check if current element matches the target
            return i        # If found, return the index
    return -1               # If not found, return -1

# ---------------------------------------------------
# Binary Search Function: O(log n) time complexity
# This function uses divide-and-conquer on sorted list
# ---------------------------------------------------
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0  # Set low to beginning of list if not provided
    if high is None:
        high = len(l) - 1  # Set high to end of list if not provided

    if high < low:
        return -1  # If bounds cross, target not found

    midpoint = (low + high) // 2  # Find the midpoint index

    if l[midpoint] == target:     # If middle value is target
        return midpoint           # Return the midpoint index
    elif target < l[midpoint]:    # If target is smaller than middle value
        return binary_search(l, target, low, midpoint - 1)  # Search in left half
    else:
        return binary_search(l, target, midpoint + 1, high)  # Search in right half

# ------------------------------------------
# Main execution block — entry point of code
# ------------------------------------------
if __name__ == '__main__':
    length = 10000  # Define the size of the list

    # Create a set to store unique random integers
    sorted_list = set()
    while len(sorted_list) < length:
        # Add random integers between -30000 and 30000
        sorted_list.add(random.randint(-3 * length, 3 * length))

    # Convert set to a sorted list
    sorted_list = sorted(list(sorted_list))

    # --------------------------
    # Measure Naive Search Time
    # --------------------------
    start = time.time()  # Start time for naive search
    for target in sorted_list:
        naive_search(sorted_list, target)  # Call naive search for each element
    end = time.time()  # End time for naive search
    print("Naive search time: ", (end - start), "seconds")  # Print duration

    # --------------------------
    # Measure Binary Search Time
    # --------------------------
    start = time.time()  # Start time for binary search
    for target in sorted_list:
        binary_search(sorted_list, target)  # Call binary search for each element
    end = time.time()  # End time for binary search
    print("Binary search time: ", (end - start), "seconds")  # Print duration
