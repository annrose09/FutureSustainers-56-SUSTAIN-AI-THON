import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
import os

# Define the cleaned dataset path
cleaned_data_file = "data/cleaned_chennai_population.csv"

def load_cleaned_data(file_path):
    """Load the cleaned dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Cleaned dataset loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None

def label_encode_city(data):
    """Apply Label Encoding to the 'City' column."""
    if "City" not in data.columns:
        print("Error: 'City' column not found in the dataset.")
        return None
    
    label_encoder = LabelEncoder()
    data['City_Encoded'] = label_encoder.fit_transform(data['City'])
    print("Label encoding applied to the 'City' column.")
    return data

def preprocess_data_for_clustering(data):
    """Standardize the data for clustering."""
    if not {"City_Encoded", "Population"}.issubset(data.columns):
        print("Error: Required columns ('City_Encoded', 'Population') not found in the dataset.")
        return None

    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[["City_Encoded", "Population"]])
    print("Data standardized for clustering.")
    return scaled_data

def apply_kmeans_clustering(scaled_data, n_clusters=4):
    """Apply KMeans clustering to the standardized data."""
    if scaled_data is None:
        print("No data available for clustering.")
        return None, None

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)
    print(f"KMeans clustering applied with {n_clusters} clusters.")
    return clusters, kmeans

def add_clusters_to_data(data, clusters):
    """Add cluster labels to the dataset."""
    if clusters is None:
        print("No clusters to add to the dataset.")
        return None

    data['Cluster'] = clusters
    print("Clusters successfully added to the dataset.")
    return data

def save_clustered_data(data, file_path):
    """Save the clustered dataset to a CSV file."""
    try:
        data.to_csv(file_path, index=False)
        print(f"Clustered data saved successfully to {file_path}.")
    except Exception as e:
        print(f"An error occurred while saving the clustered data: {e}")

def visualize_clusters(data):
    """Visualize clusters using a scatter plot."""
    if not {"Cluster", "City_Encoded", "Population"}.issubset(data.columns):
        print("Error: Required columns ('Cluster', 'City_Encoded', 'Population') not found in the dataset.")
        return

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="Population", y="City_Encoded", hue="Cluster", data=data, palette="Set1", alpha=0.7)
    plt.title("Clusters Based on Population and City (Encoded)", fontsize=16)
    plt.xlabel("Population", fontsize=12)
    plt.ylabel("City (Encoded)", fontsize=12)
    plt.grid(axis="both", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("visualizations/clusters_visualization.png")
    plt.show()
    print("Cluster visualization saved in 'visualizations/'.")

def main():
    # Load the cleaned dataset
    data = load_cleaned_data(cleaned_data_file)

    # Create a directory for visualizations
    os.makedirs("visualizations", exist_ok=True)

    # Apply label encoding to the 'City' column
    data = label_encode_city(data)

    # Preprocess data for clustering
    scaled_data = preprocess_data_for_clustering(data)

    # If preprocessing fails, exit gracefully
    if scaled_data is None:
        print("Preprocessing failed. Ensure the dataset contains the required columns.")
        return

    # Apply KMeans clustering
    clusters, kmeans_model = apply_kmeans_clustering(scaled_data, n_clusters=4)

    # If clustering fails, exit gracefully
    if clusters is None:
        print("Clustering failed. Ensure the data is valid and correctly preprocessed.")
        return

    # Add cluster labels to the dataset
    clustered_data = add_clusters_to_data(data, clusters)

    # Save the clustered dataset
    if clustered_data is not None:
        save_clustered_data(clustered_data, "data/clustered_chennai_population.csv")

    # Visualize clusters
    if clustered_data is not None:
        visualize_clusters(clustered_data)

if __name__ == "__main__":
    main()
