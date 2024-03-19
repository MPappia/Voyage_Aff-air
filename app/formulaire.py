from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    prenom_user = StringField('Prénom', validators=[DataRequired()])
    nom_user = StringField('Nom', validators=[DataRequired()])
    email_user = StringField('Adresse email', validators=[DataRequired(), Email()])
    pseudo_user = StringField('Pseudo', validators=[DataRequired()])
    password_user = PasswordField('Mot de passe', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmer le mot de passe', validators=[DataRequired(), EqualTo('password_user')])
    submit = SubmitField('S\'inscrire')

class LoginForm(FlaskForm):
    email_user = StringField('Adresse email', validators=[DataRequired()])
    password_user = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')
