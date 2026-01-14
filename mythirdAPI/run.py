from app import app
import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS etudiants (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, adresse TEXT, pincode TEXT)')
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)