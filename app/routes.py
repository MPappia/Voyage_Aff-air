from flask import render_template, redirect, url_for, flash, request
from app import app
from app.forms import RegistrationForm, LoginForm
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

df=pd.read_csv('data/prez_data.csv')

@app.route('/visualisation')
def visualisation():
    page = request.args.get('page', 1, type=int)
    elements_per_page = 50
    debut = (page-1)*elements_per_page
    fin = debut + elements_per_page
    data_page = df.iloc[debut:fin]
    nombre_pages = df.shape[0] // elements_per_page + 1 if df.shape[0] % elements_per_page != 0 else df.shape[0] // elements_per_page
    return render_template('visualisation.html', title='Visualisation', data=data_page, page=page, nombre_pages=nombre_pages)