# callbacks_completo

import matplotlib
matplotlib.use('Agg')  # Define o backend não interativo
import io
import tempfile
import matplotlib.pyplot as plt
import textwrap
import plotly.graph_objs as go
import pandas as pd
import datetime

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
            # Remove todos os pontos (separadores de milhares) e troca a vírgula pelo ponto como separador decimal
            value = value.replace('.', '').replace(',', '.')
        return float(value)
    except (ValueError, TypeError):
        return 0.0  # Retorna 0.0 se a conversão falhar

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

    # Callback para salvar dados do formulário Orçamento Completo em dcc.Store -------------------------
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

        # Retorna None para cada campo do formulário e redefine o dcc.Store
        return [None] * len(FIELDS_TO_CLEAR_COMPLETO) + [None]


    # Callback para atualizar a tabela, gráficos e cards no Relatório Completo -------------------------
    @app.callback(
        [
            Output('results-table-completo', 'data'),
            Output('pyramid-chart-completo', 'figure'),
            Output('card-id-loteamento-completo', 'children'),
            Output('card-valor-total-completo', 'children'),
            Output('card-sub-total-completo', 'children'),   
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
            # Retorna valores vazios para todos os outputs (8 no total)
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
            return [], {}, "", "Erro: 'Dados INCC Antigo' não pode ser zero ou vazio.", "", "", "", ""
        if not dados_incc_atual or dados_incc_atual == 0:
            return [], {}, "", "Erro: 'Dados INCC Atual' não pode ser zero ou vazio.", "", "", "", ""

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

        # Cálculos para os valores totais
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

        # Cálculos para valores corrigidos (VALOR TOTAL)
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
            {"item": "Fechamento Perimetral", "custo_unitario": convert_from_float(fechamento_perimetral), "quantitativo": convert_from_float(perimetro), "valor_total_corrigido": convert_from_float(vt1)},                                          
            {"item": "Meio fio", "custo_unitario": convert_from_float(meio_fio), "quantitativo": convert_from_float(comprimento_viario * 2), "valor_total_corrigido": convert_from_float(vt2)},                            
            {"item": "Rede de Distribuição Elétrica", "custo_unitario": convert_from_float(rede_eletrica), "quantitativo": convert_from_float(comprimento_viario), "valor_total_corrigido": convert_from_float(vt3)},     
            {"item": "Rede de Abastecimento de Água", "custo_unitario": convert_from_float(rede_agua), "quantitativo": convert_from_float(comprimento_viario * 2), "valor_total_corrigido": convert_from_float(vt4)},     
            {"item": "Rede de Drenagem", "custo_unitario": convert_from_float(sum(diametro_custos) / len(diametro_custos) if diametro_custos else 0), "quantitativo": convert_from_float(sum(diametro_comprimentos)), "valor_total_corrigido": convert_from_float(vt5)},
            {"item": "Rede de Coleta de Esgoto", "custo_unitario": convert_from_float(rede_esgoto), "quantitativo": convert_from_float(comprimento_viario), "valor_total_corrigido": convert_from_float(vt6)},      
            {"item": "Pavimentação", "custo_unitario": convert_from_float((base_bgs * 0.21) + imprimacao + pintura + ((1182 / 12312.48) * cbuq)), "quantitativo": convert_from_float(area_viario), "valor_total_corrigido": convert_from_float(vt7)},
            {"item": "Terraplenagem", "custo_unitario": convert_from_float((limpeza_camada_vegetal + volume_corte_custo + volume_aterro_custo + volume_transporte_custo) / 4), "quantitativo": convert_from_float(area_total), "valor_total_corrigido": convert_from_float(vt8)},                     
            {"item": "Edificações", "custo_unitario": convert_from_float(edificacoes), "quantitativo": convert_from_float(get_value('area-construida-completo')), "valor_total_corrigido": convert_from_float(vt9)},
            {"item": "Supressão de Vegetação", "custo_unitario": convert_from_float(supressao_vegetacao), "quantitativo": convert_from_float(area_total), "valor_total_corrigido": convert_from_float(vt10)},
            {"item": "Quadra Society", "custo_unitario": convert_from_float(quadra_society), "quantitativo": convert_from_float(get_value('area-quadra-completo')), "valor_total_corrigido": convert_from_float(vt11)},
        ]


        # >>> Subtotal e Valor Total (com acréscimo de 20%) <<<
        subtotal = sum([ct1, ct2, ct3, ct4, ct5, ct6, ct7, ct8, ct9, ct10, ct11])
        valor_total_orcamento = subtotal / 0.80

        # >>> Atualizar cartões <<<
        card_id_loteamento = id_loteamento_completo
        card_sub_total = f"R$ {convert_from_float(subtotal)}"
        card_valor_total = f"R$ {convert_from_float(valor_total_orcamento)}"

        # CC/AT
        cc_at = valor_total_orcamento / area_total if area_total else 0
        card_cc_at = f"R$ {convert_from_float(cc_at)}/m²"

        # CC/AP
        cc_ap = valor_total_orcamento / area_lotes if area_lotes else 0
        card_cc_ap = f"R$ {convert_from_float(cc_ap)}/m²"

        # CC/VGV
        if vgv and vgv != 0 and area_lotes and area_lotes != 0 and qtd_lotes_completo and qtd_lotes_completo != 0:
            cc_vgv_value = valor_total_orcamento / (area_lotes * vgv * qtd_lotes_completo)
            card_cc_vgv = f"{convert_from_float(cc_vgv_value)}"
        else:
            cc_vgv_value = 0.0
            card_cc_vgv = "0,00"

        # *************** Gráfico *******************
        
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
            card_sub_total,      
            card_cc_at,
            card_cc_ap,
            card_cc_vgv          
        )



    # Callback para exportar a tabela para Excel
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
            df.to_excel, 
            "relatorio_completo.xlsx", 
            sheet_name="Relatório Completo", 
            index=False
        )

    # Callback para gerar PDF 
    @app.callback(
        Output('download-pdf-completo', 'data'),
        [Input('generate-pdf-button-completo', 'n_clicks')],
        [
            State('results-table-completo', 'data'),
            State('card-id-loteamento-completo', 'children'),
            State('card-valor-total-completo', 'children'),
            State('card-sub-total-completo', 'children'),
            State('card-cc-at-completo', 'children'),
            State('card-cc-ap-completo', 'children'),
            State('card-cc-vgv-completo', 'children'),
            State('shared-data-completo', 'data')
        ],
        prevent_initial_call=True
    )
    def generate_pdf_completo(n_clicks, table_data, id_loteamento, valor_total_orcamento, subtotal, cc_at, cc_ap, cc_vgv_value, input_data):
        if n_clicks is None or not table_data:
            raise PreventUpdate
        
        try:
            # Define paleta de cores do gráfico
            custom_colors = [
                '#E0F3F9', '#C6E7F1', '#ADDCE9', '#94D1E1', '#7BC5D8',
                '#62B9D0', '#499EB5', '#346F7A', '#345F6C', '#2D5260',
                '#264552', '#1F3844'
            ]

            # Criar PDF em formato paisagem
            buffer = io.BytesIO()
            pdf = canvas.Canvas(buffer, pagesize=landscape(letter))
            pdf.setTitle("Orçamento Completo")

            # Dimensões da página
            pagina_largura, pagina_altura = landscape(letter)

            
            ### ===================== PÁGINA 1 ===================== 
            
            # 1) Preencher com cor de fundo
            pdf.setFillColor(HexColor("#345F6C"))  # Define a cor de fundo
            pdf.rect(0, 0, pagina_largura, pagina_altura, fill=1)  # Preenche toda a página

            # 2) Inserir o título "Orçamento Paramétrico" centralizado acima da logo
            pdf.setFillColor(HexColor("#FFFFFF"))  # Cor branca para o texto
            pdf.setFont("Helvetica-Bold", 30)
            titulo_capa = "Orçamento Paramétrico"
            titulo_largura = pdf.stringWidth(titulo_capa, "Helvetica-Bold", 26)
            pdf.drawString(
                (pagina_largura - titulo_largura) / 2,  # Centralizar na página
                pagina_altura - 120,  # Posicionamento vertical (ajustável)
                titulo_capa
            )

            # 3) Inserir a logo centralizada (ajustando proporção corretamente)
            try:
                capa_logo = "assets/logoor2.png"
                
                # Definir um tamanho base sem distorção
                max_width = 300  # Largura máxima permitida
                max_height = 130  # Altura máxima permitida

                # Obter dimensões originais da imagem
                from PIL import Image
                with Image.open(capa_logo) as img:
                    original_width, original_height = img.size
                    aspect_ratio = original_width / original_height  # Proporção original da imagem
                
                # Calcular novo tamanho mantendo a proporção
                if original_width > max_width or original_height > max_height:
                    if aspect_ratio > 1:  # Se for mais larga do que alta
                        new_width = max_width
                        new_height = max_width / aspect_ratio
                    else:  # Se for mais alta do que larga
                        new_height = max_height
                        new_width = max_height * aspect_ratio
                else:
                    new_width, new_height = original_width, original_height  # Mantém tamanho original se for pequeno

                # Posicionar no centro
                x_center = (pagina_largura - new_width) / 2
                y_center = pagina_altura - 350  # Ajuste fino da posição vertical

                # Inserir a logo ajustada
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

            # --------------------------------------------------------------
            
            # Inserir texto "info-geral" abaixo da logo
            pdf.setFont("Helvetica", 16)
            pdf.setFillColor(HexColor("#FFFFFF"))

            # Pegar `info_geral_completo` do input_data (agora corrigido)
            info_geral_texto = input_data.get('info-geral-completo', 'Nenhuma informação disponível')

            y_texto = y_center - 60
            text_width = pdf.stringWidth(info_geral_texto, "Helvetica", 16)
            max_line_width = 600

            if text_width > max_line_width:
                linhas = textwrap.wrap(info_geral_texto, width=70)
                for linha in linhas:
                    line_width = pdf.stringWidth(linha, "Helvetica", 16)
                    pdf.drawString((pagina_largura - line_width) / 2, y_texto, linha)
                    y_texto -= 20
            else:
                pdf.drawString((pagina_largura - text_width) / 2, y_texto, info_geral_texto)

            # Inserir nome do responsável na parte inferior esquerda
            pdf.setFont("Helvetica", 16)
            responsavel_texto = input_data.get('responsavel-relatorio-completo', 'Não informado')
            pdf.drawString(50, 50, f"Responsável: {responsavel_texto}")

            # Inserir data na parte inferior direita
            data_atual = datetime.now().strftime("%d/%m/%Y")
            data_text_width = pdf.stringWidth(data_atual, "Helvetica", 16)
            pdf.drawString(pagina_largura - data_text_width - 50, 50, data_atual)

            # Finalizar a capa (Página 1)
            pdf.showPage()
            
                      
            ### ===================== PÁGINA 2 =====================
            # Inserir logo no canto superior direito
            logo_path = 'assets/logoor.png'
            try:
                pdf.drawImage(logo_path, x=pagina_largura - 90, y=pagina_altura - 60,
                            width=80, height=40, mask='auto')
            except Exception as e:
                print(f"Erro ao inserir a logo: {e}")
            
            # 1) Título principal
            pdf.setFont("Helvetica-Bold", 16)
            titulo_texto = "Orçamento Completo"
            titulo_largura = pdf.stringWidth(titulo_texto, "Helvetica-Bold", 16)
            pdf.drawString((pagina_largura - titulo_largura) / 2, pagina_altura - 50, titulo_texto)

            y_position = pagina_altura - 80  # Ajusta a posição logo abaixo do título

            # 2) Seção Resultados
            pdf.setFont("Helvetica-Bold", 8)
            pdf.drawString(50, y_position, "Resultados:")
            y_position -= 15

            # Exibição dos Resultados ---------------------------

            pdf.setFont("Helvetica-Bold", 7)
            pdf.drawString(50, y_position, "Valor Total do Orçamento: ")
            pdf.setFont("Helvetica", 7)
            pdf.drawString(200, y_position, f"{valor_total_orcamento}")
            y_position -= 12
            
            # Subtotal (80% do Valor Total)
            pdf.setFont("Helvetica-Bold", 7)
            pdf.drawString(50, y_position, "Subtotal (80% do Valor Total): ")
            pdf.setFont("Helvetica", 7)
            pdf.drawString(200, y_position, f"{subtotal}")  
            y_position -= 12

            pdf.setFont("Helvetica-Bold", 7)
            pdf.drawString(50, y_position, "CC/AT: ")
            pdf.setFont("Helvetica", 7)
            pdf.drawString(200, y_position, f"{cc_at}")
            y_position -= 12

            pdf.setFont("Helvetica-Bold", 7)
            pdf.drawString(50, y_position, "CC/AP: ")
            pdf.setFont("Helvetica", 7)
            pdf.drawString(200, y_position, f"{cc_ap}")
            y_position -= 12
            
            pdf.setFont("Helvetica-Bold", 7)
            pdf.drawString(50, y_position, "CC/VGV: ")
            pdf.setFont("Helvetica", 7)
            pdf.drawString(200, y_position, f"{cc_vgv_value}")  
            y_position -= 18  # Espaço adicional para separar da próxima seção
            
            #-------------------------------------------------    
            # 3) Seção "Dados do Orçamento Completo" (não alterado)
            #-------------------------------------------------   
            pdf.setFont("Helvetica-Bold", 8)
            pdf.drawString(50, y_position, "Dados do Orçamento Completo:")
            y_position -= 15

            pdf.setFont("Helvetica", 7)

            # Definir a ordem e labels dos inputs
            input_keys = [
                'info-geral-completo',
                'id-loteamento-completo', 'localizacao-completo', 'revisao-completo',
                'area-total-completo', 'perimetro-completo', 'area-lotes-completo',
                'area-viario-completo', 'comprimento-viario-completo', 'area-construida-completo',
                'area-quadra-completo', 'dados-incc-antigo-completo', 'dados-incc-atual-completo',
                'volume-corte-completo', 'volume-aterro-completo', 'volume-transporte-completo',
                'fechamento-perimetral-completo', 'meio-fio-completo', 'rede-eletrica-completo',
                'rede-agua-completo', 'rede-esgoto-completo', 'supressao-vegetacao-completo',
                'edificacoes-completo', 'quadra-society-completo', 'base-bgs-completo',
                'imprimacao-completo', 'pintura-completo', 'cbuq-completo', 'limpeza-camada-vegetal-completo',
                'volume-corte-completo-custo', 'volume-aterro-completo-custo', 'volume-transporte-completo-custo',
                'diametro-300-completo-custo', 'diametro-375-completo-custo', 'diametro-450-completo-custo',
                'diametro-500-completo-custo', 'diametro-600-completo-custo', 'diametro-800-completo-custo',
                'diametro-1000-completo-custo'
            ]
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

            # Exibir valor de 'info-geral-completo' isolado
            info_geral_value = input_data.get('info-geral-completo', '')
            pdf.setFont("Helvetica-Bold", 8)
            pdf.drawString(50, y_position, "Informações Gerais:")
            y_position -= 12

            pdf.setFont("Helvetica", 7)
            text_object = pdf.beginText(50, y_position)
            wrapped_lines = textwrap.wrap(info_geral_value, width=180)
            for wrapped_line in wrapped_lines:
                text_object.textLine(wrapped_line)
                y_position -= 10
                if y_position < 50:
                    pdf.drawText(text_object)
                    pdf.showPage()
                    y_position = pagina_altura - 50
                    pdf.setFont("Helvetica", 7)
                    text_object = pdf.beginText(50, y_position)
            pdf.drawText(text_object)
            y_position -= 10

            # Renderização dos demais inputs em colunas
            input_items = []
            for key in input_keys[1:]:  # Pulamos 'info-geral-completo' pois já exibimos
                label = input_labels.get(key, key)
                value = input_data.get(key, '')
                if isinstance(value, float):
                    value_str = convert_from_float(value)
                else:
                    value_str = str(value)
                input_items.append((label, value_str))

            # Ajuste a distância entre rótulo e valor
            spacing_between_label_and_value = 140  

            # Definir posições X para as colunas
            x_positions = [50, 280, 550]  # Ajuste os espaçamentos entre as colunas

            for i in range(0, len(input_items), 3):
                y_position -= 12
                if y_position < 50:
                    pdf.showPage()
                    y_position = pagina_altura - 50
                    pdf.setFont("Helvetica", 7)

                for col in range(3):
                    if i + col < len(input_items):
                        label, value_str = input_items[i + col]
                        
                        pdf.setFont("Helvetica-Bold", 7)  # Rótulo em negrito
                        pdf.drawString(x_positions[col], y_position, f"{label}:")
                        
                        pdf.setFont("Helvetica", 7)  # Valor em fonte normal
                        pdf.drawString(x_positions[col] + spacing_between_label_and_value, y_position, f"{value_str}")  # Espaçamento ajustado


            # Espaço antes da tabela
            y_position -= 20
            if y_position < 100:
                pdf.showPage()
                y_position = pagina_altura - 50
                pdf.setFont("Helvetica", 7)
             
            # ---------------------------------------------------------------------    
            # 5. Seção "Resultados"

            # Título da tabela
            pdf.setFont("Helvetica-Bold", 8)
            pdf.drawString(50, y_position, "Resultados:")
            y_position -= 15

            # Cabeçalhos da tabela
            pdf.setFont("Helvetica-Bold", 8)
            headers = ["Item", "Valor Total Corrigido"]
            x_positions_table = [50, 200]
            for i, header in enumerate(headers):
                pdf.drawString(x_positions_table[i], y_position, header)
            y_position -= 12

            # Dados da tabela (Apenas "Item" e "Valor Total Corrigido")
            pdf.setFont("Helvetica", 7)
            for item in table_data:
                item_name = item.get('item', '')
                valor_total_corrigido = convert_to_float(item.get('valor_total_corrigido', 0.0))

                # Formatação
                valor_total_corrigido_str = f"R$ {convert_from_float(valor_total_corrigido)}"

                # Rótulo do item em negrito
                pdf.setFont("Helvetica-Bold", 7)
                pdf.drawString(x_positions_table[0], y_position, str(item_name))  # Item
                
                # Valor total corrigido 
                pdf.setFont("Helvetica", 7)
                pdf.drawString(x_positions_table[1], y_position, valor_total_corrigido_str)  
                
                y_position -= 12 # Ajuste de espaçamento entre as linhas

                if y_position < 50:
                    pdf.showPage()
                    y_position = pagina_altura - 50
                    pdf.setFont("Helvetica", 8)

            
            ### ===================== PÁGINA 3 ===================== 
            
            # --- Segunda Página (Gráfico) ---
            pdf.showPage()
            y_position = pagina_altura - 50

            try:
                pdf.drawImage(
                    logo_path,
                    x=pagina_largura - 90,
                    y=pagina_altura - 60,
                    width=80,
                    height=40,
                    mask='auto'
                )
            except Exception as e:
                print(f"Erro ao inserir a logo: {e}")

            pdf.setFont("Helvetica-Bold", 16)
            titulo_grafico = "Gráfico"
            titulo_largura = pdf.stringWidth(titulo_grafico, "Helvetica-Bold", 16)
            pdf.drawString((pagina_largura - titulo_largura) / 2, y_position, titulo_grafico)
            y_position -= 30

            # Construção do gráfico Matplotlib (barras horizontais)
            fig, ax = plt.subplots(figsize=(14, 6))

            itens = [item['item'] for item in table_data]
            valores = [convert_to_float(item['valor_total_corrigido']) for item in table_data]
            total_valores = sum(valores)
            percentuais = [(v / total_valores) * 100 if total_valores else 0 for v in valores]

            # Ordenação por maior valor
            data_for_chart = sorted(zip(percentuais, itens, valores), reverse=True)
            percentuais_ordenados, itens_ordenados, valores_ordenados = zip(*data_for_chart)

            # **Paleta de azul **
            blue_palette = ['#499EB5', '#346F7A', '#345F6C', '#2D5260', '#264552', '#1F3844']
            cmap = LinearSegmentedColormap.from_list('blue_gradient', blue_palette)

            # Normalizar os valores para mapear cores
            max_valor = max(valores_ordenados)
            min_valor = min(valores_ordenados)
            valor_range = max_valor - min_valor if max_valor != min_valor else 1
            norm_vals = [(val - min_valor) / valor_range for val in valores_ordenados]
            cores_mapeadas = [cmap(n) for n in norm_vals]

            # Converter as cores para formato hexadecimal
            cores_hex = [
                '#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255))
                for r, g, b, _ in cores_mapeadas
            ]

            # Criar gráfico de barras horizontais
            bars = ax.barh(itens_ordenados, percentuais_ordenados, color=cores_hex)

            # Adicionar os percentuais dentro das barras (texto branco para contraste)
            for bar, percentual in zip(bars, percentuais_ordenados):
                width = bar.get_width()
                ax.annotate(
                    f'{percentual:.2f}%',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0),
                    textcoords="offset points",
                    ha='left',
                    va='center',
                    fontsize=10,
                    color='black'  # Texto preto
                )

            ax.invert_yaxis()  # Inverter a ordem para o maior ficar no topo
            ax.set_title('Participação Percentual dos Serviços', fontsize=14, weight='bold')
            ax.set_xlabel('Percentual (%)', fontsize=12)
            ax.set_ylabel('Serviços', fontsize=12)
            ax.tick_params(axis='x', labelsize=10)
            ax.tick_params(axis='y', labelsize=10)
            ax.grid(True, axis='x', linestyle='--', alpha=0.7)
            plt.tight_layout()

            # Salvar gráfico temporário para inserção no PDF
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
                plt.savefig(tmpfile.name, format='png', bbox_inches='tight')
                plt.close(fig)

                # Inserir o gráfico no PDF
                grafico_x = 50
                grafico_y = (pagina_altura - 400) / 2
                grafico_width = 700
                grafico_height = 400

                pdf.drawImage(
                    tmpfile.name,
                    x=grafico_x,
                    y=grafico_y,
                    width=grafico_width,
                    height=grafico_height,
                    mask='auto'
                )

            # Finalizar PDF
            pdf.save()
            buffer.seek(0)

            return dcc.send_bytes(buffer.getvalue(), filename="relatorio_completo.pdf")


        except Exception as e:
            print(f"Erro ao gerar o PDF: {e}")
            raise PreventUpdate
