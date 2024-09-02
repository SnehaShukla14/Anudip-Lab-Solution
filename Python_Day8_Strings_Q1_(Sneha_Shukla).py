# Q.1) Write a Python program to count the occurrences of each word in a given sentence 

# string = “To change the overall look of your document. To change the look available in the gallery”

# CODE:

# Define the string
string = "To change the overall look of your document. To change the look available in the gallery"

# Normalize the string: Convert to lowercase and remove punctuation
def normalize_string(s):
    normalized = ""
    for char in s:
        if char.isalnum() or char.isspace():
            normalized += char
    return normalized.lower()

# Normalize the string
normalized_string = normalize_string(string)

# Split the string into words
words = normalized_string.split()

# Count occurrences of each word using a dictionary
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word counts
for word, count in word_count.items():
    print(f"'{word}': {count}")

# OUTPUT:

# 'to': 2
# 'change': 2
# 'the': 3
# 'overall': 1
# 'look': 2
# 'of': 1
# 'your': 1
# 'document': 1
# 'available': 1
# 'in': 1
# 'gallery': 1
