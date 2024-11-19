import pickle

# Dictionary to store users' information (username: [user_id, password])
users_db = {}

# Function to add a new user
def add_user(username, user_id, password):
    users_db[username] = [user_id, password]
    print(f"User {username} added successfully.")

# Function to save the user data to a file
def save_users():
    with open("users_db.pkl", "wb") as file:
        pickle.dump(users_db, file)
    print("User data saved successfully.")

# Function to load user data from the file
def load_users():
    global users_db
    try:
        with open("users_db.pkl", "rb") as file:
            users_db = pickle.load(file)
        print("User data loaded successfully.")
    except FileNotFoundError:
        print("No existing user data found.")

# Main function to run the script
def main():
    load_users()  # Load existing user data (if any)

    while True:
        print("\n1. Add user")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            user_id = input("Enter user ID: ")
            password = input("Enter password: ")

            # Add the user to the dictionary
            add_user(username, user_id, password)

            # Save the users to the file
            save_users()

        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()