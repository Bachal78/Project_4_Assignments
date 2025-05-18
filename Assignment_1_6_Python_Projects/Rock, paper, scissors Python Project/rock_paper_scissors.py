import random  # Importing the random module to let the computer make a random choice

def play():
    # Prompt user to input their choice
    user = input("'r' for rock, 'p' for paper, 's' for scissors:")
    
    # Computer randomly chooses between rock, paper, or scissors
    computer = random.choice(['r', 'p', 's'])
    
    # If user and computer choose the same thing, it's a tie
    if user == computer:
        return 'It\'s a tie!'
    
    # If user wins (according to game rules), return win message
    if is_win(user, computer):
        return 'You won!'
    
    # If not a tie or a win, user must have lost
    return 'You lost!'

def is_win(player, opponent):
    # Return true if player wins
    # Rock beats scissors, paper beats rock, scissors beats paper
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    return False

# Variable to control game loop
is_playing = True

# Loop to keep playing until user decides to stop
while is_playing:
    print(play())  # Call play() function and print the result
    
    # Ask the user if they want to play again
    play_again = input("Play again? (y/n): ").lower()
    
    # If user doesn't enter 'y', exit the loop
    if play_again != 'y':
        is_playing = False

# Thank the user for playing after loop ends
print("Thanks for playing!")
