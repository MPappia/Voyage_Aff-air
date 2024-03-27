from dash import html, dcc

def create_layout():
    layout = html.Div([
        dcc.Dropdown(
            id='fonction_filter',  
            options=[
                {'label': 'Président', 'value': 'president de la republique'},  
                {'label': 'Premier Ministère', 'value': 'premier ministre'}
            ],
            value='president de la republique'  
        ),
        dcc.Dropdown(
            id='location_filter', 
            options=[
                {'label': 'domicile', 'value': 'domiciles'}, 
                {'label': 'étranger', 'value': 'etrangers'}
            ],
            value='etrangers' 
        ),
        dcc.Dropdown(
            id='location_filter_2', 
            options=[],
            placeholder="Choisir un pays/une ville",  
            value=None,
        ),
        dcc.Graph(id='travel-graph')  
    ])
    return layout
