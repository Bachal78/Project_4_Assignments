# Define a function to get user info
def get_user_info():
    # Prompt user for first name
    first_name: str = input("What is your first name?: ")
    
    # Prompt user for last name
    last_name: str = input("What is your last name?: ")
    
    # Prompt user for email address
    email_address: str = input("What is your email address?: ")
    
    # Return all three values as a tuple
    return first_name, last_name, email_address


########## No need to edit code past this point :) ##########

# Main function where we call get_user_info and print the returned tuple
def main():
    # Call the function and store the returned tuple in user_data
    user_data = get_user_info()
    
    # Print the data received
    print("Received the following user data:", user_data)

# Ensures the main function runs when this file is executed
if __name__ == "__main__":
    main()
