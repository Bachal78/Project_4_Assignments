# Function to check if a number n is between low and high (inclusive)
def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

# Main function to get user input and test the in_range function
def main():
    # Get user inputs for the number, lower bound, and upper bound
    n = int(input("Enter the number to check: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    # Call the in_range function and print result
    result = in_range(n, low, high)
    print("Is the number in range?", result)

# Ensures the main function only runs when the script is executed directly
if __name__ == '__main__':
    main()
