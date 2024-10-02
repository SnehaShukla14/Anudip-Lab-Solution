# Q.1) Create a pie chart to visualize the distribution of your monthly income by source. You have collected data on the various sources of your income, such as salary, freelance work, investments, and rental income. Share your conclusion/analysis.

# Input: income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other'] 

# monthly_income = [5000, 1500, 1000, 600, 400]

# CODE:

# Import the necessary library
import matplotlib.pyplot as plt

# Data: sources of income
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']

# Data: corresponding monthly income amounts
monthly_income = [5000, 1500, 1000, 600, 400]

# Create the pie chart
plt.figure(figsize=(7,7))  # Set the figure size for better visualization

# Plot the pie chart
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=90)

# Add a title to the chart
plt.title('Distribution of Monthly Income by Source')

# Ensure the pie chart is displayed as a circle
plt.axis('equal')  

# Display the chart
plt.show()

# Conclusion/Analysis:
# The salary accounts for the majority of your monthly income (approximately 65.8%)
# Freelance work contributes a significant portion (about 19.7%), while investments and rental income provide smaller shares (around 13% combined). Other sources account for 5.3%.
# This breakdown suggests you rely primarily on salary but have a good diversification of income streams from other areas such as freelance work and investments.



