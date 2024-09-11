# Q.3) Write a Python program to find duplicate values from a list and display those

# CODE:

# Define a list with some duplicate values
numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 1, 8, 9, 4]

# Create a dictionary to count occurrences of each number
occurrences = {}

# Count the occurrences of each number
for num in numbers:
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1

# Find and display duplicate values
duplicates = [num for num, count in occurrences.items() if count > 1]

# Print the results
print("Duplicate values in the list are:", duplicates)

# OUTPUT:
# Duplicate values in the list are: [1, 2, 3, 4]
