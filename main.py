from flask import Flask, render_template, url_for, request, jsonify, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SECRET_KEY'] = 'dev-secret-key'
db = SQLAlchemy(app)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tcg_store"
    )

def hash_password(password):
    ph = PasswordHasher()
    return ph.hash(password)

@app.route("/")
def home():
    pass



if __name__ == "__main__":
    app.run(debug=True)