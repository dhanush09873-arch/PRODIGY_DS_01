# Import required libraries
import matplotlib.pyplot as plt

# Sample data: ages of people in a population
ages = [18, 19, 20, 21, 21, 22, 22, 23, 23, 23, 24, 24, 25, 25, 
        26, 27, 28, 29, 30, 32, 34, 36, 38, 40, 42]

# Create a histogram
plt.figure()
plt.hist(ages, bins=8)

# Add heading and labels
plt.title("Distribution of Ages in a Population")
plt.xlabel("Age")
plt.ylabel("Number of People")

# Show the chart
plt.show()
