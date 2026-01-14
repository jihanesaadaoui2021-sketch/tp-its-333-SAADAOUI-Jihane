from app import db

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    # Relation : Un groupe vers plusieurs étudiants
    etudiants = db.relationship('Etudiant', backref='groupe', lazy=True)

class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    adresse = db.Column(db.String(200))
    pincode = db.Column(db.String(10))
    # Clé étrangère vers le groupe
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))