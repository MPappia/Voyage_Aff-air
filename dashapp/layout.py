from dash import html, dcc

def create_layout():
    layout = html.Div([
         # Création d'un menu déroulant pour le filtre de fonction (Président ou Premier Ministre)
        dcc.Dropdown(
            id='fonction_filter',  # Identifiant du composant
            options=[
                {'label': 'Président', 'value': 'president de la republique'},  
                {'label': 'Premier Ministère', 'value': 'premier ministre'}
            ],
            value='president de la republique'   # Valeur par défaut du menu déroulant
        ),
        # Création d'un deuxième menu déroulant pour le filtre de localisation (domicile ou étranger)
        dcc.Dropdown(
            id='location_filter', 
            options=[
                {'label': 'domicile', 'value': 'domiciles'}, 
                {'label': 'étranger', 'value': 'etrangers'}
            ],
            value='etrangers' 
        ),
        # Création d'un troisième menu déroulant dépendant du choix dans le deuxième menu
        dcc.Dropdown(
            id='location_filter_2', 
            options=[], # Les options seront mises à jour dynamiquement en fonction de la sélection dans le menu précédent
            placeholder="Choisir un pays/une ville",  # Texte affiché lorsqu'aucune option n'est sélectionnée
            value=None, # Aucune valeur sélectionnée par défaut
        ),
         # Création d'un composant pour afficher des graphiques
        dcc.Graph(id='travel-graph')  
    ])
    return layout # Retourne la mise en page définie
