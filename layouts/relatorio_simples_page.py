# relatorio_simples_page.py

from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Definir cores personalizadas (pode ser usado em outros elementos)
custom_colors = [
    '#FFF3E0', '#FFE0B2', '#FFCC80', '#FFB74D', '#FFA726',
    '#FF9800', '#FB8C00', '#F57C00', '#EF6C00', '#E65100'
]

# Configurar uma figura de gráfico de barras horizontais vazia
pyramid_chart_figure = go.Figure(
    layout=go.Layout(
        title=dict(
            text="Participação Percentual dos Serviços",
            font=dict(size=26, family="Montserrat", color="#FF8C00"),
            x=0.5,
            xanchor="center",
        ),
        xaxis=dict(
            title=dict(
                text="Valor Total Corrigido (R$)",
                font=dict(size=16, family="Arial")
            ),
            tickfont=dict(size=14, family="Arial"),
            gridcolor="rgba(200,200,200,0.5)",
            zeroline=False,
        ),
        yaxis=dict(
            title=dict(
                text="Serviços",
                font=dict(size=16, family="Arial")
            ),
            tickfont=dict(size=14, family="Arial"),
            categoryorder="total ascending",
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=120, r=40, t=80, b=50),
        annotations=[
            dict(
                text="Sem dados para exibir",
                showarrow=False,
                font=dict(size=16),
                x=0.5,
                y=0.5,
                xanchor="center",
                yanchor="middle",
                align="center",
            )
        ],
        height=600,
    )
)

# Largura dos cards ajustada
card_width = "230px"

# Estilo moderno para os cards alaranjados (ID Cond. Horizontais até CC/AP)
modern_card_style_orange = {
    "border": "none",
    "borderRadius": "10px",
    "background": "linear-gradient(135deg, #FFA726, #FB8C00)",
    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
    "minHeight": "20px",
    "padding": "6px",
    "marginBottom": "10px",
    "width": card_width,
}

# Estilo moderno para o card CC/VGV (verde)
modern_card_style_green = {
    "border": "none",
    "borderRadius": "10px",
    "background": "linear-gradient(135deg, #2ecc71, #27ae60)",
    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
    "minHeight": "20px",
    "padding": "6px",
    "marginBottom": "10px",
    "width": card_width,
}

# Estilos modernos para os botões de exportação
excel_button_style = {
    'margin-bottom': '10px',
    'margin-left': '15px',
    'background': 'linear-gradient(90deg, #28a745, #66bb6a)',
    'border': 'none',
    'color': 'white',
    'height': '40px',
    'width': 'auto',
    'text-align': 'center',
    'display': 'flex',
    'align-items': 'center',
    'justify-content': 'center',
    'font-family': 'Montserrat, sans-serif',
    'font-size': '14px',
    'borderRadius': '8px',
    'boxShadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
    'transition': 'background 0.3s ease'
}

pdf_button_style = {
    'margin-bottom': '10px',
    'margin-left': '1px',
    'background': 'linear-gradient(90deg, #d9534f, #e57373)',
    'border': 'none',
    'color': 'white',
    'height': '40px',
    'width': 'auto',
    'text-align': 'center',
    'display': 'flex',
    'align-items': 'center',
    'justify-content': 'center',
    'font-family': 'Montserrat, sans-serif',
    'font-size': '14px',
    'borderRadius': '8px',
    'boxShadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
    'transition': 'background 0.3s ease'
}

