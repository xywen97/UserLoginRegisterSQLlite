from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.database = 'users.db'

def init_db():
    with sqlite3.connect(app.database) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)
        conn.commit()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        with sqlite3.connect(app.database) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (username, password) VALUES (?, ?)
            """, (username, hashed_password))
            conn.commit()
            return redirect(url_for('login'))
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        with sqlite3.connect(app.database) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM users WHERE username = ? AND password = ?
            """, (username, hashed_password))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user[0]
                return redirect(url_for('home'))
            else:
                return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        with sqlite3.connect(app.database) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM users WHERE id = ?
            """, (session['user_id'],))
            user = cursor.fetchone()
            return render_template('home.html', username=user[1])
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run()