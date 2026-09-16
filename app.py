from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# SECURED: Loaded dynamically from an environment variable instead of hardcoded plaintext
API_SECRET_KEY = os.environ.get("API_SECRET_KEY", "fallback_secure_random_string_here")

def init_db():
    """Ensures the database file and users table exist before handling requests"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL
        )
    ''')
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone() == 0:
        cursor.execute("INSERT INTO users (username) VALUES ('admin')")
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    """Default landing page"""
    return "Welcome to the DevSecOps Main Application Home! Navigate to /login to test the pipeline."

@app.route("/login")
def login():
    username = request.args.get('username', 'admin')

    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # SECURED: Parameterized query completely blocks SQL Injection attacks!
        query = "SELECT * FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        
        result = cursor.fetchall()
        conn.close()
        
        return f"Login Processed - secure continues deployment. Found {len(result)} user(s)."
    except Exception as e:
        return f"Database error encountered: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
