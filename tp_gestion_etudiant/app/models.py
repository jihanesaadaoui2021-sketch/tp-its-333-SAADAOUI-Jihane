from app import db

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    students = db.relationship('Etudiant', backref='groupe', lazy=True)

class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    adresse = db.Column(db.String(200))
    pincode = db.Column(db.String(10))
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))