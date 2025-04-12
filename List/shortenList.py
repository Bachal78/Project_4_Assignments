# Define the maximum allowed length of the list
MAX_LENGTH: int = 3  # This constant controls how many items the list should have at most

def shorten(lst):
    """
    Removes elements from the end of the list until it is MAX_LENGTH long.
    Prints each removed element.
    """
    while len(lst) > MAX_LENGTH:  # Continue as long as the list is too long
        last_elem = lst.pop()     # Remove the last item in the list
        print(last_elem)          # Print the item that was removed

def get_lst():
    """
    Prompts the user to enter one element of the list at a time.
    Stops when the user presses enter with no input.
    Returns the completed list.
    """
    lst = []  # Start with an empty list

    # Ask the user for input
    elem = input("Please enter an element of the list or press enter to stop. ")

    # Keep asking for input until the user presses enter with no input
    while elem != "":
        lst.append(elem)  # Add the input element to the list
        elem = input("Please enter an element of the list or press enter to stop. ")  # Ask again

    return lst  # Return the final list

def main():
    lst = get_lst()     # Get a list from the user
    shorten(lst)        # Call the shorten function to limit its size and print removed elements

# This ensures main() runs only when this script is executed directly (not imported)
if __name__ == '__main__':
    main()
