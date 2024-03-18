from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    prenom_user = StringField('Prénom', validators=[DataRequired(), Length(min=2, max=35)])
    nom_user = StringField('Nom', validators=[DataRequired(), Length(min=2, max=35)])
    email_user = StringField('Email', validators=[DataRequired(), Email(), Length(max=35)])
    pseudo_user = StringField('Pseudo', validators=[DataRequired(), Length(min=2, max=35)])
    password_user = PasswordField('Mot de passe', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmer le mot de passe', validators=[DataRequired(), EqualTo('password_user')])
    submit = SubmitField('S\'inscrire')

class LoginForm(FlaskForm):
    email_user = StringField('Email', validators=[DataRequired(), Email(), Length(max=35)])
    password_user = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')
