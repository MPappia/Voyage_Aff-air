from dash import Dash

dash_app = Dash(__name__)

from .layout import layout
from .callbacks import register_callbacks

dash_app.layout = layout

register_callbacks(dash_app)
