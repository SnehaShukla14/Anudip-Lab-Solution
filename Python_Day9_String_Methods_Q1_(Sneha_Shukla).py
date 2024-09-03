# Q.1) Write a Python program to Count all letters, digits, and special symbols from the given string

# Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3

# CODE:

def count_characters(input_string):
    """
    This function counts the number of letters, digits, and special symbols
    in the provided string and prints the results.
    
    Parameters:
    input_string (str): The string to analyze.

    Returns:
    None: The function prints the counts directly.
    """
    
    # Initialize counters for letters, digits, and special symbols
    letter_count = 0
    digit_count = 0
    symbol_count = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        
        # Check if the character is a letter (alphabetical character)
        if char.isalpha():
            letter_count += 1
            
        # Check if the character is a digit (numerical character)
        elif char.isdigit():
            digit_count += 1
            
        # If the character is neither a letter nor a digit, classify it as a special symbol
        else:
            symbol_count += 1
    
    # Print the counts of letters, digits, and symbols
    print(f"Chars = {letter_count}")  # Number of letters in the string
    print(f"Digits = {digit_count}")  # Number of digits in the string
    print(f"Symbols = {symbol_count}")  # Number of special symbols in the string

# Example usage
input_string = "P@#yn26at^&i5ve"
count_characters(input_string)

"""
OUTPUT:
Chars = 8
Digits = 3
Symbols = 4
"""
