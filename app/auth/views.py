from flask import render_template

from . import auth

@auth.route("/login", methods = ["POST", "GET"])
def login():
    return render_template("auth/login.html")
