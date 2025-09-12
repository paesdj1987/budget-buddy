## callbacks_dashboards.py

import os
import pandas as pd
import io
import base64
import plotly.io as pio
import tempfile
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash
import plotly.graph_objects as go

# Lista de itens válidos para a coluna "Item" 
ITENS_VALIDOS = [
    "Fechamento Perimetral",
    "Meio fio",
    "Rede de Distribuição Elétrica",
    "Rede de Abastecimento de Água",
    "Rede de Drenagem",
    "Rede de Coleta de Esgoto",
    "Pavimentação",
    "Supressão de Vegetação",
    "Terraplenagem",
    "Edificações"
] 

# Lista de colunas esperadas para o novo modelo 
EXPECTED_COLUMNS = ["Nome_Projeto", "Item", "Valor"]

def register_callbacks_dashboards(app):

    @app.callback(
        [Output("download-template", "data"),
         Output("download-message", "children")],
        Input("download-template-button", "n_clicks"),
        prevent_initial_call=True
    )
    def download_template(n_clicks):
        file_path = "assets/projeto.xlsx"
        if not os.path.exists(file_path):
            return dcc.send_string("Erro: Arquivo não encontrado!", filename="erro.txt"), None
        return dcc.send_file(file_path), html.Span("Download realizado com sucesso!", style={"font-weight": "bold"})


    @app.callback(
        Output("output-planilha-1", "children"),
        Input("upload-planilha-1", "contents"),
        State("upload-planilha-1", "filename"),
        prevent_initial_call=True
    )
    def upload_planilha_1(contents, filename):
        return process_uploaded_file(contents, filename, "Planilha 1")

    @app.callback(
        Output("output-planilha-2", "children"),
        Input("upload-planilha-2", "contents"),
        State("upload-planilha-2", "filename"),
        prevent_initial_call=True
    )
    def upload_planilha_2(contents, filename):
        return process_uploaded_file(contents, filename, "Planilha 2")

    @app.callback(
        Output("upload-error-message", "children"),
        Input("generate-analysis-button", "n_clicks"),
        State("upload-planilha-1", "filename"),
        State("upload-planilha-2", "filename")
    )
    def validar_geracao_analise(n_clicks, planilha1, planilha2):
        if not n_clicks:
            raise PreventUpdate
        if not planilha1 or not planilha2:
            return "⚠️ Por favor, envie as duas planilhas antes de gerar a análise!"
        return ""

    # ***************************
    # callbacks para limpar dados
    # ***************************

    @app.callback(
        [
            Output("upload-planilha-1", "contents"),
            Output("upload-planilha-1", "filename"),
            Output("upload-planilha-2", "contents"),
            Output("upload-planilha-2", "filename"),
            Output("output-planilha-1", "children"),
            Output("output-planilha-2", "children"),
            Output("upload-error-message", "children")
        ],
        Input("clear-uploads-button", "n_clicks"),
    )
    def limpar_uploads(n_clicks):
        if not n_clicks:
            raise PreventUpdate
        return None, None, None, None, "", "", ""
 
    # ***************************
    # callbacks para ocultar gráficos
    # ***************************
    @app.callback(
        Output("section-graficos", "style"),
        Input("generate-analysis-button", "n_clicks")
    )
    def mostrar_secoes(n_clicks):
        if n_clicks and n_clicks > 0:
            return {"display": "block"}
        raise PreventUpdate


    # ***************************
    # GRÁFICO COMPARATIVO (Bar Chart)
    # ***************************
    @app.callback(
        Output("analysis-chart", "figure"),
        Input("generate-analysis-button", "n_clicks"),
        State("upload-planilha-1", "contents"),
        State("upload-planilha-2", "contents"),
        State("filter-dropdown", "value"),  # Filtro de itens
        prevent_initial_call=True
    )
    def generate_chart(n_clicks, contents1, contents2, selected_items):
        if not n_clicks:
            raise PreventUpdate
        if contents1 is None or contents2 is None:
            return go.Figure()

        # Processa Planilha 1
        content_type, content_string = contents1.split(",")
        decoded1 = base64.b64decode(content_string)
        df1 = pd.read_excel(io.BytesIO(decoded1))
        df1.columns = df1.columns.str.strip()
        items1 = df1["Item"].astype(str).str.strip().iloc[0:10].tolist()
        valores1 = df1["Valor"].iloc[0:10].tolist()
        proj_name1 = (df1["Nome_Projeto"].dropna().astype(str).iloc[0]
                    if not df1["Nome_Projeto"].dropna().empty else "Projeto 1")

        # Processa Planilha 2
        content_type, content_string = contents2.split(",")
        decoded2 = base64.b64decode(content_string)
        df2 = pd.read_excel(io.BytesIO(decoded2))
        df2.columns = df2.columns.str.strip()
        items2 = df2["Item"].astype(str).str.strip().iloc[0:10].tolist()
        valores2 = df2["Valor"].iloc[0:10].tolist()
        proj_name2 = (df2["Nome_Projeto"].dropna().astype(str).iloc[0]
                    if not df2["Nome_Projeto"].dropna().empty else "Projeto 2")

        # Aplica filtro, se houver
        if selected_items is not None and len(selected_items) > 0:
            # Para Planilha 1
            filtered1 = [(i, v) for i, v in zip(items1, valores1) if i in selected_items]
            if filtered1:
                items1, valores1 = zip(*filtered1)
                items1, valores1 = list(items1), list(valores1)
            else:
                items1, valores1 = [], []
            # Para Planilha 2
            filtered2 = [(i, v) for i, v in zip(items2, valores2) if i in selected_items]
            if filtered2:
                items2, valores2 = zip(*filtered2)
                items2, valores2 = list(items2), list(valores2)
            else:
                items2, valores2 = [], []

        # Calcula percentuais para os labels
        total1 = sum(valores1) if valores1 else 1
        percentuais1 = [valor / total1 for valor in valores1]
        total2 = sum(valores2) if valores2 else 1
        percentuais2 = [valor / total2 for valor in valores2]

        customdata1 = [[p * 100] for p in percentuais1]
        customdata2 = [[p * 100] for p in percentuais2]

        # Monta o gráfico de barras comparativas
        fig = go.Figure()

        # Trace para o Projeto 1
        fig.add_trace(go.Bar(
            x=items1,
            y=valores1,
            name=proj_name1,
            marker_color='#FF5733',
            customdata=customdata1,
            texttemplate="%{y:.1f} (%{customdata[0]:.0f}%)",
            textposition='outside',
            textfont=dict(
                size=14,
                color="black",
                family="Arial"
            ),
            textangle=0,  # Texto alinhado horizontalmente
            cliponaxis=False,
            hovertemplate="<b>%{x}</b><br>Valor: %{y:.1f}<br>Percentual: %{customdata[0]:.0f}%<extra></extra>"
        ))

        # Trace para o Projeto 2
        fig.add_trace(go.Bar(
            x=items2,
            y=valores2,
            name=proj_name2,
            marker_color='#33C1FF',
            customdata=customdata2,
            texttemplate="%{y:.1f} (%{customdata[0]:.0f}%)",
            textposition='outside',
            textfont=dict(
                size=24,
                color="black",
                family="Arial"
            ),
            textangle=45,  # Texto inclinado em 45°
            cliponaxis=False,
            hovertemplate="<b>%{x}</b><br>Valor: %{y:.1f}<br>Percentual: %{customdata[0]:.0f}%<extra></extra>"
        ))

        # Atualiza o layout do gráfico
        fig.update_layout(
            autosize=True,
            height=700,  # Altura fixa para o gráfico
            barmode='group',
            title="Gráfico de Barras Comparativas",
            title_font=dict(color="#1D3B53", size=16, family="Arial Black"),
            title_x=0.5,
            xaxis_title="Item",
            yaxis_title="Valor",
            plot_bgcolor="#DCE3EA",
            paper_bgcolor="#DCE3EA",
            font=dict(size=12, color="#1D3B53"),
            legend=dict(title="Projeto", font=dict(color="#1D3B53")),
            margin=dict(t=80)  # Ajuste conforme necessário
        )



        return fig


    # ***************************
    # GRÁFICO DE COMPARAÇÃO (SLOPE CHART)
    # ***************************
    @app.callback(
        Output("slope-chart", "figure"),
        Input("generate-analysis-button", "n_clicks"),
        State("upload-planilha-1", "contents"),
        State("upload-planilha-2", "contents"),
        State("filter-dropdown", "value"),
        prevent_initial_call=True
    )
    def generate_slope_chart(n_clicks, contents1, contents2, selected_items):
        if not n_clicks:
            raise PreventUpdate
        if contents1 is None or contents2 is None:
            return go.Figure()

        # Processa Planilha 1
        content_type, content_string = contents1.split(",")
        decoded1 = base64.b64decode(content_string)
        df1 = pd.read_excel(io.BytesIO(decoded1))
        df1.columns = df1.columns.str.strip()
        items1 = df1["Item"].astype(str).str.strip().iloc[0:10].tolist()
        valores1 = df1["Valor"].iloc[0:10].tolist()
        proj_name1 = (df1["Nome_Projeto"].dropna().astype(str).iloc[0]
                    if not df1["Nome_Projeto"].dropna().empty else "Projeto 1")

        # Processa Planilha 2
        content_type, content_string = contents2.split(",")
        decoded2 = base64.b64decode(content_string)
        df2 = pd.read_excel(io.BytesIO(decoded2))
        df2.columns = df2.columns.str.strip()
        items2 = df2["Item"].astype(str).str.strip().iloc[0:10].tolist()
        valores2 = df2["Valor"].iloc[0:10].tolist()
        proj_name2 = (df2["Nome_Projeto"].dropna().astype(str).iloc[0]
                    if not df2["Nome_Projeto"].dropna().empty else "Projeto 2")

        # Aplica filtro, se houver
        if selected_items is not None and len(selected_items) > 0:
            filtered1 = [(i, v) for i, v in zip(items1, valores1) if i in selected_items]
            if filtered1:
                items1, valores1 = zip(*filtered1)
                items1, valores1 = list(items1), list(valores1)
            else:
                items1, valores1 = [], []

            filtered2 = [(i, v) for i, v in zip(items2, valores2) if i in selected_items]
            if filtered2:
                items2, valores2 = zip(*filtered2)
                items2, valores2 = list(items2), list(valores2)
            else:
                items2, valores2 = [], []

        # Calcula os totais para os percentuais
        total1 = sum(valores1) if valores1 else 1
        total2 = sum(valores2) if valores2 else 1

        # Cria o Slope Chart
        fig = go.Figure()
        for idx in range(len(items1)):
            item = items1[idx]
            y1 = valores1[idx]
            y2 = valores2[idx]
            mid = (y1 + y2) / 2

            # Calcula percentuais para cada projeto
            percent1 = y1 / total1 * 100
            percent2 = y2 / total2 * 100

            # Define os rótulos: exibindo somente nos pontos das extremidades
            text_labels = [
                f"{y1:.1f} ({percent1:.0f}%)",
                "",
                f"{y2:.1f} ({percent2:.0f}%)"
            ]

            fig.add_trace(go.Scatter(
                x=[0, 0.5, 1],
                y=[y1, mid, y2],
                mode='lines+markers+text',
                marker=dict(size=[10, 8, 10]),
                line=dict(width=2),
                name=item,
                text=text_labels,
                textposition=["top center", "middle center", "top center"],
                textfont=dict(size=10),
                hovertemplate=(
                    f"{item}<br>{proj_name1}: {y1:.1f} ({percent1:.0f}%)<br>"
                    f"{proj_name2}: {y2:.1f} ({percent2:.0f}%)<extra></extra>"
                )
            ))

        # Atualiza o layout com altura fixa e configurações de estilo
        fig.update_layout(
            autosize=True,
            title="Gráfico de Comparação - Slope Chart",
            title_font=dict(color="#1D3B53", size=16, family="Arial Black"),
            title_x=0.5,
            xaxis=dict(
                tickmode='array',
                tickvals=[0, 1],
                ticktext=[proj_name1, proj_name2]
            ),
            xaxis_title="Projeto",
            yaxis_title="Valor",
            plot_bgcolor="#DCE3EA",
            paper_bgcolor="#DCE3EA",
            font=dict(size=12, color="#1D3B53"),
            legend=dict(title="Item", font=dict(color="#1D3B53")),
            height=700,  # Define altura fixa para o gráfico
            margin=dict(t=160)
        )
        return fig




    # ***************************
    # GRÁFICO RADAR
    # ***************************
    @app.callback(
        Output("radar-chart", "figure"),
        Input("generate-analysis-button", "n_clicks"),
        State("upload-planilha-1", "contents"),
        State("upload-planilha-2", "contents"),
        State("filter-dropdown", "value"),
        prevent_initial_call=True
    )
    def generate_radar_chart(n_clicks, contents1, contents2, selected_items):
        if not n_clicks or contents1 is None or contents2 is None:
            raise PreventUpdate

        # Processa Planilha 1
        content_type, content_string = contents1.split(",")
        decoded1 = base64.b64decode(content_string)
        df1 = pd.read_excel(io.BytesIO(decoded1))
        df1.columns = df1.columns.str.strip()
        categories = ITENS_VALIDOS  # lista completa
        df1_items = df1.set_index("Item")
        total1 = df1_items["Valor"].sum()
        percents1 = [(df1_items.loc[item, "Valor"] / total1 * 100) if item in df1_items.index else 0 for item in categories]
        proj_name1 = (df1["Nome_Projeto"].dropna().astype(str).iloc[0]
                    if not df1["Nome_Projeto"].dropna().empty else "Projeto 1")

        # Processa Planilha 2
        content_type, content_string = contents2.split(",")
        decoded2 = base64.b64decode(content_string)
        df2 = pd.read_excel(io.BytesIO(decoded2))
        df2.columns = df2.columns.str.strip()
        df2_items = df2.set_index("Item")
        total2 = df2_items["Valor"].sum()
        percents2 = [(df2_items.loc[item, "Valor"] / total2 * 100) if item in df2_items.index else 0 for item in categories]
        proj_name2 = (df2["Nome_Projeto"].dropna().astype(str).iloc[0]
                    if not df2["Nome_Projeto"].dropna().empty else "Projeto 2")

        # Aplica filtro para Radar
        if selected_items is not None and len(selected_items) > 0:
            filtered_categories = [cat for cat in categories if cat in selected_items]
            if filtered_categories:
                percents1 = [percents1[categories.index(cat)] for cat in filtered_categories]
                percents2 = [percents2[categories.index(cat)] for cat in filtered_categories]
                categories = filtered_categories
            else:
                categories = []
                percents1 = []
                percents2 = []

        # Calcula os Valores (Valor) para cada categoria
        values1 = [df1_items.loc[cat, "Valor"] if cat in df1_items.index else 0 for cat in categories]
        values2 = [df2_items.loc[cat, "Valor"] if cat in df2_items.index else 0 for cat in categories]

        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=percents1,
            theta=categories,
            fill='toself',
            name=proj_name1,
            customdata=values1,
            hovertemplate="Item: %{theta}<br>Valor: %{customdata:.1f}<br>Percentual: %{r:.0f}%<extra></extra>",
            line=dict(color="#FF5733")
        ))
        fig.add_trace(go.Scatterpolar(
            r=percents2,
            theta=categories,
            fill='toself',
            name=proj_name2,
            customdata=values2,
            hovertemplate="Item: %{theta}<br>Valor: %{customdata:.1f}<br>Percentual: %{r:.0f}%<extra></extra>",
            line=dict(color="#33C1FF")
        ))

        max_val = max(max(percents1) if percents1 else 0, max(percents2) if percents2 else 0)
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max_val * 1.1],
                    gridcolor="#AAB9C3",
                    linecolor="#AAB9C3",
                    tickfont=dict(color="#1D3B53")
                ),
                angularaxis=dict(
                    tickfont=dict(color="#1D3B53")
                ),
                bgcolor="#DCE3EA"
            ),
            showlegend=True,
            title="Gráfico Radar Chart",
            title_font=dict(color="#1D3B53", size=16, family="Arial Black"),
            title_x=0.5,
            paper_bgcolor="#DCE3EA",
            plot_bgcolor="#DCE3EA",
            font=dict(size=12, color="#1D3B53"),
            height=700,
            margin=dict(t=160)
        )
        return fig





