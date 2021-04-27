import sqlite3
from flask import Flask, redirect, url_for, render_template, request, g

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("homePage.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/admin_login")
def admin_login():
    return render_template("admin_login.html")


@app.route("/contact us")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
