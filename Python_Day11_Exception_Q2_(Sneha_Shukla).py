# Q.2) Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# CODE:

def get_integer_input():
    try:
        # Prompt the user to enter an integer
        user_input = input("Please enter an integer: ")
        
        # Attempt to convert the input to an integer
        integer_value = int(user_input)
        
        # If successful, return the integer value
        return integer_value
    except ValueError:
        # If a ValueError occurs (input is not a valid integer), raise an exception
        raise ValueError("Error: The input is not a valid integer.")

# Main part of the program
def main():
    try:
        # Call the function to get the integer input
        integer = get_integer_input()
        print(f"You entered a valid integer: {integer}")
    except ValueError as e:
        # Handle the ValueError raised by get_integer_input
        print(e)

# Execute the main function
if __name__ == "__main__":
    main()

# OUTPUT:

"""
Please enter an integer: 12
You entered a valid integer: 12

Please enter an integer: 2.3
Error: The input is not a valid integer.

Please enter an integer: abc
Error: The input is not a valid integer.
"""
