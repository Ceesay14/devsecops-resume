from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# SECURITY FLAW: Hardcoded API Secret Key (Your scanner should catch this!)
API_SECRET_KEY = "SUPER_SECRET_PASSWORD_12345"

def init_db():
    """Ensures the database file and users table exist before handling requests"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Create the table if it's missing to prevent 500 Internal Server errors
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL
        )
    ''')
    # Insert a dummy user to query against if the table was empty
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (username) VALUES ('admin')")
    conn.commit()
    conn.close()

# Initialize database mapping on startup
init_db()

@app.route("/")
def home():
    """New default landing page so the plain IP address doesn't throw a 404"""
    return "Welcome to the DevSecOps Main Application Home! Navigate to /login to test the pipeline."

@app.route("/login")
def login():
    username = request.args.get('username', 'admin') # Default to 'admin' if no parameter passed

    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # SECURITY FLAW: SQL Injection Vulnerability (Your scanner should catch this too!)
        query = f"SELECT * FROM users WHERE username = '{username}'"
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        
        return f"Login Processed - secure continues deployment. Found {len(result)} user(s)."
    except Exception as e:
        return f"Database error encountered: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
