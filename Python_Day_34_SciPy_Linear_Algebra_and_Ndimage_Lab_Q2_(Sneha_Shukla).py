# Lab2: Using SciPy Linear Algebra please solve the below problem. Input: 7x + 2y = 8 4x + 5y = 10

# CODE:

# Import necessary libraries
import numpy as np
from scipy import linalg

# Define the coefficients of the equations as a matrix A
A = np.array([[7, 2], [4, 5]])

# Define the constants on the right-hand side as matrix B
B = np.array([8, 10])

# Solve the system of linear equations
solution = linalg.solve(A, B)

# Extracting x and y
x, y = solution

# Display the solution
print(f"Solution: x = {x}, y = {y}")

# OUTPUT:
# Solution: x = 0.7407407407407407, y = 1.4074074074074074
