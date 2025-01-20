import pandas as pd

# Define file paths
input_file = "data/chennai_population.csv"
output_file = "data/cleaned_chennai_population.csv"

def load_data(file_path):
    """Load the dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Dataset loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None

def clean_data(data):
    """Clean the dataset by handling missing values and removing duplicates."""
    if data is None:
        print("No data to clean.")
        return None

    # Display initial data info
    print("Initial Dataset Info:")
    print(data.info())

    # Drop duplicates
    data = data.drop_duplicates()
    print(f"Removed duplicates. Remaining rows: {data.shape[0]}.")

    # Handle missing values
    missing_columns = data.columns[data.isnull().any()]
    for col in missing_columns:
        # Fill numerical columns with the median and categorical columns with the mode
        if data[col].dtype in ['float64', 'int64']:
            data[col].fillna(data[col].median(), inplace=True)
            print(f"Filled missing values in numerical column '{col}' with the median.")
        else:
            data[col].fillna(data[col].mode()[0], inplace=True)
            print(f"Filled missing values in categorical column '{col}' with the mode.")

    # Ensure no missing values remain
    if data.isnull().sum().sum() == 0:
        print("All missing values handled successfully.")
    else:
        print("Warning: Some missing values could not be handled.")

    return data

def save_cleaned_data(data, file_path):
    """Save the cleaned dataset to a CSV file."""
    try:
        data.to_csv(file_path, index=False)
        print(f"Cleaned data saved successfully to {file_path}.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def main():
    # Load the raw data
    raw_data = load_data(input_file)

    # Clean the data
    cleaned_data = clean_data(raw_data)

    # Save the cleaned data
    if cleaned_data is not None:
        save_cleaned_data(cleaned_data, output_file)

if __name__ == "__main__":
    main()
