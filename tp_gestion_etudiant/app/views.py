from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Etudiant, Group

@app.route('/')
def index():
    # Récupère tous les étudiants pour les afficher
    tous_les_etudiants = Etudiant.query.all()
    return render_template('index.html', etudiants=tous_les_etudiants)

@app.route('/new')
def new():
    # Envoie la liste des groupes au formulaire
    groupes = Group.query.all()
    return render_template('new.html', groupes=groupes)

@app.route('/add', methods=['POST'])
def add():
    # Création d'un nouvel étudiant via le formulaire
    nouvel_etudiant = Etudiant(
        nom=request.form['nom'],
        adresse=request.form['adresse'],
        pincode=request.form['pincode'],
        group_id=request.form['group_id']
    )
    db.session.add(nouvel_etudiant)
    db.session.commit()
    return redirect(url_for('index'))