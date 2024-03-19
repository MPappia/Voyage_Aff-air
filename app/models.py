from app import app, db
from datetime import datetime
from sqlalchemy.orm import relationship

class _person_(db.Model):
    __tablename__ = "Person"
    
    id = db.Column(db.Integer, primary_key=True)
    fonction = db.Column(db.String(45), nullable=False)
    nom = db.Column(db.String(45), nullable=False)
    nationalite_code = db.Column(db.String(45), db.ForeignKey('pays.id'), nullable=False)
    Date_debut_mandat = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    Date_fin = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    parti = db.Column(db.String(45), nullable=True)

    # Relations 
    nationalite = relationship("_pays_", back_populates="people")
    person_to_depla = relationship("_depla_etranger_F_", back_populates="depla_to_person")
    person_to_depla_A = relationship("_depla_etranger_A_", back_populates="depla_A_to_person")
    person_to_depla_F = relationship("_depla_domicile_F_", back_populates="depla_F_to_person")
    
    def __repr__(self):
        return f"Person('{self.id}', '{self.fonction}', '{self.nom}', '{self.Date_debut_mandat}', '{self.Date_fin}', '{self.parti}')"

class _mairie_services_(db.Model):
    __tablename__ = "Mairie_Services"

    # Person_id =
    # Ville_id = 
    id = db.Column(db.Integer, primary_key=True)
    date_debut_service = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    date_fin_service = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)

    def __repr__(self):
        return f"Mairie_services('{self.id}', '{self.date_debut_service}', '{self.date_fin_service}')"

class _depla_etranger_F_(db.Model):
    __tablename__ = "Depla_etranger_F"
    
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('Person.id'), nullable=False)
    pays_id = db.Column(db.Integer, db.ForeignKey('pays.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relations
    depla_to_pays = relationship("_pays_", back_populates="pays_to_depla")
    depla_to_person = relationship("_person_", back_populates="person_to_depla")


    def __repr__(self):
        return f"Depla_etranger_F('{self.id}', '{self.person_id}', '{self.pays_id}', '{self.date}')"


class _depla_etranger_A_(db.Model):
    __tablename__ = "Depla_etranger_A"

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('Person.id'), nullable=False)
    pays_id = db.Column(db.Integer, db.ForeignKey('pays.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relations
    depla_A_to_person = relationship("_person_", back_populates="person_to_depla_A")
    depla_A_to_pays = relationship("_pays_", back_populates="pays_to_depla_A")

    def __repr__(self):
        return f"Depla_etranger_A('{self.id}', '{self.person_id}', '{self.pays_id}', '{self.date}')"

class _depla_domicile_F_(db.Model):
    __tablename__ = "Depla_domicile_F"

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('Person.id'), nullable=False)
    ville_id = db.Column(db.Integer, db.ForeignKey('Ville.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    mairie_id = db.Column(db.Integer, db.ForeignKey('Mairie_Services.id'), nullable=False)

    # relations 
    depla_F_to_person = relationship("_person_", back_populates="person_to_depla_F")
    depla_F_to_ville = relationship("_ville_", back_populates="ville_to_deplace_F")
    
    def __repr__(self):
        return f"Depla_domicile_F('{self.id}', '{self.person_id}', '{self.ville_id}', '{self.date}', '{self.mairie_id}')"
    
class _ville_(db.Model):
    __tablename__ = "Ville"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(45), nullable=False)

    # Relations 
    ville_to_deplace_F = relationship("_depla_domicile_F_", back_populates="depla_F_to_ville")
    
    def __repr__(self):
        return f"Ville('{self.id}', '{self.nom}')"


class _pays_(db.Model):
    __tablename__ = "pays"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(45), nullable=False)
    Continent_id = db.Column(db.Integer, db.ForeignKey('Continent.id'), nullable=False)

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
    

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    nom_user = db.Column(db.String(35))
    prenom_user = db.Column(db.String(35))
    email_user = db.Column(db.String(35), unique=True, nullable=False)
    pseudo_user = db.Column(db.String(35), unique=True, nullable=False)
    password_user = db.Column(db.String(35), nullable=False)
    id_role = db.Column(db.Integer, db.ForeignKey('role.id_role'))


class Role(db.Model):
    id_role = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(35))
    is_admin = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(35))
