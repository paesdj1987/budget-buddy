# Orcamento_simples_page.py

from dash import html, dcc
import dash_bootstrap_components as dbc

# Layout da página Orçamento Simples
layout = html.Div(
    className="main-content",  # Classe para aplicar estilos específicos
    children=[

        # Espaçamento superior geral da página
        html.Div(style={"padding-top": "40px"}),

        # Título da página
        html.H3(
            "Orçamento Simplificado",
            style={
                "margin-bottom": "40px",
                "font-size": "2.5rem",
                "text-align": "center",
                "color": "#345F6C",
                "font-weight": "bold"
            }
        ),
        
        # Seção de seleção de empreendimento
        html.H4("Padrões de Empreendimento", style={"margin-bottom": "20px", "color": "#345F6C","margin-top": "50px"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Selecione"),
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
                    ],
                    width=3,
                ),
                dbc.Col(
                    dbc.Button(
                        "Aplicar",
                        id="empreendimento-aplicar-button",
                        color="primary",
                        style={
                                "font-size": "1.0rem",
                                "padding": "8px 16px",
                                "margin-top": "27px",
                                'background-color': '#007bff',  # Cor azul
                                'color': 'white',  # Texto branco
                                "border-color": "#007bff"    
                            }
                    ),
                    width="auto"
                ),
            ],
            style={"margin-bottom": "20px"}
        ),


        # Seção "Dados do Empreendimento" com caixas verdes claras
        html.H4("Dados do Empreendimento", style={"margin-bottom": "20px", "color": "#345F6C","margin-top": "50px"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Informações Gerais"),
                        dbc.Textarea(
                            id="info-geral",
                            placeholder="Inserir texto",
                            style={"background-color": "#ffffff",
                                   "width": "282%",
                                   "height": "120px"}
                        ),
                    ],
                    width=3,
                ),
            ],
            style={"margin-bottom": "20px"}
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("ID Condomínios Horizontais", style={"margin-right": "0px"}),
                        dbc.Input(
                            id="id-loteamento",
                            type="text",
                            placeholder="Inserir dado",
                            style={"background-color": "#fff3cd",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Localização", style={"margin-right": "0px"}),
                        dbc.Input(
                            id="localizacao",
                            type="text",
                            placeholder="Inserir texto",
                            style={"background-color": "#fff3cd",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Revisão", style={"margin-right": "0px"}),
                        dbc.Input(
                            id="revisao",
                            type="text",
                            placeholder="Inserir texto",
                            style={"background-color": "#fff3cd",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Valor da venda / m²", style={"margin-right": "0px"}),
                        dbc.Input(
                            id="vgv",
                            type="number",
                            placeholder="Inserir dado",
                            style={"background-color": "#d1ecf1",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
            ],
            style={"margin-bottom": "30px"}
        ),

        # Seção "Dados Urbanísticos" com caixas vermelhas claras
        html.H4("Dados Urbanísticos", style={"margin-bottom": "12px", "color": "#345F6C"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Área Total do Terreno - m²"),
                        dbc.Input(
                            id="area-total",
                            type="number",
                            placeholder="Inserir dado",
                            style={"background-color": "#f8d7da",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Perímetro do Terreno - m"),
                        dbc.Input(
                            id="perimetro",
                            type="number",
                            placeholder="Inserir dado",
                            style={"background-color": "#f8d7da",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Área do Lote - m²"),
                        dbc.Input(
                            id="area-lotes",
                            type="number",
                            placeholder="Inserir dado",
                            style={"background-color": "#f8d7da",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Área do Viário - m²"),
                        dbc.Input(
                            id="area-viario",
                            type="number",
                            placeholder="Inserir dado",
                            style={"background-color": "#f8d7da",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
            ],
            style={"margin-bottom": "20px"}
        ),
        dbc.Row(
            [                
                dbc.Col(
                    [
                        dbc.Label("Comprimento do Viário - m"),
                        dbc.Input(
                            id="comprimento-viario",
                            type="number",
                            placeholder="Inserir dado",
                            style={"background-color": "#f8d7da",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Área Construída - m²"),
                        dbc.Input(
                            id="area-construida",
                            type="number",
                            placeholder="Inserir dado",
                            style={"background-color": "#f8d7da",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Área da Quadra - m²"),
                        dbc.Input(
                            id="area-quadra",
                            type="number",
                            placeholder="Inserir dado",
                            style={"background-color": "#f8d7da",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Quantidade de Lotes"),
                        dbc.Input(
                            id="qtd-lotes",
                            type="number",
                            placeholder="Inserir dado",
                            style={"background-color": "#f8d7da",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
            ],
            style={"margin-bottom": "20px"}
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
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
                            placeholder="Inserir dado",
                            style={"background-color": "#f8d7da",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        # Adicionando o botão ao lado do label "Dados INCC Atual"
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
                            placeholder="Inserir dado",
                            style={"background-color": "#f8d7da",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
            ],
            style={"margin-bottom": "30px"}
        ),

        # Seção "Terraplanagem" com caixas verdes claras
        html.H4("Terraplenagem", style={"margin-bottom": "15px", "color": "#345F6C"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Volume de Corte - m³"),
                        dbc.Input(
                            id="volume-corte",
                            type="number",
                            placeholder="Inserir dado",
                            style={"background-color": "#d4edda",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Volume de Aterro - m³"),
                        dbc.Input(
                            id="volume-aterro",
                            type="number",
                            placeholder="Inserir dado",
                            style={"background-color": "#d4edda",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Volume de Transporte Interno - m³"),
                        dbc.Input(
                            id="volume-transporte",
                            type="number",
                            placeholder="Inserir dado",
                            style={"background-color": "#d4edda",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
            ],
            style={"margin-bottom": "30px"}
        ),

        # Seção "Custos Unitários" com caixas azuis claras
        html.H4("Custos Unitários", style={"margin-bottom": "15px", "color": "#345F6C"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Fechamento Perimetral - cc/m"),
                        dbc.Input(
                            id="fechamento-perimetral",
                            type="number",
                            placeholder="Inserir custo",
                            style={"background-color": "#d1ecf1",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Meio Fio - cc/m"),
                        dbc.Input(
                            id="meio-fio",
                            type="number",
                            placeholder="Inserir custo",
                            style={"background-color": "#d1ecf1",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Rede Distribuição Elétrica - cc/m"),
                        dbc.Input(
                            id="rede-eletrica",
                            type="number",
                            placeholder="Inserir custo",
                            style={"background-color": "#d1ecf1",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Rede Abastecimento de Água - cc/m"),
                        dbc.Input(
                            id="rede-agua",
                            type="number",
                            placeholder="Inserir custo",
                            style={"background-color": "#d1ecf1",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
            ],
            style={"margin-bottom": "20px"}
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Rede de Drenagem - cc/m"),
                        dbc.Input(
                            id="rede-drenagem",
                            type="number",
                            placeholder="Inserir custo",
                            style={"background-color": "#d1ecf1",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Rede Coleta de Esgoto - cc/m"),
                        dbc.Input(
                            id="rede-esgoto",
                            type="number",
                            placeholder="Inserir custo",
                            style={"background-color": "#d1ecf1",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Pavimentação - cc/m²"),
                        dbc.Input(
                            id="pavimentacao",
                            type="number",
                            placeholder="Inserir custo",
                            style={"background-color": "#d1ecf1",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Supressão de Vegetação - cc/m²"),
                        dbc.Input(
                            id="supressao-vegetacao",
                            type="number",
                            placeholder="Inserir custo",
                            style={"background-color": "#d1ecf1",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
            ],
            style={"margin-bottom": "20px"}
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Terraplenagem - cc/m²"),
                        dbc.Input(
                            id="custo-terraplanagem",
                            type="number",
                            placeholder="Inserir custo",
                            style={"background-color": "#d1ecf1",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Edificações - cc/m²"),
                        dbc.Input(
                            id="edificacoes",
                            type="number",
                            placeholder="Inserir custo",
                            style={"background-color": "#d1ecf1",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Quadra Society - cc/m²"),
                        dbc.Input(
                            id="quadra-society",
                            type="number",
                            placeholder="Inserir custo",
                            style={"background-color": "#d1ecf1",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
            ],
            style={"margin-bottom": "30px"}
        ),
        
        # Campo para inserir o nome do responsável pelo relatório
        html.H4("Nome do Responsável pelo Relatório Simplificado", style={"margin-bottom": "12px", "color": "#345F6C"}),
        html.Div(
            [
                dbc.Input(
                    id="responsavel-relatorio-simples",
                    type="text",
                    placeholder="Digite o nome completo",
                    style={
                        "width": "30%",  # Definir largura de 30% da tela
                        "margin-bottom": "20px",
                        "padding": "8px",
                        "font-size": "1rem",
                        "border": "1px solid #ced4da",
                        "border-radius": "5px"
                    }
                ),
            ],
            style={"margin-bottom": "20px"}
        ),

        # Botão "Gerar Relatório Simples" e "Limpar Dados" abaixo das seções
        html.Div(
            [
            dbc.Button(
                "Gerar Relatório Simples",
                id="generate-report-button",
                color="primary",
                n_clicks=0,
                style={
                    "font-size": "1.0rem",
                    "padding": "8px 16px",
                    "margin-top": "60px",
                    'background-color': '#007bff',  # Cor azul
                    'color': 'white',  # Texto branco
                    "border-color": "#007bff"
                }
            ),
            dbc.Button(
                    "Limpar Dados",
                    id="clear-button",
                    color="secondary",
                    n_clicks=0,
                    style={
                        "font-size": "1.0rem",
                        "padding": "8px 16px",
                        "margin-top": "60px",
                        "margin-left": "20px",  
                        "background-color": "#6c757d",
                        "border-color": "#6c757d",
                    }
                ),
            ],
            style={"text-align": "center"}
        )
    ]
)