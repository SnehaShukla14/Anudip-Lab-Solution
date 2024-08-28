# Q.1) Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

# CODE:

# Define a function named div with two parameters: num1 and num2
def div(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    # Return the result of dividing num1 by num2
    return num1 / num2

# Call the function with two numbers and display their division
result = div(10, 2)

# Print the result of the division
print(f"The result of division is: {result}")

# OUTPUT:

# The result of division is: 5.0



