# This function returns the number of specific fruits in stock.
def num_in_stock(fruit):
    """
    This function returns the number of a given fruit Sophia has in stock.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        # If the fruit is not listed, return 0
        return 0

# Main function where user interaction happens
def main():
    # Ask the user to enter the name of a fruit
    fruit = input("Enter a fruit: ")

    # Get the number of that fruit in stock
    stock = num_in_stock(fruit)

    # Check if the fruit is in stock or not
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

# This ensures main() only runs when this script is executed directly
if __name__ == '__main__':
    main()
