from flask import render_template, request, redirect, url_for, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from app import app, db
from app.models import Etudiant, Group

# Route pour obtenir un Token JWT
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # Test simple : admin / admin
    if username == "admin" and password == "admin":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Identifiants incorrects"}), 401

@app.route('/')
def index():
    tous_les_etudiants = Etudiant.query.all()
    return render_template('index.html', etudiants=tous_les_etudiants)

# Route protégée par JWT pour l'ajout (côté API)
@app.route('/api/add', methods=['POST'])
@jwt_required()
def api_add_student():
    data = request.json
    nouvel_etudiant = Etudiant(
        nom=data['nom'],
        adresse=data['adresse'],
        pincode=data['pincode'],
        group_id=data['group_id']
    )
    db.session.add(nouvel_etudiant)
    db.session.commit()
    return jsonify({"msg": "Étudiant ajouté avec succès via JWT"}), 201