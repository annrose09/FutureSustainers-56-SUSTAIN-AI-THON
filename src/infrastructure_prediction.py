import pandas as pd
from sklearn.cluster import KMeans

def cluster_areas(data_path, n_clusters=3):
    """Cluster areas based on population density and demographics."""
    data = pd.read_csv(data_path)
    model = KMeans(n_clusters=n_clusters, random_state=42)
    data['Cluster'] = model.fit_predict(data[['population_density', 'income']])
    data.to_csv("data/clustered_data.csv", index=False)
    print("Clustering complete!")
    return data

if __name__ == "__main__":
    cluster_areas("data/cleaned_population_data.csv")
