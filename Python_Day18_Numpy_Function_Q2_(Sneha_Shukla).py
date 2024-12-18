# 2.Suppose you have two sets of employee data—one containing information about full-time employees and another containing information about part-time employees. You want to combine this data to create a comprehensive employee dataset for HR analysis. 

# Input: # Employee data for full-time employees

# full_time_employees = np.array([

# [101, 'John Doe', 'Full-Time', 55000],

# [102, 'Jane Smith', 'Full-Time', 60000], 

# [103, 'Mike Johnson', 'Full-Time', 52000] 

# ])

 # Employee data for part-time employees :

# part_time_employees = np.array([ 

# [201, 'Alice Brown', 'Part-Time', 25000], 

# [202, 'Bob Wilson', 'Part-Time', 28000],

# [203, 'Emily Davis', 'Part-Time', 22000]

# ])

# CODE:

# Importing the library
import numpy as np

# Employee data for full-time employees
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
])

# Employee data for part-time employees
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

# Combine both full-time and part-time employee data using np.concatenate
combined_employees = np.concatenate((full_time_employees, part_time_employees), axis=0)

# Display the combined employee data
print("Combined Employee Data:")
for employee in combined_employees:
    print(employee)

"""
OUTPUT:
Combined Employee Data:
['101' 'John Doe' 'Full-Time' '55000']
['102' 'Jane Smith' 'Full-Time' '60000']
['103' 'Mike Johnson' 'Full-Time' '52000']
['201' 'Alice Brown' 'Part-Time' '25000']
['202' 'Bob Wilson' 'Part-Time' '28000']
['203' 'Emily Davis' 'Part-Time' '22000']
"""
