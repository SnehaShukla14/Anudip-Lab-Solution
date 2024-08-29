# Q.1) Write a python program to check whether a number is palindrome or not?

# CODE:

# Define a function to check if a number is a palindrome or not
def is_palindrome(number):
    original_number = number
    reversed_number = 0
    
    # Use a while loop to reverse the number
    while number > 0:
        # Extract the last digit of the number
        digit = number % 10
        # Update the reversed number by shifting digits left and adding the last digit
        reversed_number = reversed_number * 10 + digit
        # Remove the last digit from the current number
        number = number // 10
        
    # Check if the original number is equal to the reversed number
    return original_number == reversed_number

# Taking the input from the user
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    
    # Display the result whether a number is a palindrome or not
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

# OUTPUT:

# Enter a number: 454
# 454 is a palindrome.

# Enter a number: 345
# 345 is not a palindrome.




    
