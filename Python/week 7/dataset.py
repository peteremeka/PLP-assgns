# Step 1: Import necessary libraries
import pandas as pd

# task One

# Loading the dataset iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv(url, header=None, names=columns)

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Exploring the structure of the dataset
print("\nData types of each column:")
print(df.dtypes)

print("\nSummary of missing values:")
print(df.isnull().sum())

# Cleaning the dataset by dropping rows with missing values
df_cleaned = df.dropna()

print("\nCleaned dataset preview:")
print(df_cleaned.head())



# Task Two

# Display first few rows
print(df.head())

# Compute basic statistic
# Basic statistics of numerical columns
stats = df.describe()
print("Basic Statistics:\n", stats)

# Group by Categorical Column and Compute Mean
# Group by species and compute mean of each numerical column
grouped_means = df.groupby('species').mean()
print("\nMean values grouped by species:\n", grouped_means)


# Data Visualization

# Line chart showing trend over time
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [2500, 2700, 3000, 3200, 3100]

plt.plot(months, sales, marker='o', linestyle='-', color='blue', label='Sales')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales (₦)')
plt.legend()
plt.grid(True)
plt.show()


# Bar chart showing the comparison of a numerical value across categories 
species = ['Setosa', 'Versicolor', 'Virginica']
avg_petal_length = [1.5, 4.3, 5.5]

plt.bar(species, avg_petal_length, color=['green', 'orange', 'purple'])
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()


# Histogram – Distribution of a Numerical Column
# Understand the frequency distribution of a variable (e.g., sepal length)

plt.hist(df['sepal_length'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()


# Scatter Plot – Relationship Between Two Variables
# Visualize correlation or clustering between two numerical features.

colors = {'Setosa':'green', 'Versicolor':'orange', 'Virginica':'purple'}

for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal_length'], subset['petal_length'], 
                label=species, color=colors[species])

plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.grid(True)
plt.show()

