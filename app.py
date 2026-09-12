from flask import Flask, request
import sqlite3

app = Flask(__name__)

# SECURITY FLAW: Hardcoded API Secret Key (Your scanner should catch this!)
API_SECRET_KEY = "SUPER_SECRET_PASSWORD_12345"

@app.route("/login")
def login():
    username = request.args.get('username')
    
    # SECURITY FLAW: SQL Injection Vulnerability (Your scanner should catch this too!)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    return "Login Processed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
