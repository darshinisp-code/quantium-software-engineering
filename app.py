import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Read the processed data
df = pd.read_csv("output.csv")

# Convert date column to date format
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    annotation_text="Price Increase"
)
# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualizer"),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)