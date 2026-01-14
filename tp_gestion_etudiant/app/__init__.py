from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restx import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'secret-its2' 

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Correction Swagger : On utilise l'API pour déclarer les routes après
api = Api(app, doc='/api/docs', title='API Gestion Étudiants ITS2')

from app import views, models