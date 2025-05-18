# This is the main function
def main():
    num: int = 7  # Start with the value 7
    num = subtract_seven(num)  # Call function to subtract 7 from num and assign result back to num
    print("this should be zero: ", num)  # Output the result, should be 0

# This function subtracts 7 from the input number
def subtract_seven(num):
    num = num - 7  # Subtract 7
    return num  # Return the result

# Python standard boilerplate to call main only when this script is run directly
if __name__ == '__main__':
    main()
