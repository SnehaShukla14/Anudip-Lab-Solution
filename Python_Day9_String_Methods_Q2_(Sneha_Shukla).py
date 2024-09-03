# Q.2) Write a Python program to remove duplicate characters of a given string.

# Input = “String and String Function” Output: String and Function

# CODE:

# Define the input string
input_string = "String and String Function"

# Split the input string into words
words = input_string.split()

# Initialize an empty list to store the result without duplicates
unique_words = []

# Initialize an empty set to keep track of seen words
seen_words = set()

# Iterate through each word in the list of words
for word in words:
    if word not in seen_words:
        # If the word is not in the set, add it to the result list and the set
        unique_words.append(word)
        seen_words.add(word)

# Join the unique words back into a single string
result_string = ' '.join(unique_words)

# Print the result
print(result_string)

# OUTPUT:
# String and Function

