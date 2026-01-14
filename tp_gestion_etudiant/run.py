from app import app, db
from app.models import Group, Etudiant

with app.app_context():
    db.create_all()
    if not Group.query.filter_by(name='ITS2').first():
        its2 = Group(name='ITS2')
        db.session.add(its2)
        db.session.add(Etudiant(nom="Jihane Saadaoui", adresse="Chevilly-Larue", pincode="94550", group_id=1))
        db.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)