# Problem #2: Index Game

# Build a text-based game that lets users interact with a list in three ways:
# Accessing an element by index
# Modifying an element at a specific index
# Slicing the list from one index to another

# Key Concepts:

# Indexing and bounds checking
# Updating elements in a list
# Slicing lists with a range
# Taking user input for choices and indices
# Loop and conditionals for a simple menu-driven interface



def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    if 0 <= start <= end <= len(lst):
        return lst[start:end]
    else:
        return "Invalid slice range."

def main():
    elements = [10, "apple", 3.14, "banana", 42]

    while True:
        print("\nChoose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print("Result:", access_element(elements, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            result = modify_element(elements, index, new_val)
            print("Updated List:", result)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slice_list(elements, start, end))

        elif choice == '4':
            print("Exiting the game.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
