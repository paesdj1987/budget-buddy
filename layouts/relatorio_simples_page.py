# relatorio_simples_page.py

from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Definir cores personalizadas
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
            x=0.5,  # Centraliza horizontalmente
            xanchor="center",
        ),
        xaxis=dict(
            title=dict(
                text="Valor Total Corrigido (R$)",
                font=dict(size=16, family="Arial")
            ),
            tickfont=dict(size=14, family="Arial"),
            gridcolor="rgba(200,200,200,0.5)",  # Linhas de grade suaves
            zeroline=False,  # Remove linha do zero
        ),
        yaxis=dict(
            title=dict(
                text="Serviços",
                font=dict(size=16, family="Arial")
            ),
            tickfont=dict(size=14, family="Arial"),
            categoryorder="total ascending",  # Ordena do maior para o menor
        ),
        paper_bgcolor="white",  # Fundo branco
        plot_bgcolor="white",  # Fundo do gráfico branco
        margin=dict(l=120, r=40, t=80, b=50),  # Margens ajustadas
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
        height=600,  # Altura padrão do gráfico
    )
)

# Layout principal
layout = html.Div(
    className="main-content",
    children=[
        dbc.Container(
            fluid=True,
            children=[
                # Título da página
                html.H3(
                    "Relatório Simplificado",
                    style={
                        "margin": "10px 0 20px 0",
                        "font-size": "2.5rem",
                        "color": "#FF8C00",
                        "text-align": "center",
                        "font-weight": "bold"
                    }
                ),

                # Linha para os botões de exportação
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Button(
                                "Exportar para Excel",
                                id="export-button",
                                color="success",
                                style={
                                    'margin-bottom': '10px',
                                    'margin-left': '15px',
                                    'background-color': '#28a745',
                                    'border-color': '#28a745',
                                    'color': 'white',
                                    'height': '36px',
                                    'width': 'auto',
                                    'text-align': 'center',
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'justify-content': 'center',
                                    'font-family': 'Montserrat',
                                    'font-size': '16px',
                                }
                            ),
                            width="auto"
                        ),
                        dbc.Col(
                            dbc.Button(
                                "Gerar PDF",
                                id="generate-pdf-button",
                                color="danger",
                                style={
                                    'margin-bottom': '10px',
                                    'margin-left': '1px',
                                    'background-color': '#d9534f',
                                    'border-color': '#d9534f',
                                    'color': 'white',
                                    'height': '36px',
                                    'width': 'auto',
                                    'text-align': 'center',
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'justify-content': 'center',
                                    'font-family': 'Montserrat',
                                    'font-size': '16px',
                                }
                            ),
                            width="auto"
                        ),
                    ],
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
                                    'lineHeight': '24px',  # Aumenta a altura das células do cabeçalho
                                },
                                style_cell={
                                    'backgroundColor': 'rgba(255,255,255,0.2)',
                                    'color': '#000',
                                    'padding': '12px',
                                    'fontSize': '14px',
                                    'textAlign': 'left',
                                    'border': '1px solid #FFA07A',
                                    'lineHeight': '24px',  # Aumenta a altura das células 
                                },
                                style_data={
                                    'backgroundColor': 'rgba(255,255,255,0.2)',
                                    'color': '#000',
                                    'border': '1px solid #FFA07A',
                                    'lineHeight': '24px',  # Aumenta a altura das células do dados
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

                        # Coluna para os cards
                        dbc.Col(
                            [
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H4(
                                            "ID Cond. Horizontais",
                                            className="card-text",
                                            style={
                                                'fontSize': '16px',
                                                'color': '#000',
                                                'fontWeight': 'bold',
                                                'fontFamily': 'Montserrat',
                                                'margin-bottom': '5px'  # Reduz espaço inferior
                                            }
                                        ),
                                        html.P(
                                            id="card-id-loteamento",
                                            className="card-title",
                                            style={
                                                'fontSize': '14px',
                                                'color': '#000',
                                                'margin': '0'  # Remove margens padrão ***
                                            }
                                        ),
                                    ]),
                                    style={
                                        'borderRadius': '10px',
                                        'backgroundColor': '#ffa80c',
                                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                                        'minHeight': '20px',  # Reduz a altura mínima  ***
                                        'padding': '6px',     # Ajusta preenchimento interno ***
                                        'margin-bottom': '10px',  # Reduz o espaçamento entre cards
                                        'width': '230px',
                                    }
                                ),
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H4(
                                            "Valor Total do Orçamento",
                                            className="card-text",
                                            style={
                                                'fontSize': '16px',
                                                'color': '#000',
                                                'fontWeight': 'bold',
                                                'fontFamily': 'Montserrat',
                                                'margin-bottom': '5px'
                                            }
                                        ),
                                        html.P(
                                            id="card-valor-total",
                                            className="card-title",
                                            style={
                                                'fontSize': '14px',
                                                'color': '#000',
                                                'margin': '0'
                                            }
                                        ),
                                    ]),
                                    style={
                                        'borderRadius': '10px',
                                        'backgroundColor': '#ffa80c',
                                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                                        'minHeight': '20px',
                                        'padding': '6px',
                                        'margin-bottom': '10px',
                                        'width': '230px',
                                    }
                                ),

                                #"CC/FIP",
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H4(
                                            "CC/FIP",
                                            className="card-text",
                                            style={
                                                'fontSize': '16px',
                                                'color': '#000',
                                                'fontWeight': 'bold',
                                                'fontFamily': 'Montserrat',
                                                'margin-bottom': '5px'
                                            }
                                        ),
                                        html.P(
                                            id="card-cc-fip",
                                            className="card-title",
                                            style={
                                                'fontSize': '14px',
                                                'color': '#000',
                                                'margin': '0'
                                            }
                                        ),
                                    ]),
                                    style={
                                        'borderRadius': '10px',
                                        'backgroundColor': '#ffa80c',
                                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                                        'minHeight': '20px',
                                        'padding': '6px',
                                        'margin-bottom': '10px',
                                        'width': '230px',
                                    }
                                ),
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H4(
                                            "CC/AT",
                                            className="card-text",
                                            style={
                                                'fontSize': '16px',
                                                'color': '#000',
                                                'fontWeight': 'bold',
                                                'fontFamily': 'Montserrat',
                                                'margin-bottom': '5px'
                                            }
                                        ),
                                        html.P(
                                            id="card-cc-at",
                                            className="card-title",
                                            style={
                                                'fontSize': '14px',
                                                'color': '#000',
                                                'margin': '0'
                                            }
                                        ),
                                    ]),
                                    style={
                                        'borderRadius': '10px',
                                        'backgroundColor': '#ffa80c',
                                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                                        'minHeight': '20px',
                                        'padding': '6px',
                                        'margin-bottom': '10px',
                                        'width': '230px',
                                    }
                                ),
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H4(
                                            "CC/AP",
                                            className="card-text",
                                            style={
                                                'fontSize': '16px',
                                                'color': '#000',
                                                'fontWeight': 'bold',
                                                'fontFamily': 'Montserrat',
                                                'margin-bottom': '5px'
                                            }
                                        ),
                                        html.P(
                                            id="card-cc-ap",
                                            className="card-title",
                                            style={
                                                'fontSize': '14px',
                                                'color': '#000',
                                                'margin': '0'
                                            }
                                        ),
                                    ]),
                                    style={
                                        'borderRadius': '10px',
                                        'backgroundColor': '#ffa80c',
                                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                                        'minHeight': '20px',
                                        'padding': '6px',
                                        'margin-bottom': '10px',
                                        'width': '230px',
                                    }
                                ),
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H4(
                                            "CC/VGV",
                                            className="card-text",
                                            style={
                                                'fontSize': '16px',
                                                'color': '#000',
                                                'fontWeight': 'bold',
                                                'fontFamily': 'Montserrat',
                                                'margin-bottom': '5px'
                                            }
                                        ),
                                        html.P(
                                            id="card-cc-vgv",
                                            className="card-title",
                                            style={
                                                'fontSize': '14px',
                                                'color': '#000',
                                                'margin': '0'
                                            }
                                        ),
                                    ]),
                                    style={
                                        'borderRadius': '10px',
                                        'backgroundColor': '#d4edda',
                                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                                        'minHeight': '20px',
                                        'padding': '6px',
                                        'margin-bottom': '10px',
                                        'width': '230px',
                                    }
                                ),
                            ],
                            width=11,
                            md=4,
                            style={
                                'margin-left': '20px'
                            }
                        ),
                    ],
                    align="start",
                    justify="between",
                    className="mb-4"
                ),

                # Componente dcc.Download
                dcc.Download(id="download-dataframe-xlsx"),
                dcc.Download(id="download-pdf"),

                # Gráfico de barras
                dbc.Row(
                    dbc.Col(
                        dcc.Graph(
                            id='bar-chart',
                            figure=pyramid_chart_figure,
                            config={
                                'responsive': True  # Permite que o gráfico se ajuste ao container
                            },
                            style={
                                'width': '100%',    # Usa toda a largura da coluna/container
                                'height': '80vh',   # Usa 80% da altura da viewport (ajuste se quiser maior/menor)
                                'maxWidth': 'none',
                                'margin': '0 auto', # Centraliza horizontalmente se houver espaço sobrando
                                'padding': '0'
                            }
                        ),
                        width=10
                    ),
                    className="mb-5"
                ),
            ],
        ),
    ]
)
