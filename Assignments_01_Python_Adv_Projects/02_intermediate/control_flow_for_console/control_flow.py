import random

NUM_ROUNDS = 5

def get_valid_guess():
    while True:
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        if guess == "higher" or guess == "lower":
            return guess
        else:
            print("Please enter either 'higher' or 'lower'.")

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {user_number}")
        guess = get_valid_guess()
        
        is_correct = False
        if guess == "higher" and user_number > computer_number:
            is_correct = True
        elif guess == "lower" and user_number < computer_number:
            is_correct = True
        
        if is_correct:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")
        print()

    # End of game message
    print("Thanks for playing!")
    print(f"Your final score was: {score}")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()
import random  # Import the random module to generate random numbers

NUM_ROUNDS = 5  # Constant to define how many rounds the game will have

# Function to get a valid guess from the user: must be either "higher" or "lower"
def get_valid_guess():
    while True:  # Keep asking until a valid guess is provided
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        if guess == "higher" or guess == "lower":  # Accept only valid inputs
            return guess
        else:
            print("Please enter either 'higher' or 'lower'.")  # Ask again if input is invalid

# Main function where the game logic runs
def main():
    print("Welcome to the High-Low Game!")  # Game welcome message
    print("--------------------------------")

    score = 0  # Initialize player score to 0

    # Loop for each round from 1 to NUM_ROUNDS (inclusive)
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")  # Show round number

        # Generate random numbers for player and computer (1 to 100 inclusive)
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {user_number}")  # Show user's number
        guess = get_valid_guess()  # Ask user if their number is higher or lower

        is_correct = False  # Variable to track if user's guess is correct

        # Determine if the user's guess is correct based on the numbers
        if guess == "higher" and user_number > computer_number:
            is_correct = True
        elif guess == "lower" and user_number < computer_number:
            is_correct = True

        # Print result and update score
        if is_correct:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Increase score for correct guess
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}")  # Display updated score
        print()  # Print blank line for visual separation

    # After all rounds, show final results
    print("Thanks for playing!")  # Thank you message
    print(f"Your final score was: {score}")  # Final score display

    # Final message based on performance
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")  # Perfect score message
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")  # Decent score message
    else:
        print("Better luck next time!")  # Low score message

# Run the game if this file is executed directly
if __name__ == '__main__':
    main()
