# app/utils/truncateval.py

import json

def truncate_json(value):
    try:
        data = json.loads(value)
        coordinates = data.get("coordinates")
        truncated_data = json.dumps(coordinates)
        return truncated_data
    except json.JSONDecodeError:
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
    if len(json_string) > max_length:
        json_data = json.loads(json_string)
        truncated_json = json.dumps(json_data)[:max_length] + '...'
        return truncated_json
    else:
        return json_string
    
def extract_coordinates(point):
    try:
        coordinates = point.strip('[]').split(', ')
        return float(coordinates[0]), float(coordinates[1])
    except (AttributeError, ValueError, IndexError):
        return None, None