# 2: Suppose you want to track and analyze your household expenses for a month. You have recorded the expenses for various categories, such as groceries, utilities, rent, transportation, and entertainment. You can represent this expense data using a Pandas Series. 

# Input: # Expense categories

# categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

# Monthly expense data (example data in USD) 

# expenses = [500, 200, 1200, 300, 150]

# CODE:

# Import the Pandas library
import pandas as pd

# List of expense categories
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

# Monthly expense data for each category (in USD)
expenses = [500, 200, 1200, 300, 150]

# Create a Pandas Series to represent the household expenses
# The 'categories' list will be the index, and 'expenses' will be the values
expense_series = pd.Series(data=expenses, index=categories)

# Display the Series
print(expense_series)

# OUTPUT:

# Groceries          500
# Utilities          200
# Rent              1200
# Transportation     300
# Entertainment      150
# dtype: int64


