def main():
    # Get the year to check from the user and convert the input to an integer
    year = int(input('Please input a year: '))

    # First condition: check if the year is divisible by 4
    if year % 4 == 0:
        # If it is divisible by 4, check if it is also divisible by 100
        if year % 100 == 0:
            # If it is divisible by 100, check if it is also divisible by 400
            if year % 400 == 0:
                # If divisible by 400, then it's definitely a leap year
                print("That's a leap year!")
            else:
                # If divisible by 100 but not by 400, then it's not a leap year
                print("That's not a leap year.")
        else:
            # If divisible by 4 but NOT divisible by 100, it's a leap year
            print("That's a leap year!")
    else:
        # If not divisible by 4 at all, it's not a leap year
        print("That's not a leap year.")


# This ensures the main function is called only when the script is executed directly
if __name__ == '__main__':
    main()
