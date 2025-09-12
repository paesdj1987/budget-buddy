## callbacks_simples.py

import matplotlib
matplotlib.use('Agg')  
import plotly.graph_objs as go
import pandas as pd
import matplotlib.pyplot as plt
import io
import tempfile
import textwrap
import datetime
import re
from matplotlib import cm, colors  
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import dcc
from dash import callback_context
from dash import html
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from matplotlib.colors import LinearSegmentedColormap
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from PIL import Image



# Função para converter valores de string no formato "000.000.000,00" para float
def convert_to_float(value):
    """Converte strings como '1.234,56', '1234.56', 'R$ 1 234,56' etc. em float.
    Retorna 0.0 em caso de falha."""
    try:
        if value is None or value == "":
            return 0.0
        if isinstance(value, (int, float)):
            return float(value)
        s = str(value).strip().replace("\u00A0", " ")  # NBSP -> espaço normal
        # remove tudo que não for dígitos, vírgula, ponto ou sinal
        s = re.sub(r"[^\d,\.\-]", "", s)
        if "," in s and "." in s:
            # padrão pt-BR '1.234,56' -> '.' milhar, ',' decimal
            s = s.replace(".", "").replace(",", ".")
        elif "," in s:
            # '1234,56' -> ',' decimal
            s = s.replace(".", "").replace(",", ".")
        else:
            # '1,234.56' ou '1234.56' -> '.' decimal, remove vírgulas de milhar
            s = s.replace(",", "")
        return float(s)
    except (ValueError, TypeError):
        return 0.0
# Função para converter float para string no formato "000.000.000,00"
def convert_from_float(value):
    try:
        return '{:,.2f}'.format(value).replace(',', 'X').replace('.', ',').replace('X', '.')
    except (ValueError, TypeError):
        return '0,00'


