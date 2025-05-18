def main():
    # This for-loop starts at 0 and goes up to (but does not include) 20
    # So it runs 20 times: i will be 0, 1, 2, ..., 19
    for i in range(20):
        # For each number i, multiply it by 2 and print the result
        print(i * 2)  # This prints the even numbers from 0 to 38

# This part checks if the script is being run directly (not imported),
# and if so, it calls the main() function to start the program.
if __name__ == "__main__":
    main()
