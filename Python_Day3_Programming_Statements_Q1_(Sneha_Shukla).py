# Q1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd.

# CODE:

# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd using a ternary operator
result = "Even" if number % 2 == 0 else "Odd"

# Print the result
print(f"The number {number} is {result}.")

# OUTPUT:

# Enter a number: 45
# The number 45 is Odd.

# Enter a number: 86
# The number 86 is Even.
