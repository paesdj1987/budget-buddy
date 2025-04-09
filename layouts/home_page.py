# home_page.py

from dash import html, dcc

layout = html.Div(
    className="content-wrapper",
    children=[

        # Espaçamento superior geral da página
        html.Div(style={"padding-top": "10px"}),

        # Container das logos e do pipe
        html.Div(
            className="logo-container",
            children=[
                html.Div(
                    className="logo-wrapper",
                    children=[
                        html.Img(src="/assets/logo2.png", alt="Logo Centralizado"),
                        html.Span("|", className="pipe"),
                        html.Img(src="/assets/logoor.png", alt="Logo OR"),
                    ]
                )
            ]
        ),

        # Imagem principal
        html.Div(
            className="image-container",
            children=[
                html.Img(src="/assets/imagem1.jpg", alt="Imagem Centralizada")
            ]
        ),
        
        # Botões abaixo da imagem
        html.Div(
            className="buttons-below-image",
            children=[
                dcc.Link(html.Button("Acessar Manual do Usuário", className="btn"), href="/manual-do-usuario"),
                dcc.Link(html.Button("Acessar Orçamento Simplificado", className="btn"), href="/orcamento-simples"),
                dcc.Link(html.Button("Acessar Orçamento Completo", className="btn"), href="/orcamento-completo"),
                dcc.Link(html.Button("Acessar Dashboards", className="btn"), href="/dashboards"),
            ]
        ),

        # Texto de direitos autorais no canto inferior esquerdo
        html.Div(
            "© 2025 OR Empreendimentos LTDA. Todos os direitos reservados.",
            className="footer"
        )
    ]
)
