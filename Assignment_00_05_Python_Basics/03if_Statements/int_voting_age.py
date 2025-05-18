# Set the legal voting ages for three fictional countries
PETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48

def main():
    # Ask the user how old they are and convert the input to an integer
    user_age = int(input("How old are you? "))

    # Check if the user's age is equal to or above the voting age in Peturksbouipo
    if user_age >= PETURKSBOUIPO_AGE:
        # If yes, print a message saying they can vote there
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        # Otherwise, print a message saying they cannot vote there
        print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")

    # Do the same check for Stanlau
    if user_age >= STANLAU_AGE or user_age >=18:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
        print("You can vote in Pakistan where the voting age is above " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")

    # Do the same check for Mayengua
    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")

# This runs the main function only if the script is executed directly
if __name__ == '__main__':
    main()
