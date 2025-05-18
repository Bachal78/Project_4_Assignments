# Define a function that prints the message multiple times
def print_multiple(message: str, repeats: int):
    # Loop to repeat the message 'repeats' number of times
    for i in range(repeats):
        print(message)

# This is the main function that handles input from the user
def main():
    # Prompt the user to type a message
    message = input("Please type a message: ")
    
    # Prompt the user to enter how many times to repeat the message
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the print_multiple function with the provided inputs
    print_multiple(message, repeats)

# This line ensures the main() function runs when the file is executed directly
if __name__ == '__main__':
    main()
