# Orcamento_completo_page.py


from dash import html
import dash_bootstrap_components as dbc

# Layout da página Orçamento Completo
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

        # Espaçamento superior geral da página
        html.Div(style={"padding-top": "40px"}),

        html.H3(
            "📑 Orçamento Completo",
            style={
                "margin-bottom": "40px",
                "font-size": "2rem",
                "text-align": "center",
                "color": "#345F6C",
                "font-weight": "bold"
            }
        ),

        # =========================
        # 1) DADOS DO EMPREENDIMENTO
        # =========================
        dbc.Card(
            dbc.CardBody([
                html.H4("🏢 Dados do Empreendimento", style={"color": "#345F6C"}),

                # Informações Gerais
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Informações Gerais"),
                        dbc.Textarea(
                            id="info-geral-completo",
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
                            id="id-loteamento-completo",
                            type="text",
                            placeholder="Inserir Dado...",
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
                                id="maps-link-completo",
                                href="#",
                                target="_blank"
                            )
                        ], style={"display": "flex", "align-items": "center"}),

                        dbc.Input(
                            id="localizacao-completo",
                            type="text",
                            placeholder="Inserir Texto...",
                            style={"background-color": "#fff3cd"}
                        ),
                    ], width=3),

                    dbc.Col([
                        dbc.Label("Revisão"),
                        dbc.Input(
                            id="revisao-completo",
                            type="text",
                            placeholder="Inserir Texto...",
                            style={"background-color": "#fff3cd"}
                        ),
                    ], width=3),

                    dbc.Col([
                        dbc.Label("Valor de Venda (R$/m²)"),
                        dbc.Input(
                            id="vgv-completo",
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

                # Primeira Linha de Inputs
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Área Total do Terreno (m²)"),
                        dbc.Input(
                            id="area-total-completo",
                            type="number",
                            placeholder="Inserir Dado...",
                            style={"background-color": "#f8d7da"}
                        ),
                    ], width=3),

                    dbc.Col([
                        dbc.Label("Perímetro do Terreno (m)"),
                        dbc.Input(
                            id="perimetro-completo",
                            type="number",
                            placeholder="Inserir Dado...",
                            style={"background-color": "#f8d7da"}
                        ),
                    ], width=3),

                    dbc.Col([
                        dbc.Label("Área dos Lotes (m²)"),
                        dbc.Input(
                            id="area-lotes-completo",
                            type="number",
                            placeholder="Inserir Dado...",
                            style={"background-color": "#f8d7da"}
                        ),
                    ], width=3),

                    dbc.Col([
                        dbc.Label("Área do Viário (m²)"),
                        dbc.Input(
                            id="area-viario-completo",
                            type="number",
                            placeholder="Inserir Dado...",
                            style={"background-color": "#f8d7da"}
                        ),
                    ], width=3),
                ], className="mb-3"),

                # Segunda Linha de Inputs
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Comprimento do Viário (m)"),
                        dbc.Input(
                            id="comprimento-viario-completo",
                            type="number",
                            placeholder="Inserir Dado...",
                            style={"background-color": "#f8d7da"}
                        ),
                    ], width=3),

                    dbc.Col([
                        dbc.Label("Área Construída (m²)"),
                        dbc.Input(
                            id="area-construida-completo",
                            type="number",
                            placeholder="Inserir Dado...",
                            style={"background-color": "#f8d7da"}
                        ),
                    ], width=3),

                    dbc.Col([
                        dbc.Label("Área da Quadra (m²)"),
                        dbc.Input(
                            id="area-quadra-completo",
                            type="number",
                            placeholder="Inserir Dado...",
                            style={"background-color": "#f8d7da"}
                        ),
                    ], width=3),

                    dbc.Col([
                        dbc.Label("Quantidade de Lotes"),
                        dbc.Input(
                            id="qtd-lotes-completo",
                            type="number",
                            placeholder="Inserir Dado...",
                            style={"background-color": "#f8d7da"}
                        ),
                    ], width=3),
                ], className="mb-3"),

                # Terceira Linha de Inputs (INCC)
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
                            id="dados-incc-antigo-completo",
                            type="number",
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
                            id="dados-incc-atual-completo",
                            type="number",
                            placeholder="Inserir Dado...",
                            style={"background-color": "#f8d7da"}
                        ),
                    ], width=3),
                ], className="mb-3"),
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
                            id="volume-corte-completo",
                            type="number",
                            placeholder="Inserir Dado...",
                            style={"background-color": "#d4edda"}
                        ),
                    ], width=3),

                    dbc.Col([
                        dbc.Label("Volume de Aterro (m³)"),
                        dbc.Input(
                            id="volume-aterro-completo",
                            type="number",
                            placeholder="Inserir Dado...",
                            style={"background-color": "#d4edda"}
                        ),
                    ], width=3),

                    dbc.Col([
                        dbc.Label("Volume de Transporte Interno (m³)"),
                        dbc.Input(
                            id="volume-transporte-completo",
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
        # 4) DRENAGEM
        # =========================
        dbc.Card(
            dbc.CardBody([
                html.H4("🌧 Drenagem", style={
                    "margin-bottom": "20px",
                    "color": "#345F6C"
                }),

            # Primeira Linha de Inputs
            dbc.Row([
                dbc.Col([
                    dbc.Label("Diâmetro 300 mm (m)"),
                    dbc.Input(
                        id="diametro-300-completo",
                        type="number",
                        placeholder="Inserir Dado...",
                        style={"background-color": "#fff3cd"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Diâmetro 375 mm (m)"),
                    dbc.Input(
                        id="diametro-375-completo",
                        type="number",
                        placeholder="Inserir Dado...",
                        style={"background-color": "#fff3cd"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Diâmetro 450 mm (m)"),
                    dbc.Input(
                        id="diametro-450-completo",
                        type="number",
                        placeholder="Inserir Dado...",
                        style={"background-color": "#fff3cd"}
                    ),
                ], width=3),
            ], className="mb-3"),

            # Segunda Linha de Inputs
            dbc.Row([
                dbc.Col([
                    dbc.Label("Diâmetro 500 mm (m)"),
                    dbc.Input(
                        id="diametro-500-completo",
                        type="number",
                        placeholder="Inserir Dado...",
                        style={"background-color": "#fff3cd"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Diâmetro 600 mm (m)"),
                    dbc.Input(
                        id="diametro-600-completo",
                        type="number",
                        placeholder="Inserir Dado...",
                        style={"background-color": "#fff3cd"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Diâmetro 800 mm (m)"),
                    dbc.Input(
                        id="diametro-800-completo",
                        type="number",
                        placeholder="Inserir Dado...",
                        style={"background-color": "#fff3cd"}
                    ),
                ], width=3),
            ], className="mb-3"),

            # Terceira Linha de Inputs
            dbc.Row([
                dbc.Col([
                    dbc.Label("Diâmetro 1000 mm (m)"),
                    dbc.Input(
                        id="diametro-1000-completo",
                        type="number",
                        placeholder="Inserir Dado...",
                        style={"background-color": "#fff3cd"}
                    ),
                ], width=3),
            ], className="mb-3"),

        ]),
        className="mb-4 shadow-sm border-0",
        style={"border-radius": "12px", "backgroundColor": "#f5f5f5"},
    ),


        # =========================
        # 5) CUSTOS UNITÁRIOS
        # =========================
        dbc.Card(
            dbc.CardBody([
                html.H4("💲 Custos Unitários", style={
                    "margin-bottom": "20px",
                    "color": "#345F6C"
                }),

            # Primeira Linha de Inputs
            dbc.Row([
                dbc.Col([
                    dbc.Label("Fechamento Perimetral (cc/m)"),
                    dbc.Input(
                        id="fechamento-perimetral-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Meio-fio (cc/m)"),
                    dbc.Input(
                        id="meio-fio-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Rede Dist. Elétrica (cc/m)"),
                    dbc.Input(
                        id="rede-eletrica-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Rede Abastecimento de Água (cc/m)"),
                    dbc.Input(
                        id="rede-agua-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),
            ], className="mb-3"),

            # Segunda Linha de Inputs
            dbc.Row([
                dbc.Col([
                    dbc.Label("Rede Coleta de Esgoto (cc/m)"),
                    dbc.Input(
                        id="rede-esgoto-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Supressão de Vegetação (cc/m²)"),
                    dbc.Input(
                        id="supressao-vegetacao-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Edificações (cc/m²)"),
                    dbc.Input(
                        id="edificacoes-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Quadra Society (cc/m²)"),
                    dbc.Input(
                        id="quadra-society-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),
            ], className="mb-3"),

            # Terceira Linha de Inputs
            dbc.Row([
                dbc.Col([
                    dbc.Label("Base em BGS (cc/m³)"),
                    dbc.Input(
                        id="base-bgs-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Imprimação (cc/m²)"),
                    dbc.Input(
                        id="imprimacao-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Pintura (cc/m²)"),
                    dbc.Input(
                        id="pintura-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("CBUQ (cc/t)"),
                    dbc.Input(
                        id="cbuq-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),
            ], className="mb-3"),

            # Quarta Linha de Inputs
            dbc.Row([
                dbc.Col([
                    dbc.Label("Limpeza Camada Vegetal (cc/m²)"),
                    dbc.Input(
                        id="limpeza-camada-vegetal-completo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Volume de Corte (cc/m³)"),
                    dbc.Input(
                        id="volume-corte-completo-custo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Volume de Aterro (cc/m³)"),
                    dbc.Input(
                        id="volume-aterro-completo-custo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Volume de Transp. Interno (cc/m³)"),
                    dbc.Input(
                        id="volume-transporte-completo-custo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),
            ], className="mb-3"),

            # Quinta Linha de Inputs (Drenagem)
            dbc.Row([
                dbc.Col([
                    dbc.Label("Diâm. 300 mm (cc/m)"),
                    dbc.Input(
                        id="diametro-300-completo-custo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Diâm. 375 mm (cc/m)"),
                    dbc.Input(
                        id="diametro-375-completo-custo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Diâm. 450 mm (cc/m)"),
                    dbc.Input(
                        id="diametro-450-completo-custo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Diâm. 500 mm (cc/m)"),
                    dbc.Input(
                        id="diametro-500-completo-custo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),
            ], className="mb-3"),

            # Sexta Linha de Inputs (Drenagem - Continuação)
            dbc.Row([
                dbc.Col([
                    dbc.Label("Diâm. 600 mm (cc/m)"),
                    dbc.Input(
                        id="diametro-600-completo-custo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Diâm. 800 mm (cc/m)"),
                    dbc.Input(
                        id="diametro-800-completo-custo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),

                dbc.Col([
                    dbc.Label("Diâm. 1000 mm (cc/m)"),
                    dbc.Input(
                        id="diametro-1000-completo-custo",
                        type="number",
                        placeholder="Inserir Custo...",
                        style={"background-color": "#d1ecf1"}
                    ),
                ], width=3),
            ], className="mb-3"),
        ]),
        className="mb-4 shadow-sm border-0",
        style={"border-radius": "12px", "backgroundColor": "#f5f5f5"},
    ),

        # =========================
        # 6) RESPONSÁVEL
        # =========================
                dbc.Card(
                    dbc.CardBody([
                        html.H4("👤 Responsável pelo Relatório Simplificado", style={"margin-bottom": "12px","color": "#345F6C"}),

                        dbc.Row([
                            dbc.Col([
                                dbc.Input(
                                    id="responsavel-relatorio-completo", 
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


        
        # =========================
        # BOTÕES FINAIS
        # =========================
                html.Div(
                    [
                        dbc.Button(
                            "📄 Gerar Relatório Simplificado",
                            id="generate-report-button-completo",  
                            color="success",
                            n_clicks=0,
                            className="me-2",
                            style={"padding": "6px 14px", "font-size": "1rem", "border-radius": "8px","margin-top": "60px",}
                        ),
                        dbc.Button(
                            "🧹 Limpar Dados",
                            id="clear-data-button-completo",  
                            color="secondary",
                            n_clicks=0,
                            style={"padding": "6px 14px", "font-size": "1rem", "border-radius": "8px","margin-top": "60px",}
                        ),
                    ],
                    style={"text-align": "center", "margin-bottom": "40px"}
                ),
    ]
)
