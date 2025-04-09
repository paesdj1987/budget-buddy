# Orcamento_simples_page.py

from dash import html, dcc
import dash_bootstrap_components as dbc

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
                html.Div(style={"padding-top": "40px"}),  # Espaçamento superior

                # TÍTULO PRINCIPAL
                html.H3(
                    "📋 Orçamento Simplificado",
                    style={
                        "margin-bottom": "40px",
                        "font-size": "2rem",
                        "text-align": "center",
                        "color": "#345F6C",
                        "font-weight": "bold",
                    }
                ),

                # SEÇÃO: PADRÕES DE EMPREENDIMENTO
                dbc.Card(
                    dbc.CardBody([
                        html.H4("🏗️ Padrões de Empreendimento", style={"color": "#345F6C"}),
                        html.P(
                            "Selecione um padrão para preencher automaticamente alguns custos.",
                            style={"color": "#666"}
                        ),
                        dbc.Row([
                            dbc.Col(
                                dcc.Dropdown(
                                    id="empreendimento-dropdown",
                                    options=[
                                        {"label": "Default", "value": "default"},
                                        {"label": "Padrão Econômico", "value": "economico"},
                                        {"label": "Padrão Médio/Alto", "value": "medio_alto"},
                                    ],
                                    value="default",
                                    clearable=False,
                                    style={"width": "100%"}
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                dbc.Button(
                                    "Aplicar",
                                    id="empreendimento-aplicar-button",
                                    color="primary",
                                    className="mt-1",
                                    style={
                                        "padding": "8px 16px",
                                        "font-size": "1rem",
                                        "height": "40px",
                                        "line-height": "40px",
                                        "width": "120%",
                                        "display": "flex",
                                        "align-items": "center",
                                        "justify-content": "center",
                                        "position": "relative",
                                        "top": "-6px"}
                                ),
                                width="auto",
                            ),
                        ]),
                    ]),
                    className="mb-4 shadow-sm border-0",
                    style={"border-radius": "12px", "backgroundColor": "#f5f5f5"},
                ),

                # =========================
                # 2) DADOS DO EMPREENDIMENTO
                # =========================
                dbc.Card(
                    dbc.CardBody([
                        html.H4("🏢 Dados do Empreendimento", style={"color": "#345F6C", "margin-bottom": "20px"}),

                        # Informações Gerais
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Informações Gerais"),
                                dbc.Textarea(
                                    id="info-geral",  
                                    placeholder="Insira aqui informações gerais do projeto...",
                                    style={
                                        "background-color": "#ffffff",
                                        "height": "120px",
                                    }
                                ),
                            ], width=6),
                        ], className="mb-3"),

                        # Linha de inputs (ID, Localização, Revisão, Valor venda)
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("ID Condomínios Horizontais"),
                                dbc.Input(
                                    id="id-loteamento",  
                                    type="text",
                                    placeholder="Inserir dado...",
                                    style={"background-color": "#fff3cd"}
                                ),
                            ], width=3),

                            dbc.Col([
                                dbc.Label([
                                    "Localização ",
                                    html.A(
                                        html.Img(
                                            src="/assets/googlemaps.png",
                                            style={"width": "25px", "height": "25px", "margin-left": "5px", "margin-top": "-3px"}
                                        ),
                                        id="maps-link",
                                        href="#",
                                        target="_blank"
                                    )
                                ], style={"display": "flex", "align-items": "center"}),

                                dbc.Input(
                                    id="localizacao",  
                                    type="text",
                                    placeholder="Inserir Texto...",
                                    style={"background-color": "#fff3cd"}
                                ),
                            ], width=3),

                            dbc.Col([
                                dbc.Label("Revisão"),
                                dbc.Input(
                                    id="revisao",  
                                    type="text",
                                    placeholder="Inserir texto",
                                    style={"background-color": "#fff3cd"}
                                ),
                            ], width=3),

                            dbc.Col([
                                dbc.Label("Valor da venda / m²"),
                                dbc.Input(
                                    id="vgv",  
                                    type="number",
                                    placeholder="Inserir Valor...",
                                    style={"background-color": "#d1ecf1"}
                                ),
                            ], width=3),
                        ], className="mb-3"),
                    ]),
                    className="mb-4 shadow-sm border-0",
                    style={"border-radius": "12px", "backgroundColor": "#f5f5f5"},
                ),

                # =========================
                # 2) DADOS URBANÍSTICOS
                # =========================
                dbc.Card(
                    dbc.CardBody([
                        html.H4("🏙️ Dados Urbanísticos", style={"color": "#345F6C"}),

                        # Linha 1
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Área Total do Terreno (m²)"),
                                dbc.Input(
                                    id="area-total",  
                                    type="number",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#f8d7da"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Perímetro do Terreno (m)"),
                                dbc.Input(
                                    id="perimetro",  
                                    type="number",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#f8d7da"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Área do Lote (m²)"),
                                dbc.Input(
                                    id="area-lotes",  
                                    type="number",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#f8d7da"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Área do Viário (m²)"),
                                dbc.Input(
                                    id="area-viario",  
                                    type="number",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#f8d7da"}
                                ),
                            ], width=3),
                        ], className="mb-3"),

                        # Linha 2
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Comprimento do Viário (m)"),
                                dbc.Input(
                                    id="comprimento-viario",  
                                    type="number",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#f8d7da"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Área Construída (m²)"),
                                dbc.Input(
                                    id="area-construida",  
                                    type="number",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#f8d7da"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Área da Quadra (m²)"),
                                dbc.Input(
                                    id="area-quadra",  
                                    type="number",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#f8d7da"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Quantidade de Lotes"),
                                dbc.Input(
                                    id="qtd-lotes",  
                                    type="number",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#f8d7da"}
                                ),
                            ], width=3),
                        ], className="mb-3"),

                        # Linha 3 (INCC)
                        dbc.Row([
                            dbc.Col([
                                dbc.Label([
                                    "Dados INCC Antigo ",
                                    html.A(
                                        html.Img(
                                            src="/assets/html.png",
                                            style={"width": "30px", "height": "30px", "margin-left": "5px"}
                                        ),
                                        href="https://indiceseconomicos.secovi.com.br/indicadormensal.php?idindicador=59",
                                        target="_blank"
                                    )
                                ]),
                                dbc.Input(
                                    id="dados-incc-antigo",  
                                    type="text",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#f8d7da"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label([
                                    "Dados INCC Atual ",
                                    html.A(
                                        html.Img(
                                            src="/assets/html.png",
                                            style={"width": "30px", "height": "30px", "margin-left": "5px"}
                                        ),
                                        href="https://indiceseconomicos.secovi.com.br/indicadormensal.php?idindicador=59",
                                        target="_blank"
                                    )
                                ]),
                                dbc.Input(
                                    id="dados-incc-atual",  
                                    type="number",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#f8d7da"}
                                ),
                            ], width=3),
                        ]),
                    ]),
                    className="mb-4 shadow-sm border-0",
                    style={"border-radius": "12px", "backgroundColor": "#f5f5f5"},
                ),

                # =========================
                # 3) TERRAPLENAGEM
                # =========================
                dbc.Card(
                    dbc.CardBody([
                        html.H4("🚜 Terraplenagem", style={"color": "#345F6C"}),

                        # Linha de Inputs
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Volume de Corte (m³)"),
                                dbc.Input(
                                    id="volume-corte",
                                    type="number",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#d4edda"}
                                ),
                            ], width=3),

                            dbc.Col([
                                dbc.Label("Volume de Aterro (m³)"),
                                dbc.Input(
                                    id="volume-aterro",
                                    type="number",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#d4edda"}
                                ),
                            ], width=3),

                            dbc.Col([
                                dbc.Label("Volume de Transporte Interno (m³)"),
                                dbc.Input(
                                    id="volume-transporte",
                                    type="number",
                                    placeholder="Inserir Dado...",
                                    style={"background-color": "#d4edda"}
                                ),
                            ], width=3),
                        ], className="mb-3"),
                    ]),
                    className="mb-4 shadow-sm border-0",
                    style={"border-radius": "12px", "backgroundColor": "#f5f5f5"},
                ),

                # =========================
                # 4) CUSTOS UNITÁRIOS
                # =========================
                dbc.Card(
                    dbc.CardBody([
                        html.H4("💲 Custos Unitários", style={"margin-bottom": "20px","color": "#345F6C"}),

                        # Linha 1
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Fechamento Perimetral (cc/m)"),
                                dbc.Input(
                                    id="fechamento-perimetral",  
                                    type="number",
                                    placeholder="Inserir Custo...",
                                    style={"background-color": "#d1ecf1"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Meio Fio (cc/m)"),
                                dbc.Input(
                                    id="meio-fio",  
                                    type="number",
                                    placeholder="Inserir Custo...",
                                    style={"background-color": "#d1ecf1"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Rede Distribuição Elétrica (cc/m)"),
                                dbc.Input(
                                    id="rede-eletrica",  
                                    type="number",
                                    placeholder="Inserir custo...",
                                    style={"background-color": "#d1ecf1"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Rede Abastecimento de Água (cc/m)"),
                                dbc.Input(
                                    id="rede-agua",  
                                    type="number",
                                    placeholder="Inserir Custo...",
                                    style={"background-color": "#d1ecf1"}
                                ),
                            ], width=3),
                        ], className="mb-3"),

                        # Linha 2
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Rede de Drenagem (cc/m)"),
                                dbc.Input(
                                    id="rede-drenagem",  
                                    type="number",
                                    placeholder="Inserir Custo...",
                                    style={"background-color": "#d1ecf1"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Rede Coleta de Esgoto (cc/m)"),
                                dbc.Input(
                                    id="rede-esgoto",  
                                    type="number",
                                    placeholder="Inserir Custo...",
                                    style={"background-color": "#d1ecf1"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Pavimentação (cc/m²)"),
                                dbc.Input(
                                    id="pavimentacao",  
                                    type="number",
                                    placeholder="Inserir Custo...",
                                    style={"background-color": "#d1ecf1"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Supressão de Vegetação (cc/m²)"),
                                dbc.Input(
                                    id="supressao-vegetacao",  
                                    type="number",
                                    placeholder="Inserir Custo...",
                                    style={"background-color": "#d1ecf1"}
                                ),
                            ], width=3),
                        ], className="mb-3"),

                        # Linha 3
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Terraplenagem (cc/m²)"),
                                dbc.Input(
                                    id="custo-terraplanagem",  
                                    type="number",
                                    placeholder="Inserir Custo...",
                                    style={"background-color": "#d1ecf1"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Edificações (cc/m²)"),
                                dbc.Input(
                                    id="edificacoes",  
                                    type="number",
                                    placeholder="Inserir Custo...",
                                    style={"background-color": "#d1ecf1"}
                                ),
                            ], width=3),
                            dbc.Col([
                                dbc.Label("Quadra Society (cc/m²)"),
                                dbc.Input(
                                    id="quadra-society",  
                                    type="number",
                                    placeholder="Inserir Custo...",
                                    style={"background-color": "#d1ecf1"}
                                ),
                            ], width=3),
                        ]),
                    ]),
                    className="mb-4 shadow-sm border-0",
                    style={"border-radius": "12px", "backgroundColor": "#f5f5f5"},
                ),

                # ===============================
                # 5) RESPONSÁVEL PELO RETLATÓRIO
                # ===============================
                dbc.Card(
                    dbc.CardBody([
                        html.H4("👤 Responsável pelo Relatório Simplificado", style={"color": "#345F6C"}),

                        dbc.Row([
                            dbc.Col([
                                dbc.Input(
                                    id="responsavel-relatorio-simples",  
                                    type="text",
                                    placeholder="Digite o nome completo",
                                    style={"background-color": "#ffffff"}
                                ),
                            ], width=6),
                        ], className="mb-3"),
                    ]),
                    className="mb-4 shadow-sm border-0",
                    style={"border-radius": "12px", "backgroundColor": "#f5f5f5"},
                ),


                # BOTÕES (Gerar / Limpar)
                html.Div(
                    [
                        dbc.Button(
                            "📄 Gerar Relatório Simplificado",
                            id="generate-report-button",  
                            color="success",
                            n_clicks=0,
                            className="me-2",
                            style={"padding": "6px 14px", "font-size": "1rem", "border-radius": "8px","margin-top": "60px",}
                        ),
                        dbc.Button(
                            "🧹 Limpar Dados",
                            id="clear-button",  
                            color="secondary",
                            n_clicks=0,
                            style={"padding": "6px 14px", "font-size": "1rem", "border-radius": "8px","margin-top": "60px",}
                        ),
                    ],
                    style={"text-align": "center", "margin-bottom": "40px"}
                ),
            ],
        ),
    ]
)
