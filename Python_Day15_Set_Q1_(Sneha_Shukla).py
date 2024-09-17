# Q.1) Write a Python program to Get Only unique items from two sets. 

# Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70}

# CODE:

# Define two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Combine the two sets using union to get unique items
unique_items = set1.union(set2)

# Print the unique items
print("Unique items from both sets:", unique_items)


# OUTPUT:
# Unique items from both sets: {70, 40, 10, 50, 20, 60, 30}
