from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Cherche le fichier index.html juste à côté de ce script
    return send_from_directory(os.getcwd(), 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)