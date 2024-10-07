# 1: Write a Pandas program to create a dataframe from a dictionary and display it.

# Sample data:

# score={'Math':[78,85,96,80,86], 'English':[84,94,89,83,86],'Hindi':[86,97,96,72,83]}

# CODE:

# Importing the library
import pandas as pd

# Sample data
score = {
    'Math': [78, 85, 96, 80, 86],
    'English': [84, 94, 89, 83, 86],
    'Hindi': [86, 97, 96, 72, 83]
}

# Creating DataFrame from the dictionary
df = pd.DataFrame(score)

# Displaying the DataFrame
# This will print the DataFrame in a tabular format
print("DataFrame created from the dictionary:")
print(df)


"""
OUTPUT:
DataFrame created from the dictionary:
   Math  English  Hindi
0    78       84     86
1    85       94     97
2    96       89     96
3    80       83     72
4    86       86     83
"""
