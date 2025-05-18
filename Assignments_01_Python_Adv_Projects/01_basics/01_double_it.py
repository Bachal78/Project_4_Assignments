def main():
    # Ask user for a number
    curr_value = int(input("Enter a number: "))

    # Keep doubling and printing the number until it's 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

# Required to call main
if __name__ == '__main__':
    main()
