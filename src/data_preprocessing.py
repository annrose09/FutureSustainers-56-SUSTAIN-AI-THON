import pandas as pd
import geopandas as gpd

def load_data(file_path):
    """Load population density and demographics data."""
    data = pd.read_csv(file_path)
    print(f"Data loaded: {data.shape[0]} rows, {data.shape[1]} columns")
    return data

def clean_data(data):
    """Clean and preprocess the dataset."""
    data = data.dropna()  # Drop rows with missing values
    data = data[data['population_density'] > 0]  # Filter invalid values
    return data

if __name__ == "__main__":
    # Replace with your data file path
    data = load_data("data/population_data.csv")
    clean_data = clean_data(data)
    clean_data.to_csv("data/cleaned_population_data.csv", index=False)
    print("Data preprocessing complete!")
