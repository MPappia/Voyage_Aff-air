from flask import send_file, render_template, redirect, url_for, flash, request
import csv, os
from app import app, db, login_manager
from app.models import users as User, Comment
from flask_login import current_user, login_user, logout_user, login_required
from app.formulaire import RegistrationForm, LoginForm, CommentForm
from app.utils.truncateval import truncate_json, truncate_json_string
from datetime import datetime
from app.utils.transformations import clean_arg
from flask_paginate import Pagination, get_page_args
import pandas as pd


#erreurs 
@app.errorhandler(404)
def not_found_error(error):
    return render_template('erreurs/404.html'), 404

@app.errorhandler(500)
@app.errorhandler(503)
def internal_error(error):
    db.session.rollback()
    return render_template('erreurs/500.html'), 500

@app.route('/')
def index():
    year = datetime.now().year
    return render_template('index.html', title='Accueil', year=year)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Vérifier si le pseudo utilisateur est déjà pris
        existing_user = User.query.filter_by(pseudo_user=form.pseudo_user.data).first()
        if existing_user:
            flash('Le pseudo est déjà pris. Veuillez choisir un autre pseudo.', 'danger')
            return render_template('register.html', title='Inscription', form=form)
        
        # Si le pseudo n'est pas déjà pris, ajouter l'utilisateur à la base de données
        user = User(pseudo_user=form.pseudo_user.data, email_user=form.email_user.data,
                    password_user=form.password_user.data, id_role=1)  # Ajoutez l'ID du rôle approprié
        db.session.add(user)
        db.session.commit()
        flash('Félicitations, vous êtes maintenant inscrit !', 'success')
        return redirect(url_for('index'))  # Rediriger vers la page d'accueil
    return render_template('register.html', title='Inscription', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(pseudo_user=form.pseudo_user.data).first()
        if user and user.password_user == form.password_user.data:
            login_user(user)  # Authentification de l'utilisateur
            flash('Vous êtes connecté avec succès !', 'success')
            return redirect(url_for('index'))
        else:
            flash('Pseudo ou mot de passe incorrect.', 'danger')
    return render_template('login.html', title='Connexion', form=form)


@app.route('/logout')
def logout():
    logout_user()  # Déconnexion de l'utilisateur
    flash('Vous avez été déconnecté.', 'success')
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Page Tableau données

@app.route('/tableau')
def tableau():
    df = pd.read_csv('app/static/data/prez_data_2.csv', sep=';')

     # Tronquer les données de la colonne 'Lieu (contours)'
    df['Lieu (contours)'] = df['Lieu (contours)'].apply(lambda x: str(x))

    # Tronquer les données JSON dans la colonne "Lieu (contours)"
    df['Lieu (contours)'] = df['Lieu (contours)'].apply(lambda x: truncate_json_string(x, max_length=100))

    # Déterminez le nombre total de lignes dans le DataFrame
    total_rows = df.shape[0]

    # Récupérez le numéro de page à partir des arguments de requête
    page, per_page, offset = get_page_args()

    # Calculez les lignes à afficher pour la page actuelle
    start = offset
    end = offset + per_page

    # Divisez le DataFrame en pages
    df_page = df.iloc[start:end]

    # Convertissez le DataFrame de la page en HTML
    tableau_html = df_page.to_html(classes='table table-striped', index=False)

    # Créez une instance de pagination
    pagination = Pagination(page=page, per_page=per_page, total=total_rows,
                            css_framework='bootstrap4', record_name='data')

    # Renvoyez le modèle HTML avec le tableau et la pagination
    return render_template('tableau2.html', title='Tableau de données',
                           tableau_html=tableau_html, pagination=pagination)

@app.route('/download')
def download():
    p = "/Users/mpappia/Desktop/Voyage_Aff-air/data/prez_data.csv"
    return send_file(p, as_attachment=True)

#Page À propos
@app.route('/about')
def about():
    return render_template('about.html', title='À propos')

#Page Visualitation Dash
@app.route('/visualisation', methods=['GET', 'POST'])
def visualisation():
    # Créer une instance du formulaire de commentaire
    form = CommentForm()

    # Récupérer les commentaires existants depuis la base de données
    comments = Comment.query.all()

    # Traitement de la soumission du formulaire
    if form.validate_on_submit():
        # Créer une instance de commentaire et attribuer l'utilisateur actuel
        comment = Comment(id_user=current_user.id, content=form.content.data)
        db.session.add(comment)
        db.session.commit()
        flash('Votre commentaire a été ajouté avec succès!', 'success')
        return redirect(url_for('visualisation'))

    # Rendre le modèle HTML avec les commentaires et le formulaire
    return render_template('visualisation.html', title='Visualisation', comments=comments, form=form)
