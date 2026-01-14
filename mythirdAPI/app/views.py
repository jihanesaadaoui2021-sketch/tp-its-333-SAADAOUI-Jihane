from flask import render_template, request, redirect, url_for
from app import app
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    etudiants = conn.execute('SELECT * FROM etudiants').fetchall()
    conn.close()
    return render_template('index.html', etudiants=etudiants)

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/add', methods=['POST'])
def add():
    nom = request.form['nom']
    adresse = request.form['adresse']
    pincode = request.form['pincode']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO etudiants (nom, adresse, pincode) VALUES (?, ?, ?)',
                 (nom, adresse, pincode))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))