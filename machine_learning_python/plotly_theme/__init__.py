import plotly as pl
import plotly.io as pio

from ._mlp_plotly_theme import mlp_plotly_theme

pio.templates["mlp"] = mlp_plotly_theme
pio.templates.default = "simple_white+mlp"
