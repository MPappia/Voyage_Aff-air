#models.py

from app import db, login_manager as login
from datetime import datetime
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class _person_(db.Model):
    __tablename__ = "Person"
    
    id = db.Column(db.Integer, primary_key=True)
    fonction = db.Column(db.String(45), nullable=False)
    nom = db.Column(db.String(45), nullable=False)
    nationalite_code = db.Column(db.String(45), db.ForeignKey('pays.id'), primary_key=True)
    Date_debut_mandat = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    Date_fin = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    parti = db.Column(db.String(45), nullable=True)

    # Relations 
    nationalite = relationship("_pays_", back_populates="people")
    person_to_depla = relationship("_depla_etranger_F_", back_populates="depla_to_person")
    person_to_depla_A = relationship("_depla_etranger_A_", back_populates="depla_A_to_person")
    person_to_depla_F = relationship("_depla_domicile_F_", back_populates="depla_F_to_person", uselist=False)
    person_to_depla_F_optional = relationship("_depla_domicile_F_", back_populates="depla_F_to_person_optional", uselist=False, overlaps="person_to_depla_F")
    person_to_mairie_service = relationship("_mairie_services_", back_populates="mairie_service_to_person")
    
    def __repr__(self):
        return f"Person('{self.id}', '{self.fonction}', '{self.nom}', '{self.Date_debut_mandat}', '{self.Date_fin}', '{self.parti}')"

class _mairie_services_(db.Model):
    __tablename__ = "Mairie_Services"

    Person_id = db.Column(db.Integer, db.ForeignKey('Person.id'), nullable=True)
    ville_id = db.Column(db.Integer, db.ForeignKey('Ville.id'), nullable=True)
    id = db.Column(db.Integer, primary_key=True)
    date_debut_service = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    date_fin_service = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)

    # Relation
    mairie_service_to_ville = relationship("_ville_", back_populates="ville_to_mairie_service")
    mairie_service_to_person = relationship("_person_", back_populates="person_to_mairie_service")

    def __repr__(self):
        return f"Mairie_services('{self.id}', '{self.date_debut_service}', '{self.date_fin_service}')"

class _depla_etranger_F_(db.Model):
    __tablename__ = "Depla_etranger_F"
    
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('Person.id'), primary_key=True)
    pays_id = db.Column(db.Integer, db.ForeignKey('pays.id'), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relations
    depla_to_pays = relationship("_pays_", back_populates="pays_to_depla")
    depla_to_person = relationship("_person_", back_populates="person_to_depla")


    def __repr__(self):
        return f"Depla_etranger_F('{self.id}', '{self.person_id}', '{self.pays_id}', '{self.date}')"


class _depla_etranger_A_(db.Model):
    __tablename__ = "Depla_etranger_A"

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('Person.id'), primary_key=True)
    pays_id = db.Column(db.Integer, db.ForeignKey('pays.id'), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relations
    depla_A_to_person = relationship("_person_", back_populates="person_to_depla_A")
    depla_A_to_pays = relationship("_pays_", back_populates="pays_to_depla_A")

    def __repr__(self):
        return f"Depla_etranger_A('{self.id}', '{self.person_id}', '{self.pays_id}', '{self.date}')"

class _depla_domicile_F_(db.Model):
    __tablename__ = "Depla_domicile_F"

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('Person.id'), primary_key=True)
    ville_id = db.Column(db.Integer, db.ForeignKey('Ville.id'), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    mairie_id = db.Column(db.Integer, db.ForeignKey('Mairie_Services.id'), nullable=False)

    # relations 
    depla_F_to_person_optional = relationship("_person_", back_populates="person_to_depla_F_optional", uselist=False, overlaps="person_to_depla_F", viewonly=True)
    depla_F_to_person = relationship("_person_", back_populates="person_to_depla_F", uselist=False, overlaps="person_to_depla_F_optional", viewonly=True)
    depla_F_to_ville = relationship("_ville_", back_populates="ville_to_deplace_F")
    
    def __repr__(self):
        return f"Depla_domicile_F('{self.id}', '{self.person_id}', '{self.ville_id}', '{self.date}', '{self.mairie_id}')"


class _ville_(db.Model):
    __tablename__ = "Ville"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(45), nullable=False)

    # Relations 
    ville_to_deplace_F = relationship("_depla_domicile_F_", back_populates="depla_F_to_ville")
    ville_to_mairie_service = relationship("_mairie_services_", back_populates="mairie_service_to_ville")
    
    def __repr__(self):
        return f"Ville('{self.id}', '{self.nom}')"


class _pays_(db.Model):
    __tablename__ = "pays"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(45), nullable=False)
    Continent_id = db.Column(db.Integer, db.ForeignKey('Continent.id'), primary_key=True)

    # Relations
    continent = relationship("_continent_", back_populates="countries")
    people = relationship("_person_", back_populates="nationalite")
    pays_to_depla = relationship("_depla_etranger_F_", back_populates="depla_to_pays")
    pays_to_depla_A = relationship("_depla_etranger_A_", back_populates="depla_A_to_pays")

    def __repr__(self):
        return f"pays('{self.id}', '{self.nom}', '{self.Continent_id}')"

class _continent_(db.Model):
    __tablename__ = "Continent"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(45), nullable=False)

    # Relations
    countries = relationship("_pays_", back_populates="continent")

    def __repr__(self):
        return f"Continent('{self.id}', '{self.nom}')"


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
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Comment('{self.id_user}', '{self.created_at}', '{self.content}')"