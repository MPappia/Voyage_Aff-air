from ..app import app, db
from Datetime import datetime

class person(db.Model):
    __tablename__ = "Person"
    
    fonction = db.Column
    nom = db.Column
    nationalite_code = db.Column
    Date_debut_mandat = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    Date_fin = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    parti = db.Column(db.String(45, nullable=True)




