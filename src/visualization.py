import geopandas as gpd
import folium
import pandas as pd

def create_map(data_path, output_map):
    """Visualize population density on a map."""
    data = pd.read_csv(data_path)
    m = folium.Map(location=[20, 77], zoom_start=5)  # Adjust location as needed
    
    for _, row in data.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=row['population_density'] / 1000,
            color='blue',
            fill=True,
            fill_opacity=0.6
        ).add_to(m)
    
    m.save(output_map)
    print(f"Map saved as {output_map}")

if __name__ == "__main__":
    create_map("data/clustered_data.csv", "data/population_map.html")
visualization.py
