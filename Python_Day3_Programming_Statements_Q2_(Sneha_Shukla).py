# Q.2) Using input function take two number and then swap the number.

# CODE:

# Take input from the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Print the numbers before swapping
print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swap the numbers using tuple unpacking
num1, num2 = num2, num1

# Print the swapped numbers
print(f"After swapping: First number = {num1}, Second number = {num2}")

# OUTPUT:

# Enter the first number: 67
# Enter the second number: 45
# Before swapping: num1 = 67, num2 = 45
# fter swapping: First number = 45, Second number = 67
