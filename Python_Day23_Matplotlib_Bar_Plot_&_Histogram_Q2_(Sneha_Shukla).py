# Q.2) Visualize the daily temperature changes over time in a city and give your conclusion
# Input: days = list(range(1, 32)) 
# Daily temperature data (replace with your own data) 
# temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# CODE:

# Import necessary libraries
import matplotlib.pyplot as plt

# Days of the month (1 to 31)
days = list(range(1, 32))

# Daily temperature data (replace this with your own data if necessary)
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create a line plot to visualize temperature changes over time
plt.figure(figsize=(10,6))  # Set the figure size for better visibility
plt.plot(days, temperature, marker='o', linestyle='-', color='blue')  # Plot with markers on data points

# Add labels and title
plt.xlabel('Days of the Month')  # X-axis label
plt.ylabel('Temperature (°F)')  # Y-axis label
plt.title('Daily Temperature Changes Over Time in the City')  # Title of the plot

# Show grid for better readability
plt.grid(True)

# Show the plot
plt.show()

# Conclusion: The temperature shows an overall increasing trend at the start of the month, peaking around day 25, 
# followed by a slight drop towards the end of the month. There are some fluctuations, but the general pattern
# indicates warmer temperatures as the month progresses.
