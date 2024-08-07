import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:/Users/ADMIN/Desktop/Python/urcs_digital_transformation_dataset.csv")

# Ensure the dataset is loaded correctly
print("Dataset loaded successfully")
print(df.head())

# Encode categorical features
label_encoder = LabelEncoder()
df['Digital Training Programs'] = label_encoder.fit_transform(df['Digital Training Programs'])

# Define features and target variable
features = ['Employees', 'Internet Access (%)', 'IT Staff', 'Mobile Phone Usage (%)']
target = 'Digital Training Programs'

# Split the data into training
