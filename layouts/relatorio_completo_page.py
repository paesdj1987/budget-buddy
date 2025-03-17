# relatorio_completo_page.py

from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Definir cores personalizadas
custom_colors = [
    '#E0F3F9', '#C6E7F1', '#ADDCE9', '#94D1E1', '#7BC5D8',
    '#62B9D0', '#499EB5', '#346F7A', '#345F6C', '#2D5260',
    '#264552', '#1F3844'
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


layout = html.Div(
    className="main-content",
    children=[
        dbc.Container(
            fluid=True,
            children=[
                # Título da página
                html.H3(
                    "Relatório Completo",
                    style={
                        "margin": "10px 0 20px 0",
                        "font-size": "2.5rem",
                        "color": "#345F6C",
                        "text-align": "center",
                        "font-weight": "bold"
                    }
                ),

                # Linha para os botões de exportação
                dbc.Row(
                    [
                        # Botão de exportação para Excel
                        dbc.Col(
                            dbc.Button(
                                "Exportar para Excel",
                                id="export-button-completo",
                                color="success",  # Cor verde
                                style={
                                    'margin-bottom': '10px',
                                    'margin-left': '15px',
                                    'background-color': '#28a745',  # Cor verde personalizada
                                    'border-color': '#28a745',
                                    'color': 'white',
                                    'height': '36px',  # Ajuste de altura para igualar ao botão de exportar
                                    'width': 'auto',
                                    'text-align': 'center',  # Centralizar o texto no botão
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'justify-content': 'center',
                                    'font-family': 'Montserrat',  # Alterar a fonte para Montserrat
                                    'font-size': '16px',  # Tamanho da fonte
                                }
                            ),
                            width="auto"
                        ),

                        # Botão de gerar PDF
                        dbc.Col(
                            dbc.Button(
                                "Gerar PDF",
                                id="generate-pdf-button-completo",
                                color="danger",  # Cor vermelha
                                style={
                                    'margin-bottom': '10px',
                                    'margin-left': '1px',
                                    'background-color': '#d9534f',  # Cor vermelha personalizada
                                    'border-color': '#d9534f',
                                    'color': 'white',
                                    'height': '36px',  # Ajuste de altura para igualar ao botão de exportar
                                    'width': 'auto',
                                    'text-align': 'center',  # Centralizar o texto no botão
                                    'display': 'flex',
                                    'align-items': 'center',
                                    'justify-content': 'center',
                                    'font-family': 'Montserrat',  # Alterar a fonte para Montserrat
                                    'font-size': '16px',  # Tamanho da fonte
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
                                id='results-table-completo',
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
                                data=[],  # Os dados serão inseridos pelo callback
                                style_table={
                                    'width': '110%',
                                    'overflowX': 'auto',
                                    'boxSizing': 'border-box',
                                    'border': '1px solid #345F6C',
                                    'borderRadius': '15px',
                                },
                                style_header={
                                    'backgroundImage': 'linear-gradient(to right, #346F7A, #345F6C, #2D5260)',  # Gradiente de azul
                                    'color': '#FFFFFF',  # Texto branco
                                    'fontWeight': 'bold',
                                    'fontSize': '15px',
                                    'textAlign': 'left',
                                    'border': '1px solid #345F6C',  # Borda azul escuro
                                    'lineHeight': '24px',  # Aumenta a altura das células do cabeçalho
                                },
                                style_cell={
                                    'backgroundColor': '#FFFFFF',  # Fundo branco nas células
                                    'color': '#000',  # Texto preto para legibilidade
                                    'padding': '12px',
                                    'fontSize': '14px',
                                    'textAlign': 'left',
                                    'border': '1px solid #345F6C',  # Borda azul escuro
                                    'lineHeight': '24px',  # Aumenta a altura das células
                                },
                                style_data={
                                    'backgroundColor': '#FFFFFF',  # Fundo branco nas células de dados
                                    'color': '#000',  # Texto preto
                                    'border': '1px solid #345F6C',  # Borda azul escuro
                                    'lineHeight': '24px',  # Aumenta a altura das células do dados
                                },
                                style_data_conditional=[
                                    {
                                        'if': {'state': 'active'},
                                        'backgroundColor': '#C6E7F1',  # Azul mais claro quando ativo
                                        'color': '#000',
                                        'border': '1px solid #345F6C',  # Borda azul escuro
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
                                                'margin-bottom': '5px'  # Reduziu espaço inferior
                                            }
                                        ),
                                        html.P(
                                            id="card-id-loteamento-completo",
                                            className="card-title",
                                            style={
                                                'fontSize': '14px',
                                                'color': '#000',
                                                'margin': '0'  # Remove margens padrão do <p>
                                            }
                                        ),
                                    ]),
                                    style={
                                        'borderRadius': '10px',
                                        'backgroundColor': '#B0E0E6',   # Cor de fundo (alterável)
                                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                                        'minHeight': '20px',           # Reduz a altura mínima
                                        'padding': '6px',             # Ajusta preenchimento interno
                                        'margin-bottom': '10px',      # Espaçamento entre cards
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
                                            id="card-valor-total-completo",
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
                                        'backgroundColor': '#B0E0E6',
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
                                            "Subtotal",
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
                                            id="card-sub-total-completo",
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
                                        'backgroundColor': '#B0E0E6',
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
                                            id="card-cc-at-completo",
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
                                        'backgroundColor': '#B0E0E6',
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
                                            id="card-cc-ap-completo",
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
                                        'backgroundColor': '#B0E0E6',
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
                                            id="card-cc-vgv-completo",
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
                            style={'margin-left': '20px'}
                        ),

                    ],
                    align="start",
                    justify="between",
                    className="mb-4"
                ),

                # Componente dcc.Download
                dcc.Download(id="download-dataframe-xlsx-completo"),
                dcc.Download(id="download-pdf-completo"),

                # Gráfico de Barras Horizontais
                dbc.Row(
                    dbc.Col(
                        dcc.Graph(
                            id='pyramid-chart-completo',
                            figure=pyramid_chart_figure,
                            config={'responsive': True},
                            style={'height': '650px', 'width': '100%', 'margin-top': '40px'}
                        ),
                        width=10
                    ),
                    className="mb-5"
                ),
            ],
        ),
    ]
)
