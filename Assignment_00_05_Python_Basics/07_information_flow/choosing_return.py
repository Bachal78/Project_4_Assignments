# Define the minimum age for adulthood in the U.S.
ADULT_AGE: int = 18

# Function to check if the given age qualifies as an adult
def is_adult(age: int):
    # Return True if age is 18 or older, else return False
    if age >= ADULT_AGE:
        return True
    return False

# Main function to get user input and display the result
def main():
    # Ask the user for their age and convert it to integer
    age = int(input("How old is this person?: "))
    
    # Call the function and print the result (True or False)
    print(is_adult(age))

# Standard Python condition to ensure main runs only when this file is executed directly
if __name__ == "__main__":
    main()
