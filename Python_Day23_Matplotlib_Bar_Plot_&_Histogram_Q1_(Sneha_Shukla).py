# Q1.Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. 

# Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] 

# Monthly expenses in dollars (replace with your own data)

# CODE:

# Importing the library
expenses = [1200, 400, 200, 150, 250]
import matplotlib.pyplot as plt

# Categories and corresponding expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Creating the bar chart
plt.figure(figsize=(8,6))  # Set the figure size for better visibility
plt.bar(categories, expenses, color='blue')
# Title of the chart
plt.title('Monthly Expenses by Category')
# X-axis label
plt.xlabel('Categories')
# Y-axis label
plt.ylabel('Expenses in Dollars')  # Y-axis label

# Display the chart
plt.show()

# Conclusion: Rent is the largest expense, accounting for a significant portion of the monthly expenses.
# Groceries and Transportation follow, while Utilities and Entertainment have smaller portions of the monthly budget.
