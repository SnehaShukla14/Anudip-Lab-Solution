# 2: Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels. 

# Sample Python dictionary data and list labels: 

# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 

# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 

# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

# CODE:

# Importing the necessary libraries
import pandas as pd
import numpy as np

# Sample data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# Specifying index labels
index_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Creating DataFrame with specified index labels
df = pd.DataFrame(exam_data, index=index_labels)

# Displaying the DataFrame
print("DataFrame created from the dictionary:")
print(df)

"""
OUTPUT:
DataFrame created from the dictionary:
        name  score  attempts qualify
A  Anastasia   12.5         1     yes
B       Dima    9.0         3      no
C  Katherine   16.5         2     yes
D      James    NaN         3      no
E      Emily    9.0         2      no
F    Michael   20.0         3     yes
G    Matthew   14.5         1     yes
H      Laura    NaN         1      no
I      Kevin    8.0         2      no
J      Jonas   19.0         1     yes
"""
