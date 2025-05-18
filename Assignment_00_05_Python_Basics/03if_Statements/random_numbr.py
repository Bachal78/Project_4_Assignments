import random  # To generate random numbers

# Constants
N_NUMBERS: int = 10         # Total numbers to generate
MIN_VALUE: int = 1         # Minimum value of each random number
MAX_VALUE: int = 100        # Maximum value of each random number

def main():
    # Create an empty list to store random numbers
    random_numbers = []

    # Generate N_NUMBERS random numbers
    for _ in range(N_NUMBERS):
        num = random.randint(MIN_VALUE, MAX_VALUE)  # Random number between MIN_VALUE and MAX_VALUE
        random_numbers.append(num)  # Add the number to our list

    # Print the list of random numbers
    print("Generated numbers:", random_numbers)

    # Calculate and print statistics
    print("Sum:", sum(random_numbers))                       # Total sum of the numbers
    print("Average:", sum(random_numbers) / N_NUMBERS)       # Average of the numbers
    print("Max:", max(random_numbers))                       # Largest number
    print("Min:", min(random_numbers))                       # Smallest number

# Run the program
if __name__ == '__main__':
    main()
