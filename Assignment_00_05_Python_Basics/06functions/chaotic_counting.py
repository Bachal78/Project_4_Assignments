import random

DONE_LIKELIHOOD = 0.2  # Chance of stopping early (feel free to adjust)

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # End function and return control to main()
        print(curr_num, end=" ")  # Print on the same line

def done():
    """Returns True with a probability of DONE_LIKELIHOOD"""
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done")

if __name__ == "__main__":
    main()
