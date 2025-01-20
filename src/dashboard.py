import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Define the clustered dataset path
clustered_data_file = "data/clustered_chennai_population.csv"

# Load the dataset
def load_clustered_data(file_path):
    """Load the clustered dataset from a CSV file."""
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

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Population Clustering Dashboard"

# Load data
data = load_clustered_data(clustered_data_file)

if data is None:
    raise FileNotFoundError(f"Error: Dataset not found at {clustered_data_file}. Please ensure the file exists.")

# Define layout of the dashboard
app.layout = html.Div([
    html.H1("Population Clustering Dashboard", style={"text-align": "center"}),

    # Dropdown for cluster selection
    html.Div([
        html.Label("Select Cluster:"),
        dcc.Dropdown(
            id="cluster-dropdown",
            options=[{"label": f"Cluster {i}", "value": i} for i in sorted(data['Cluster'].unique())],
            value=None,  # Default value
            placeholder="Select a cluster",
            multi=True,
        )
    ], style={"width": "40%", "margin": "0 auto"}),

    # Scatter plot
    dcc.Graph(id="scatter-plot"),

    # Feature distribution
    html.Div([
        html.Label("Select Feature for Distribution:"),
        dcc.Dropdown(
            id="feature-dropdown",
            options=[
                {"label": "Population", "value": "Population"},
                {"label": "City_Encoded", "value": "City_Encoded"}
            ],
            value="Population",
        )
    ], style={"width": "40%", "margin": "20px auto"}),

    dcc.Graph(id="feature-distribution"),
])

# Define callback for scatter plot
@app.callback(
    Output("scatter-plot", "figure"),
    [Input("cluster-dropdown", "value")]
)
def update_scatter_plot(selected_clusters):
    """Update the scatter plot based on selected clusters."""
    if selected_clusters:
        filtered_data = data[data['Cluster'].isin(selected_clusters)]
    else:
        filtered_data = data

    fig = px.scatter(
        filtered_data,
        x="Population",  # Using Population for the X-axis
        y="City_Encoded",  # Using City_Encoded for the Y-axis
        color="Cluster",
        title="Scatter Plot: Population vs City Encoded",
        labels={"Population": "Population", "City_Encoded": "City Encoded"},
        template="plotly",
    )
    fig.update_traces(marker=dict(size=10, opacity=0.7))
    return fig

# Define callback for feature distribution
@app.callback(
    Output("feature-distribution", "figure"),
    [Input("feature-dropdown", "value")]
)
def update_feature_distribution(selected_feature):
    """Update the feature distribution plot based on selected feature."""
    fig = px.box(
        data,
        x="Cluster",
        y=selected_feature,
        color="Cluster",
        title=f"Distribution of {selected_feature} Across Clusters",
        labels={selected_feature: selected_feature, "Cluster": "Cluster"},
        template="plotly",
    )
    fig.update_traces(boxmean="sd")
    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
