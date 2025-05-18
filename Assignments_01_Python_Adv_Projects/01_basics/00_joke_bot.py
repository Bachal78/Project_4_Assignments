# Constants for messages
PROMPT: str = "What do you want? "
JOKE: str = ("Here is a joke for you--Sophia is heading out to the grocery store. "
             "A programmer tells her: get a liter of milk, and if they have eggs, get 12. "
             "Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'")
SORRY: str = "Sorry I only tell jokes."

def main():
    # Ask the user what they want
    user_input = input(PROMPT)

    # Check if the user exactly typed "Joke"
    if user_input == "Joke" or user_input == "joke":
        print(JOKE)
    else:
        print(SORRY)

# This ensures main() only runs when the script is executed directly
if __name__ == "__main__":
    main()
