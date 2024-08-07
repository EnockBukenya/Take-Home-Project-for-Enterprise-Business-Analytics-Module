import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load the dataset
df = pd.read_csv("C:/Users/ADMIN/Desktop/Python/urcs_digital_transformation_dataset.csv")

# Ensure the dataset has the expected number of samples
print("Number of samples in dataset:", len(df))

# Select features for clustering
clustering_features = ['Employees', 'Internet Access (%)', 'IT Staff']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[clustering_features])

# Determine the optimal number of clusters using the elbow method
inertia = []
for k in range(1, len(df) + 1):  # Adjust range to be up to the number of samples
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(df) + 1), inertia, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal Clusters")
plt.show()

# Choose an appropriate number of clusters based on the elbow plot
optimal_clusters = 3  # Set this to a value determined from the elbow method
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Employees', y='Internet Access (%)', hue='Cluster', data=df, palette='viridis')
plt.title("K-Means Clustering")
plt.show()
