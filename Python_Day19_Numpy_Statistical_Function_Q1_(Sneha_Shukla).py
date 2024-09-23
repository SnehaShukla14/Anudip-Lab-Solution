# Q.1) Compute the median of the flattened NumPy array 

# Input: x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

# CODE:

# Import NumPy
import numpy as np

# Sample array (odd number of elements)
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

# Flatten the array (although it's already 1D in this case)
# np.flatten() is useful when working with multi-dimensional arrays
flattened_array = x_odd.flatten()

# Compute the median of the flattened array
median_value = np.median(flattened_array)

# Output the median
print("Median of the array:", median_value)

# OUTPUT:
# Median of the array: 4.0
