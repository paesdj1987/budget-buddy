# Orcamento_completo_page.py

from dash import html
import dash_bootstrap_components as dbc

# Layout da página Orçamento Completo
layout = html.Div(
    className="main-content",  # Classe para aplicar estilos específicos
    children=[
        # Espaçamento superior geral da página
        html.Div(style={"padding-top": "40px"}),

        # Título da página
        html.H3(
            "Orçamento Completo",
            style={
                "margin-bottom": "40px",
                "font-size": "2.5rem",
                "text-align": "center",
                "color": "#345F6C",
                "font-weight": "bold"
            }
        ),
        
         # Seção "Dados do Empreendimento" com caixas verdes claras
        html.H4("Dados do Empreendimento", style={"margin-bottom": "20px", "color": "#345F6C","margin-top": "50px"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Informações Gerais"),
                        dbc.Textarea(
                            id="info-geral-completo",
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
                        dbc.Label("ID Condomínios Horizontais", ),
                        dbc.Input(
                            id="id-loteamento-completo",
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
                            id="localizacao-completo",
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
                            id="revisao-completo",
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
                            id="vgv-completo",
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
                            id="area-total-completo",
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
                            id="perimetro-completo",
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
                            id="area-lotes-completo",
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
                            id="area-viario-completo",
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
                            id="comprimento-viario-completo",
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
                            id="area-construida-completo",
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
                            id="area-quadra-completo",
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
                            id="qtd-lotes-completo",
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
                            id="dados-incc-antigo-completo",
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
        
        # Seção "Terraplenagem" com caixas amarelas claras
        html.H4("Terraplenagem", style={"margin-bottom": "15px", "color": "#345F6C"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Volume de Corte - m³"),
                        dbc.Input(
                            id="volume-corte-completo",
                            type="number",
                            placeholder="Inserir comprimento",
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
                            id="volume-aterro-completo",
                            type="number",
                            placeholder="Inserir comprimento",
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
                            id="volume-transporte-completo",
                            type="number",
                            placeholder="Inserir comprimento",
                            style={"background-color": "#d4edda",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
            ],
            style={"margin-bottom": "20px"}
        ),



        # Seção "Drenagem" com caixas amarelas claras
        html.H4("Drenagem", style={"margin-bottom": "15px", "color": "#345F6C"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Diâmetro 300 mm"),
                        dbc.Input(
                            id="diametro-300-completo",
                            type="number",
                            placeholder="Inserir comprimento",
                            style={"background-color": "#fff3cd",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Diâmetro 375 mm"),
                        dbc.Input(
                            id="diametro-375-completo",
                            type="number",
                            placeholder="Inserir comprimento",
                            style={"background-color": "#fff3cd",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Diâmetro 450 mm"),
                        dbc.Input(
                            id="diametro-450-completo",
                            type="number",
                            placeholder="Inserir comprimento",
                            style={"background-color": "#fff3cd",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Diâmetro 500 mm"),
                        dbc.Input(
                            id="diametro-500-completo",
                            type="number",
                            placeholder="Inserir comprimento",
                            style={"background-color": "#fff3cd",
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
                        dbc.Label("Diâmetro 600 mm"),
                        dbc.Input(
                            id="diametro-600-completo",
                            type="number",
                            placeholder="Inserir comprimento",
                            style={"background-color": "#fff3cd",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Diâmetro 800 mm"),
                        dbc.Input(
                            id="diametro-800-completo",
                            type="number",
                            placeholder="Inserir comprimento",
                            style={"background-color": "#fff3cd",
                                   "width": "70%"}
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Label("Diâmetro 1000 mm"),
                        dbc.Input(
                            id="diametro-1000-completo",
                            type="number",
                            placeholder="Inserir comprimento",
                            style={"background-color": "#fff3cd",
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
                            id="fechamento-perimetral-completo",
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
                        dbc.Label("Meio fio - cc/m"),
                        dbc.Input(
                            id="meio-fio-completo",
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
                            id="rede-eletrica-completo",
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
                            id="rede-agua-completo",
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
                        dbc.Label("Rede Coleta de Esgoto - cc/m"),
                        dbc.Input(
                            id="rede-esgoto-completo",
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
                            id="supressao-vegetacao-completo",
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
                            id="edificacoes-completo",
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
                            id="quadra-society-completo",
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
                        dbc.Label("Base em BGS - cc/m³"),
                        dbc.Input(
                            id="base-bgs-completo",
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
                        dbc.Label("Imprimação - cc/m²"),
                        dbc.Input(
                            id="imprimacao-completo",
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
                        dbc.Label("Pintura - cc/m²"),
                        dbc.Input(
                            id="pintura-completo",
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
                        dbc.Label("CBUQ - cc/t"),
                        dbc.Input(
                            id="cbuq-completo",
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
                        dbc.Label("Limpeza da Camada Vegetal - cc/m²"),
                        dbc.Input(
                            id="limpeza-camada-vegetal-completo",
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
                        dbc.Label("Volume de Corte - cc/m³"),
                        dbc.Input(
                            id="volume-corte-completo-custo",
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
                        dbc.Label("Volume de Aterro - cc/m³"),
                        dbc.Input(
                            id="volume-aterro-completo-custo",
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
                        dbc.Label("Volume de Transporte Interno - cc/m³"),
                        dbc.Input(
                            id="volume-transporte-completo-custo",
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
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Diâmetro 300 mm - cc/m"),
                        dbc.Input(
                            id="diametro-300-completo-custo",
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
                        dbc.Label("Diâmetro 375 mm - cc/m"),
                        dbc.Input(
                            id="diametro-375-completo-custo",
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
                        dbc.Label("Diâmetro 450 mm - cc/m"),
                        dbc.Input(
                            id="diametro-450-completo-custo",
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
                        dbc.Label("Diâmetro 500 mm - cc/m"),
                        dbc.Input(
                            id="diametro-500-completo-custo",
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
                        dbc.Label("Diâmetro 600 mm - cc/m"),
                        dbc.Input(
                            id="diametro-600-completo-custo",
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
                        dbc.Label("Diâmetro 800 mm - cc/m"),
                        dbc.Input(
                            id="diametro-800-completo-custo",
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
                        dbc.Label("Diâmetro 1000 mm - cc/m"),
                        dbc.Input(
                            id="diametro-1000-completo-custo",
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
        
        # Campo para inserir o nome do responsável pelo relatório completo
        html.H4("Nome do Responsável pelo Relatório Completo", style={"margin-bottom": "12px", "color": "#345F6C"}),
        html.Div(
            [
                dbc.Input(
                    id="responsavel-relatorio-completo",
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

        # Botão "Gerar Relatório Completo" e "Limpar Pesquisa" abaixo das seções
        html.Div(
            [
            dbc.Button(
                "Gerar Relatório Completo",
                id="generate-report-button-completo",
                color="warning",
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
                    id="clear-data-button-completo",
                    color="secondary",
                    n_clicks=0,
                    style={
                        "font-size": "1.0rem",
                        "padding": "8px 16px",
                        "margin-top": "60px",
                        "margin-left": "20px",  
                        "background-color": "#6c757d",  # Gray color
                        "border-color": "#6c757d"
                    }
                )
            ],
            style={"text-align": "center"}
        )
    ]
)
