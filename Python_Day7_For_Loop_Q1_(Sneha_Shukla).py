# Q.1) Python program to check if the given string is a palindrome 

# CODE:

# Define a function
def is_palindrome(s):
    # Preprocess the string
    # Remove any spaces and convert to lowercase for uniform comparison
    s = s.replace(" ", "").lower()
    
    # Get the length of the string
    length = len(s)
    
    # Loop through the first half of the string
    for i in range(length // 2):
        
        # Compare characters from the beginning and end
        if s[i] != s[length - i - 1]:
            
            # If characters do not match, it is not a palindrome
            return False
    
    # If all character comparisons are successful, it is a palindrome
    return True

# Take input from the user
input_string = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

# OUTPUT:

# Enter a string: summer
# "summer" is not a palindrome.

# Enter a string: radar
# "radar" is a palindrome.
