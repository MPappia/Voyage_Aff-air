from flask import render_template, redirect, url_for, flash, request
from app import app, db, login_manager
from app.models import users
from flask_login import current_user, login_user, logout_user, login_required
from app.formulaire import RegistrationForm, LoginForm
from datetime import datetime
from app.utils.transformations import clean_arg
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
        user = users(pseudo_user=form.pseudo_user.data, email_user=form.email_user.data,
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
        user = users.query.filter_by(pseudo_user=form.pseudo_user.data).first()
        if user and user.password_user == form.password_user.data:
            flash('Vous êtes connecté avec succès !', 'success')
            return redirect(url_for('index'))
        else:
            flash('Pseudo ou mot de passe incorrect.', 'danger')
    return render_template('login.html', title='Connexion', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))