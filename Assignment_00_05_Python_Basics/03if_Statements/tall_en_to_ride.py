# MINIMUM_HEIGHT is a constant that sets the required height to ride.
# We use a type hint (int) and set it to 50 units (arbitrary, could be cm/inches).
MINIMUM_HEIGHT: float = 5.5  # #constant #threshold #readability

def main():
    # Ask the user for their height using input().
    # Convert the string input to a float so we can compare it numerically.
    height = float(input("How tall are you? and specify height in decimal: "))  # #input #typecasting #float

    # Check if the user's height is equal to or above the minimum height
    if height >= MINIMUM_HEIGHT:  # #condition #comparison
        print("You're tall enough to ride!")  # #output #success
    else:
        print("You're not tall enough to ride, but maybe next year!")  # #output #failure #encouragement

# This block ensures that the main() function runs only when this file is executed directly.
# It prevents the code from running when the file is imported as a module elsewhere.
if __name__ == '__main__':  # #entrypoint #safetycheck
    main()
