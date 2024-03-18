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
        # Logique pour enregistrer l'utilisateur dans la base de données
        flash('Félicitations, vous êtes maintenant inscrit !', 'success')
        return redirect(url_for('login'))
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