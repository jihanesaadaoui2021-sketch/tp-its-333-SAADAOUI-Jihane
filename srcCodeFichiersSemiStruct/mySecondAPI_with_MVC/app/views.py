from app import app
from flask import render_template, request, jsonify

### EXO1 - simple API
@app.route('/api/simple')
def simple_api():
    return jsonify({"message": "Hello World"})

### EXO2 - API with simple display
@app.route('/simple-display')
def simple_display():
    return render_template('index.html')

### EXO3 - API with parameters display
@app.route('/api/param-display')
def param_display():
    # On définit une variable Python
    nom_utilisateur = "Jihane"
    
    # On transmet cette variable au fichier HTML
    return render_template('index.html', name=nom_utilisateur)

### EXO4 - API with parameters retrieved from URL
@app.route('/api/user/<name>')
def user_profile(name):
    # La variable 'name' est automatiquement récupérée depuis l'URL
    # On l'envoie au template index.html pour l'afficher
    return render_template('index.html', name=name)
