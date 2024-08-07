import pandas as pd

# Initial sample data for the dataset
data = {
    "Branch": ["Kampala", "Gulu", "Mbarara", "Jinja", "Arua"],
    "Employees": [120, 80, 75, 50, 45],
    "Volunteers": [200, 150, 130, 100, 90],
    "Annual Budget (USD)": [500000, 300000, 250000, 200000, 180000],
    "Digital Tools": ["CRM, ERP", "ERP", "CRM", "None", "CRM"],
    "Internet Access (%)": [90, 80, 75, 60, 50],
    "IT Staff": [5, 3, 2, 1, 1],
    "Beneficiaries Served": [10000, 7500, 7000, 5000, 4500],
    "Response Time (hours)": [2, 3, 3, 4, 5],
    "Partnerships": ["WHO, UNICEF", "UNICEF", "WHO", "None", "WHO"],
    "Digital Training Programs": ["Yes", "No", "Yes", "No", "No"],
    "Internet Penetration Rate (%)": [45, 45, 45, 45, 45],
    "Mobile Phone Usage (%)": [70, 65, 68, 60, 55],
    "Literacy Rate (%)": [76, 74, 75, 72, 70]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 1: Handle Missing Values
# Introduce some missing values for demonstration
df.loc[2, "Volunteers"] = None  # Set Volunteers for Mbarara as missing
df.loc[4, "Annual Budget (USD)"] = None  # Set Annual Budget for Arua as missing

print("Before Handling Missing Values:")
print(df)

# Fill missing values
df["Volunteers"] = df["Volunteers"].fillna(df["Volunteers"].mean())  # Fill with mean
df["Annual Budget (USD)"] = df["Annual Budget (USD)"].fillna(df["Annual Budget (USD)"].median())  # Fill with median

print("\nAfter Handling Missing Values:")
print(df)

# Step 2: Remove Duplicates
# Introduce a duplicate row for demonstration
df = df.append(df.loc[3], ignore_index=True)

print("\nBefore Removing Duplicates:")
print(df)

# Remove duplicates
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# Step 3: Correct Errors
print("\nBefore Correcting Errors:")
print(df)

# Standardize 'Digital Tools' and 'Partnerships' capitalization
df["Digital Tools"] = df["Digital Tools"].str.title()  # Capitalize each word
df["Partnerships"] = df["Partnerships"].str.upper()  # Convert to uppercase

print("\nAfter Correcting Errors:")
print(df)

# Step 4: Standardize Data Formats
print("\nBefore Standardizing Data Formats:")
print(df)

# Ensure consistent numeric format for percentages
df["Internet Access (%)"] = df["Internet Access (%)"].astype(float)
df["Internet Penetration Rate (%)"] = df["Internet Penetration Rate (%)"].astype(float)
df["Mobile Phone Usage (%)"] = df["Mobile Phone Usage (%)"].astype(float)
df["Literacy Rate (%)"] = df["Literacy Rate (%)"].astype(float)

# Standardize Response Time to float for consistency
df["Response Time (hours)"] = df["Response Time (hours)"].astype(float)

print("\nAfter Standardizing Data Formats:")
print(df)
