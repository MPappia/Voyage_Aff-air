#models.py

from app import db, login_manager as login
from datetime import datetime
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

#models utilisateurs / authentification

class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email_user = db.Column(db.String(120), unique=True, nullable=False)
    pseudo_user = db.Column(db.String(64), unique=True, nullable=False)
    password_user = db.Column(db.String(128), nullable=False)
    id_role = db.Column(db.Integer, db.ForeignKey('role.id'))

    # Méthodes requises par Flask-Login
    def get_id(self):
        return self.id

    @login.user_loader
    def get_user_by_id(id):
        return users.query.get(int(id))
    @property
    def is_authenticated(self):
        return True  # À adapter selon votre logique d'authentification

    @staticmethod
    def identification(pseudo_user, password_user):
        user = users.query.filter(pseudo_user==pseudo_user).first()
        if user and check_password_hash(user.password_user, password_user):
            return user
        return None

    @staticmethod
    def ajout(email_user, pseudo_user, password_user):
        erreurs = []
        if not email_user:
            erreurs.append("L'email est vide")
        if not pseudo_user:
            erreurs.append("Le pseudo est vide")
        if not password_user or len(password_user) < 6:
            erreurs.append("Le mot de passe est vide ou trop court")

        unique = users.query.filter(
            db.or_(users.email_user == email_user, users.pseudo_user == pseudo_user)
        ).count()
        if unique > 0:
            erreurs.append("L'email ou le pseudo existe déjà")

        if len(erreurs) > 0:
            return False, erreurs
        
        utilisateur = users(
            email_user=email_user,
            pseudo_user=pseudo_user,
            password_user=generate_password_hash(password_user)
        )

        try:
            db.session.add(utilisateur)
            db.session.commit()
            return True, utilisateur
        except Exception as erreur:
            return False, [str(erreur)]

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(35))
    is_admin = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(35))

    def __repr__(self):
        return f"Role('{self.id}', '{self.role}', '{self.is_admin}', '{self.description}')"

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pseudo = db.Column(db.String(64), db.ForeignKey('users.pseudo_user'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.String(255), nullable=False)

    user = relationship('users',foreign_keys=[id_user], backref=db.backref('comments', lazy=True))
    def __repr__(self):
        return f"Comment('{self.pseudo}', '{self.created_at}', '{self.content}')"