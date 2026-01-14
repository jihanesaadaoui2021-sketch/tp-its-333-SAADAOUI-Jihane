from app import app
from flask import render_template, abort

# 1. Base de données avec tes noms spécifiques
data_sante = {
    "jihane": {
        "tension": "12/8", 
        "pouls": 75, 
        "poids": 69,
        "groupe": "A+"
    },
    "siham": {
        "tension": "11/7", 
        "pouls": 70, 
        "poids": 55,
        "groupe": "O+"
    },
    "hafsa": {
        "tension": "13/8", 
        "pouls": 80, 
        "poids": 62,
        "groupe": "B+"
    },
    "soundouss": {
        "tension": "12/7", 
        "pouls": 72, 
        "poids": 65,
        "groupe": "AB-"
    }
}

# 2. La route pour afficher le site web
@app.route('/sante/<nom>/<mesure>')
def consulter_sante_web(nom, mesure):
    # On cherche la personne (en minuscule pour éviter les erreurs de frappe)
    personne = data_sante.get(nom.lower())
    
    if personne:
        # On cherche la mesure précise demandée (poids, tension, pouls, ou groupe)
        valeur = personne.get(mesure.lower())
        
        if valeur:
            # On envoie les données au fichier HTML 'sante.html'
            return render_template(
                'sante.html', 
                nom=nom, 
                type_donnee=mesure, 
                valeur=valeur
            )
    
    # Message si le nom ou la donnée n'existe pas
    return f"Désolé, aucune donnée trouvée pour {nom} concernant : {mesure}", 404