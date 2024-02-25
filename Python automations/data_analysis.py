#Generate dummy data
import pandas as pd
import numpy as np

# Sample data for 8 employees
data = {
  'Weekly_Hours': [35, 40, 45, 30, 55, 50, 38, 42],
  'Productivity': [88, 90, 85, 95, 80, 75, 92, 89]
}
df = pd.DataFrame(data, columns=['Weekly_Hours','Productivity'])
df

# Summary statistics 
print(df.describe())
#correlation
print(df.corr())


# Calculate the correlation coefficient
corr_coef = np.corrcoef(df.Weekly_Hours, df.Productivity)[0, 1]
print(f"Correlation Coefficient: {corr_coef:.2f}")

# Fit a linear regression line
m, b = np.polyfit(df.Weekly_Hours, df.Productivity, 1)

# Creating the scatter plot
plt.figure(figsize=(10, 6))  # Set the figure size
plt.scatter(df.Weekly_Hours, df.Productivity, color='blue', alpha=0.5)  # Plot data points
plt.plot(df.Weekly_Hours, m*np.array(df.Weekly_Hours) + b, color='red')  # Plot the regression line

# Adding titles and labels
plt.title(f'Employee Work Hours vs. Productivity Scores\nCorrelation Coefficient: {corr_coef:.2f}')
plt.xlabel('Weekly Hours')
plt.ylabel('Productivity Scores')

# Display the plot
plt.grid(True)  # Optional: Adds a grid for better readability
plt.show()
