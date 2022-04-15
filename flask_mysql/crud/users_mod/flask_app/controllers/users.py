from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html")