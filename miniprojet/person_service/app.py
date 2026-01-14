from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Autorise les requêtes du navigateur
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/persons', methods=['POST'])
def create_person():
    data = request.json
    new_p = Person(name=data.get('name'))
    db.session.add(new_p)
    db.session.commit()
    return jsonify({"id": new_p.id, "name": new_p.name}), 201

@app.route('/persons', methods=['GET'])
def list_persons():
    persons = Person.query.all()
    return jsonify([{"id": p.id, "name": p.name} for p in persons]), 200

@app.route('/persons/<int:id>', methods=['GET'])
def get_person(id):
    p = Person.query.get(id)
    return jsonify({"id": p.id, "name": p.name}) if p else (jsonify({"error": "Non trouvé"}), 404)

@app.route('/persons/<int:id>', methods=['DELETE'])
def delete_person(id):
    p = Person.query.get(id)
    if p:
        db.session.delete(p)
        db.session.commit()
        return jsonify({"msg": "Supprimé"}), 200
    return jsonify({"error": "Non trouvé"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)