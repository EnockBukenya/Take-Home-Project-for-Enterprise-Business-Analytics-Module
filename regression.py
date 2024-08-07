import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv("C:/Users/ADMIN/Desktop/Python/urcs_digital_transformation_dataset.csv")

# Ensure the dataset has sufficient data
print("Number of samples in dataset:", len(df))

# Select features and target variable
features = ['Employees', 'Annual Budget (USD)']
target = 'Beneficiaries Served'

# Split the data into training and testing sets
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Check the size of the training and test sets
print("Training set size:", len(X_train))
print("Test set size:", len(X_test))

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Plotting the predictions
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Beneficiaries Served")
plt.ylabel("Predicted Beneficiaries Served")
plt.title("Actual vs Predicted Beneficiaries Served")
plt.show()
