import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:/Users/ADMIN/Desktop/Python/urcs_digital_transformation_dataset.csv")

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check the structure of the dataset
print("\nDataset Information:")
print(df.info())

# Summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Checking for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values if any
# For demonstration purposes, we'll fill missing values with the median for numerical columns
df.fillna(df.median(numeric_only=True), inplace=True)

# Categorical data: fill with mode
df.fillna(df.mode().iloc[0], inplace=True)

# Recheck missing values
print("\nMissing Values after filling:")
print(df.isnull().sum())

# Distribution of numerical features using histograms
df.hist(figsize=(15, 10))
plt.suptitle("Histograms of Numerical Features")
plt.show()

# Boxplot for numerical features to detect outliers
plt.figure(figsize=(15, 10))
sns.boxplot(data=df.select_dtypes(include=['int64', 'float64']))
plt.title("Boxplot of Numerical Features")
plt.xticks(rotation=45)
plt.show()

# Bar plots for categorical features
plt.figure(figsize=(12, 6))
sns.countplot(x="Branch", data=df, order=df["Branch"].value_counts().index)
plt.title("Branch Distribution")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x="Region", data=df, order=df["Region"].value_counts().index)
plt.title("Region Distribution")
plt.xticks(rotation=45)
plt.show()

# Correlation matrix to analyze relationships between numerical variables
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Scatter plot: Employees vs Beneficiaries Served
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Employees', y='Beneficiaries Served', data=df, hue='Region')
plt.title('Employees vs Beneficiaries Served')
plt.show()

# Scatter plot: Internet Access (%) vs Response Time (hours)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Internet Access (%)', y='Response Time (hours)', data=df, hue='Digital Tools')
plt.title('Internet Access (%) vs Response Time (hours)')
plt.show()
