from app import app, db
from app.models import Group, Etudiant

# Dictionnaire de ton groupe pour l'injection automatique
MEMBRES_ITS2 = [
    {"nom": "Jihane", "adresse": "Paris", "pincode": "75000"},
    {"nom": "Hafsa", "adresse": "Chevilly-larue", "pincode": "94550"},
    {"nom": "Siham", "adresse": "Créteil", "pincode": "94000"}
]

def setup_app():
    with app.app_context():
        db.create_all()
        # Créer le groupe ITS2 s'il n'existe pas
        its2 = Group.query.filter_by(name='ITS2').first()
        if not its2:
            its2 = Group(name='ITS2')
            db.session.add(its2)
            db.session.commit()

        # Ajouter les membres si la table est vide
        if Etudiant.query.count() == 0:
            for m in MEMBRES_ITS2:
                db.session.add(Etudiant(nom=m['nom'], adresse=m['adresse'], 
                                        pincode=m['pincode'], group_id=its2.id))
            db.session.commit()
            print("Base initialisée avec les membres du dictionnaire.")

if __name__ == '__main__':
    setup_app()
    app.run(debug=True)