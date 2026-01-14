from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restx import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'ma_cle_secrete' 

db = SQLAlchemy(app)
jwt = JWTManager(app)
# SwaggerUI sera disponible sur /api/docs
api = Api(app, doc='/api/docs', title='API Gestion Étudiants', description='Documentation SwaggerUI')

from app import views, models