import sqlite3
import pandas as pd


def get_db_connection(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def get_data(conn, fonction, location_type, location_filter_2=None):

    params = [fonction]

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
        return pd.DataFrame()

    query = f"""
    SELECT strftime('%Y', d.date) AS year, COUNT(*) AS nombre_voyage
    FROM {table_name} d
    JOIN Persons p ON p.id = d.person_id
    {location_condition}
    WHERE p.fonction = ?
    GROUP BY year
    ORDER BY year
    """
    
    df = pd.read_sql_query(query, conn, params=params)

    print(df)

    return df


def get_countries(conn):
    query = "SELECT nom FROM pays"
    df = pd.read_sql_query(query, conn)
    return [{'label': row['nom'], 'value': row['nom']} for index, row in df.iterrows()]

def get_cities(conn):
    query = "SELECT nom FROM Villes"
    df = pd.read_sql_query(query, conn)
    return [{'label': row['nom'], 'value': row['nom']} for index, row in df.iterrows()]