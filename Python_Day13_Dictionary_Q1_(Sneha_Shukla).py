# Q.1) Write a Python program and calculate the mean of the below dictionary.
# test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

# CODE:

# Given dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Extract values from the dictionary
values = test_dict.values()

# Calculate the sum of values
total_sum = sum(values)

# Calculate the number of values
num_values = len(values)

# Calculate the mean
mean = total_sum / num_values

# Print the mean
print(f"The mean of the dictionary values is: {mean:.1f}")

# OUTPUT:
# The mean of the dictionary values is: 6.2