def register_callbacks_simples(app):
    # Definir cores personalizadas (custom_colors)
    custom_colors = [
        '#FFF3E0', '#FFE0B2', '#FFCC80', '#FFB74D', '#FFA726',
        '#FF9800', '#FB8C00', '#F57C00', '#EF6C00', '#E65100',
        '#DD2C00'
    ]

    # ***************************
    # Callback para atualizar o link do Google Maps no ícone
    # ***************************
    @app.callback(
        Output("maps-link", "href"),
        Input("localizacao", "value")
    )
    def update_google_maps_link(address):
        if not address or address.strip() == "":
            return None  

        # Criar o link do Google Maps formatado
        base_url = "https://www.google.com/maps/search/?api=1&query="
        formatted_address = address.replace(" ", "+")  
        return base_url + formatted_address

    

    # ***************************
    # Callback para preenchimento da lista suspensa 
    # ***************************
    @app.callback(
    [
        Output('fechamento-perimetral', 'value'),
        Output('meio-fio', 'value'),
        Output('rede-eletrica', 'value'),
        Output('rede-agua', 'value'),
        Output('rede-drenagem', 'value'),
        Output('rede-esgoto', 'value'),
        Output('pavimentacao', 'value'),
        Output('supressao-vegetacao', 'value'),
        Output('custo-terraplanagem', 'value'),
        Output('edificacoes', 'value'),
        Output('quadra-society', 'value'),
        Output('dados-incc-antigo', 'value'),
    ],
    Input('empreendimento-aplicar-button', 'n_clicks'),
    State('empreendimento-dropdown', 'value')
    )
    def aplicar_empreendimento(n_clicks, empreendimento):
        if not n_clicks:
            raise PreventUpdate
        
        if empreendimento == 'default':
            return [None]*12
        
        if empreendimento == 'economico':
            return [
                '97.33',
                '56.09',
                '399.33',
                '94.65',
                '492.23',
                '410.49',
                '141.34',
                '0.71',
                '25.39',
                '3569.14',
                '469.09',
                '1149,17'
            ]
        
        if empreendimento == 'medio_alto':
            return [
                '83.58',
                '81.23',
                '1658.88',
                '582.88',
                '492.23',
                '137.88',
                '148.75',
                '1.32',
                '25.39',
                '3143.09',
                '315.87',
                '1149,17'
            ]

        return [None]*12
    
    # ***************************
    # Callback para salvar dados do formulário Orçamento Simples em dcc.Store 
    # ***************************
    @app.callback(
        Output('shared-data', 'data'),
        [
            Input('responsavel-relatorio-simples', 'value'),
            Input('info-geral', 'value'),
            Input('id-loteamento', 'value'),
            Input('localizacao', 'value'),
            Input('revisao', 'value'),
            Input('vgv', 'value'),
            Input('area-total', 'value'),
            Input('perimetro', 'value'),
            Input('area-lotes', 'value'),
            Input('area-viario', 'value'),
            Input('comprimento-viario', 'value'),
            Input('area-construida', 'value'),
            Input('area-quadra', 'value'),
            Input('qtd-lotes', 'value'),
            Input('dados-incc-antigo', 'value'),
            Input('dados-incc-atual', 'value'),
            Input('volume-corte', 'value'),
            Input('volume-aterro', 'value'),
            Input('volume-transporte', 'value'),
            Input('fechamento-perimetral', 'value'),
            Input('meio-fio', 'value'),
            Input('rede-eletrica', 'value'),
            Input('rede-agua', 'value'),
            Input('rede-drenagem', 'value'),
            Input('rede-esgoto', 'value'),
            Input('pavimentacao', 'value'),
            Input('supressao-vegetacao', 'value'),
            Input('custo-terraplanagem', 'value'),
            Input('edificacoes', 'value'),
            Input('quadra-society', 'value'),
        ],
        State('shared-data', 'data')
    )
    def save_data(
        responsavel_relatorio_simples, info_geral, id_loteamento, localizacao, revisao, vgv, area_total, perimetro,
        area_lotes, area_viario, comprimento_viario, area_construida, area_quadra, qtd_lotes,
        dados_incc_antigo, dados_incc_atual, volume_corte, volume_aterro,
        volume_transporte, fechamento_perimetral, meio_fio, rede_eletrica,
        rede_agua, rede_drenagem, rede_esgoto, pavimentacao,
        supressao_vegetacao, custo_terraplanagem, edificacoes, quadra_society,
        current_data
    ):
        if current_data is None:
            current_data = {}
        
        current_data.update({
            'responsavel_relatorio_simples': responsavel_relatorio_simples,
            'info_geral': info_geral,
            'id_loteamento': id_loteamento,
            'localizacao': localizacao,
            'revisao': revisao,
            'vgv': convert_to_float(vgv),
            'area_total': convert_to_float(area_total),
            'perimetro': convert_to_float(perimetro),
            'area_lotes': convert_to_float(area_lotes),
            'area_viario': convert_to_float(area_viario),
            'comprimento_viario': convert_to_float(comprimento_viario),
            'area_construida': convert_to_float(area_construida),
            'area_quadra': convert_to_float(area_quadra),
            'qtd_lotes': convert_to_float(qtd_lotes),
            'dados_incc_antigo': convert_to_float(dados_incc_antigo),
            'dados_incc_atual': convert_to_float(dados_incc_atual),
            'volume_corte': convert_to_float(volume_corte),
            'volume_aterro': convert_to_float(volume_aterro),
            'volume_transporte': convert_to_float(volume_transporte),
            'fechamento_perimetral': convert_to_float(fechamento_perimetral),
            'meio_fio': convert_to_float(meio_fio),
            'rede_eletrica': convert_to_float(rede_eletrica),
            'rede_agua': convert_to_float(rede_agua),
            'rede_drenagem': convert_to_float(rede_drenagem),
            'rede_esgoto': convert_to_float(rede_esgoto),
            'pavimentacao': convert_to_float(pavimentacao),
            'supressao_vegetacao': convert_to_float(supressao_vegetacao),
            'custo_terraplanagem': convert_to_float(custo_terraplanagem),
            'edificacoes': convert_to_float(edificacoes),
            'quadra_society': convert_to_float(quadra_society),
        })
        return current_data

    # Callback para carregar os dados do dcc.Store nos inputs quando a página é acessada -------------------------
    @app.callback(
        [
            Output('responsavel-relatorio-simples', 'value'),
            Output('info-geral', 'value'),
            Output('id-loteamento', 'value'),
            Output('localizacao', 'value'),
            Output('revisao', 'value'),
            Output('vgv', 'value'),
            Output('area-total', 'value'),
            Output('perimetro', 'value'),
            Output('area-lotes', 'value'),
            Output('area-viario', 'value'),
            Output('comprimento-viario', 'value'),
            Output('area-construida', 'value'),
            Output('area-quadra', 'value'),
            Output('qtd-lotes', 'value'),
            Output('dados-incc-antigo', 'value'),
            Output('dados-incc-atual', 'value'),
            Output('volume-corte', 'value'),
            Output('volume-aterro', 'value'),
            Output('volume-transporte', 'value'),
            Output('fechamento-perimetral', 'value'),
            Output('meio-fio', 'value'),
            Output('rede-eletrica', 'value'),
            Output('rede-agua', 'value'),
            Output('rede-drenagem', 'value'),
            Output('rede-esgoto', 'value'),
            Output('pavimentacao', 'value'),
            Output('supressao-vegetacao', 'value'),
            Output('custo-terraplanagem', 'value'),
            Output('edificacoes', 'value'),
            Output('quadra-society', 'value'),
        ],
        [
            Input('url', 'pathname')  # Atualiza quando a URL muda
        ],
        [
            State('shared-data', 'data') # Carrega os dados salvos no Store
        ]
    )
    def load_data(pathname, data):
        if pathname != '/orcamento-simples':
            raise PreventUpdate  
        if data is None:
            return [None] * 30
        return [
            data.get('responsavel_relatorio_simples', None),
            data.get('info_geral', None),
            data.get('id_loteamento', None),
            data.get('localizacao', None),
            data.get('revisao', None),
            convert_from_float(data.get('vgv', 0)),
            convert_from_float(data.get('area_total', 0)),
            convert_from_float(data.get('perimetro', 0)),
            convert_from_float(data.get('area_lotes', 0)),
            convert_from_float(data.get('area_viario', 0)),
            convert_from_float(data.get('comprimento_viario', 0)),
            convert_from_float(data.get('area_construida', 0)),
            convert_from_float(data.get('area_quadra', 0)),
            convert_from_float(data.get('qtd_lotes', 0)),
            convert_from_float(data.get('dados_incc_antigo', 0)),
            convert_from_float(data.get('dados_incc_atual', 0)),
            convert_from_float(data.get('volume_corte', 0)),
            convert_from_float(data.get('volume_aterro', 0)),
            convert_from_float(data.get('volume_transporte', 0)),
            convert_from_float(data.get('fechamento_perimetral', 0)),
            convert_from_float(data.get('meio_fio', 0)),
            convert_from_float(data.get('rede_eletrica', 0)),
            convert_from_float(data.get('rede_agua', 0)),
            convert_from_float(data.get('rede_drenagem', 0)),
            convert_from_float(data.get('rede_esgoto', 0)),
            convert_from_float(data.get('pavimentacao', 0)),
            convert_from_float(data.get('supressao_vegetacao', 0)),
            convert_from_float(data.get('custo_terraplanagem', 0)),
            convert_from_float(data.get('edificacoes', 0)),
            convert_from_float(data.get('quadra_society', 0)),
        ]

    # Callback para gerar o relatório simples -------------------------
    @app.callback(
        Output('url', 'pathname'),
        [Input('generate-report-button', 'n_clicks')],
        [State('shared-data', 'data')]
    )
    def generate_simple_report(n_clicks, data):
        if n_clicks is None or n_clicks == 0:
            raise PreventUpdate
        if data is None:
            raise PreventUpdate
        return '/relatorio-simples'

    # Lista dos campos do formulário que serão limpos
    FIELDS_TO_CLEAR = [
        "responsavel-relatorio-simples",
        "info-geral",
        "id-loteamento",
        "localizacao",
        "revisao",
        "vgv",
        "area-total",
        "perimetro",
        "area-lotes",
        "area-viario",
        "comprimento-viario",
        "area-construida",
        "area-quadra",
        "qtd-lotes",
        "dados-incc-antigo",
        "dados-incc-atual",
        "volume-corte",
        "volume-aterro",
        "volume-transporte",
        "fechamento-perimetral",
        "meio-fio",
        "rede-eletrica",
        "rede-agua",
        "rede-drenagem",
        "rede-esgoto",
        "pavimentacao",
        "supressao-vegetacao",
        "custo-terraplanagem",
        "edificacoes",
        "quadra-society",
    ]

    # Callback para limpar os campos do formulário Orçamento Simples -------------------------
    @app.callback(
        [Output(field, "value") for field in FIELDS_TO_CLEAR] + [Output('shared-data', 'data')],
        Input("clear-button", "n_clicks")
    )
    def clear_simple_form(n_clicks):
        if not n_clicks:
            raise PreventUpdate
        return [None] * len(FIELDS_TO_CLEAR) + [None]

    
    # Callback para atualizar a tabela, os cards e gerar o gráfico de barras na página Relatório Simples -------------------------
    @app.callback(
        [
            Output('results-table', 'data'),
            Output('bar-chart', 'figure'),
            Output('card-id-loteamento', 'children'),
            Output('card-valor-total', 'children'),
            Output('card-cc-fip', 'children'),
            Output('card-cc-at', 'children'),
            Output('card-cc-ap', 'children'),
            Output('card-cc-vgv', 'children'),
        ],
            Input('url', 'pathname'),
            Input('shared-data', 'data'),   
    )
    def update_results_table_and_graph(pathname, data):
        if pathname != '/relatorio-simples':
            raise PreventUpdate
        if data is None:
            return [], {}, "", "", "", "", "", ""
        
        def get_value(key):
            return data.get(key, 0.0)

        # DADOS URBANÍSTICOS 
        perimetro = convert_to_float(data.get('perimetro', 0.0))
        comprimento_viario = convert_to_float(data.get('comprimento_viario', 0.0))
        area_viario = convert_to_float(data.get('area_viario', 0.0))
        area_total = convert_to_float(data.get('area_total', 0.0))
        area_lotes = convert_to_float(data.get('area_lotes', 0.0))
        area_construida = convert_to_float(data.get('area_construida', 0.0))
        area_quadra = convert_to_float(data.get('area_quadra', 0.0))
        qtd_lotes = convert_to_float(data.get('qtd_lotes', 0.0))
        dados_incc_antigo = convert_to_float(data.get('dados_incc_antigo', 0.0))
        dados_incc_atual = convert_to_float(data.get('dados_incc_atual', 0.0))
        id_loteamento = data.get('id_loteamento', '')
        vgv = convert_to_float(data.get('vgv', 0.0))
        # TERRAPLANAGEM 
        volume_corte = convert_to_float(data.get('volume_corte', 0.0))
        volume_aterro = convert_to_float(data.get('volume_aterro', 0.0))
        volume_transporte = convert_to_float(data.get('volume_transporte', 0.0))
        # CUSTOS UNITÁRIOS
        fechamento_perimetral = convert_to_float(data.get('fechamento_perimetral', 0.0))
        meio_fio = convert_to_float(data.get('meio_fio', 0.0))
        rede_eletrica = convert_to_float(data.get('rede_eletrica', 0.0))
        rede_agua = convert_to_float(data.get('rede_agua', 0.0))
        rede_drenagem = convert_to_float(data.get('rede_drenagem', 0.0))
        rede_esgoto = convert_to_float(data.get('rede_esgoto', 0.0))
        pavimentacao = convert_to_float(data.get('pavimentacao', 0.0))
        supressao_vegetacao = convert_to_float(data.get('supressao_vegetacao', 0.0))
        custo_terraplanagem = convert_to_float(data.get('custo_terraplanagem', 0.0))
        edificacoes = convert_to_float(data.get('edificacoes', 0.0))
        quadra_society = convert_to_float(data.get('quadra_society', 0.0))

        # Verificar se os dados do INCC são válidos
        if not dados_incc_antigo or dados_incc_antigo == 0:
            return [], {}, "", "Dados INCC Antigo não pode ser zero ou vazio.", "", "", ""
        if not dados_incc_atual or dados_incc_atual == 0:
            return [], {}, "", "Dados INCC Atual não pode ser zero ou vazio.", "", "", ""

        # Cálculos para Coluna Quantitativo (Antigo)
        #v1 = fechamento_perimetral * perimetro
        #v2 = meio_fio * (comprimento_viario * 2)
        #v3 = rede_eletrica * comprimento_viario
        #v4 = rede_agua * (comprimento_viario * 2)
        #v5 = rede_drenagem * comprimento_viario  
        #v6 = rede_esgoto * comprimento_viario
        #v7 = pavimentacao * area_viario
        #v8 = supressao_vegetacao * area_total
        #v9 = custo_terraplanagem * (volume_corte + volume_aterro + volume_transporte)
        #v10 = edificacoes * area_construida
        #v11 = quadra_society * area_quadra

        # Cálculos para Coluna Quantitativo
        v1 = perimetro
        v2 = comprimento_viario * 2
        v3 = comprimento_viario
        v4 = comprimento_viario * 2
        v5 = comprimento_viario  
        v6 = comprimento_viario
        v7 = area_viario
        v8 = area_total
        v9 = volume_corte + volume_aterro + volume_transporte
        v10 = area_construida
        v11 = area_quadra

        # Cálculos para VALOR TOTAL
        fator_correcao = dados_incc_atual / dados_incc_antigo
        ct1 = (fechamento_perimetral * perimetro) * fator_correcao
        ct2 = (meio_fio * (comprimento_viario * 2)) * fator_correcao
        ct3 = (rede_eletrica * comprimento_viario) * fator_correcao
        ct4 = (rede_agua * (comprimento_viario * 2)) * fator_correcao
        ct5 = (rede_drenagem * comprimento_viario) * fator_correcao  
        ct6 = (rede_esgoto * comprimento_viario) * fator_correcao
        ct7 = (pavimentacao * area_viario) * fator_correcao
        ct8 = (supressao_vegetacao * area_total) * fator_correcao
        ct9 = (custo_terraplanagem * (volume_corte + volume_aterro + volume_transporte)) * fator_correcao
        ct10 = (edificacoes * area_construida) * fator_correcao
        ct11 = (quadra_society * area_quadra) * fator_correcao

        # Dados da tabela
        table_data = [
            {"item": "Fechamento Perimetral", "custo_unitario": convert_from_float(fechamento_perimetral), "quantitativo": convert_from_float(v1), "valor_total_corrigido": convert_from_float(ct1)},
            {"item": "Meio fio", "custo_unitario": convert_from_float(meio_fio), "quantitativo": convert_from_float(v2), "valor_total_corrigido": convert_from_float(ct2)},
            {"item": "Rede de Distribuição Elétrica", "custo_unitario": convert_from_float(rede_eletrica), "quantitativo": convert_from_float(v3), "valor_total_corrigido": convert_from_float(ct3)},
            {"item": "Rede de Abastecimento de Água", "custo_unitario": convert_from_float(rede_agua), "quantitativo": convert_from_float(v4), "valor_total_corrigido": convert_from_float(ct4)},
            {"item": "Rede de Drenagem", "custo_unitario": convert_from_float(rede_drenagem), "quantitativo": convert_from_float(v5), "valor_total_corrigido": convert_from_float(ct5)},
            {"item": "Rede de Coleta de Esgoto", "custo_unitario": convert_from_float(rede_esgoto), "quantitativo": convert_from_float(v6), "valor_total_corrigido": convert_from_float(ct6)},
            {"item": "Pavimentação", "custo_unitario": convert_from_float(pavimentacao), "quantitativo": convert_from_float(v7), "valor_total_corrigido": convert_from_float(ct7)},
            {"item": "Supressão de Vegetação", "custo_unitario": convert_from_float(supressao_vegetacao), "quantitativo": convert_from_float(v8), "valor_total_corrigido": convert_from_float(ct8)},
            {"item": "Terraplenagem", "custo_unitario": convert_from_float(custo_terraplanagem), "quantitativo": convert_from_float(v9), "valor_total_corrigido": convert_from_float(ct9)},
            {"item": "Edificações", "custo_unitario": convert_from_float(edificacoes), "quantitativo": convert_from_float(v10), "valor_total_corrigido": convert_from_float(ct10)},
            {"item": "Quadra Society", "custo_unitario": convert_from_float(quadra_society), "quantitativo": convert_from_float(v11), "valor_total_corrigido": convert_from_float(ct11)},
        ]

        # Calcular subtotal (soma dos valores corrigidos sem o acréscimo)
        subtotal = sum([ct1, ct2, ct3, ct4, ct5, ct6, ct7, ct8, ct9, ct10, ct11])

        # Valor total do orçamento (com acréscimo de 20%)
        valor_total_orcamento = subtotal / 0.80

        # Atualiza os cards
        card_id_loteamento = id_loteamento
        card_valor_total = f"R$ {convert_from_float(valor_total_orcamento)}"
        card_sub_total = f"R$ {convert_from_float(subtotal)}/m²"

        # Cálculo do CC/FIP
        cc_fip = valor_total_orcamento / qtd_lotes if qtd_lotes else 0.0
        card_cc_fip = f"R$ {convert_from_float(cc_fip)}/lote"

        # Calcular CC/AT (Custo de Construção por Área Total)
        cc_at = valor_total_orcamento / area_total if area_total else 0.0
        card_cc_at = f"R$ {convert_from_float(cc_at)}/m²"

        # Calcular CC/AP (Custo de Construção por Área de Projeto)
        cc_ap = valor_total_orcamento / area_lotes if area_lotes else 0.0
        card_cc_ap = f"R$ {convert_from_float(cc_ap)}/m²"
        
        # Calcular CC/VGV (Custo de Construção por Valor Geral de Vendas)
        if vgv and vgv != 0 and area_lotes and area_lotes != 0 and qtd_lotes and qtd_lotes != 0:
            cc_vgv_value = valor_total_orcamento / (area_lotes * vgv * qtd_lotes) * 100.0
            card_cc_vgv = f"{convert_from_float(cc_vgv_value)}%"
        else:
            cc_vgv_value = 0.0
            card_cc_vgv = "0,00"

        # *************************** Gráfico ***************************
        
        # Itens e valores para o gráfico
        itens = [item['item'] for item in table_data]
        valores = [convert_to_float(item['valor_total_corrigido']) for item in table_data]

        # Calcular o total e os percentuais
        total_valores = sum(valores)
        percentuais = [(valor / total_valores) * 100 if total_valores != 0 else 0 for valor in valores]

        # Ordenar os dados do maior para o menor percentual
        data_for_chart = sorted(zip(percentuais, itens, valores), reverse=True)
        percentuais_ordenados, itens_ordenados, valores_ordenados = zip(*data_for_chart)

        # Paleta de cores (tons de laranja fortes)
        strong_orange_colors = ['#FFA726', '#FF9800', '#FB8C00', '#F57C00', '#EF6C00', '#E65100']

        # Criar um colormap ajustado para tons mais fortes
        cmap = LinearSegmentedColormap.from_list('strong_orange', strong_orange_colors)

        # Normalizar os valores para mapear nas cores
        max_valor = max(valores_ordenados)
        min_valor = min(valores_ordenados)
        valor_range = max_valor - min_valor if max_valor != min_valor else 1
        norm_valores = [(valor - min_valor) / valor_range for valor in valores_ordenados]

        # Mapear os valores normalizados para cores
        cores_mapeadas = [cmap(norm) for norm in norm_valores]

        # Converter as cores para formato hexadecimal
        cores_hex = [
            '#{:02x}{:02x}{:02x}'.format(
                int(r * 255), int(g * 255), int(b * 255)
            ) for r, g, b, _ in cores_mapeadas
        ]

        # Dados para o gráfico
        fig = go.Figure(
            data=[
                go.Bar(
                    x=percentuais_ordenados,      # Percentuais no eixo X
                    y=itens_ordenados,            # Itens no eixo Y
                    orientation='h',              # Orientação horizontal
                    text=[f"{percentual:.2f}%" for percentual in percentuais_ordenados],  # Texto como percentual
                    textposition='inside',        # Texto dentro das barras
                    textfont=dict(
                        family="Arial",
                        size=14,
                        color="white"
                    ),
                    marker=dict(
                        color=cores_hex,          # Paleta de cores personalizada
                        line=dict(width=1, color="orange"),  # Contorno laranja
                    ),
                    hovertemplate=(
                    "<b>%{y}</b><br>"  # Nome do serviço
                    "Percentual: %{x:.2f}%<br>"  # Percentual
                    "Valor: R$ %{customdata[0]:,.2f}<extra></extra>"  # Valor absoluto formatado
                ),
                    customdata=[[valor] for valor in valores_ordenados],  # Adiciona os valores ao tooltip
                )
            ]
        )
                                                                               
        # Atualizações no layout
        fig.update_layout(
            title=dict(
                text="Participação Percentual dos Serviços",
                font=dict(size=24, family="Montserrat", color="#FF8C00"),
                x=0.5,  # Centralizado horizontalmente
                xanchor="center",
            ),
            xaxis=dict(
                title=dict(
                    text="Percentual (%)",  
                    font=dict(size=16, family="Montserrat")
                ),
                tickfont=dict(size=14, family="Montserrat"),
                gridcolor="rgba(200,200,200,0.5)",
                zeroline=False,
            ),
            yaxis=dict(
                title=dict(
                    text="Serviços",  
                    font=dict(size=16, family="Montserrat")
                ),
                tickfont=dict(size=14, family="Montserrat"),
                categoryorder="total ascending",
            ),
            paper_bgcolor="white",
            plot_bgcolor="white",                  # Fundo branco
            margin=dict(l=120, r=40, t=80, b=50),  # Margens ajustadas
            height=600,                            # Altura do gráfico
        )

        # Exibir o gráfico atualizado
        return table_data, fig, card_id_loteamento, card_valor_total, card_cc_fip, card_cc_at, card_cc_ap, card_cc_vgv


    # ====================================================================================
    # Callback para exportar a tabela para Excel 
    # ====================================================================================
    @app.callback(
        Output("download-dataframe-xlsx", "data"),
        [Input("export-button", "n_clicks")],
        [State("results-table", "data")],
        prevent_initial_call=True,
    )
    def export_table_to_excel(n_clicks, table_data):
        if n_clicks is None or not table_data:
            raise PreventUpdate

        # Converter os dados da tabela em um DataFrame
        df = pd.DataFrame(table_data)

        # Retornar o DataFrame para download em formato Excel
        return dcc.send_data_frame(
            df.to_excel, "relatorio_simples.xlsx", sheet_name="Relatório Simples", index=False
        )

    # ====================================================================================
    # CALLBACK PARA GERAR PDF (Orçamento Simplificado)
    # ====================================================================================
    @app.callback(
        Output('download-pdf', 'data'),
        [Input('generate-pdf-button', 'n_clicks')],
        [
            State('results-table', 'data'),
            State('card-id-loteamento', 'children'),
            State('card-valor-total', 'children'),
            State('card-cc-fip', 'children'),
            State('card-cc-at', 'children'),
            State('card-cc-ap', 'children'),
            State('card-cc-vgv', 'children'),
            State('shared-data', 'data'),
        ],
        prevent_initial_call=True
    )
    def generate_pdf(n_clicks, table_data, id_loteamento, valor_total_orcamento, cc_fip, cc_at, cc_ap, cc_vgv, input_data):
        if n_clicks is None or not table_data:
            raise PreventUpdate

        try:
            import datetime, tempfile, textwrap
            from reportlab.lib.pagesizes import letter, landscape
            from reportlab.lib.colors import HexColor
            from reportlab.pdfgen import canvas
            from matplotlib.colors import LinearSegmentedColormap
            import matplotlib.pyplot as plt
            import io

            buffer = io.BytesIO()
            pdf = canvas.Canvas(buffer, pagesize=landscape(letter))
            pdf.setTitle("Orçamento Simplificado")
            pagina_largura, pagina_altura = landscape(letter)

            # --------------------------------------------------------------------------------
            # PÁGINA 1 (Capa)
            # --------------------------------------------------------------------------------
            # Fundo
            pdf.setFillColor(HexColor("#3d5462"))
            pdf.rect(0, 0, pagina_largura, pagina_altura, fill=1)
            # Título
            pdf.setFillColor(HexColor("#FFFFFF"))
            pdf.setFont("Helvetica-Bold", 30)
            titulo_capa = "Orçamento Paramétrico"
            titulo_largura = pdf.stringWidth(titulo_capa, "Helvetica-Bold", 26)
            pdf.drawString((pagina_largura - titulo_largura) / 2, pagina_altura - 120, titulo_capa)
            # Logo na capa
            try:
                capa_logo = "assets/logoor2.png"
                max_width = 300
                max_height = 130
                from PIL import Image
                with Image.open(capa_logo) as img:
                    original_width, original_height = img.size
                    aspect_ratio = original_width / original_height
                if original_width > max_width or original_height > max_height:
                    if aspect_ratio > 1:
                        new_width = max_width
                        new_height = max_width / aspect_ratio
                    else:
                        new_height = max_height
                        new_width = max_height * aspect_ratio
                else:
                    new_width, new_height = original_width, original_height
                x_center = (pagina_largura - new_width) / 2
                y_center = pagina_altura - 350
                pdf.drawImage(capa_logo, x_center, y_center, width=new_width, height=new_height, mask='auto')
            except Exception as e:
                print(f"Erro ao inserir a logo de capa: {e}")

            # Texto info-geral na capa
            pdf.setFont("Helvetica", 16)
            pdf.setFillColor(HexColor("#FFFFFF"))
            info_geral_texto = input_data.get('info_geral', 'Nenhuma informação disponível')
            y_texto = y_center - 60
            text_width = pdf.stringWidth(info_geral_texto, "Helvetica", 16)
            max_line_width = 600
            if text_width > max_line_width:
                linhas = textwrap.wrap(info_geral_texto, width=70)
                for linha in linhas:
                    lw = pdf.stringWidth(linha, "Helvetica", 16)
                    pdf.drawString((pagina_largura - lw) / 2, y_texto, linha)
                    y_texto -= 20
            else:
                pdf.drawString((pagina_largura - text_width) / 2, y_texto, info_geral_texto)

            # Responsável (inferior esquerdo)
            pdf.setFont("Helvetica", 16)
            pdf.setFillColor(HexColor("#FFFFFF"))
            responsavel_texto = f"Responsável: {input_data.get('responsavel_relatorio_simples', 'Não informado')}"
            pdf.drawString(50, 50, responsavel_texto)
            # Data (inferior direito)
            data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
            data_text_width = pdf.stringWidth(data_atual, "Helvetica", 16)
            pdf.drawString(pagina_largura - data_text_width - 50, 50, data_atual)

            pdf.showPage()

            # --------------------------------------------------------------------------------
            # PÁGINA 2 
            # --------------------------------------------------------------------------------
            bar_height = 60
            pdf.setFillColor(HexColor("#3d5462"))
            pdf.rect(0, pagina_altura - bar_height, pagina_largura, bar_height, fill=1)

            # Inserir a logoor2.png à esquerda da barra
            logo_path = "assets/logoor2.png"
            try:
                logo_y = pagina_altura - bar_height + (bar_height - 40) / 2
                pdf.drawImage(logo_path, x=10, y=logo_y, width=80, height=40, mask='auto')
            except Exception as e:
                print(f"Erro ao inserir a logo esquerda: {e}")

            # Inserir o simbolo_or.png à direita da barra
            simbolo_path = "assets/simbolo_or.png"
            try:
                pdf.drawImage(simbolo_path, x=pagina_largura - 90, y=logo_y, width=55, height=35, mask='auto')
            except Exception as e:
                print(f"Erro ao inserir o símbolo direito: {e}")

            # Inserir o título dentro da barra, centralizado
            pdf.setFont("Helvetica-Bold", 16)
            titulo_texto = "Orçamento Simplificado"
            titulo_largura = pdf.stringWidth(titulo_texto, "Helvetica-Bold", 16)
            titulo_y = pagina_altura - bar_height + (bar_height - 16) / 2
            pdf.setFillColor(HexColor("#FFFFFF"))
            pdf.drawString((pagina_largura - titulo_largura) / 2, titulo_y, titulo_texto)

            # Afastar o conteúdo da barra
            y_position = pagina_altura - bar_height - 40

            # Resultados
            pdf.setFillColor(HexColor("#4B2C20"))
            pdf.setFont("Helvetica-Bold", 10)
            pdf.drawString(50, y_position, "Resultados:")
            pdf.setFillColor(HexColor("#000000"))
            y_position -= 15
            resultados = [
                ("Valor Total do Orçamento", valor_total_orcamento),
                ("CC/FIP", cc_fip),
                ("CC/AT", cc_at),
                ("CC/AP", cc_ap),
                ("CC/VGV", cc_vgv),
            ]
            for label, value in resultados:
                pdf.setFont("Helvetica-Bold", 8)
                pdf.drawString(50, y_position, f"{label}: ")
                offset = pdf.stringWidth(f"{label}: ", "Helvetica-Bold", 8)
                pdf.setFont("Helvetica", 8)
                pdf.drawString(50 + offset, y_position, f"{value}")
                y_position -= 16

            # Linha laranja entre Resultados e Informações Gerais
            pdf.setStrokeColor(HexColor("#FFA500"))
            pdf.setLineWidth(1)
            pdf.line(50, y_position, pagina_largura - 50, y_position)
            pdf.setStrokeColor(HexColor("#000000"))
            y_position -= 20

            # Informações Gerais
            pdf.setFillColor(HexColor("#283747"))
            info_geral_value = input_data.get('info_geral', '')
            pdf.setFont("Helvetica-Bold", 10)
            pdf.drawString(50, y_position, "Informações Gerais:")
            pdf.setFillColor(HexColor("#000000"))
            y_position -= 12
            pdf.setFont("Helvetica", 8)
            text_object = pdf.beginText(50, y_position)
            wrapped_lines = textwrap.wrap(info_geral_value, width=180)
            for wrapped_line in wrapped_lines:
                text_object.textLine(wrapped_line)
                y_position -= 12
                if y_position < 50:
                    pdf.drawText(text_object)
                    pdf.showPage()
                    y_position = pagina_altura - 50
                    pdf.setFont("Helvetica", 8)
                    text_object = pdf.beginText(50, y_position)
            pdf.drawText(text_object)
            y_position -= 15

            # Linha laranja entre Informações Gerais e Dados do Projeto
            pdf.setStrokeColor(HexColor("#FFA500"))
            pdf.setLineWidth(1)
            pdf.line(50, y_position, pagina_largura - 50, y_position)
            pdf.setStrokeColor(HexColor("#000000"))
            y_position -= 15

            # Rótulos de inputs
            input_labels = {
                'info_geral': 'Informações Gerais',
                'id_loteamento': 'ID Condomínios Horizontais',
                'localizacao': 'Localização',
                'revisao': 'Revisão',
                'vgv': 'Valor de Venda/m²',
                'area_total': 'Área Total do Terreno (m²)',
                'perimetro': 'Perímetro do Terreno (m)',
                'area_lotes': 'Área dos Lotes (m²)',
                'area_viario': 'Área do Viário (m²)',
                'comprimento_viario': 'Comprimento do Viário (m)',
                'area_construida': 'Área Construída (m²)',
                'area_quadra': 'Área da Quadra (m²)',
                'qtd_lotes': 'Quantidade de Lotes', ### incluido
                'dados_incc_antigo': 'Dados INCC Antigo',
                'dados_incc_atual': 'Dados INCC Atual',
                'volume_corte': 'Volume de Corte (m³)',
                'volume_aterro': 'Volume de Aterro (m³)',
                'volume_transporte': 'Volume de Transporte Interno (m³)',
                'fechamento_perimetral': 'Fechamento Perimetral (cc/m)',
                'meio_fio': 'Meio Fio (cc/m)',
                'rede_eletrica': 'Rede Distribuição Elétrica (cc/m)',
                'rede_agua': 'Rede Abastecimento de Água (cc/m)',
                'rede_drenagem': 'Rede de Drenagem (cc/m)',
                'rede_esgoto': 'Rede Coleta de Esgoto (cc/m)',
                'pavimentacao': 'Pavimentação (cc/m²)',
                'supressao_vegetacao': 'Supressão de Vegetação (cc/m²)',
                'custo_terraplanagem': 'Terraplenagem (cc/m²)',
                'edificacoes': 'Edificações (cc/m²)',
                'quadra_society': 'Quadra Society (cc/m²)',
            }

            # Dados do Projeto
            dados_projeto_keys = [
                'id_loteamento', 'localizacao', 'revisao', 'vgv',
                'area_total', 'perimetro', 'area_lotes', 'area_viario',
                'comprimento_viario', 'area_construida', 'area_quadra',
                'qtd_lotes', ### incluido
                'dados_incc_antigo', 'dados_incc_atual', 'volume_corte',
                'volume_aterro', 'volume_transporte'
            ]
            pdf.setFillColor(HexColor("#2E5633"))
            pdf.setFont("Helvetica-Bold", 10)
            pdf.drawString(50, y_position, "Dados do Projeto:")
            pdf.setFillColor(HexColor("#000000"))
            y_position -= 15

            n_cols = 3
            row_height = 16
            x_positions = [50, 280, 510]
            n_rows = (len(dados_projeto_keys) + n_cols - 1) // n_cols
            for row in range(n_rows):
                for col in range(n_cols):
                    index = row * n_cols + col
                    if index < len(dados_projeto_keys):
                        key = dados_projeto_keys[index]
                        label = input_labels.get(key, key)
                        value = input_data.get(key, '')
                        if key == 'qtd_lotes' and isinstance(value, (int, float)):
                            try:
                                value_str = str(int(round(value)))
                            except Exception:
                                value_str = str(value)
                        elif isinstance(value, (int, float)):
                            value_str = convert_from_float(value)
                        else:
                            value_str = str(value)
                        pdf.setFont("Helvetica-Bold", 8)
                        pdf.drawString(x_positions[col], y_position - (row * row_height), f"{label}: ")
                        offset = pdf.stringWidth(f"{label}: ", "Helvetica-Bold", 8)
                        pdf.setFont("Helvetica", 8)
                        pdf.drawString(x_positions[col] + offset, y_position - (row * row_height), value_str)
            y_position -= n_rows * row_height + 20

            # Linha laranja entre Dados do Projeto e Custo Unitário
            pdf.setStrokeColor(HexColor("#FFA500"))
            pdf.setLineWidth(1)
            pdf.line(50, y_position, pagina_largura - 50, y_position)
            pdf.setStrokeColor(HexColor("#000000"))
            y_position -= 15

            # Custo Unitário
            custo_unitario_keys = [
                'fechamento_perimetral', 'meio_fio', 'rede_eletrica',
                'rede_agua', 'rede_drenagem', 'rede_esgoto', 'pavimentacao',
                'supressao_vegetacao', 'custo_terraplanagem', 'edificacoes', 'quadra_society'
            ]
            pdf.setFillColor(HexColor("#1F3A52"))
            pdf.setFont("Helvetica-Bold", 10)
            pdf.drawString(50, y_position, "Custo Unitário:")
            pdf.setFillColor(HexColor("#000000"))
            y_position -= 15

            n_cols = 3
            row_height = 16
            n_rows = (len(custo_unitario_keys) + n_cols - 1) // n_cols
            for row in range(n_rows):
                for col in range(n_cols):
                    index = row * n_cols + col
                    if index < len(custo_unitario_keys):
                        key = custo_unitario_keys[index]
                        label = input_labels.get(key, key)
                        value = input_data.get(key, '')
                        if isinstance(value, float):
                            value_str = f"{value:.2f}".replace('.', ',')
                        else:
                            value_str = str(value)
                        value_str = f"R$ {value_str}"
                        pdf.setFont("Helvetica-Bold", 8)
                        pdf.drawString(x_positions[col], y_position - (row * row_height), f"{label}: ")
                        offset = pdf.stringWidth(f"{label}: ", "Helvetica-Bold", 8)
                        pdf.setFont("Helvetica", 8)
                        pdf.drawString(x_positions[col] + offset, y_position - (row * row_height), value_str)
            y_position -= n_rows * row_height

            pdf.showPage()

            # --------------------------------------------------------------------------------
            # PÁGINA 3 (seção "Custo por Item de Execução")
            # --------------------------------------------------------------------------------
            bar_height = 60
            pdf.setFillColor(HexColor("#3d5462"))
            pdf.rect(0, pagina_altura - bar_height, pagina_largura, bar_height, fill=1)

            # Inserir a logoor2.png à esquerda da barra
            logo_path = "assets/logoor2.png"
            try:
                logo_y = pagina_altura - bar_height + (bar_height - 40) / 2
                pdf.drawImage(logo_path, x=10, y=logo_y, width=80, height=40, mask='auto')
            except Exception as e:
                print(f"Erro ao inserir a logo esquerda: {e}")

            # Inserir o simbolo_or.png à direita da barra
            simbolo_path = "assets/simbolo_or.png"
            try:
                pdf.drawImage(simbolo_path, x=pagina_largura - 90, y=logo_y, width=55, height=35, mask='auto')
            except Exception as e:
                print(f"Erro ao inserir o símbolo direito: {e}")

            # Inserir o título dentro da barra, centralizado
            pdf.setFont("Helvetica-Bold", 16)
            titulo_texto = "Orçamento Simplificado"
            titulo_largura = pdf.stringWidth(titulo_texto, "Helvetica-Bold", 16)
            titulo_y = pagina_altura - bar_height + (bar_height - 16) / 2
            pdf.setFillColor(HexColor("#FFFFFF"))
            pdf.drawString((pagina_largura - titulo_largura) / 2, titulo_y, titulo_texto)

            # Afastar o conteúdo da barra
            y_position = pagina_altura - bar_height - 40


            pdf.setFillColor(HexColor("#2D4159"))
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(50, y_position, "Custo por Item de Execução: ")
            pdf.setFillColor(HexColor("#000000"))
            y_position -= 25

            pdf.setFillColor(HexColor("#4B2C20"))
            pdf.setFont("Helvetica-Bold", 10)
            headers = ["Item", "Valor Total Corrigido"]
            x_positions_table = [50, 250]
            for i, header in enumerate(headers):
                pdf.drawString(x_positions_table[i], y_position, header)
            y_position -= 20
            pdf.setFillColor(HexColor("#000000"))

            pdf.setFont("Helvetica", 9)
            row_height = 18
            total_valor = 0
            for item in table_data:
                item_name = item.get('item', '')
                valor_total_corrigido = convert_to_float(item.get('valor_total_corrigido', 0.0))
                valor_total_str = f"R$ {convert_from_float(valor_total_corrigido)}"
                total_valor += valor_total_corrigido
                pdf.setFont("Helvetica-Bold", 8)
                pdf.drawString(x_positions_table[0], y_position, str(item_name))
                pdf.setFont("Helvetica", 8)
                pdf.drawString(x_positions_table[1], y_position, valor_total_str)
                y_position -= row_height
                if y_position < 50:
                    pdf.showPage()
                    y_position = pagina_altura - 50
                    pdf.setFont("Helvetica", 8)

            subtotal_valor_corrigido = total_valor * 0.2
            pdf.setStrokeColor(HexColor("#FF9999"))
            pdf.setLineWidth(1)
            pdf.line(50, y_position, pagina_largura - 450, y_position)
            pdf.setStrokeColor(HexColor("#000000"))
            y_position -= 15

            pdf.setFont("Helvetica-Bold", 9)
            pdf.drawString(x_positions_table[0], y_position, "Serviços Complementares (20%):")
            pdf.setFont("Helvetica-Bold", 9)
            pdf.drawString(x_positions_table[1], y_position, f"R$ {convert_from_float(subtotal_valor_corrigido)}")
            y_position -= 10

            pdf.setStrokeColor(HexColor("#FFA500"))
            pdf.setLineWidth(0.5)
            pdf.line(50, y_position, pagina_largura - 450, y_position)
            pdf.setStrokeColor(HexColor("#000000"))
            y_position -= 15

            pdf.setFont("Helvetica-Bold", 9)
            pdf.drawString(x_positions_table[0], y_position, "Total:")
            pdf.setFont("Helvetica-Bold", 9)
            pdf.drawString(x_positions_table[1], y_position, f"R$ {convert_from_float(total_valor)}")
            pdf.showPage()

            # --------------------------------------------------------------------------------
            # PÁGINA 4 (Gráfico - Participação Percentual dos Serviços)
            # --------------------------------------------------------------------------------
            bar_height = 60
            pdf.setFillColor(HexColor("#3d5462"))
            pdf.rect(0, pagina_altura - bar_height, pagina_largura, bar_height, fill=1)

            # Inserir a logoor2.png à esquerda da barra
            logo_path = "assets/logoor2.png"
            try:
                logo_y = pagina_altura - bar_height + (bar_height - 40) / 2
                pdf.drawImage(logo_path, x=10, y=logo_y, width=80, height=40, mask='auto')
            except Exception as e:
                print(f"Erro ao inserir a logo esquerda: {e}")

            # Inserir o simbolo_or.png à direita da barra
            simbolo_path = "assets/simbolo_or.png"
            try:
                pdf.drawImage(simbolo_path, x=pagina_largura - 90, y=logo_y, width=55, height=35, mask='auto')
            except Exception as e:
                print(f"Erro ao inserir o símbolo direito: {e}")

            # Inserir o título centralizado dentro da barra
            pdf.setFont("Helvetica-Bold", 16)
            titulo_grafico = "Gráfico de Participação Percentual dos Serviços"
            titulo_largura = pdf.stringWidth(titulo_grafico, "Helvetica-Bold", 16)
            titulo_y = pagina_altura - bar_height + (bar_height - 16) / 2
            pdf.setFillColor(HexColor("#FFFFFF"))
            pdf.drawString((pagina_largura - titulo_largura) / 2, titulo_y, titulo_grafico)

            # Definir a posição para iniciar o conteúdo abaixo da barra
            y_position = pagina_altura - bar_height - 40


            # Combinar "Edificações" e "Quadra Society" em um único item "Áreas Comuns"
            area_comuns_valor = 0
            data_para_grafico = []
            for item in table_data:
                if item['item'] in ["Edificações", "Quadra Society"]:
                    area_comuns_valor += convert_to_float(item['valor_total_corrigido'])
                else:
                    data_para_grafico.append(item)
            if area_comuns_valor > 0:
                data_para_grafico.append({
                    "item": "Áreas Comuns",
                    "valor_total_corrigido": convert_from_float(area_comuns_valor)
                })

            # Criando o gráfico no Matplotlib
            fig, ax = plt.subplots(figsize=(14, 6))

            # Extração dos dados a partir de data_para_grafico
            itens = [item['item'] for item in data_para_grafico]
            valores = [convert_to_float(item['valor_total_corrigido']) for item in data_para_grafico]
            total_valores = sum(valores)

            # Calcula percentuais e ordena os itens
            percentuais = [(v / total_valores) * 100 if total_valores else 0 for v in valores]
            data_for_chart = sorted(zip(percentuais, itens, valores), reverse=True)
            percentuais_ordenados, itens_ordenados, valores_ordenados = zip(*data_for_chart)

            # Definição da paleta de cores
            strong_orange_colors = ['#FFA726', '#FF9800', '#FB8C00', '#F57C00', '#EF6C00', '#E65100']
            cmap = LinearSegmentedColormap.from_list('strong_orange', strong_orange_colors)

            # Normalizando valores para mapeamento de cores
            max_valor = max(valores_ordenados)
            min_valor = min(valores_ordenados)
            valor_range = max_valor - min_valor if max_valor != min_valor else 1
            norm_valores = [(val - min_valor) / valor_range for val in valores_ordenados]
            cores_mapeadas = [cmap(nval) for nval in norm_valores]
            cores_hex = ['#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255)) for r, g, b, _ in cores_mapeadas]

            # Criando as barras horizontais
            bars = ax.barh(itens_ordenados, percentuais_ordenados, color=cores_hex)

            # Removendo a borda
            for spine in ax.spines.values():
                spine.set_visible(False)

            # Adicionando rótulos à direita das barras
            for bar, percentual, valor in zip(bars, percentuais_ordenados, valores_ordenados):
                valor_formatado = f"R$ {convert_from_float(valor)}"
                annotation_text = f"{percentual:.2f}% ({valor_formatado})"
                ax.annotate(
                    annotation_text,
                    xy=(bar.get_width(), bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0),
                    textcoords="offset points",
                    ha='left',
                    va='center',
                    fontsize=10,
                    weight='bold',
                    color='black'
                )

            # Ajustes no layout do gráfico
            ax.invert_yaxis()
            ax.set_xlabel('Percentual (%)', fontsize=12)
            ax.set_ylabel('Serviços', fontsize=12)
            ax.tick_params(axis='x', labelsize=10)
            ax.tick_params(axis='y', labelsize=10)
            ax.grid(True, axis='x', linestyle='--', alpha=0.7)

            plt.tight_layout()

            # Salvar o gráfico temporariamente e inseri-lo no PDF
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
                plt.savefig(tmpfile.name, format='png', bbox_inches='tight')
                plt.close(fig)
                grafico_x = 50
                grafico_y = (pagina_altura - 400) / 2
                grafico_width = 700
                grafico_height = 400
                pdf.drawImage(tmpfile.name, x=grafico_x, y=grafico_y, width=grafico_width, height=grafico_height, mask='auto')

            pdf.showPage()


            # --------------------------------------------------------------------------------
            # PÁGINA 5 (Gráfico - Custo de Construção)
            # --------------------------------------------------------------------------------
            bar_height = 60
            pdf.setFillColor(HexColor("#3d5462"))
            pdf.rect(0, pagina_altura - bar_height, pagina_largura, bar_height, fill=1)

            # Inserir a logoor2.png à esquerda da barra
            logo_path = "assets/logoor2.png"
            try:
                logo_y = pagina_altura - bar_height + (bar_height - 40) / 2
                pdf.drawImage(logo_path, x=10, y=logo_y, width=80, height=40, mask='auto')
            except Exception as e:
                print(f"Erro ao inserir a logo esquerda: {e}")

            # Inserir o simbolo_or.png à direita da barra
            simbolo_path = "assets/simbolo_or.png"
            try:
                pdf.drawImage(simbolo_path, x=pagina_largura - 90, y=logo_y, width=55, height=35, mask='auto')
            except Exception as e:
                print(f"Erro ao inserir o símbolo direito: {e}")

            # Inserir o título dentro da barra, centralizado
            pdf.setFont("Helvetica-Bold", 16)
            titulo_texto = "Gráfico de Custo de Construção"
            titulo_largura = pdf.stringWidth(titulo_texto, "Helvetica-Bold", 16)
            titulo_y = pagina_altura - bar_height + (bar_height - 16) / 2
            pdf.setFillColor(HexColor("#FFFFFF"))
            pdf.drawString((pagina_largura - titulo_largura) / 2, titulo_y, titulo_texto)

            # Ajustar a posição do conteúdo abaixo da barra
            y_position = pagina_altura - bar_height - 40


            def to_float(valor_str):
                if not isinstance(valor_str, str):
                    try:
                        return float(valor_str)
                    except:
                        return 0.0

                apenas_numeros = re.sub(r"[^0-9.,]+", "", valor_str)
                sem_pontos_milhar = apenas_numeros.replace(".", "")
                padronizado = sem_pontos_milhar.replace(",", ".")
                
                try:
                    resultado = float(padronizado)
                except:
                    resultado = 0.0
                return resultado

            # Converter
            cc_fip_val = to_float(cc_fip)
            cc_at_val = to_float(cc_at)
            cc_ap_val = to_float(cc_ap)


            labels = ["CC/FIP", "CC/AT", "CC/AP"]
            values = [cc_fip_val, cc_at_val, cc_ap_val]

            fig, ax = plt.subplots(figsize=(10, 5))
            bar_colors = ["#FF9900", "#FF9900", "#FF9900"]
            bars = ax.bar(labels, values, color=bar_colors, width=0.3)

            ax.set_xlabel("Tipo", fontsize=12)
            ax.set_ylabel("Valor (R$)", fontsize=12)
            ax.yaxis.grid(True, linestyle="--", alpha=0.6)

            max_val = max(values) if values else 0
            ax.set_ylim([0, max_val * 1.2 if max_val else 1])

            for bar in bars:
                altura = bar.get_height()
                ax.annotate(
                    f"R$ {altura:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                    xy=(bar.get_x() + bar.get_width() / 2, altura),
                    xytext=(0, 5),
                    textcoords="offset points",
                    ha='center',
                    va='bottom',
                    fontsize=10,
                    weight='bold'
                )

            plt.tight_layout()

            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
                plt.savefig(tmpfile.name, format='png', bbox_inches='tight')
                plt.close(fig)
                grafico_x = 50
                grafico_width = pagina_largura - 100
                grafico_height = 400
                grafico_y = (pagina_altura - grafico_height) / 2
                pdf.drawImage(
                    tmpfile.name,
                    x=grafico_x,
                    y=grafico_y,
                    width=grafico_width,
                    height=grafico_height,
                    mask='auto'
                )

            pdf.showPage()


            pdf.save()
            buffer.seek(0)

            # Função writer para gravar os bytes no stream
            def write_pdf_bytes(f):
                f.write(buffer.getvalue())

            return dcc.send_bytes(write_pdf_bytes, "relatorio_simplificado.pdf")


        except Exception as e:
            print(f"Erro ao gerar o PDF: {e}")
            raise PreventUpdate

