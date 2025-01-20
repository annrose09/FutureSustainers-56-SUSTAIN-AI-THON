import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define the clustered dataset path
clustered_data_file = "data/clustered_chennai_population.csv"

def load_clustered_data(file_path):
    """Load the clustered dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Clustered dataset loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None

def visualize_cluster_distribution(data):
    """Visualize the number of areas in each cluster."""
    if "Cluster" not in data.columns:
        print("Error: 'Cluster' column not found in the dataset.")
        return

    plt.figure(figsize=(8, 6))
    sns.countplot(x='Cluster', data=data, palette='Set2')
    plt.title("Cluster Distribution", fontsize=16)
    plt.xlabel("Cluster", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("visualizations/cluster_distribution.png")
    plt.show()
    print("Cluster distribution visualization saved in 'visualizations/'.")

def visualize_feature_distributions(data, features):
    """Visualize the distributions of selected features across clusters."""
    for feature in features:
        if feature not in data.columns:
            print(f"Error: Feature '{feature}' not found in the dataset.")
            continue

        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Cluster', y=feature, data=data, palette='Set3')
        plt.title(f"{feature} Distribution Across Clusters", fontsize=16)
        plt.xlabel("Cluster", fontsize=12)
        plt.ylabel(feature, fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(f"visualizations/{feature}_distribution_across_clusters.png")
        plt.show()
        print(f"{feature} distribution visualization saved in 'visualizations/'.")

def visualize_cluster_relationships(data, x_col, y_col):
    """Visualize relationships between two features with clusters."""
    if not {'Cluster', x_col, y_col}.issubset(data.columns):
        print(f"Error: Required columns ('Cluster', '{x_col}', '{y_col}') not found in the dataset.")
        return

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_col, y=y_col, hue='Cluster', data=data, palette='Set1', alpha=0.8)
    plt.title(f"Relationship Between {x_col} and {y_col} by Cluster", fontsize=16)
    plt.xlabel(x_col, fontsize=12)
    plt.ylabel(y_col, fontsize=12)
    plt.legend(title='Cluster')
    plt.grid(axis='both', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"visualizations/{x_col}_vs_{y_col}_by_cluster.png")
    plt.show()
    print(f"Relationship between {x_col} and {y_col} visualization saved in 'visualizations/'.")

def main():
    # Load the clustered dataset
    data = load_clustered_data(clustered_data_file)

    # Ensure visualizations directory exists
    os.makedirs("visualizations", exist_ok=True)

    # Visualize the cluster distribution
    visualize_cluster_distribution(data)

    # Define features for distribution visualization
    features = ['City_Encoded', 'Population']

    # Visualize feature distributions across clusters
    visualize_feature_distributions(data, features)

    # Visualize relationships between features with cluster highlights
    visualize_cluster_relationships(data, x_col='City_Encoded', y_col='Population')

if __name__ == "__main__":
    main()
