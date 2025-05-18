import random

def main():
    # Generate the secret number at random!
    secret_number: int = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Get user's first guess
    guess = int(input("Enter a guess: "))
    
    # Loop until the guess is correct
    while guess != secret_number:
        if guess < secret_number:  # If the guess is too low
            print("Your guess is too low")
        else:  # If the guess is too high
            print("Your guess is too high")
        
        print()  # Print a blank line for better formatting
        guess = int(input("Enter a new guess: "))  # Ask for a new guess
    
    print("Congrats! The number was: " + str(secret_number))

# Call the main function
if __name__ == '__main__':
    main()
