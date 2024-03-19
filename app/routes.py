from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.models import User
from app.formulaire import RegistrationForm, LoginForm
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
        user = User(nom_user=form.nom_user.data, prenom_user=form.prenom_user.data,
                    email_user=form.email_user.data, pseudo_user=form.pseudo_user.data,
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
        user = User.query.filter_by(email_user=form.email_user.data).first()
        if user and user.password_user == form.password_user.data:
            flash('Vous êtes connecté avec succès !', 'success')
            return redirect(url_for('index'))
        else:
            flash('Adresse e-mail ou mot de passe incorrect.', 'danger')
    return render_template('login.html', title='Connexion', form=form)

@app.route('/logout')
def logout():
    # Logique pour déconnecter l'utilisateur
    flash('Vous êtes déconnecté !', 'success')
    return redirect(url_for('index'))