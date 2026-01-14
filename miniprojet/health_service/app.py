import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
health_db = {}  # Stockage en mémoire (ID: Données)

def check_person_exists(person_id):
    try:
        # Communication inter-service via l'hôte Docker
        url = f"http://host.docker.internal:5001/persons/{person_id}"
        response = requests.get(url, timeout=2)
        return response.status_code == 200
    except:
        return False

@app.route('/health/<int:person_id>', methods=['GET'])
def get_health(person_id):
    # Renvoie les données ou des tirets si vide
    data = health_db.get(person_id, {"poids": "-", "taille": "-"})
    return jsonify(data), 200

@app.route('/health/<int:person_id>', methods=['POST'])
def save_health(person_id):
    if not check_person_exists(person_id):
        return jsonify({"error": "Personne inexistante"}), 404
    health_db[person_id] = request.json
    return jsonify({"status": "Données enregistrées"}), 200

@app.route('/health/<int:person_id>', methods=['DELETE'])
def delete_health(person_id):
    if person_id in health_db:
        del health_db[person_id]
    return jsonify({"status": "Santé supprimée"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)