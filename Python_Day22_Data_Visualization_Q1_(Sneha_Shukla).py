# Q.1) Install matplotlib  & you can use plt.plot() to create a line plot of given data

# x = [0, 5, 9, 10, 15, 20, 25] 

# y = [0, 1, 2, 3, 4, 5, 6]

# CODE:

# Import the library
import matplotlib.pyplot as plt

# Data
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]

# Create a line plot
plt.plot(x, y)

# Add titles and labels
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()



