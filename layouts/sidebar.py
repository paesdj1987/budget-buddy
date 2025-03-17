#sidebar.py

from dash import html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

sidebar = html.Div(
    [
        html.H2("Menu", className="display-4", style={"font-size": "1.8rem"}),  
        html.Hr(),

        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        DashIconify(icon="material-symbols:home", width=23),  
                        html.Span("Página Inicial", style={"margin-left": "12px"})  
                    ],
                    href="/",
                    active="exact"
                ),
                dbc.NavLink(
                    [
                        DashIconify(icon="mdi:book-open-variant", width=23),
                        html.Span("Manual do Usuário", style={"margin-left": "12px"})  
                    ],
                    href="/manual-do-usuario",
                    active="exact"
                ),
                dbc.NavLink(
                    [
                        DashIconify(icon="mdi:clipboard-text", width=23),
                        html.Span("Orçamento Simplificado", style={"margin-left": "12px"})  
                    ],
                    href="/orcamento-simples",
                    active="exact"
                ),
                dbc.NavLink(
                    [
                        DashIconify(icon="mdi:file-chart", width=23),
                        html.Span("Relatório Simplificado", style={"margin-left": "12px"})  
                    ],
                    href="/relatorio-simples",
                    active="exact"
                ),
                dbc.NavLink(
                    [
                        DashIconify(icon="mdi:finance", width=23),
                        html.Span("Orçamento Completo", style={"margin-left": "12px"})  
                    ],
                    href="/orcamento-completo",
                    active="exact"
                ),
                dbc.NavLink(
                    [
                        DashIconify(icon="mdi:chart-box", width=23),
                        html.Span("Relatório Completo", style={"margin-left": "12px"})  
                    ],
                    href="/relatorio-completo",
                    active="exact"
                ),
                dbc.NavLink(
                    [
                        DashIconify(icon="mdi:view-dashboard", width=23),
                        html.Span("Dashboards", style={"margin-left": "12px"})  
                    ],
                    href="/dashboards",
                    active="exact"
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar"
)
