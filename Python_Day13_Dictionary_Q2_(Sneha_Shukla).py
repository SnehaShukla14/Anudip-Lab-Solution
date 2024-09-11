# Q.2) Write a Python script to concatenate the following dictionaries to create a new one. 
# Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}

# CODE:

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate dictionaries
merged_dict = {**dic1, **dic2, **dic3}

# Print the merged dictionary
print("Merged dictionary:", merged_dict)

# OUTPUT:
# Merged dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
