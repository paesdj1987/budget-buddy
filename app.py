# app.py

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from layouts import (
    home_page,
    manual_page,
    orcamento_simples_page,
    orcamento_completo_page,
    relatorio_simples_page,
    relatorio_completo_page,
    dashboards_page
)
from layouts.sidebar import sidebar
from callbacks.callbacks_simples import register_callbacks_simples  
from callbacks.callbacks_completo import register_callbacks_completo
from callbacks.callbacks_dashboards import register_callbacks_dashboards
from dash_extensions.enrich import DashProxy, MultiplexerTransform, Input, Output  

app = DashProxy(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="BudgetBuddy",
    suppress_callback_exceptions=True,
    transforms=[MultiplexerTransform()]
)

server = app.server

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    dcc.Store(id='shared-data', storage_type='session'),
    dcc.Store(id='shared-data-completo', storage_type='session'),
    html.Div(id="page-content"),
    html.Div(id='debug-output-completo', style={'whiteSpace': 'pre-wrap', 'padding': '20px'})
])

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page_content(pathname):
    if pathname == "/":
        return home_page.layout
    elif pathname == "/manual-do-usuario":
        return html.Div([
            sidebar,
            manual_page.layout
        ])
    elif pathname == "/orcamento-simples":
        return html.Div([
            sidebar,
            orcamento_simples_page.layout
        ])
    elif pathname == "/orcamento-completo":
        return html.Div([
            sidebar,
            orcamento_completo_page.layout
        ])
    elif pathname == "/relatorio-simples":
        return html.Div([
            sidebar,
            relatorio_simples_page.layout
        ])
    elif pathname == "/relatorio-completo":
        return html.Div([
            sidebar,
            relatorio_completo_page.layout
        ])
    elif pathname == "/dashboards":
        return html.Div([sidebar, dashboards_page.layout])
    else:
        return html.Div([
            sidebar,
            html.H3("404: Página não encontrada", style={"margin-left": "260px", "padding": "20px"})
        ])

# Novo callback para atualizar os links ativos do menu
@app.callback(
    [Output("navlink-home", "active"),
     Output("navlink-manual", "active"),
     Output("navlink-orc-simples", "active"),
     Output("navlink-rel-simples", "active"),
     Output("navlink-orc-completo", "active"),
     Output("navlink-rel-completo", "active"),
     Output("navlink-dashboards", "active")],
    [Input("url", "pathname")]
)
def update_active_links(pathname):
    return [
        pathname == "/",
        pathname == "/manual-do-usuario",
        pathname == "/orcamento-simples",
        pathname == "/relatorio-simples",
        pathname == "/orcamento-completo",
        pathname == "/relatorio-completo",
        pathname == "/dashboards"
    ]

# Register callbacks dos outros módulos
register_callbacks_simples(app)  
register_callbacks_completo(app)
register_callbacks_dashboards(app)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='8051')
