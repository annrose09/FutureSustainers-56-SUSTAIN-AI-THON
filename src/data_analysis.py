import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

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

def generate_summary_statistics(data):
    """Generate and display summary statistics of the dataset."""
    if data is None:
        print("No data available for analysis.")
        return

    print("\n--- Summary Statistics ---")
    print(data.describe(include="all"))

def visualize_city(data):
    """Visualize City distribution."""
    if "City_Encoded" not in data.columns:
        print("Error: 'City_Encoded' column not found in the dataset.")
        return

    plt.figure(figsize=(10, 6))
    sns.histplot(data["City_Encoded"], kde=True, color="blue", bins=30)
    plt.title("City Distribution (Encoded)", fontsize=16)
    plt.xlabel("City (Encoded)", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("visualizations/City_distribution_encoded.png")
    plt.show()
    print("City distribution visualization saved in 'visualizations/'.")

def visualize_relationship(data):
    """Visualize relationships between variables."""
    if not {"City_Encoded", "Population"}.issubset(data.columns):
        print("Error: Required columns ('City_Encoded', 'Population') not found in the dataset.")
        return

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="Population", y="City_Encoded", data=data, alpha=0.7)
    plt.title("Relationship Between Population and City (Encoded)", fontsize=16)
    plt.xlabel("Population", fontsize=12)
    plt.ylabel("City (Encoded)", fontsize=12)
    plt.grid(axis="both", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("visualizations/population_vs_city_encoded.png")
    plt.show()
    print("Population vs. City (Encoded) visualization saved in 'visualizations/'.")

def main():
    # Load the cleaned dataset
    data = load_cleaned_data(cleaned_data_file)

    # Create a directory for visualizations
    import os
    os.makedirs("visualizations", exist_ok=True)

    # Apply label encoding to the 'City' column
    data = label_encode_city(data)

    # Generate summary statistics
    generate_summary_statistics(data)

    # Visualize population density distribution
    visualize_city(data)

    # Visualize relationships between variables
    visualize_relationship(data)

if __name__ == "__main__":
    main()
