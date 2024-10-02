# Q.1)Suppose you are a teacher, and you want to analyze the exam scores of your students in a particular subject. You have recorded the scores of your students for a recent exam, and you want to represent this data using a Pandas Series.

# Input: students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']

# exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# CODE:

# Import the Pandas library
import pandas as pd

# List of students
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']

# List of exam scores
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Create a Pandas Series to represent the exam scores of the students
# The 'students' list will be the index, and 'exam_scores' will be the values
exam_series = pd.Series(data=exam_scores, index=students)

# Display the Series
print(exam_series)

# Output

# Alice      92
# Bob        88
# Charlie    76
# David      94
# Eve        82
# Frank      90
# Grace      85
# Hannah     89
# Ivy        78
# Jack       91
# dtype: int64
