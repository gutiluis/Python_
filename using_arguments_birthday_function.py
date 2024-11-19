import pdb





def calculate_age(birth_year, current_year):
    return subtract(current_year, birth_year)


def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

# Main function
def function():
    while True:
        try:
            birth_year = int(input("Enter your birth year: "))
            current_year = int(input("Enter the current year: "))
            
            # Check for valid input
            if birth_year > current_year:
                print("Birth year can't be greater than the current year. Please try again.")
                continue
            
            break  # Exit the loop if valid input
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

    
    pdb.set_trace()

    # Calculate age using the subtract function
    age = calculate_age(birth_year, current_year)
    
    print(f"Your age is: {age}")

function()