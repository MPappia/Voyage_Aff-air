from dash.dependencies import Input, Output
import plotly.express as px
from data import get_db_connection, get_data, get_countries, get_cities

def register_callbacks(app):
    # Enregistre les rappels (callbacks) pour l'application Dash
    @app.callback(
        [Output('location_filter_2', 'options'),
         Output('location_filter_2', 'style')],
        [Input('location_filter', 'value')] # Déclenché par le changement de valeur dans le premier filtre de localisation
    )
    def update_location_filter_2_options(location_filter):
         # Fonction pour mettre à jour les options du deuxième filtre de localisation basé sur le premier filtre
        conn = get_db_connection('projet.db') # Établir la connexion à la base de données
        if location_filter == 'etrangers':
            options = [{'label': 'None', 'value': 'NONE'}] + get_countries(conn)  # Options de pays si 'etrangers' est sélectionné
        elif location_filter == 'domiciles':
            options = [{'label': 'None', 'value': 'NONE'}] + get_cities(conn)  # Options de villes si 'domiciles' est sélectionné
        else:
            options = [{'label': 'None', 'value': 'NONE'}]
        conn.close()
        style = {'display': 'block'} if options else {'display': 'none'} # Afficher le filtre si des options sont disponibles
        return options, style
    
    @app.callback(
        Output('travel-graph', 'figure'), # Mise à jour de la figure du graphique de voyage
        [Input('fonction_filter', 'value'), # Déclenché par le changement de valeur du filtre de fonction
         Input('location_filter', 'value'),  # Déclenché par le changement de valeur du premier filtre de localisation
         Input('location_filter_2', 'value')]  # Déclenché par le changement de valeur du deuxième filtre de localisation
    )
    def update_graph(fonction_filter, location_filter, location_filter_2):
        conn = get_db_connection('projet.db')
    
     # Vérifier si location_filter_2 est "NONE" et, si oui, passer None
        location_filter_2_actual = None if location_filter_2 == 'NONE' else location_filter_2

        df = get_data(conn, fonction_filter, location_filter, location_filter_2_actual)
        conn.close()# Fermer la connexion à la base de données

    # Ajuster le titre basé sur la valeur de location_filter_2
        if location_filter_2_actual:
            location = location_filter_2
            title = f"Destination : {location} | Fonction: {fonction_filter} | Nom: xxx | visite par année"
        else:
            # Si location_filter_2 est "NONE" ou non défini, construire le titre avec location_filter et fonction_filter seulement
            if location_filter == 'etrangers':
                location_type = 'étranger'
            else:
                location_type = 'domicile'
            title = f"Destination : {location_type} | Fonction: {fonction_filter} | Nom: xxx | visite par année"

        fig = px.line(df, x='year', y='nombre_voyage', title=title, markers=True)
        return fig  # Retourner le graphique configuré
