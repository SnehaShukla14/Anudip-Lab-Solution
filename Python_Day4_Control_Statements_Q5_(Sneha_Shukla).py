# Q.5) Write a Python program that determines the largest of three numbers entered by the user.

# CODE:

# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest number
largest = num1

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

# Print the largest number
print(f"The largest number is: {largest}")

# OUTPUT:

# Enter the first number: 25
# Enter the second number: 15
# Enter the third number: 13
# The largest number is: 25.0

# Enter the first number: 6.5
# Enter the second number: 7.9
# Enter the third number: 2.6
# The largest number is: 7.9

# Enter the first number: 1.2
# Enter the second number: 2.2
# Enter the third number: 3.3
# The largest number is: 3.3


