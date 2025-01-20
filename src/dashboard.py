import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def load_data(file_path):
    return pd.read_csv(file_path)

def display_dashboard():
    st.title("Infrastructure Planning Dashboard")
    data = load_data("data/clustered_data.csv")
    
    # Population Density Insights
    st.subheader("Population Density Insights")
    st.dataframe(data[['area_name', 'population_density', 'Cluster']])
    
    # Map Visualization
    st.subheader("Population Map")
    m = folium.Map(location=[20, 77], zoom_start=5)
    for _, row in data.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=row['population_density'] / 1000,
            color='blue',
            fill=True,
            fill_opacity=0.6
        ).add_to(m)
    folium_static(m)

if __name__ == "__main__":
    display_dashboard()
