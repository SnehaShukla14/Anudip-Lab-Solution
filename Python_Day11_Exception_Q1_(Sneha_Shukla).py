# Q.1) Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# CODE:

def divide_numbers(numerator, denominator):
    try:
        # Attempt to perform the division
        result = numerator / denominator
    except ZeroDivisionError:
        # Handle the case where the denominator is zero
        print("Error: Cannot divide by zero!")
        return None
    else:
        # If no exception occurs, return the result
        return result

# Prompt the user for input and convert to float
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

# Call the function and display the result
result = divide_numbers(numerator, denominator)
if result is not None:
    print(f"The result of the division is: {result}")

# OUTPUT:

"""
Enter the numerator: 6
Enter the denominator: 3
The result of the division is: 2.0

Enter the numerator: 5
Enter the denominator: 0
Error: Cannot divide by zero!
"""
