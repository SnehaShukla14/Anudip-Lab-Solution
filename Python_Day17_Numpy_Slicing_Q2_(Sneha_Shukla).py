# Q.2) Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

# CODE:

# Importing the NumPy library
import numpy as np

# Create an array with values from 2 to 10
values = np.arange(2, 11)

# Reshape it into a 3x3 matrix
matrix_3x3 = values.reshape(3, 3)

# Create a 3x3 matrix with values ranging from 2 to 10
print("3x3 Matrix with values ranging from 2 to 10:")
print(matrix_3x3)


"""
OUTPUT:
3x3 Matrix with values ranging from 2 to 10:
[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]
"""
