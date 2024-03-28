#routes.py

from flask import send_file, render_template, redirect, url_for, flash, request
import csv, os
from app import app, db, login_manager as login
from app.models import users as User, Comment
from flask_login import current_user, login_user, logout_user, login_required
from app.formulaire import RegistrationForm, LoginForm, CommentForm
from app.utils.truncateval import extract_coordinates, truncate_json_string
from datetime import datetime
from app.utils.transformations import clean_arg
from flask_paginate import Pagination, get_page_args
import plotly.graph_objs as go
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
        existing_user = User.query.filter_by(pseudo_user=form.pseudo_user.data).first()
        if existing_user:
            flash('Le pseudo est déjà pris. Veuillez choisir un autre pseudo.', 'danger')
            return render_template('register.html', title='Inscription', form=form)
        
        user = User(pseudo_user=form.pseudo_user.data, email_user=form.email_user.data,
                    password_user=form.password_user.data, id_role=1)  
        db.session.add(user)
        db.session.commit()
        flash('Félicitations, vous êtes maintenant inscrit !', 'success')
        return redirect(url_for('index')) 
    return render_template('register.html', title='Inscription', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if current_user.is_authenticated is True:
        flash('Vous êtes déjà connecté.', 'info')
        return redirect(url_for('index'))

    if form.validate_on_submit():
        user = User.identification(
            pseudo=clean_arg(request.form.get('pseudo_user', None)),
            password=clean_arg(request.form.get('password_user', None))
        )
        if user:
            flash('Connexion réussie.', 'success')
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Identifiants incorrects.', 'danger')
            return render_template('login.html', title='Connexion', form=form)
    else:
        return render_template('login.html', title='Connexion', form=form)
login.login_view = 'login'

@app.route('/logout')
def logout():
    if current_user.is_authenticated is True:
        logout_user()
    flash('Vous avez été déconnecté.', 'success')
    return redirect(url_for('index'))

# Page Tableau données

@app.route('/tableau')
def tableau():
    df = pd.read_csv('app/static/data/prez_data_2.csv', sep=';')

    df['Lieu (contours)'] = df['Lieu (contours)'].apply(lambda x: str(x))

    df['Lieu (contours)'] = df['Lieu (contours)'].apply(lambda x: truncate_json_string(x, max_length=100))

    total_rows = df.shape[0]

    page, per_page, offset = get_page_args()

    start = offset
    end = offset + per_page

    df_page = df.iloc[start:end]

    tableau_html = df_page.to_html(classes='table table-striped', index=False)

    pagination = Pagination(page=page, per_page=per_page, total=total_rows,
                            css_framework='bootstrap4', record_name='data')

    return render_template('tableau2.html', title='Tableau de données',
                           tableau_html=tableau_html, pagination=pagination)

@app.route('/download')
def download():
    p = "/Users/mpappia/Desktop/Voyage_Aff-air/data/prez_data.csv"
    return send_file(p, as_attachment=True)
    
#Page graphique
@app.route('/graphique')
def graphique():
    return render_template('graphique.html', title='À propos')
    
#Page À propos
@app.route('/about')
def about():
    return render_template('about.html', title='À propos')

#Page Visualitation Dash
@app.route('/visualisation', methods=['GET', 'POST'])
def visualisation():
    form = CommentForm()

    comments = Comment.query.all()

    df = pd.read_csv('/Users/mpappia/Desktop/Voyage_Aff-air/app/static/data/prez-us_data.csv')

    visits_by_country = df['Code_pays'].value_counts().reset_index()
    visits_by_country.columns = ['Code_pays', 'Nombre de visites']

    world_map = go.Choropleth(
        locations=visits_by_country['Code_pays'],
        z=visits_by_country['Nombre de visites'],
        locationmode='ISO-3',
        colorscale='Viridis',
        reversescale=True,
        colorbar_title='Nombre de visites'
    )

    layout = go.Layout(
        title='Carte des visites du POTUS (President of the United States) par pays',
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='mercator',
        ), 
        width=800,
        height=600,
    )

    fig = go.Figure(data=[world_map], layout=layout)

    heatmap_html = fig.to_html(full_html=False)

    # Seconde Carte
   
    df = pd.read_csv('/Users/mpappia/Desktop/Voyage_Aff-air/app/static/data/prez_data_2.csv', sep=';')

    leader = request.args.get('leader')  
    if leader:
        df = df[df['Fonction'] == leader]

    visits_by_country = df['Code pays'].value_counts().reset_index()
    visits_by_country.columns = ['Code pays', 'Nombre de visites']

    world_map = go.Choropleth(
        locations=visits_by_country['Code pays'],
        z=visits_by_country['Nombre de visites'],
        locationmode='ISO-3',
        colorscale='Viridis',
        reversescale=True,
        colorbar_title='Nombre de visites'
    )

    layout = go.Layout(
        title=f'Carte des visites des {leader} par pays',
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='mercator',
        ), 
        width=800,
        height=600,
    )

    fig = go.Figure(data=[world_map], layout=layout)

    heatmap2_html = fig.to_html(full_html=False)

    if form.validate_on_submit():
        comment = Comment(id_user=current_user.id, content=form.content.data)
        db.session.add(comment)
        db.session.commit()
        flash('Votre commentaire a été ajouté avec succès!', 'success')
        return redirect(url_for('visualisation'))

    return render_template('visualisation.html', title='Visualisation', heatmap_html=heatmap_html, heatmap2_html=heatmap2_html,comments=comments, form=form)
