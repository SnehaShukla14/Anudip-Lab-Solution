# Q.2) Write a Python program to get the largest and smallest number from a list without builtin functions.

# CODE:

# Define a list of numbers
numbers = [5, 2, 9, 1, 5, 6, 3, 7]

# Initialize the largest and smallest variables with the first element of the list
if len(numbers) == 0:
    raise ValueError("The list is empty and has no largest or smallest number.")
    
largest = smallest = numbers[0]

# Iterate through the list to find the largest and smallest numbers
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Print the results
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)

# OUTPUT:

# The largest number in the list is: 9
# The smallest number in the list is: 1

