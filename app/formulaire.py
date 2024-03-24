# formulaire.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp, ValidationError
from app.models import users as User
import re


class RegistrationForm(FlaskForm):
    pseudo_user = StringField('Pseudo', validators=[DataRequired()])
    email_user = StringField('Email', validators=[DataRequired(), Email()])
    password_user = PasswordField('Mot de passe', validators=[DataRequired(), Length(min=6, message='Le mot de passe doit avoir au moins 6 caractères.'),
                                       Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]+$',
                                              message='Le mot de passe doit contenir au moins une minuscule, une majuscule et un chiffre.')])
    confirm_password = PasswordField('Confirmer le mot de passe', validators=[DataRequired(), EqualTo('password_user', message='Les mots de passe doivent correspondre.')])
    submit = SubmitField("S'inscrire")

    def validate_email_user(self, email_user):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_user.data):
            raise ValidationError('Veuillez saisir une adresse e-mail valide.')
        existing_user = User.query.filter_by(email_user=email_user.data).first()
        if existing_user:
            raise ValidationError('Cette adresse e-mail est déjà utilisée. Veuillez choisir une autre adresse.')

class LoginForm(FlaskForm):
    pseudo_user = StringField('Pseudo', validators=[DataRequired()])
    password_user = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')


class CommentForm(FlaskForm):
    content = TextAreaField('Contenu', validators=[DataRequired()])
    submit = SubmitField('Ajouter un commentaire')