## callbacks_completo

import matplotlib
matplotlib.use('Agg')  # Define o backend não interativo
import io
import tempfile
import matplotlib.pyplot as plt
import textwrap
import plotly.graph_objs as go
import pandas as pd
import datetime
import re
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import dcc
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from matplotlib.colors import LinearSegmentedColormap
from datetime import datetime
from PIL import Image


# Função para converter valores de string no formato "000.000.000,00" para float
def convert_to_float(value):
    try:
        if isinstance(value, str):
            value = value.replace('.', '').replace(',', '.')
        return float(value)
    except (ValueError, TypeError):
        return 0.0  

# Função para converter float para string no formato "000.000.000,00"
def convert_from_float(value):
    try:
        return '{:,.2f}'.format(value).replace(',', 'X').replace('.', ',').replace('X', '.')
    except (ValueError, TypeError):
        return '0,00'

def register_callbacks_completo(app):

    
    custom_colors = [
        '#E0F3F9','#C6E7F1','#ADDCE9','#94D1E1','#7BC5D8',
        '#62B9D0','#499EB5','#346F7A','#345F6C','#2D5260',     
        '#264552','#1F3844'
    ]

    # ***************************
    # Callback para atualizar o link do Google Maps no ícone
    # ***************************
    @app.callback(
        Output("maps-link-completo", "href"),
        Input("localizacao-completo", "value")
    )
    def update_google_maps_link(address):
        if not address or address.strip() == "":
            return None  # Remove o link quando não há endereço

        # Criar o link do Google Maps formatado
        base_url = "https://www.google.com/maps/search/?api=1&query="
        formatted_address = address.replace(" ", "+") 
        return base_url + formatted_address


    # ***************************
    # Callback para salvar dados do formulário Orçamento Completo em dcc.Store 
    # ***************************
    @app.callback(
        Output('shared-data-completo', 'data'),
        [
            Input('responsavel-relatorio-completo', 'value'),
            Input('info-geral-completo', 'value'),
            Input('id-loteamento-completo', 'value'),
            Input('localizacao-completo', 'value'),
            Input('revisao-completo', 'value'),
            Input('vgv-completo', 'value'),
            Input('area-total-completo', 'value'),
            Input('perimetro-completo', 'value'),
            Input('area-lotes-completo', 'value'),
            Input('area-viario-completo', 'value'),
            Input('comprimento-viario-completo', 'value'),
            Input('area-construida-completo', 'value'),
            Input('area-quadra-completo', 'value'),
            Input('qtd-lotes-completo', 'value'),           
            Input('dados-incc-antigo-completo', 'value'),
            Input('dados-incc-atual-completo', 'value'),
            Input('limpeza-camada-vegetal-completo', 'value'),
            Input('volume-corte-completo', 'value'),
            Input('volume-aterro-completo', 'value'),
            Input('volume-transporte-completo', 'value'),
            Input('diametro-300-completo', 'value'),
            Input('diametro-375-completo', 'value'),
            Input('diametro-450-completo', 'value'),
            Input('diametro-500-completo', 'value'),
            Input('diametro-600-completo', 'value'),
            Input('diametro-800-completo', 'value'),
            Input('diametro-1000-completo', 'value'),
            Input('base-bgs-completo', 'value'),
            Input('imprimacao-completo', 'value'),
            Input('pintura-completo', 'value'),
            Input('cbuq-completo', 'value'),
            Input('fechamento-perimetral-completo', 'value'),
            Input('meio-fio-completo', 'value'),
            Input('rede-eletrica-completo', 'value'),
            Input('rede-agua-completo', 'value'),
            Input('rede-esgoto-completo', 'value'),
            Input('supressao-vegetacao-completo', 'value'),
            Input('edificacoes-completo', 'value'),
            Input('quadra-society-completo', 'value'),
            Input('volume-corte-completo-custo', 'value'),
            Input('volume-aterro-completo-custo', 'value'),
            Input('volume-transporte-completo-custo', 'value'),
            Input('diametro-300-completo-custo', 'value'),
            Input('diametro-375-completo-custo', 'value'),
            Input('diametro-450-completo-custo', 'value'),
            Input('diametro-500-completo-custo', 'value'),
            Input('diametro-600-completo-custo', 'value'),
            Input('diametro-800-completo-custo', 'value'),
            Input('diametro-1000-completo-custo', 'value')
        ],
        State('shared-data-completo', 'data')
    )
    def save_data_completo(
        responsavel_relatorio_completo, info_geral_completo, id_loteamento_completo, localizacao_completo, revisao_completo, vgv_completo, area_total, 
        perimetro, area_lotes, area_viario, comprimento_viario, area_construida, 
        area_quadra, qtd_lotes_completo, dados_incc_antigo, dados_incc_atual, limpeza_camada_vegetal, volume_corte, volume_aterro, 
        volume_transporte, diametro_300, diametro_375, diametro_450, diametro_500, diametro_600, diametro_800, 
        diametro_1000, base_bgs, imprimacao, pintura, cbuq, fechamento_perimetral, meio_fio, rede_eletrica, 
        rede_agua, rede_esgoto, supressao_vegetacao, edificacoes, quadra_society, volume_corte_custo, 
        volume_aterro_custo, volume_transporte_custo, diametro_300_custo, diametro_375_custo, diametro_450_custo, 
        diametro_500_custo, diametro_600_custo, diametro_800_custo, diametro_1000_custo, current_data
    ):
        if current_data is None:
            current_data = {}

        current_data.update({
            'responsavel-relatorio-completo': responsavel_relatorio_completo,
            'info-geral-completo': info_geral_completo,
            'id-loteamento-completo': id_loteamento_completo,
            'localizacao-completo': localizacao_completo,
            'revisao-completo': revisao_completo,
            'vgv-completo': convert_to_float(vgv_completo),
            'area-total-completo': convert_to_float(area_total),
            'perimetro-completo': convert_to_float(perimetro),
            'area-lotes-completo': convert_to_float(area_lotes),
            'area-viario-completo': convert_to_float(area_viario),
            'comprimento-viario-completo': convert_to_float(comprimento_viario),
            'area-construida-completo': convert_to_float(area_construida),
            'area-quadra-completo': convert_to_float(area_quadra),
            'qtd-lotes-completo': convert_to_float(qtd_lotes_completo),
            'dados-incc-antigo-completo': convert_to_float(dados_incc_antigo),
            'dados-incc-atual-completo': convert_to_float(dados_incc_atual),
            'limpeza-camada-vegetal-completo': convert_to_float(limpeza_camada_vegetal),
            'volume-corte-completo': convert_to_float(volume_corte),
            'volume-aterro-completo': convert_to_float(volume_aterro),
            'volume-transporte-completo': convert_to_float(volume_transporte),
            'diametro-300-completo': convert_to_float(diametro_300),
            'diametro-375-completo': convert_to_float(diametro_375),
            'diametro-450-completo': convert_to_float(diametro_450),
            'diametro-500-completo': convert_to_float(diametro_500),
            'diametro-600-completo': convert_to_float(diametro_600),
            'diametro-800-completo': convert_to_float(diametro_800),
            'diametro-1000-completo': convert_to_float(diametro_1000),
            'base-bgs-completo': convert_to_float(base_bgs),
            'imprimacao-completo': convert_to_float(imprimacao),
            'pintura-completo': convert_to_float(pintura),
            'cbuq-completo': convert_to_float(cbuq),
            'fechamento-perimetral-completo': convert_to_float(fechamento_perimetral),
            'meio-fio-completo': convert_to_float(meio_fio),
            'rede-eletrica-completo': convert_to_float(rede_eletrica),
            'rede-agua-completo': convert_to_float(rede_agua),
            'rede-esgoto-completo': convert_to_float(rede_esgoto),
            'supressao-vegetacao-completo': convert_to_float(supressao_vegetacao),
            'edificacoes-completo': convert_to_float(edificacoes),
            'quadra-society-completo': convert_to_float(quadra_society),
            'volume-corte-completo-custo': convert_to_float(volume_corte_custo),
            'volume-aterro-completo-custo': convert_to_float(volume_aterro_custo),
            'volume-transporte-completo-custo': convert_to_float(volume_transporte_custo),
            'diametro-300-completo-custo': convert_to_float(diametro_300_custo),
            'diametro-375-completo-custo': convert_to_float(diametro_375_custo),
            'diametro-450-completo-custo': convert_to_float(diametro_450_custo),
            'diametro-500-completo-custo': convert_to_float(diametro_500_custo),
            'diametro-600-completo-custo': convert_to_float(diametro_600_custo),
            'diametro-800-completo-custo': convert_to_float(diametro_800_custo),
            'diametro-1000-completo-custo': convert_to_float(diametro_1000_custo),
        })
        return current_data

    # Callback para carregar dados no formulário Orçamento Completo ao acessar a página -------------------------
    @app.callback(
        [
            Output('responsavel-relatorio-completo', 'value'),
            Output('info-geral-completo', 'value'),
            Output('id-loteamento-completo', 'value'),
            Output('localizacao-completo', 'value'),
            Output('revisao-completo', 'value'),
            Output('vgv-completo', 'value'),
            Output('area-total-completo', 'value'),
            Output('perimetro-completo', 'value'),
            Output('area-lotes-completo', 'value'),
            Output('area-viario-completo', 'value'),
            Output('comprimento-viario-completo', 'value'),
            Output('area-construida-completo', 'value'),
            Output('area-quadra-completo', 'value'),
            Output('qtd-lotes-completo', 'value'),
            Output('dados-incc-antigo-completo', 'value'),
            Output('dados-incc-atual-completo', 'value'),
            Output('limpeza-camada-vegetal-completo', 'value'),
            Output('volume-corte-completo', 'value'),
            Output('volume-aterro-completo', 'value'),
            Output('volume-transporte-completo', 'value'),
            Output('diametro-300-completo', 'value'),
            Output('diametro-375-completo', 'value'),
            Output('diametro-450-completo', 'value'),
            Output('diametro-500-completo', 'value'),
            Output('diametro-600-completo', 'value'),
            Output('diametro-800-completo', 'value'),
            Output('diametro-1000-completo', 'value'),
            Output('base-bgs-completo', 'value'),
            Output('imprimacao-completo', 'value'),
            Output('pintura-completo', 'value'),
            Output('cbuq-completo', 'value'),
            Output('fechamento-perimetral-completo', 'value'),
            Output('meio-fio-completo', 'value'),
            Output('rede-eletrica-completo', 'value'),
            Output('rede-agua-completo', 'value'),
            Output('rede-esgoto-completo', 'value'),
            Output('supressao-vegetacao-completo', 'value'),
            Output('edificacoes-completo', 'value'),
            Output('quadra-society-completo', 'value'),
            Output('volume-corte-completo-custo', 'value'),
            Output('volume-aterro-completo-custo', 'value'),
            Output('volume-transporte-completo-custo', 'value'),
            Output('diametro-300-completo-custo', 'value'),
            Output('diametro-375-completo-custo', 'value'),
            Output('diametro-450-completo-custo', 'value'),
            Output('diametro-500-completo-custo', 'value'),
            Output('diametro-600-completo-custo', 'value'),
            Output('diametro-800-completo-custo', 'value'),
            Output('diametro-1000-completo-custo', 'value'),
        ],
        [
            Input('url', 'pathname')  # Atualiza quando a URL muda
        ],
        [
            State('shared-data-completo', 'data')
        ]
    )
    def load_data_completo(pathname, data):
        if pathname != '/orcamento-completo':
            raise PreventUpdate  
        if data is None:
            return [None] * 49  # Número de outputs (incluindo custos)
        return [
            data.get('responsavel_relatorio_completo', None),
            data.get('info_geral_completo', None),
            data.get('id-loteamento-completo', None),
            data.get('localizacao_completo', None),
            data.get('revisao_completo', None),
            convert_from_float(data.get('vgv-completo', 0)),
            convert_from_float(data.get('area-total-completo', 0)),
            convert_from_float(data.get('perimetro-completo', 0)),
            convert_from_float(data.get('area-lotes-completo', 0)),
            convert_from_float(data.get('area-viario-completo', 0)),
            convert_from_float(data.get('comprimento-viario-completo', 0)),
            convert_from_float(data.get('area-construida-completo', 0)),
            convert_from_float(data.get('area-quadra-completo', 0)),
            convert_from_float(data.get('qtd-lotes-completo', 0)),
            convert_from_float(data.get('dados-incc-antigo-completo', 0)),
            convert_from_float(data.get('dados-incc-atual-completo', 0)),
            convert_from_float(data.get('limpeza-camada-vegetal-completo', 0)),
            convert_from_float(data.get('volume-corte-completo', 0)),
            convert_from_float(data.get('volume-aterro-completo', 0)),
            convert_from_float(data.get('volume-transporte-completo', 0)),
            convert_from_float(data.get('diametro-300-completo', 0)),
            convert_from_float(data.get('diametro-375-completo', 0)),
            convert_from_float(data.get('diametro-450-completo', 0)),
            convert_from_float(data.get('diametro-500-completo', 0)),
            convert_from_float(data.get('diametro-600-completo', 0)),
            convert_from_float(data.get('diametro-800-completo', 0)),
            convert_from_float(data.get('diametro-1000-completo', 0)),
            convert_from_float(data.get('base-bgs-completo', 0)),
            convert_from_float(data.get('imprimacao-completo', 0)),
            convert_from_float(data.get('pintura-completo', 0)),
            convert_from_float(data.get('cbuq-completo', 0)),
            convert_from_float(data.get('fechamento-perimetral-completo', 0)),
            convert_from_float(data.get('meio-fio-completo', 0)),
            convert_from_float(data.get('rede-eletrica-completo', 0)),
            convert_from_float(data.get('rede-agua-completo', 0)),
            convert_from_float(data.get('rede-esgoto-completo', 0)),
            convert_from_float(data.get('supressao-vegetacao-completo', 0)),
            convert_from_float(data.get('edificacoes-completo', 0)),
            convert_from_float(data.get('quadra-society-completo', 0)),
            convert_from_float(data.get('volume-corte-completo-custo', 0)),
            convert_from_float(data.get('volume-aterro-completo-custo', 0)),
            convert_from_float(data.get('volume-transporte-completo-custo', 0)),
            convert_from_float(data.get('diametro-300-completo-custo', 0)),
            convert_from_float(data.get('diametro-375-completo-custo', 0)),
            convert_from_float(data.get('diametro-450-completo-custo', 0)),
            convert_from_float(data.get('diametro-500-completo-custo', 0)),
            convert_from_float(data.get('diametro-600-completo-custo', 0)),
            convert_from_float(data.get('diametro-800-completo-custo', 0)),
            convert_from_float(data.get('diametro-1000-completo-custo', 0)),
        ]

    # Callback para gerar o Relatório Completo -------------------------
    @app.callback(
        Output('url', 'pathname'),
        Input('generate-report-button-completo', 'n_clicks'),
        State('shared-data-completo', 'data')
    )
    def generate_complete_report(n_clicks, data):
        if n_clicks is None or n_clicks == 0:
            raise PreventUpdate
        if data is None:
            raise PreventUpdate
        return '/relatorio-completo'

    # Lista de IDs dos campos que serão limpos no Orçamento Completo
    FIELDS_TO_CLEAR_COMPLETO = [
        "responsavel-relatorio-completo",
        "info-geral-completo",
        "id-loteamento-completo",
        "localizacao-completo",
        "revisao-completo",
        "vgv-completo",
        "area-total-completo",
        "perimetro-completo",
        "area-lotes-completo",
        "area-viario-completo",
        "comprimento-viario-completo",
        "area-construida-completo",
        "area-quadra-completo",
        "qtd-lotes-completo",
        "dados-incc-antigo-completo",
        "dados-incc-atual-completo",
        "limpeza-camada-vegetal-completo",
        "volume-corte-completo",
        "volume-aterro-completo",
        "volume-transporte-completo",
        "diametro-300-completo",
        "diametro-375-completo",
        "diametro-450-completo",
        "diametro-500-completo",
        "diametro-600-completo",
        "diametro-800-completo",
        "diametro-1000-completo",
        "base-bgs-completo",
        "imprimacao-completo",
        "pintura-completo",
        "cbuq-completo",
        "fechamento-perimetral-completo",
        "meio-fio-completo",
        "rede-eletrica-completo",
        "rede-agua-completo",
        "rede-esgoto-completo",
        "supressao-vegetacao-completo",
        "edificacoes-completo",
        "quadra-society-completo",
        "volume-corte-completo-custo",
        "volume-aterro-completo-custo",
        "volume-transporte-completo-custo",
        "diametro-300-completo-custo",
        "diametro-375-completo-custo",
        "diametro-450-completo-custo",
        "diametro-500-completo-custo",
        "diametro-600-completo-custo",
        "diametro-800-completo-custo",
        "diametro-1000-completo-custo",
    ]

    # Callback para limpar o formulário Orçamento Completo -------------------------
    @app.callback(
        [Output(field_id, "value") for field_id in FIELDS_TO_CLEAR_COMPLETO] + [Output("shared-data-completo", "data")],
        Input("clear-data-button-completo", "n_clicks")
    )
    def clear_form_completo(n_clicks):
        if not n_clicks:
            raise PreventUpdate
        return [None] * len(FIELDS_TO_CLEAR_COMPLETO) + [None]


    # Callback para atualizar a tabela, gráficos e cards no Relatório Completo -------------------------
    @app.callback(
        [
            Output('results-table-completo', 'data'),
            Output('pyramid-chart-completo', 'figure'),
            Output('card-id-loteamento-completo', 'children'),
            Output('card-valor-total-completo', 'children'),
            Output('card-cc-fip-completo', 'children'),   
            Output('card-cc-at-completo', 'children'),
            Output('card-cc-ap-completo', 'children'),
            Output('card-cc-vgv-completo', 'children'),      
        ],
        Input('url', 'pathname'),
        State('shared-data-completo', 'data')
    )
    def update_results_table_and_graph(pathname, data):
        if pathname != '/relatorio-completo':
            raise PreventUpdate
        if data is None:
            return [], {}, "", "", "", "", "", ""

        def get_value(key):
            return data.get(key, 0.0)

        # >>> Extração dos valores de entrada <<<
        id_loteamento_completo = data.get('id-loteamento-completo', '')
        area_total = get_value('area-total-completo')
        area_lotes = get_value('area-lotes-completo')
        qtd_lotes_completo = get_value('qtd-lotes-completo')
        vgv = get_value('vgv-completo')  
        dados_incc_antigo = get_value('dados-incc-antigo-completo')
        dados_incc_atual = get_value('dados-incc-atual-completo')

        # Verificando se os valores do INCC são válidos
        if not dados_incc_antigo or dados_incc_antigo == 0:
            return [], {}, "", "Dados INCC Antigo não pode ser zero ou vazio.", "", "", ""
        if not dados_incc_atual or dados_incc_atual == 0:
            return [], {}, "", "Dados INCC Atual não pode ser zero ou vazio.", "", "", ""

        # CUSTOS UNITÁRIOS E ADICIONAIS
        perimetro = get_value('perimetro-completo')
        comprimento_viario = get_value('comprimento-viario-completo')
        area_viario = get_value('area-viario-completo')
        
        supressao_vegetacao = get_value('supressao-vegetacao-completo')
        edificacoes = get_value('edificacoes-completo')
        quadra_society = get_value('quadra-society-completo')
        fechamento_perimetral = get_value('fechamento-perimetral-completo')
        meio_fio = get_value('meio-fio-completo')
        rede_eletrica = get_value('rede-eletrica-completo')
        rede_agua = get_value('rede-agua-completo')
        rede_esgoto = get_value('rede-esgoto-completo')
        base_bgs = get_value('base-bgs-completo')
        imprimacao = get_value('imprimacao-completo')
        pintura = get_value('pintura-completo')
        cbuq = get_value('cbuq-completo')
        limpeza_camada_vegetal = get_value('limpeza-camada-vegetal-completo')
        # TERRAPLANAGEM
        volume_corte = get_value('volume-corte-completo')
        volume_aterro = get_value('volume-aterro-completo')
        volume_transporte = get_value('volume-transporte-completo')
        # CUSTOS ADICIONAIS
        volume_corte_custo = get_value('volume-corte-completo-custo')
        volume_aterro_custo = get_value('volume-aterro-completo-custo')
        volume_transporte_custo = get_value('volume-transporte-completo-custo')
        # DRENAGEM: COMPRIMENTOS e CUSTOS
        diametros = ['300', '375', '450', '500', '600', '800', '1000']
        diametro_comprimentos = [get_value(f'diametro-{d}-completo') for d in diametros]
        diametro_custos = [get_value(f'diametro-{d}-completo-custo') for d in diametros]

        # Cálculos para achar o VT
        vt1 = fechamento_perimetral * perimetro
        vt2 = meio_fio * (comprimento_viario * 2)
        vt3 = rede_eletrica * comprimento_viario
        vt4 = rede_agua * (comprimento_viario * 2)
        vt5 = sum(c * k for c, k in zip(diametro_comprimentos, diametro_custos))
        vt6 = rede_esgoto * comprimento_viario
        # Pavimentação
        vt7 = (area_viario * base_bgs * 0.21) + \
            (area_viario * imprimacao) + \
            (area_viario * pintura) + \
            ((area_viario * 1182 / 12312.48) * cbuq)
        # Terraplenagem
        vt8 = (limpeza_camada_vegetal * area_total) + \
            (volume_corte * volume_corte_custo) + \
            (volume_aterro * volume_aterro_custo) + \
            (volume_transporte * volume_transporte_custo)
        vt9 = edificacoes * get_value('area-construida-completo')
        vt10 = supressao_vegetacao * area_total
        vt11 = quadra_society * get_value('area-quadra-completo')

        # Cálculos para coluna VALOR TOTAL CORRIGIDO
        fator_correcao = dados_incc_atual / dados_incc_antigo
        ct1 = vt1 * fator_correcao
        ct2 = vt2 * fator_correcao
        ct3 = vt3 * fator_correcao
        ct4 = vt4 * fator_correcao
        ct5 = vt5 * fator_correcao
        ct6 = vt6 * fator_correcao
        ct7 = vt7 * fator_correcao
        ct8 = vt8 * fator_correcao
        ct9 = vt9 * fator_correcao
        ct10 = vt10 * fator_correcao
        ct11 = vt11 * fator_correcao

        # Dados da tabela
        table_data = [
            {"item": "Fechamento Perimetral", "custo_unitario": convert_from_float(fechamento_perimetral), "quantitativo": convert_from_float(perimetro), "valor_total_corrigido": convert_from_float(ct1)},                                          
            {"item": "Meio fio", "custo_unitario": convert_from_float(meio_fio), "quantitativo": convert_from_float(comprimento_viario * 2), "valor_total_corrigido": convert_from_float(ct2)},                            
            {"item": "Rede de Distribuição Elétrica", "custo_unitario": convert_from_float(rede_eletrica), "quantitativo": convert_from_float(comprimento_viario), "valor_total_corrigido": convert_from_float(ct3)},     
            {"item": "Rede de Abastecimento de Água", "custo_unitario": convert_from_float(rede_agua), "quantitativo": convert_from_float(comprimento_viario * 2), "valor_total_corrigido": convert_from_float(ct4)},     
            {"item": "Rede de Drenagem", "custo_unitario": convert_from_float(sum(diametro_custos) / len(diametro_custos) if diametro_custos else 0), "quantitativo": convert_from_float(sum(diametro_comprimentos)), "valor_total_corrigido": convert_from_float(ct5)},
            {"item": "Rede de Coleta de Esgoto", "custo_unitario": convert_from_float(rede_esgoto), "quantitativo": convert_from_float(comprimento_viario), "valor_total_corrigido": convert_from_float(ct6)},      
            {"item": "Pavimentação", "custo_unitario": convert_from_float((base_bgs * 0.21) + imprimacao + pintura + ((1182 / 12312.48) * cbuq)), "quantitativo": convert_from_float(area_viario), "valor_total_corrigido": convert_from_float(ct7)},
            {"item": "Terraplenagem", "custo_unitario": convert_from_float((limpeza_camada_vegetal + volume_corte_custo + volume_aterro_custo + volume_transporte_custo) / 4), "quantitativo": convert_from_float(area_total), "valor_total_corrigido": convert_from_float(ct8)},                     
            {"item": "Edificações", "custo_unitario": convert_from_float(edificacoes), "quantitativo": convert_from_float(get_value('area-construida-completo')), "valor_total_corrigido": convert_from_float(ct9)},
            {"item": "Supressão de Vegetação", "custo_unitario": convert_from_float(supressao_vegetacao), "quantitativo": convert_from_float(area_total), "valor_total_corrigido": convert_from_float(ct10)},
            {"item": "Quadra Society", "custo_unitario": convert_from_float(quadra_society), "quantitativo": convert_from_float(get_value('area-quadra-completo')), "valor_total_corrigido": convert_from_float(ct11)},
        ]

        # >>> Subtotal e Valor Total (com acréscimo de 20%) <<<
        subtotal = sum([ct1, ct2, ct3, ct4, ct5, ct6, ct7, ct8, ct9, ct10, ct11])
        valor_total_orcamento = subtotal / 0.80

        # >>> Atualizar cartões <<<
        card_id_loteamento = id_loteamento_completo
        card_sub_total = f"R$ {convert_from_float(subtotal)}"
        card_valor_total = f"R$ {convert_from_float(valor_total_orcamento)}"

        # Cálculo do CC/FIP
        cc_fip_completo = valor_total_orcamento / qtd_lotes_completo if qtd_lotes_completo else 0.0
        card_cc_fip_completo = f"R$ {convert_from_float(cc_fip_completo)}/m²"

        # CC/AT
        cc_at = valor_total_orcamento / area_total if area_total else 0
        card_cc_at = f"R$ {convert_from_float(cc_at)}/m²"

        # CC/AP
        cc_ap = valor_total_orcamento / area_lotes if area_lotes else 0
        card_cc_ap = f"R$ {convert_from_float(cc_ap)}/m²"

        # CC/VGV
        if vgv and vgv != 0 and area_lotes and area_lotes != 0 and qtd_lotes_completo and qtd_lotes_completo != 0:
            cc_vgv_value = valor_total_orcamento / (area_lotes * vgv * qtd_lotes_completo)
            card_cc_vgv = f"{convert_from_float(cc_vgv_value)}%"
        else:
            cc_vgv_value = 0.0
            card_cc_vgv = "0,00"

        # ************************ Gráfico *************************
        
        itens = [row["item"] for row in table_data]
        valores_float = [convert_to_float(row["valor_total_corrigido"]) for row in table_data]

        total_valores = sum(valores_float)
        percentuais = [(val / total_valores) * 100 if total_valores != 0 else 0 for val in valores_float]

        data_for_chart = sorted(zip(percentuais, itens, valores_float), reverse=True)
        percentuais_ordenados, itens_ordenados, valores_ordenados = zip(*data_for_chart)

        # Paleta de cores (tons de azul)
        custom_blue_colors = [
            '#499EB5', '#346F7A', '#345F6C', '#2D5260',
            '#264552', '#1F3844'
        ]
        from matplotlib.colors import LinearSegmentedColormap
        cmap = LinearSegmentedColormap.from_list('custom_blue', custom_blue_colors)

        max_valor = max(valores_ordenados)
        min_valor = min(valores_ordenados)
        valor_range = max_valor - min_valor if max_valor != min_valor else 1
        norm_valores = [(v - min_valor) / valor_range for v in valores_ordenados]
        cores_mapeadas = [cmap(norm) for norm in norm_valores]

        cores_hex = [
            '#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255))
            for r, g, b, _ in cores_mapeadas
        ]

        fig = go.Figure(
            data=[
                go.Bar(
                    x=percentuais_ordenados,
                    y=itens_ordenados,
                    orientation='h',
                    text=[f"{p:.2f}%" for p in percentuais_ordenados],
                    textposition='inside',
                    textfont=dict(family="Arial", size=14, color="white"),
                    marker=dict(
                        color=cores_hex,
                        line=dict(width=1, color="#345F6C"),  # Borda azul-escuro
                    ),
                    hovertemplate=(
                        "<b>%{y}</b><br>"
                        "Percentual: %{x:.2f}%<br>"
                        "Valor: R$ %{customdata[0]:,.2f}<extra></extra>"
                    ),
                    customdata=[[val] for val in valores_ordenados],
                )
            ]
        )

        fig.update_layout(
            title=dict(
                text="Participação Percentual dos Serviços",
                font=dict(size=24, family="Montserrat", color="#345F6C"),
                x=0.5,
                xanchor="center",
            ),
            xaxis=dict(
                title=dict(text="Percentual (%)", font=dict(size=16, family="Montserrat")),  
                tickfont=dict(size=14, family="Montserrat"),
                gridcolor="rgba(200,200,200,0.5)",
                zeroline=False,
            ),
            yaxis=dict(
                title=dict(text="Serviços", font=dict(size=16, family="Montserrat")),  
                tickfont=dict(size=14, family="Montserrat"),
                categoryorder="total ascending",
            ),
            paper_bgcolor="white",
            plot_bgcolor="white",
            margin=dict(l=120, r=40, t=80, b=50),
            height=600,
        )


        return (
            table_data,
            fig,
            card_id_loteamento,
            card_valor_total,
            card_cc_fip_completo,      
            card_cc_at,
            card_cc_ap,
            card_cc_vgv          
        )


    # ====================================================================================
    # Callback para exportar a tabela para Excel 
    # ====================================================================================
    @app.callback(
        Output("download-dataframe-xlsx-completo", "data"),
        Input("export-button-completo", "n_clicks"),
        State("results-table-completo", "data"),
        prevent_initial_call=True
    )
    def export_table_to_excel(n_clicks, table_data):
        if n_clicks is None or not table_data:
            raise PreventUpdate

        # Converter os dados da tabela para DataFrame
        df = pd.DataFrame(table_data)

        # Retornar o DataFrame para download no formato Excel
        return dcc.send_data_frame(
            df.to_excel, "relatorio_completo.xlsx", sheet_name="Relatório Completo", index=False                     
        )

    # ====================================================================================
    # CALLBACK PARA GERAR PDF (Orçamento Simplificado)
    # ====================================================================================
    @app.callback(
        Output('download-pdf-completo', 'data'),
        [Input('generate-pdf-button-completo', 'n_clicks')],
        [
            State('results-table-completo', 'data'),
            State('card-id-loteamento-completo', 'children'),
            State('card-valor-total-completo', 'children'),
            State('card-cc-fip-completo', 'children'),
            State('card-cc-at-completo', 'children'),
            State('card-cc-ap-completo', 'children'),
            State('card-cc-vgv-completo', 'children'),
            State('shared-data-completo', 'data')
        ],
        prevent_initial_call=True
        )
    def generate_pdf_completo(
            n_clicks,
            table_data,
            id_loteamento,
            valor_total_orcamento,
            cc_fip_completo,
            cc_at,
            cc_ap,
            cc_vgv_value,
            input_data
        ):
            if n_clicks is None or not table_data:
                raise PreventUpdate

            try:
                # -----------------------------------------------------------------------------
                # Configurações iniciais de PDF e cores
                # -----------------------------------------------------------------------------
                buffer = io.BytesIO()
                pdf = canvas.Canvas(buffer, pagesize=landscape(letter))
                pdf.setTitle("Orçamento Completo")

                pagina_largura, pagina_altura = landscape(letter)

                # -----------------------------------------------------------------------------
                # PÁGINA 1 (Capa)
                # -----------------------------------------------------------------------------
                pdf.setFillColor(HexColor("#3d5462"))
                pdf.rect(0, 0, pagina_largura, pagina_altura, fill=1)  # fundo

                pdf.setFillColor(HexColor("#FFFFFF"))
                pdf.setFont("Helvetica-Bold", 30)
                titulo_capa = "Orçamento Paramétrico"
                titulo_largura = pdf.stringWidth(titulo_capa, "Helvetica-Bold", 26)
                pdf.drawString(
                    (pagina_largura - titulo_largura) / 2,
                    pagina_altura - 120,
                    titulo_capa
                )

                # Inserir logo na capa
                try:
                    capa_logo = "assets/logoor2.png"
                    max_width = 300
                    max_height = 130

                    from PIL import Image
                    with Image.open(capa_logo) as img:
                        original_width, original_height = img.size
                        aspect_ratio = original_width / original_height

                    # Ajuste proporcional
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

                    pdf.drawImage(
                        capa_logo,
                        x_center,
                        y_center,
                        width=new_width,
                        height=new_height,
                        mask='auto'
                    )
                except Exception as e:
                    print(f"Erro ao inserir a logo de capa: {e}")

                # Texto info-geral-completo
                pdf.setFont("Helvetica", 16)
                pdf.setFillColor(HexColor("#FFFFFF"))
                info_geral_texto = input_data.get('info-geral-completo', 'Nenhuma informação disponível')

                y_texto = (y_center - 60)
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

                # Responsável (canto inferior esquerdo)
                pdf.setFont("Helvetica", 16)
                responsavel_texto = input_data.get('responsavel-relatorio-completo', 'Não informado')
                pdf.drawString(50, 50, f"Responsável: {responsavel_texto}")

                # Data (canto inferior direito)
                data_atual = datetime.now().strftime("%d/%m/%Y")
                data_text_w = pdf.stringWidth(data_atual, "Helvetica", 16)
                pdf.drawString(pagina_largura - data_text_w - 50, 50, data_atual)

                pdf.showPage()

                # -----------------------------------------------------------------------------
                # PÁGINA 2 - Resultados + Dados do Orçamento Completo (Atualizado)
                # -----------------------------------------------------------------------------
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
                titulo_texto = "Orçamento Completo"
                titulo_largura = pdf.stringWidth(titulo_texto, "Helvetica-Bold", 16)
                titulo_y = pagina_altura - bar_height + (bar_height - 16) / 2
                pdf.setFillColor(HexColor("#FFFFFF"))
                pdf.drawString((pagina_largura - titulo_largura) / 2, titulo_y, titulo_texto)

                # Definir y_position para o conteúdo abaixo da barra
                y_position = pagina_altura - bar_height - 40


                # 1) Exibir Resultados
                pdf.setFillColor(HexColor("#4B2C20"))  
                pdf.setFont("Helvetica-Bold", 10)
                pdf.drawString(50, y_position, "Resultados:")
                pdf.setFillColor(HexColor("#000000"))
                y_position -= 15

                resultados = [
                    ("Valor Total do Orçamento", valor_total_orcamento),
                    ("CC/FIP", cc_fip_completo),
                    ("CC/AT", cc_at),
                    ("CC/AP", cc_ap),
                    ("CC/VGV", cc_vgv_value),
                ]
                for label, value in resultados:
                    pdf.setFont("Helvetica-Bold", 8)
                    pdf.drawString(50, y_position, f"{label}: ")
                    offset = pdf.stringWidth(f"{label}: ", "Helvetica-Bold", 8)
                    pdf.setFont("Helvetica", 8)
                    pdf.drawString(50 + offset, y_position, str(value))
                    y_position -= 16

                # Linha laranja entre Resultados e Informações Gerais
                pdf.setStrokeColor(HexColor("#FFA500"))
                pdf.setLineWidth(1)
                pdf.line(50, y_position, pagina_largura - 50, y_position)
                pdf.setStrokeColor(HexColor("#000000"))
                y_position -= 20  # Espaço extra após a linha

                # 2) Exibir o campo "info-geral-completo"
                pdf.setFillColor(HexColor("#283747"))  # Azul Petróleo Profundo
                info_geral = input_data.get('info-geral-completo', '')
                pdf.setFont("Helvetica-Bold", 10)
                pdf.drawString(50, y_position, "Informações Gerais:")
                pdf.setFillColor(HexColor("#000000"))
                y_position -= 12
                pdf.setFont("Helvetica", 8)
                text_object = pdf.beginText(50, y_position)
                wrapped_lines = textwrap.wrap(info_geral, width=180)
                for line in wrapped_lines:
                    text_object.textLine(line)
                    y_position -= 12
                    if y_position < 50:
                        pdf.drawText(text_object)
                        pdf.showPage()
                        y_position = pagina_altura - 50
                        pdf.setFont("Helvetica", 8)
                        text_object = pdf.beginText(50, y_position)
                pdf.drawText(text_object)
                y_position -= 15

                # Linha fina laranja entre Informações Gerais e Dados do Projeto
                pdf.setStrokeColor(HexColor("#FFA500"))
                pdf.setLineWidth(1)
                pdf.line(50, y_position, pagina_largura - 50, y_position)
                pdf.setStrokeColor(HexColor("#000000"))
                y_position -= 20

                # --------------------------------------------------
                # Definição dos rótulos para os inputs
                # --------------------------------------------------
                input_labels = {
                    'info-geral-completo': 'Informações Gerais',
                    'id-loteamento-completo': 'ID Condomínios Horizontais',
                    'localizacao-completo': 'Localização',
                    'revisao-completo': 'Revisão',
                    'area-total-completo': 'Área Total do Terreno (m²)',
                    'perimetro-completo': 'Perímetro do Terreno (m)',
                    'area-lotes-completo': 'Área dos Lotes (m²)',
                    'area-viario-completo': 'Área do Viário (m²)',
                    'comprimento-viario-completo': 'Comprimento do Viário (m)',
                    'area-construida-completo': 'Área Construída (m²)',
                    'area-quadra-completo': 'Área da Quadra (m²)',
                    'dados-incc-antigo-completo': 'Dados INCC Antigo',
                    'dados-incc-atual-completo': 'Dados INCC Atual',
                    'volume-corte-completo': 'Volume de Corte (m³)',
                    'volume-aterro-completo': 'Volume de Aterro (m³)',
                    'volume-transporte-completo': 'Volume de Transporte Interno (m³)',
                    'fechamento-perimetral-completo': 'Fechamento Perimetral (cc/m)',
                    'meio-fio-completo': 'Meio Fio (cc/m)',
                    'diametro-300-completo': 'Diâmetro 300 mm',
                    'diametro-375-completo': 'Diâmetro 375 mm',
                    'diametro-450-completo': 'Diâmetro 450 mm',
                    'diametro-500-completo': 'Diâmetro 500 mm',
                    'diametro-600-completo': 'Diâmetro 600 mm',
                    'diametro-800-completo': 'Diâmetro 800 mm',
                    'diametro-1000-completo': 'Diâmetro 1000 mm',
                    'rede-eletrica-completo': 'Rede Distribuição Elétrica (cc/m)',
                    'rede-agua-completo': 'Rede Abastecimento de Água (cc/m)',
                    'rede-esgoto-completo': 'Rede Coleta de Esgoto (cc/m)',
                    'supressao-vegetacao-completo': 'Supressão de Vegetação (cc/m²)',
                    'edificacoes-completo': 'Edificações (cc/m²)',
                    'quadra-society-completo': 'Quadra Society (cc/m²)',
                    'base-bgs-completo': 'Base em BGS (cc/m³)',
                    'imprimacao-completo': 'Imprimação (cc/m²)',
                    'pintura-completo': 'Pintura (cc/m²)',
                    'cbuq-completo': 'CBUQ (cc/t)',
                    'limpeza-camada-vegetal-completo': 'Limpeza da Camada Vegetal (cc/m²)',
                    'volume-corte-completo-custo': 'Custo Volume de Corte (cc/m³)',
                    'volume-aterro-completo-custo': 'Custo Volume de Aterro (cc/m³)',
                    'volume-transporte-completo-custo': 'Custo Volume de Transp. Interno (cc/m³)',
                    'diametro-300-completo-custo': 'Custo Diâmetro 300 mm (cc/m)',
                    'diametro-375-completo-custo': 'Custo Diâmetro 375 mm (cc/m)',
                    'diametro-450-completo-custo': 'Custo Diâmetro 450 mm (cc/m)',
                    'diametro-500-completo-custo': 'Custo Diâmetro 500 mm (cc/m)',
                    'diametro-600-completo-custo': 'Custo Diâmetro 600 mm (cc/m)',
                    'diametro-800-completo-custo': 'Custo Diâmetro 800 mm (cc/m)',
                    'diametro-1000-completo-custo': 'Custo Diâmetro 1000 mm (cc/m)',
                }

                # --------------------------------------------------
                # Seção: Dados do Projeto (24 itens)
                # --------------------------------------------------
                dados_projeto_keys = [
                    'id-loteamento-completo',
                    'localizacao-completo',
                    'revisao-completo',
                    'area-total-completo',
                    'perimetro-completo',
                    'area-lotes-completo',
                    'area-viario-completo',
                    'comprimento-viario-completo',
                    'area-construida-completo',
                    'area-quadra-completo',
                    'dados-incc-antigo-completo',
                    'dados-incc-atual-completo',
                    'volume-corte-completo',
                    'volume-aterro-completo',
                    'volume-transporte-completo',
                    'fechamento-perimetral-completo',
                    'meio-fio-completo',
                    'diametro-300-completo',
                    'diametro-375-completo',
                    'diametro-450-completo',
                    'diametro-500-completo',
                    'diametro-600-completo',
                    'diametro-800-completo',
                    'diametro-1000-completo'
                ]

                x_positions = [50, 280, 550]
                n_cols = 3
                row_height = 16
                n_rows = (len(dados_projeto_keys) + n_cols - 1) // n_cols
                pdf.setFillColor(HexColor("#2E5633"))
                pdf.setFont("Helvetica-Bold", 10)
                pdf.drawString(50, y_position, "Dados do Projeto:")
                pdf.setFillColor(HexColor("#000000"))
                y_position -= 15

                for row in range(n_rows):
                    for col in range(n_cols):
                        index = row * n_cols + col
                        if index < len(dados_projeto_keys):
                            key = dados_projeto_keys[index]
                            label = input_labels.get(key, key)
                            if key.endswith('-completo-custo'):
                                label = label.replace("Custo ", "")
                            valor = input_data.get(key, '')
                            if isinstance(valor, float):
                                valor_str = convert_from_float(valor)
                            else:
                                valor_str = str(valor)
                            pdf.setFont("Helvetica-Bold", 8)
                            pdf.drawString(x_positions[col], y_position - (row * row_height), f"{label}: ")
                            offset = pdf.stringWidth(f"{label}: ", "Helvetica-Bold", 8)
                            pdf.setFont("Helvetica", 8)
                            pdf.drawString(x_positions[col] + offset, y_position - (row * row_height), valor_str)
                y_position -= n_rows * row_height + 10

                # Linha fina laranja entre Dados do Projeto e Custos Unitário
                pdf.setStrokeColor(HexColor("#FFA500"))
                pdf.setLineWidth(1)
                pdf.line(50, y_position, pagina_largura - 50, y_position)
                pdf.setStrokeColor(HexColor("#000000"))
                y_position -= 20

                # --------------------------------------------------
                # Seção: Custos Unitário (23 itens)
                # --------------------------------------------------
                custo_unitario_keys = [
                    'fechamento-perimetral-completo',
                    'meio-fio-completo',
                    'rede-eletrica-completo',
                    'rede-agua-completo',
                    'rede-esgoto-completo',
                    'supressao-vegetacao-completo',
                    'edificacoes-completo',
                    'quadra-society-completo',
                    'base-bgs-completo',
                    'imprimacao-completo',
                    'pintura-completo',
                    'cbuq-completo',
                    'limpeza-camada-vegetal-completo',
                    'volume-corte-completo-custo',
                    'volume-aterro-completo-custo',
                    'volume-transporte-completo-custo',
                    'diametro-300-completo-custo',
                    'diametro-375-completo-custo',
                    'diametro-450-completo-custo',
                    'diametro-500-completo-custo',
                    'diametro-600-completo-custo',
                    'diametro-800-completo-custo',
                    'diametro-1000-completo-custo'
                ]

                n_cols = 3
                row_height = 16
                n_rows = (len(custo_unitario_keys) + n_cols - 1) // n_cols
                pdf.setFillColor(HexColor("#1F3A52"))
                pdf.setFont("Helvetica-Bold", 10)
                pdf.drawString(50, y_position, "Custo Unitário:")
                pdf.setFillColor(HexColor("#000000"))
                y_position -= 15

                for row in range(n_rows):
                    for col in range(n_cols):
                        index = row * n_cols + col
                        if index < len(custo_unitario_keys):
                            key = custo_unitario_keys[index]
                            label = input_labels.get(key, key)
                            valor = input_data.get(key, '')

                            try:
                                valor = float(valor)
                                valor_str = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                            except ValueError:
                                valor_str = str(valor)

                            pdf.setFont("Helvetica-Bold", 8)
                            pdf.drawString(x_positions[col], y_position - (row * row_height), f"{label}: ")
                            offset = pdf.stringWidth(f"{label}: ", "Helvetica-Bold", 8)
                            pdf.setFont("Helvetica", 8)
                            pdf.drawString(x_positions[col] + offset, y_position - (row * row_height), valor_str)
                y_position -= n_rows * row_height

                # Encerrar PÁGINA 2
                pdf.showPage()


                # -----------------------------------------------------------------------------
                # PÁGINA 3 - Tabela (Resultados)
                # -----------------------------------------------------------------------------
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
                titulo_texto = "Orçamento Completo"
                titulo_largura = pdf.stringWidth(titulo_texto, "Helvetica-Bold", 16)
                titulo_y = pagina_altura - bar_height + (bar_height - 16) / 2
                pdf.setFillColor(HexColor("#FFFFFF"))
                pdf.drawString((pagina_largura - titulo_largura) / 2, titulo_y, titulo_texto)

                # Definir y_position para o conteúdo abaixo da barra
                y_position = pagina_altura - bar_height - 40

                # Seção "Custo por Item de Execução"
                pdf.setFillColor(HexColor("#2D4159")) 
                pdf.setFont("Helvetica-Bold", 12)
                pdf.drawString(50, y_position, "Custo por Item de Execução: ")
                pdf.setFillColor(HexColor("#000000"))
                y_position -= 25


                # Cabeçalhos da tabela
                pdf.setFillColor(HexColor("#4B2C20"))  # Marrom Terra Profundo
                pdf.setFont("Helvetica-Bold", 10)
                headers = ["Item", "Valor Total Corrigido"]
                x_positions_table = [50, 250]  
                for i, header in enumerate(headers):
                    pdf.drawString(x_positions_table[i], y_position, header)
                y_position -= 20  
                pdf.setFillColor(HexColor("#000000"))

                pdf.setFont("Helvetica", 9)
                row_height = 18  

                total_valor_completo = 0  # Inicializa o total
                
                
                for row in table_data:
                    item_name = row.get('item', '')
                    valor_corrigido = convert_to_float(row.get('valor_total_corrigido', 0.0))
                    valor_str = f"R$ {valor_corrigido:.2f}".replace('.', ',')
                    total_valor_completo += valor_corrigido  # Soma ao total

                    pdf.setFont("Helvetica-Bold", 8)
                    pdf.drawString(x_positions_table[0], y_position, str(item_name))

                    pdf.setFont("Helvetica", 8)
                    pdf.drawString(x_positions_table[1], y_position, valor_str)

                    y_position -= row_height  # Altura entre os itens

                    if y_position < 50:
                        pdf.showPage()
                        y_position = pagina_altura - 50
                        pdf.setFont("Helvetica", 8)

                # Cálculo do subtotal (20% do total)
                subtotal_valor_corrigido_completo = total_valor_completo * 0.2

                # Inserir linha separadora antes do subtotal e total
                pdf.setStrokeColor(HexColor("#FF9999"))  # Vermelho
                pdf.setLineWidth(1)
                pdf.line(50, y_position, pagina_largura - 450, y_position)
                pdf.setStrokeColor(HexColor("#000000"))
                y_position -= 15 

                # Exibir o subtotal
                pdf.setFont("Helvetica-Bold", 9)
                pdf.drawString(x_positions_table[0], y_position, "Serviços Complementares (20%):")
                pdf.setFont("Helvetica-Bold", 9)
                pdf.drawString(x_positions_table[1], y_position, f"R$ {convert_from_float(subtotal_valor_corrigido_completo)}")
                y_position -= 10

                # Inserir linha vermelha entre o subtotal e o total
                pdf.setStrokeColor(HexColor("#FFA500"))  # Laranja
                pdf.setLineWidth(0.5)
                pdf.line(50, y_position, pagina_largura - 450, y_position)
                pdf.setStrokeColor(HexColor("#000000"))
                y_position -= 15  

                # Exibir o total
                pdf.setFont("Helvetica-Bold", 9)
                pdf.drawString(x_positions_table[0], y_position, "Total:")
                pdf.setFont("Helvetica-Bold", 9)
                pdf.drawString(x_positions_table[1], y_position, f"R$ {convert_from_float(total_valor_completo)}")

                pdf.showPage()

                # --------------------------------------------------------------------------------
                # PÁGINA 4 - Gráfico (Participação Percentual dos Serviços)
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
                data_para_grafico = []
                area_comuns_valor = 0
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

                # Removendo a borda do gráfico
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
                # PÁGINA 5 - Gráfico (Custo de Construção)
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
                titulo_grafico = "Gráfico de Custo de Construção"
                titulo_largura = pdf.stringWidth(titulo_grafico, "Helvetica-Bold", 16)
                titulo_y = pagina_altura - bar_height + (bar_height - 16) / 2
                pdf.setFillColor(HexColor("#FFFFFF"))
                pdf.drawString((pagina_largura - titulo_largura) / 2, titulo_y, titulo_grafico)

                # Definir a posição para iniciar o conteúdo abaixo da barra
                y_position = pagina_altura - bar_height - 40

                def to_float(valor_str):
                    try:
                        if not isinstance(valor_str, str):
                            return float(valor_str)
                        valor_str = re.sub(r"[^\d,\.]", "", valor_str)
                        valor_str = valor_str.replace(".", "").replace(",", ".")
                        return float(valor_str)
                    except Exception as e:
                        return 0.0

                # Extração dos valores dos Resultados 
                cc_fip_val = to_float(cc_fip_completo)
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
                        xy=(bar.get_x() + bar.get_width()/2, altura),
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
                    pdf.drawImage(tmpfile.name, x=grafico_x, y=grafico_y,
                                width=grafico_width, height=grafico_height, mask='auto')
                pdf.showPage()


                pdf.save()
                buffer.seek(0)

                return dcc.send_bytes(buffer.getvalue(), filename="relatorio_completo.pdf")

            except Exception as e:
                print(f"Erro ao gerar o PDF: {e}")
                raise PreventUpdate
