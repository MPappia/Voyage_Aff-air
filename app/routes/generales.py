from flask import Blueprint, Response
import matplotlib.pyplot as plt
from io import BytesIO

# Créez un objet Blueprint pour les routes générales
generales_bp = Blueprint('generales', __name__)

@generales_bp.route('/plot')
def plot():
    # Création de données de test
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Création de la visualisation
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Exemple de Dataviz avec Matplotlib')
    
    # Sauvegarde de la visualisation dans un objet BytesIO
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    # Effacer le contenu de la figure pour libérer la mémoire
    plt.clf()

    # Retourne l'image en tant que réponse HTTP
    return Response(img.getvalue(), mimetype='image/png')
