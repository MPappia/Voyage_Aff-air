from ..app import app, db
from Datetime import datetime

class _person_(db.Model):
    __tablename__ = "Person"
    
    fonction = db.Column(db.String(45), nullable=False)
    nom = db.Column(db.String(45), nullable=False)
    # nationalite_code = db.Column
    Date_debut_mandat = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    Date_fin = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    parti = db.Column(db.String(45), nullable=True)

class _mairie_services_(db.Model):
    __tablename__ = "Mairie_Services"

    # Person_id =
    # Ville_id = 
    date_debut_service = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    date_fin_service = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)

class _depla_etranger_F_(db.Model):
    __tablename__ = "Depla_etranger_F"

    # id = 
    # person_id = 
    # pays_id =
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

class _depla_etranger_A_(db.Model):
    __tablename__ = "Depla_etranger_A"

    # id = 
    # Person_id =
    # pays_id =
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class _depla_domicile_F_(db.Model):
    __tablename__ = "Depla_domicile_F"

    # id =
    # Person_id = 
    # Ville_id = 
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # mairie_id = 

class _ville_(db.Model):
    __tablename__ = "Ville"

    # id = 
    nom = db.Column(db.String(45), nullable=False)



class _pays_(db.Model):
    __tablename__ = "pays"

    # id =
    nom = db.Column(db.String(45), nullable=False)
    # Continent_id = 

class _continent_(db.Model):
    __tablename__ = "Continent"

    # id
    nom = db.Column(db.String(45), nullable=False)
