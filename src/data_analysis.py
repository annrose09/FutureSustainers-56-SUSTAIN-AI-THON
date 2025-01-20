import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_population_density(data_path):
    """Analyze population density distribution."""
    data = pd.read_csv(data_path)
    plt.figure(figsize=(10, 6))
    sns.histplot(data['population_density'], kde=True, bins=30)
    plt.title("Population Density Distribution")
    plt.xlabel("Density")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    analyze_population_density("data/cleaned_population_data.csv")
