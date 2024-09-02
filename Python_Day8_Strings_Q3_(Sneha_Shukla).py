# Q.3) Write a Python program to reverse words in a string 

# String = “Deeptech Python Training”

# CODE:

# Define the string
string = "Deeptech Python Training"

# Split the string into words
words = string.split()

# Reverse the order of words
reversed_words = words[::-1]

# Join the reversed words into a single string
reversed_string = ' '.join(reversed_words)

# Print the result
print("Original string:")
print(string)
print("\nReversed words string:")
print(reversed_string)

# OUTPUT:

# Original string:
# Deeptech Python Training

# Reversed words string:
# Training Python Deeptech