layout = html.Div(
    className="main-content",
    style={
        "font-family": "'Montserrat', sans-serif",
        "position": "relative"  
    },
    children=[

        # Imagem logoor.png 
        html.Img(
            src="assets/logoor.png",
            style={
                "position": "absolute",
                "top": "20px",
                "right": "20px",
                "width": "80px"  
            }
        ),

        dbc.Container(
            fluid=True,
            children=[
                # Espaçamento superior
                html.Div(style={"padding-top": "40px"}),

                # Título da página
                html.H3(
                    "📄 Relatório Simplificado",
                    style={
                        "margin": "10px 0 20px 0",
                        "font-size": "2rem",
                        "color": "#345F6C",
                        "text-align": "center",
                        "font-weight": "bold"
                    }
                ),
               
                # Linha para os botões de exportação
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Button(
                                [
                                    html.I(className="fas fa-file-excel", style={"marginRight": "8px"}),
                                    "Exportar para Excel"
                                ],
                                id="export-button",
                                style=excel_button_style,
                                n_clicks=0
                            ),
                            width="auto"
                        ),
                        dbc.Col(
                            dbc.Button(
                                [
                                    html.I(className="fas fa-file-pdf", style={"marginRight": "8px"}),
                                    "Gerar PDF"
                                ],
                                id="generate-pdf-button",
                                style=pdf_button_style,
                                n_clicks=0
                            ),
                            width="auto"
                        ),
                    ],
                    style={"marginTop": "50px"},
                    justify="start",
                ),
                
                # Linha para a tabela e os cards
                dbc.Row(
                    [
                        # Coluna para a tabela
                        dbc.Col(
                            dash_table.DataTable(
                                id='results-table',
                                columns=[
                                    {"name": "Item", "id": "item"},
                                    {
                                        "name": "Custo Unitário",
                                        "id": "custo_unitario",
                                        "type": "numeric",
                                        "format": {
                                            "locale": {"symbol": ["R$", ""]},
                                            "specifier": "$,.2f"
                                        }
                                    },
                                    {
                                        "name": "Quantitativo",
                                        "id": "quantitativo",
                                        "type": "numeric",
                                        "format": {
                                            "locale": {"symbol": ["R$", ""]},
                                            "specifier": "$,.2f"
                                        }
                                    },
                                    {
                                        "name": "Valor Total",
                                        "id": "valor_total_corrigido",
                                        "type": "numeric",
                                        "format": {
                                            "locale": {"symbol": ["R$", ""]},
                                            "specifier": "$,.2f"
                                        }
                                    }
                                ],
                                data=[],
                                style_table={
                                    'width': '110%',
                                    'overflowX': 'auto',
                                    'boxSizing': 'border-box',
                                    'border': '1px solid #FFA07A',
                                    'borderRadius': '15px',
                                },
                                style_header={
                                    'backgroundImage': 'linear-gradient(to right, #FFA80B, #FFC75F)',
                                    'color': '#000',
                                    'fontWeight': 'bold',
                                    'fontSize': '15px',
                                    'textAlign': 'left',
                                    'border': '1px solid #FFA07A',
                                    'lineHeight': '24px',
                                },
                                style_cell={
                                    'backgroundColor': 'rgba(255,255,255,0.2)',
                                    'color': '#000',
                                    'padding': '12px',
                                    'fontSize': '14px',
                                    'textAlign': 'left',
                                    'border': '1px solid #FFA07A',
                                    'lineHeight': '24px',
                                },
                                style_data={
                                    'backgroundColor': 'rgba(255,255,255,0.2)',
                                    'color': '#000',
                                    'border': '1px solid #FFA07A',
                                    'lineHeight': '24px',
                                },
                                style_data_conditional=[
                                    {
                                        'if': {'state': 'active'},
                                        'backgroundColor': 'rgba(255,255,255,0.3)',
                                        'color': '#000',
                                        'border': '1px solid #FFA07A',
                                    },
                                ],
                            ),
                            width=11,
                            md=7
                        ),
                        
                        # Coluna para os cards modernos
                        dbc.Col(
                            [
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H5(
                                            "ID Cond. Horizontais",
                                            className="card-title",
                                            style={"fontWeight": "600", "color": "white", "marginBottom": "0.5rem", "fontSize": "14px"}
                                        ),
                                        html.H2(
                                            id="card-id-loteamento",
                                            style={"fontWeight": "700", "color": "white", "margin": "0", "fontSize": "16px"}
                                        ),
                                    ], style={"textAlign": "center", "padding": "1rem"}),
                                    style=modern_card_style_orange
                                ),
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H5(
                                            "Valor Total do Orçamento",
                                            className="card-title",
                                            style={"fontWeight": "600", "color": "white", "marginBottom": "0.5rem", "fontSize": "14px"}
                                        ),
                                        html.H2(
                                            id="card-valor-total",
                                            style={"fontWeight": "700", "color": "white", "margin": "0", "fontSize": "16px"}
                                        ),
                                    ], style={"textAlign": "center", "padding": "1rem"}),
                                    style=modern_card_style_orange
                                ),
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H5(
                                            "CC/FIP",
                                            className="card-title",
                                            style={"fontWeight": "600", "color": "white", "marginBottom": "0.5rem", "fontSize": "14px"}
                                        ),
                                        html.H2(
                                            id="card-cc-fip",
                                            style={"fontWeight": "700", "color": "white", "margin": "0", "fontSize": "16px"}
                                        ),
                                    ], style={"textAlign": "center", "padding": "1rem"}),
                                    style=modern_card_style_orange
                                ),
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H5(
                                            "CC/AT",
                                            className="card-title",
                                            style={"fontWeight": "600", "color": "white", "marginBottom": "0.5rem", "fontSize": "14px"}
                                        ),
                                        html.H2(
                                            id="card-cc-at",
                                            style={"fontWeight": "700", "color": "white", "margin": "0", "fontSize": "16px"}
                                        ),
                                    ], style={"textAlign": "center", "padding": "1rem"}),
                                    style=modern_card_style_orange
                                ),
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H5(
                                            "CC/AP",
                                            className="card-title",
                                            style={"fontWeight": "600", "color": "white", "marginBottom": "0.5rem", "fontSize": "14px"}
                                        ),
                                        html.H2(
                                            id="card-cc-ap",
                                            style={"fontWeight": "700", "color": "white", "margin": "0", "fontSize": "16px"}
                                        ),
                                    ], style={"textAlign": "center", "padding": "1rem"}),
                                    style=modern_card_style_orange
                                ),
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H5(
                                            "CC/VGV",
                                            className="card-title",
                                            style={"fontWeight": "600", "color": "white", "marginBottom": "0.5rem", "fontSize": "14px"}
                                        ),
                                        html.H2(
                                            id="card-cc-vgv",
                                            style={"fontWeight": "700", "color": "white", "margin": "0", "fontSize": "16px"}
                                        ),
                                    ], style={"textAlign": "center", "padding": "1rem"}),
                                    style=modern_card_style_green
                                ),
                            ],
                            width=11,
                            md=4,
                            style={'margin-left': '40px'}
                        ),
                    ],
                    align="start",
                    justify="between",
                    className="mb-4"
                ),
                
                # Componentes para download
                dcc.Download(id="download-dataframe-xlsx"),
                dcc.Download(id="download-pdf"),
                
                # Gráfico de barras
                dbc.Row(
                    dbc.Col(
                        dcc.Graph(
                            id='bar-chart',
                            figure=pyramid_chart_figure,
                            config={'responsive': True},
                            style={'height': '650px', 'width': '105%', 'margin-top': '40px'}
                        ),
                        width=10
                    ),
                    className="mb-5"
                ),
            ],
        ),
    ]
)
