def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    # print(lst[0])  # Access and print the first element in the list
    # print(lst[len(lst) - 1])  # Access and print the last element in the list using length
    print(lst[-1])  # Access and print the last element in the list using negative indexing



def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []  # Initialize an empty list to store user inputs

    # Ask the user for input
    elem: str = input("Please enter an element of the list or press enter to stop. ")

    # Loop until the user presses Enter without typing anything
    while elem != "":
        lst.append(elem)  # Add the element to the list
        elem = input("Please enter an element of the list or press enter to stop. ")  # Prompt again

    return lst  # Return the completed list


def main():
    lst = get_lst()          # Get the list from the user
    get_first_element(lst)   # Print the first element of the list


if __name__ == '__main__':
    main()  # Start the program by calling main() if this file is run directly
