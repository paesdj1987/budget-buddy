# dashboards_page.py

from dash import html, dcc
import dash_bootstrap_components as dbc
from callbacks.callbacks_dashboards import ITENS_VALIDOS
import plotly.graph_objects as go 

layout = html.Div(
    className="main-content",
    style={
        "font-family": "'Montserrat', sans-serif",
        "position": "relative"  
    }, 
    children=[
        dbc.Container(
            fluid=True,
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

                # Espaçamento superior geral da página
                html.Div(style={"padding-top": "40px"}),

                # Título Principal
                html.H3(
                    "📊 Análise Comparativa de Projetos",
                    style={
                        "margin-bottom": "40px",
                        "font-size": "2rem",
                        "text-align": "center",
                        "color": "#345F6C",
                        "font-weight": "bold"
                    }
                ),

                # SEÇÃO DE DOWNLOAD DO TEMPLATE
                dbc.Card(
                    dbc.CardBody([
                        html.H4("📥 Baixar Planilha Modelo", style={"color": "#1D3B53", "font-size": "16px", "font-weight": "600"}),
                        html.P(
                            "Faça o download da planilha modelo, preencha os dados e envie para análise comparativa.",
                            style={"color": "#666", "text-align": "center"}
                        ),
                        html.Div(
                            dbc.Button(
                                "Baixar Modelo",
                                id="download-template-button",
                                color="primary",
                                className="mt-2",
                                style={
                                    "font-size": "1rem",
                                    "padding": "6px 14px",
                                    "border-radius": "8px"
                                }
                            ),
                            style={"textAlign": "center"}
                        ),
                        dcc.Download(id="download-template"),
                        html.Div(
                            id="download-message",
                            style={"textAlign": "center", "color": "#28a745", "margin-top": "10px"}
                        )
                    ]),
                    className="mb-4 shadow-sm",
                    style={
                        "border-radius": "12px",
                        "backgroundColor": "#f5f5f5",  
                        "border": "1px solid #e0e0e0"
                    }
                ),

                # SEÇÃO DE UPLOAD (Para Enviar 2 Planilhas)
                dbc.Card(
                    dbc.CardBody([
                        html.H4(
                            "📂 Realizar Uploads de Planilhas",
                            style={"color": "#1D3B53", "fontSize": "16px", "fontWeight": "600"}
                        ),
                        html.P(
                            "Envie duas planilhas preenchidas para comparar diferentes projetos.",
                            style={"color": "#666", "textAlign": "center"}
                        ),
                        dbc.Row(
                            [
                                # Upload da Planilha 1
                                dbc.Col(
                                    html.Div([  
                                        html.Label("📑 Planilha 1:", style={"fontWeight": "bold", "display": "block", "marginBottom": "8px"}),
                                        dcc.Upload(
                                            id="upload-planilha-1",
                                            children=html.Div([
                                                "Arraste ou ",
                                                html.Span("clique para selecionar o arquivo", style={"color": "#007bff"}),
                                                html.I(className="fas fa-upload", style={"marginLeft": "5px"})
                                            ], style={"fontSize": "14px"}),
                                            style={
                                                "width": "90%",
                                                "height": "60px",
                                                "lineHeight": "60px",
                                                "borderWidth": "2px",
                                                "borderStyle": "dashed",
                                                "borderRadius": "6px",
                                                "borderColor": "#FFA07A",
                                                "textAlign": "center",
                                                "cursor": "pointer",
                                                "backgroundColor": "#ffffff",
                                                "fontWeight": "bold",
                                                "color": "#666",
                                                "margin": "0 auto"  # Centraliza horizontalmente
                                            },
                                            multiple=False
                                        ),
                                        html.Div(
                                            id="output-planilha-1",
                                            style={"color": "#28a745", "marginTop": "10px", "fontWeight": "bold"}
                                        )
                                    ], style={"textAlign": "center"}),
                                    width=6
                                ),

                                dbc.Col(
                                    html.Div([
                                        html.Label("📑 Planilha 2:", style={"fontWeight": "bold", "display": "block", "marginBottom": "8px"}),
                                        dcc.Upload(
                                            id="upload-planilha-2",
                                            children=html.Div([
                                                "Arraste ou ",
                                                html.Span("clique para selecionar o arquivo", style={"color": "#007bff"}),
                                                html.I(className="fas fa-upload", style={"marginLeft": "5px"})
                                            ], style={"fontSize": "14px"}),
                                            style={
                                                "width": "90%",
                                                "height": "60px",
                                                "lineHeight": "60px",
                                                "borderWidth": "2px",
                                                "borderStyle": "dashed",
                                                "borderRadius": "6px",
                                                "borderColor": "#FFA07A",
                                                "textAlign": "center",
                                                "cursor": "pointer",
                                                "backgroundColor": "#ffffff",
                                                "fontWeight": "bold",
                                                "color": "#666",
                                                "margin": "0 auto"
                                            },
                                            multiple=False
                                        ),
                                        html.Div(
                                            id="output-planilha-2",
                                            style={"color": "#28a745", "marginTop": "10px", "fontWeight": "bold"}
                                        )
                                    ], style={"textAlign": "center"}),
                                    width=6
                                ),

                            ],
                            className="mb-3"
                        ),

                        # Linha separadora fina acima da seção "Filtrar Itens"
                        html.Hr(style={"border": "0", "borderTop": "1.5px solid orange", "margin": "10px auto", "width": "70%"}),

                        # Seção de Filtro de Itens
                        html.Div(
                            [
                                html.H4(
                                    "🧮 Filtrar Itens",
                                    style={"color": "#1D3B53", "fontSize": "16px", "fontWeight": "600", "margin": "0"}
                                )
                            ],
                            style={
                                "display": "flex",
                                "alignItems": "center",
                                "marginTop": "20px",
                                "marginBottom": "20px",
                                "textAlign": "left"
                            }
                        ),
                        html.Div(
                            "Selecione os itens abaixo para filtrar a análise. Caso faça alguma alteração, clique no botão Gerar Análise novamente.",
                            style={"textAlign": "center", "color": "#666", "fontSize": "14px",  "marginTop": "20px", "marginBottom": "20px"}
                        ),
                        dcc.Dropdown(
                            id="filter-dropdown",
                            options=[{"label": item, "value": item} for item in ITENS_VALIDOS],
                            value=ITENS_VALIDOS,
                            multi=True,
                            placeholder="Selecione os itens",
                            style={
                                "fontSize": "14px",
                                "padding": "4px",
                                "lineHeight": "20px",
                                "borderRadius": "6px",
                                "minHeight": "42px"  
                            }
                        ),
                        

                        # Linha separadora fina acima da seção "Filtrar Itens"
                        html.Hr(style={"border": "0", "borderTop": "1.5px solid orange", "margin": "10px auto", "width": "70%"}),

                        # Botões de Ação e Mensagem de Erro
                        html.Div(
                            [
                                dbc.Button(
                                    "📊 Gerar Análise",
                                    id="generate-analysis-button",
                                    color="success",
                                    style={
                                        "fontSize": "1rem",
                                        "padding": "6px 14px",
                                        "borderRadius": "8px",
                                        "marginRight": "10px"
                                    }
                                ),
                                dbc.Button(
                                    "🧹 Limpar",
                                    id="clear-uploads-button",
                                    color="secondary",
                                    style={
                                        "fontSize": "1rem",
                                        "padding": "6px 14px",
                                        "borderRadius": "8px"
                                    }
                                ),
                                html.Div(
                                    id="upload-error-message",
                                    style={"textAlign": "center", "marginTop": "15px", "color": "red", "fontWeight": "bold"}
                                ),
                            ],
                            style={"textAlign": "center", "marginTop": "40px"}
                        ),
                    ]),
                    className="mb-4 shadow-sm",
                    style={
                        "borderRadius": "12px",
                        "backgroundColor": "#f5f5f5",  
                        "border": "1px solid #e0e0e0"
                    }
                ),

                
                # Agrupa os gráficos em um container oculto inicialmente
                html.Div(
                    id="section-graficos",
                    style={"display": "none"},  # Inicialmente oculto
                    children=[
                        # SEÇÃO DO GRÁFICO COMPARATIVO
                        dbc.Card(
                            dbc.CardBody([
                                html.Div(
                                    dcc.Graph(
                                        id="analysis-chart",
                                        figure=go.Figure(),  # Figura vazia para ser atualizada pelo callback
                                        style={"width": "100%", "height": "700px"},  # Altura fixa de 700px
                                        config={
                                            "responsive": True,   # O gráfico se ajusta ao tamanho do container
                                            "displayModeBar": True,
                                            "modeBarButtonsToAdd": ["toImage"],
                                            "toImageButtonOptions": {
                                                "format": "png",
                                                "filename": "grafico_comparativo",
                                                "width": 1000,
                                                "height": 700,
                                                "scale": 2
                                            }
                                        }
                                    ),
                                    style={"width": "100%"}  # Garante que o div ocupe toda a largura disponível
                                ),
                                html.Br(),
                                html.Div(
                                    "Clique no ícone 📷 no canto superior direito do gráfico para fazer o download.",
                                    style={
                                        "textAlign": "center",
                                        "color": "#1D3B53",
                                        "fontWeight": "bold",
                                        "font-size": "14px"
                                    }
                                )
                            ]),
                            className="mb-4 shadow-sm",
                            style={
                                "border-radius": "12px",
                                "backgroundColor": "#DCE3EA",
                                "border": "1px solid #e0e0e0"
                            }
                        ),


                        # SEÇÃO DO GRÁFICO DE COMPARAÇÃO (SLOPE CHART)
                        dbc.Card(
                            dbc.CardBody([
                                html.Div(
                                    dcc.Graph(
                                        id="slope-chart",
                                        figure=go.Figure(),  # Seta figura vazia inicialmente
                                        config={
                                            "displayModeBar": True,
                                            "responsive": True
                                        },
                                        style={"width": "100%", "height": "700px"}  # Força o gráfico a ocupar 100% da largura e 700px de altura
                                    ),
                                    style={"width": "100%"}  # Remove overflow ou qualquer limitação horizontal
                                ),
                                html.Br(),
                                html.Div(
                                    "Clique no ícone 📷 no canto superior direito do gráfico para fazer o download.",
                                    style={
                                        "textAlign": "center",
                                        "color": "#1D3B53",
                                        "fontWeight": "bold",
                                        "font-size": "14px"
                                    }
                                )
                            ]),
                            className="mb-4 shadow-sm",
                            style={
                                "border-radius": "12px",
                                "backgroundColor": "#DCE3EA",
                                "border": "1px solid #e0e0e0"
                            }
                        ),


                        # SEÇÃO DO GRÁFICO RADAR
                        dbc.Card(
                            dbc.CardBody([
                                html.Div(
                                    dcc.Graph(
                                        id="radar-chart",
                                        config={
                                            "displayModeBar": True,
                                            "responsive": True
                                        },
                                        style={"width": "100%", "height": "auto"}
                                    ),
                                    style={"overflowX": "auto", "width": "100%"}
                                ),
                                html.Br(),
                                html.Div(
                                    "Clique no ícone 📷 no canto superior direito do gráfico para fazer o download.",
                                    style={"textAlign": "center", "color": "#1D3B53", "fontWeight": "bold", "font-size": "14px"}
                                )
                            ]),
                            className="mb-4 shadow-sm",
                            style={
                                "border-radius": "12px",
                                "backgroundColor": "#DCE3EA",     
                                "border": "1px solid #e0e0e0"
                            }
                        )
                    ]
                )

               
            ],
        ),
    ]
)
