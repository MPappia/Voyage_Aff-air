from dash.dependencies import Input, Output
import plotly.express as px
from data import get_db_connection, get_data, get_countries, get_cities

def register_callbacks(app):
    @app.callback(
        [Output('location_filter_2', 'options'),
         Output('location_filter_2', 'style')],
        [Input('location_filter', 'value')]
    )
    def update_location_filter_2_options(location_filter):
        conn = get_db_connection('projet.db')
        if location_filter == 'etrangers':
            options = [{'label': 'None', 'value': 'NONE'}] + get_countries(conn)
        elif location_filter == 'domiciles':
            options = [{'label': 'None', 'value': 'NONE'}] + get_cities(conn)
        else:
            options = [{'label': 'None', 'value': 'NONE'}]
        conn.close()
        style = {'display': 'block'} if options else {'display': 'none'}
        return options, style
    
    @app.callback(
        Output('travel-graph', 'figure'),
        [Input('fonction_filter', 'value'),
         Input('location_filter', 'value'),
         Input('location_filter_2', 'value')]
    )
    def update_graph(fonction_filter, location_filter, location_filter_2):
        conn = get_db_connection('projet.db')
    
    # 检查location_filter_2是否为"NONE"，如果是，则传递None
        location_filter_2_actual = None if location_filter_2 == 'NONE' else location_filter_2

        df = get_data(conn, fonction_filter, location_filter, location_filter_2_actual)
        conn.close()

    # 根据location_filter_2的值调整标题
        if location_filter_2_actual:
            location = location_filter_2
            title = f"Destination : {location} | Fonction: {fonction_filter} | Nom: xxx | visite par année"
        else:
            # 如果location_filter_2为"NONE"或未设置，只使用location_filter和fonction_filter构建标题
            if location_filter == 'etrangers':
                location_type = 'étranger'
            else:
                location_type = 'domicile'
            title = f"Destination : {location_type} | Fonction: {fonction_filter} | Nom: xxx | visite par année"

        fig = px.line(df, x='year', y='nombre_voyage', title=title, markers=True)
        return fig
