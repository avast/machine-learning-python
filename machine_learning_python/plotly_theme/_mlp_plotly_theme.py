import plotly.graph_objects as go

mlp_plotly_theme = go.layout.Template(
    layout=go.Layout(
        font_family="Arial",
        font_size=14,
        title_y=0.95,
        title_x=0.5,
        xaxis_showgrid=True,
        yaxis_showgrid=True,
        xaxis_title_standoff=5,
        yaxis_title_standoff=3,
        colorway=[
            "#2D364C",
            "#FF7800",
            "#0CB754",
            "#6534AC",
            "#F5203E",
            "#5890FF",
            "#f1c039",
            "#f152b6",
            "#b4b7d4",
            "#863563",
            "#5cd6f4",
            "#166d2a",
        ],
        colorscale_sequential=[[0.0, "#2D364C"], [1.0, "#FF7800"]],
        colorscale_sequentialminus=[[0.0, "#FF7800"], [1.0, "#2D364C"]],
        coloraxis_colorbar={"outlinewidth": 0, "ticklen": 6, "tickwidth": 1},
        boxgap=0.5,
        boxgroupgap=0.5,
        margin_t=50,
        margin_b=30,
        bargap=0.2,
        width=800,
        height=600,
    )
)
