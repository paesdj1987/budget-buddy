#dashboard

from dash import html
import dash_bootstrap_components as dbc

layout = html.Div(
    className="main-content",
    children=[
        dbc.Container(
            fluid=True,
            children=[
                html.H3(
                    "Página em Construção",
                    style={
                        "margin": "10px 0 20px 0",
                        "font-size": "2.5rem",
                        "color": "#345F6C",
                        "text-align": "center",
                        "font-weight": "bold"
                    }
                ),
            ],
        ),
    ]
)
