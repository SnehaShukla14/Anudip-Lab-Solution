# Q.2) Write a python program finding the factorial of a given number using a while loop

# CODE:

def factorial(number):
    # Check if the number is negative
    if number < 0:
        return "Factorial is not defined for negative numbers"
    
    # Initialize result to 1
    result = 1
    
    # Loop to multiply result by each number from the input down to 1
    while number > 1:
        # Multiply result by the current number
        result *= number
        # Decrement the number by 1
        number -= 1       
    
    return result

# Main program execution
if __name__ == "__main__":
    
    # Prompt user for input
    num = int(input("Enter a number: "))
    
    # Calculate factorial and print result
    print(f"The factorial of {num} is {factorial(num)}")

# OUTPUT:

# Enter a number: 6
# The factorial of 6 is 720

# Enter a number: -5
# The factorial of -5 is Factorial is not defined for negative numbers
