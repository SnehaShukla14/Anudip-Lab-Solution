# Q.2) Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

# Input: my_list = [1, 2, 3, 4, 5]

# CODE:

import numpy as np

# Define the list
my_list = [1, 2, 3, 4, 5]

# Convert the list to a numpy array
my_array = np.array(my_list)

# Display the numpy array
print("Numpy Array:")
print(my_array)

# Display the first and last index
print("First element:", my_array[0])
print("Last element:", my_array[-1])

# Multiply each element by 2
result_array = my_array * 2

# Display the result
print("Array after multiplying each element by 2:")
print(result_array)

"""
OUTPUT:
Numpy Array:
[1 2 3 4 5]
First element: 1
Last element: 5
Array after multiplying each element by 2:
[ 2  4  6  8 10]
"""
