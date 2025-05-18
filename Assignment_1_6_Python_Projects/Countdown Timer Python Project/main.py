import time  # Import the time module

# Step 1: Ask the user for countdown time in seconds
countdown_time = int(input("Enter time in seconds: "))

# Step 2: Start the countdown
while countdown_time:
    mins, secs = divmod(countdown_time, 60)  # Convert to minutes and seconds
    timer = '{:02d}:{:02d}'.format(mins, secs)  # Format time as MM:SS
    print(timer, end='\r')  # Print time on the same line
    time.sleep(1)  # Wait for 1 second
    countdown_time -= 1  # Decrease the time by 1 second

# Step 3: When done, print a message
print("Time's up!")
