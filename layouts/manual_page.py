from dash import html
import dash_bootstrap_components as dbc

# Layout da página Manual do Usuário
layout = html.Div(
    className="main-content",
    style={"font-family": "'Montserrat', sans-serif"},  # Aplicando Montserrat
    children=[
        # Espaçamento superior
        html.Div(style={"padding-top": "40px"}),

        # Título com a cor #345F6C
        html.H3(
            "Manual do Usuário",
            style={
                "margin-bottom": "30px",
                "font-size": "2.5rem",
                "text-align": "center",
                "font-weight": "bold",
                "color": "#345F6C",  # Cor do título ajustada conforme solicitado
                "font-family": "'Montserrat', sans-serif",  # Aplicando Montserrat
            }
        ),

        # Conteúdo estilizado
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                # Título da seção
                                html.H4(
                                    "Conteúdo do Manual",
                                    style={
                                        "font-size": "1.5rem",
                                        "margin-top": "20px",
                                        "margin-bottom": "15px",
                                        "font-weight": "bold",
                                        "color": "#345F6C",  # Mantendo a cor do título
                                        "text-align": "center",
                                        "font-family": "'Montserrat', sans-serif",  # Aplicando Montserrat
                                    }
                                ),

                                # Caixa de conteúdo aprimorada
                                html.Div(
                                    [
                                        html.Ul(
                                            [
                                                html.Li([
                                                    html.I(className="fas fa-book-open", style={"margin-right": "10px"}),
                                                    "Seção 1: Introdução"
                                                ], style={"margin-bottom": "10px"}),
                                                html.Li([
                                                    html.I(className="fas fa-cogs", style={"margin-right": "10px"}),
                                                    "Seção 2: Premissas do Orçamento Paramétrico Simplificado",
                                                    html.Ul([
                                                        html.Li("2.1: Terraplenagem"),
                                                        html.Li("2.2: Rede de Drenagem Pluvial"),
                                                        html.Li("2.3: Rede de Energia Elétrica, Rede de Água e Rede de Esgoto"),
                                                        html.Li("2.4: Pavimentação Asfáltica"),
                                                        html.Li("2.5: Áreas Comuns"),
                                                    ], style={"margin-left": "20px"})
                                                ], style={"margin-bottom": "10px"}),
                                                html.Li([
                                                    html.I(className="fas fa-calculator", style={"margin-right": "10px"}),
                                                    "Seção 3: Premissas do Orçamento Paramétrico Completo",
                                                    html.Ul([
                                                        html.Li("3.1: Rede de Drenagem Pluvial"),
                                                        html.Li("3.2: Pavimentação Asfáltica"),
                                                        html.Li("3.3: Terraplenagem"),
                                                    ], style={"margin-left": "20px"})
                                                ], style={"margin-bottom": "10px"}),
                                                html.Li([
                                                    html.I(className="fas fa-chart-line", style={"margin-right": "10px"}),
                                                    "Seção 4: Parâmetros e unidades de referência"
                                                ], style={"margin-bottom": "10px"}),
                                                html.Li([
                                                    html.I(className="fas fa-sitemap", style={"margin-right": "10px"}),
                                                    "Seção 5: Fluxograma para utilização da Plataforma"
                                                ], style={"margin-bottom": "10px"}),
                                            ],
                                            style={
                                                "font-size": "0.9rem",
                                                "line-height": "1.8",
                                                "color": "#555",
                                                "list-style-type": "none",
                                                "padding-left": "0",
                                                "font-family": "'Montserrat', sans-serif",  # Aplicando Montserrat
                                            }
                                        ),
                                    ],
                                    style={
                                        "background-color": "#f9f9f9",
                                        "padding": "30px",
                                        "border-radius": "8px",
                                        "border": "1px solid #ddd",
                                    }
                                ),

                                # Botão vermelho estilizado
                                html.Div(
                                    [
                                        html.A(
                                            "Abrir Manual em PDF",
                                            href="/assets/roteiro.pdf",
                                            target="_blank",
                                            style={
                                                "display": "inline-block",
                                                "font-size": "1.1rem",
                                                "font-weight": "bold",
                                                "padding": "12px 25px",
                                                "color": "#fff",
                                                "background-color": "#e74c3c",  # Vermelho para o botão
                                                "border-radius": "5px",
                                                "text-decoration": "none",
                                                "margin-top": "30px",
                                                "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                                                "font-family": "'Montserrat', sans-serif",  # Aplicando Montserrat
                                            },
                                            className="button-red",
                                        )
                                    ],
                                    style={"text-align": "center"}
                                )
                            ],
                            width=12
                        )
                    ]
                ),
            ],
            fluid=True,
            style={
                "padding": "20px 0px",
            }
        ),
    ]
)
