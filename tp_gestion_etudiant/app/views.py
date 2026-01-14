from flask import render_template, request, redirect, url_for, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_restx import Resource
from app import app, db, api
from app.models import Etudiant, Group

# Point 2 : Route pour obtenir un Token JWT
@app.route('/login-api', methods=['POST'])
def login_api():
    return jsonify(access_token=create_access_token(identity="admin"))

# Point 3 : Routes déclarées dans Swagger (api.route)
@api.route('/api/students')
class StudentList(Resource):
    def get(self):
        """Liste des étudiants pour Swagger"""
        return [{"id": s.id, "nom": s.nom} for s in Etudiant.query.all()]

# Route pour ton interface Web
@app.route('/')
def index():
    return render_template('index.html', etudiants=Etudiant.query.all(), groupes=Group.query.all())

@app.route('/add', methods=['POST'])
def add():
    new_e = Etudiant(nom=request.form['nom'], adresse=request.form['adresse'], 
                     pincode=request.form['pincode'], group_id=request.form['group_id'])
    db.session.add(new_e)
    db.session.commit()
    return redirect(url_for('index'))