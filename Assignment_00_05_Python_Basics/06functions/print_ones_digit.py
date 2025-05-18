# Function to print the ones digit of a given number
def print_ones_digit(num):
    # Using modulo operator to get the last digit (ones digit)
    print("The ones digit is", num % 10)

# Main function to take input from user and call the above function
def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    
    # Call the function with the entered number
    print_ones_digit(num)

# Standard line to call main() when the script is run directly
if __name__ == '__main__':
    main()
