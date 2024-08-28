# Q.2) Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

# CODE:

# Get the user's age
age = int(input("Enter your age: "))

# Check if the age is 18 or older
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# OUTPUT:

# Enter your age: 15
# You are not eligible to vote yet.

# Enter your age: 21
# You are eligible to vote.


