import os




# Function to initialize the database (if it doesn't already exist)
def initialize_db():
    if not os.path.exists("users_db.txt"):
        with open("users_db.txt", "w") as f:
            f.write("username,user_id,password\n")  # Column headers (can be ignored later)
        print("Database initialized successfully.")

# Function to add a user to the database
def add_user(username, user_id, password):
    with open("users_db.txt", "a") as f:
        f.write(f"{username},{user_id},{password}\n")
    print(f"User {username} added successfully.")

# Function to read all users from the database
def read_users():
    users = []
    with open("users_db.txt", "r") as f:
        lines = f.readlines()[1:]  # Skip the header line
        for line in lines:
            username, user_id, password = line.strip().split(",")
            users.append({"username": username, "user_id": user_id, "password": password})
    return users

# Function to authenticate a user (username and password check)
def authenticate_user(username, password):
    users = read_users()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

# Function to update a user's password
def update_password(username, new_password):
    users = read_users()
    updated = False
    with open("users_db.txt", "w") as f:
        f.write("username,user_id,password\n")  # Re-write the header
        for user in users:
            if user["username"] == username:
                user["password"] = new_password
                updated = True
            f.write(f"{user['username']},{user['user_id']},{user['password']}\n")
    
    if updated:
        print(f"Password for {username} updated successfully.")
    else:
        print(f"User {username} not found.")

# Function to delete a user from the database
def delete_user(username):
    users = read_users()
    updated_users = [user for user in users if user["username"] != username]
    
    with open("users_db.txt", "w") as f:
        f.write("username,user_id,password\n")  # Re-write the header
        for user in updated_users:
            f.write(f"{user['username']},{user['user_id']},{user['password']}\n")
    
    print(f"User {username} deleted successfully.")

# Main function to demonstrate usage
def main():
    initialize_db()  # Initialize the database (if not already initialized)
    
    # Add new users
    add_user("alice", "001", "password123")
    add_user("bob", "002", "password456")
    
    # Read and display all users
    print("\nAll users:")
    users = read_users()
    for user in users:
        print(user)
    
    # Authenticate user
    username = input("\nEnter your username to login: ")
    password = input("Enter your password: ")
    if authenticate_user(username, password):
        print(f"Welcome back, {username}!")
    else:
        print("Invalid username or password.")
    
    # Update password
    username_to_update = input("\nEnter the username to update the password: ")
    new_password = input("Enter the new password: ")
    update_password(username_to_update, new_password)
    
    # Delete user
    username_to_delete = input("\nEnter the username to delete: ")
    delete_user(username_to_delete)

if __name__ == "__main__":
    main()