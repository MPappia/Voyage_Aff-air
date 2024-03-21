# app/utils/truncateval.py

import json

def truncate_json(value):
    try:
        # Charger les données JSON
        data = json.loads(value)
        # Récupérer seulement les coordonnées
        coordinates = data.get("coordinates")
        # Convertir les coordonnées en une chaîne de caractères
        truncated_data = json.dumps(coordinates)
        return truncated_data
    except json.JSONDecodeError:
        # Si une erreur se produit lors du chargement JSON, retourner la valeur d'origine
        return value


def truncate_json_string(json_string, max_length):
    """
    Tronque une chaîne de caractères JSON à une longueur maximale.

    Args:
        json_string (str): Chaîne de caractères JSON à tronquer.
        max_length (int): Longueur maximale de la chaîne de caractères tronquée.

    Returns:
        str: Chaîne de caractères JSON tronquée.
    """
    # Vérifiez si la longueur de la chaîne de caractères dépasse la longueur maximale
    if len(json_string) > max_length:
        # Chargez la chaîne de caractères JSON
        json_data = json.loads(json_string)
        # Convertissez le dictionnaire en une chaîne de caractères JSON tronquée
        truncated_json = json.dumps(json_data)[:max_length] + '...'
        return truncated_json
    else:
        return json_string