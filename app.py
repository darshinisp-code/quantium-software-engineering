import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Soul Foods Sales Visualizer",
        id = "header",
        style={
            "textAlign": "center",
            "color": "#2c3e50",
            "backgroundColor": "#d6eaf8",
            "padding": "15px",
            "borderRadius": "10px"
        }
    ),

    html.H3(
        "Select Region",
        style={
            "textAlign": "center",
            "color": "#34495e"
        }
    ),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"}
        ],
        value="All",
        inline=True,
        style={
            "textAlign": "center",
            "padding": "10px"
        }
    ),

    dcc.Graph(id="sales-chart")

], style={
    "backgroundColor": "#f4f6f7",
    "padding": "20px"
})


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "All":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region}"
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        annotation_text="Price Increase"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f4f6f7",
        font=dict(size=14)
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)