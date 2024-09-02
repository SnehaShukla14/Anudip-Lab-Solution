# Q.2) Write a Python program to remove a newline in Python

# String = "\nBest \nDeeptech \nPython \nTraining\n"

# CODE:

# Define the string with newline characters
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Using str.replace()
cleaned_string = string.replace('\n', '')

# Print the original and cleaned strings
print("Original String with newlines:")
print(string)  # This will include newlines
print("String with newlines removed:")
print(cleaned_string) # Newlines are removed

# OUTPUT:

# Original String with newlines:

# Best 
# Deeptech 
# Python 
# Training

# String with newlines removed:
# Best Deeptech Python Training

