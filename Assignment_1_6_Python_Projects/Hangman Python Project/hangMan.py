import random
import string

# A simple built-in word list to play with
words = ["python", "hangman", "developer", "keyboard", "laptop", "algorithm", "programming", "function", "variable", "debug"]

def get_valid_word(words):
    word = random.choice(words)  # Randomly select a word from the list
    while '-' in word or ' ' in word:  # Ensure the word doesn't contain hyphens or spaces
        word = random.choice(words)
    return word.upper()  # Convert the word to uppercase for consistency

def hangman():
    word = get_valid_word(words)  # Get a valid word for the game
    word_letters = set(word)  # Create a set of letters in the word
    alphabet = set(string.ascii_uppercase)  # Set of uppercase letters
    used_letters = set()  # Set to keep track of guessed letters

    lives = 6  # Number of lives

    while len(word_letters) > 0 and lives > 0:
        # Show current game info
        print("You have", lives, "lives left and used these letters:", ' '.join(used_letters))

        # Display current progress in the word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", ' '.join(word_list))

        # Get user input
        user_letter = input("Guess a letter: ").upper()

        # If it's a new valid letter
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in the word.")

        # Already guessed letter
        elif user_letter in used_letters:
            print("You already guessed that letter.")

        # Invalid character
        else:
            print("Invalid character. Please try again.")

    # Game result
    if lives == 0:
        print("You died. The word was", word)
    else:
        print("Yay! You guessed the word", word, "!!")

# Start the game
hangman()
