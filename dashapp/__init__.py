from dash import Dash
from app import app as server
from .layout import layout
from .callbacks import register_callbacks

dash_app = Dash(__name__, server=server, routes_pathname_prefix='/dash/')
    
# Set the layout 
dash_app.layout = layout
    
# Register the callbacks
register_callbacks(dash_app)
