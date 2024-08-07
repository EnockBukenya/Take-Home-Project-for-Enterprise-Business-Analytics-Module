import pandas as pd

# Sample data for the dataset
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

# Save the DataFrame to an Excel file
excel_path = r'C:\Users\ADMIN\Desktop\Python\urcs_digital_transformation_dataset.xlsx'
df.to_excel(excel_path, index=False)

print(f"Excel file saved at: {excel_path}")
