from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    pseudo_user = StringField('Pseudo', validators=[DataRequired()])
    email_user = StringField('Email', validators=[DataRequired(), Email()]) 
    password_user = PasswordField('Mot de passe', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmer le mot de passe', validators=[DataRequired(), EqualTo('password_user')])
    submit = SubmitField("S'inscrire")

class LoginForm(FlaskForm):
    password_user = PasswordField('Mot de passe', validators=[DataRequired()])
    pseudo_user = StringField('Pseudo', validators=[DataRequired()])
    submit = SubmitField('Se connecter')
