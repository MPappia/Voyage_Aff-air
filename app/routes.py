from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.models.formulaire import RegistrationForm, LoginForm
from datetime import datetime
import pandas as pd


@app.route('/')
def index():
    year = datetime.now().year
    return render_template('index.html', title='Accueil', year=year)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Récupérer les données du formulaire
        prenom_user = form.prenom_user.data
        nom_user = form.nom_user.data
        email_user = form.email_user.data
        pseudo_user = form.pseudo_user.data
        password_user = form.password_user.data

        # Insérer le code pour enregistrer l'utilisateur dans la base de données ici
        # Par exemple, si vous utilisez SQLAlchemy :
        # from app.models import User
        # new_user = User(prenom=prenom_user, nom=nom_user, email=email_user, pseudo=pseudo_user, password=password_user)
        # db.session.add(new_user)
        # db.session.commit()

        flash('Félicitations, vous êtes maintenant inscrit !', 'success')
        return redirect(url_for('login'))  # Rediriger vers la page de connexion après l'inscription réussie
    return render_template('register.html', title='Inscription', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Logique pour vérifier les informations de connexion de l'utilisateur
        flash('Vous êtes connecté avec succès !', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title='Connexion', form=form)

@app.route('/logout')
def logout():
    # Logique pour déconnecter l'utilisateur
    flash('Vous êtes déconnecté !', 'success')
    return redirect(url_for('index'))