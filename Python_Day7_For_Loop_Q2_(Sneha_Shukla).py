# Q.2) Python program to check if a given number is an Armstrong number

# CODE:

# Define a function
def is_armstrong_number(number):
    # Convert the number to a string to easily access individual digits
    str_number = str(number)
    
    # Find the number of digits
    num_digits = len(str_number)
    
    # Initialize a variable to hold the sum of powers
    sum_of_powers = 0
    
    # Loop through each digit in the string representation of the number
    for digit in str_number:
        
        # Convert the character back to an integer
        int_digit = int(digit)
        
        # Calculate the power and add to the sum
        sum_of_powers += int_digit ** num_digits
    
    # Check if the sum of powers equals the original number
    if sum_of_powers == number:
        return True
    else:
        return False

# Take input from the user
try:
    input_number = int(input("Enter a number: "))
    
    # Check if the input number is an Armstrong number
    if is_armstrong_number(input_number):
        print(f"{input_number} is an Armstrong number.")
    else:
        print(f"{input_number} is not an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")

# OUTPUT:

# Enter a number: 123
# 123 is not an Armstrong number.

# Enter a number: 153
# 153 is an Armstrong number.

