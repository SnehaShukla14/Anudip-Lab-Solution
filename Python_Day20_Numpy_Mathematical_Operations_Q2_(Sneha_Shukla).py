# Q.2) Calculate the profit made by a company

# Input: revenue = np.array([10000, 12000, 11000, 10500]) 

# expenses = np.array([4000, 5000, 4500, 4800])

# CODE:

# Importing the library
import numpy as np

# Define the revenue array and expenses array
revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

# Calculate profit for each entry
profit = revenue - expenses

# Print the calculated profit
print("Profit made by a company:", profit)

# OUTPUT:
# Profit made by a company: [6000 7000 6500 5700]
