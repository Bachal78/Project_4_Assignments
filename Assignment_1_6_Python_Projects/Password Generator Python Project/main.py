import random
import string

# Step 1: Get user input
num_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("Enter the length of each password: "))

# Step 2: Define characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Generate passwords
print("\nHere are your passwords:")
for _ in range(num_passwords):
    password = ''.join(random.choice(characters) for _ in range(password_length))
    print(password)
