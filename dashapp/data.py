import sqlite3
import pandas as pd

# Fonction pour établir une connexion à la base de données SQLite
def get_db_connection(db_path):
    conn = sqlite3.connect(db_path)
    return conn
    
# Fonction pour récupérer des données filtrées depuis la base de données
def get_data(conn, fonction, location_type, location_filter_2=None):

    params = [fonction]# Paramètres initiaux pour la requête SQL

     # Détermination de la table et de la condition de jointure selon le type de localisation
    if location_type == 'etrangers':
        table_name = 'Depla_etranger_F'
        if location_filter_2:
            location_condition = "JOIN Pays ON d.pays_id = Pays.id AND Pays.nom = ?"
            params = [location_filter_2, fonction]
        else:
            location_condition = "JOIN Pays ON d.pays_id = Pays.id"

    elif location_type == 'domiciles':
        table_name = 'Depla_domicile_F'
        if location_filter_2:
            location_condition = "JOIN Villes ON d.ville_id = Villes.id AND Villes.nom = ?"
            params = [location_filter_2, fonction]
        else:
            location_condition = "JOIN Villes ON d.ville_id = Villes.id"
    else:
        return pd.DataFrame() # Retourne un DataFrame vide si le type de localisation n'est pas reconnu

     # Construction de la requête SQL
    query = f"""
    SELECT strftime('%Y', d.date) AS year, COUNT(*) AS nombre_voyage
    FROM {table_name} d
    JOIN Persons p ON p.id = d.person_id
    {location_condition}
    WHERE p.fonction = ?
    GROUP BY year
    ORDER BY year
    """
    
    # Exécution de la requête et chargement des résultats dans un DataFrame
    df = pd.read_sql_query(query, conn, params=params)

    print(df) # Affichage du DataFrame

    return df # Retour du DataFrame avec les résultats

# Fonction pour récupérer la liste des pays depuis la base de données
def get_countries(conn):
    query = "SELECT nom FROM pays"
    df = pd.read_sql_query(query, conn)
     # Transformation des résultats en une liste de dictionnaires pour l'affichage dans les filtres
    return [{'label': row['nom'], 'value': row['nom']} for index, row in df.iterrows()]

# Fonction pour récupérer la liste des villes depuis la base de données
def get_cities(conn):
    query = "SELECT nom FROM Villes"
    df = pd.read_sql_query(query, conn)
     # Transformation des résultats en une liste de dictionnaires pour l'affichage dans les filtres
    return [{'label': row['nom'], 'value': row['nom']} for index, row in df.iterrows()]