# ------------------------- FUNÇÃO AUXILIAR PARA PROCESSAR UPLOADS ------------------------- #
def process_uploaded_file(contents, filename, planilha_nome):
    if contents is None:
        return ""
    try:
        content_type, content_string = contents.split(",")
        decoded = base64.b64decode(content_string)
        df = pd.read_excel(io.BytesIO(decoded))
        df.columns = df.columns.str.strip()

        # Verifica se as colunas esperadas estão presentes
        for col in EXPECTED_COLUMNS:
            if col not in df.columns:
                return html.Div(
                    f"Erro: A coluna '{col}' está ausente na {planilha_nome}. Certifique-se de seguir o modelo.",
                    style={"color": "red", "font-weight": "bold"}
                )

        # Validação dos itens (somente as 10 primeiras linhas)
        items_uploaded = df["Item"].astype(str).str.strip().iloc[0:10].tolist()
        if len(items_uploaded) < 10:
            return html.Div(
                f"Erro: A {planilha_nome} não contém a quantidade necessária de itens na coluna 'Item'.",
                style={"color": "red", "font-weight": "bold"}
            )
        if items_uploaded != ITENS_VALIDOS:
            return html.Div(
                f"Erro: A {planilha_nome} contém valores inválidos na coluna 'Item'. Utilize apenas os itens permitidos da planilha modelo.",
                style={"color": "red", "font-weight": "bold"}
            )

        return html.Div(f"{filename} enviada com sucesso!", style={"color": "green", "font-weight": "bold"})
    except Exception as e:
        return html.Div(f"Erro ao processar {planilha_nome}: {str(e)}", style={"color": "red", "font-weight": "bold"})
