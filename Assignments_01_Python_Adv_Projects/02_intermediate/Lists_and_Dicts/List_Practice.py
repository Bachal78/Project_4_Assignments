# Problem #1: List Practice

# Create a list of fruits, display its length, add a new fruit ('mango'), and print the updated list.

# Key Concepts:

# Creating a list
# Using len() to get the number of elements
# Using append() to add a new element
# Printing a list





def main():
    # Create a list called fruit_list that contains the following fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    print("Length of the list:", len(fruit_list))

    # Add 'mango' at the end of the list
    fruit_list.append('mango')

    # Print the updated list
    print("Updated fruit list:", fruit_list)

if __name__ == "__main__":
    main()
