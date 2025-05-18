# # Concatenation means joining strings together using the + sign:
# name = "Ali"
# print("Hello, my name is " + name + ".")


# # An f-string is a way to put variables inside a string by adding
# # an f before the string and placing variables inside curly braces {}.

# name = "Ali"
# print(f"Hello, my name is {name}.")


# # The format() method is another way to insert variables into a string.
# # You use curly braces {} as placeholders and call the format() method on the string.
# name = "Ali"
# print("Hello, my name is {}.".format(name))















# # Mad Libs Game
# # This is a simple Mad Libs game where the user inputs words to create a funny story.

# def main():
#     # Welcome message
#     print("Welcome to the Mad Libs Game!\n")

#     # Get words from the user
#     adjective = input("Enter an adjective: ")   # Asking the user to enter a descriptive word
#     noun = input("Enter a noun: ")              # Asking the user to enter a noun (person/place/thing)
#     verb = input("Enter a verb: ")              # Asking the user to enter an action word
#     place = input("Enter a place: ")            # Asking for a place
#     emotion = input("Enter an emotion: ")       # Asking for an emotion (e.g., happy, sad)
#     food = input("Enter a type of food: ")      # Asking for a type of food

#     # Create the story using the inputs
#     story = f"""
#     Today I went to the {place}. 
#     It was a {adjective} day. I saw a {noun} trying to {verb} in the middle of the road! 
#     Everyone looked very {emotion}, but I just laughed and ate my {food}.
#     What a weird day!
#     """

#     # Print the story to the user
#     print("\n Here's your Mad Libs story:")
#     print(story)

# # Run the game
# if __name__ == '__main__':
#     main()   # Starts the game if the script is run directly












def main():
    print("Mad Libs Game")

    adjective= input("enter adjective: ")
    noun= input("enter noun: ")
    verb= input("enter verb: ")

    story= f"""
    Once upon a time, there was a {adjective} {noun} 
    who loved to {verb}."""

    print(story)
    print("Thank you for playing!")

if __name__ == "__main__":
    main()