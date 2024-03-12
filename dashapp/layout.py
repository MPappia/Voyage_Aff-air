from dash import dcc, html
import plotly.graph_objs as go

data1 = go.Scatter(x=[1, 2, 3], y=[4, 1, 2])
data2 = go.Scatter(x=[1, 2, 3], y=[2, 3, 4])
data3 = go.Scatter(x=[1, 2, 3], y=[5, 4, 3])

layout = html.Div([
    # grand graphique en haut
    dcc.Graph(
        id='large-graph',
        figure={
            'data': [data1],
            'layout': go.Layout(title='Jouez avec les données')
        }
    ),
    # 2 petit graphiques en bas pour comparer 
    html.Div([
        dcc.Graph(
            id='small-graph-1',
            figure={
                'data': [data2],
                'layout': go.Layout(title='déplacements internationaux')
            },
            style={'display': 'inline-block', 'width': '49%'}  
        ),
        dcc.Graph(
            id='small-graph-2',
            figure={
                'data': [data3],
                'layout': go.Layout(title='déplacements domiciles')
            },
            style={'display': 'inline-block', 'width': '49%'}
        )
    ])
])
