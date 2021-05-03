from flask import render_template, redirect, request
from flask_login import login_required, login_user, current_user
from app.models import User

from . import auth

@auth.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["user_mail"]).first()
        if user is not None and user.verify_password(request.form["user_password"]):
            login_user(user)
            return "<h1>Hello {}</h1>".format(current_user)
    return render_template("auth/login.html")

@auth.route("/logout", methods = ["POST", "GET"])
def logout():
    return "<h1>goodbye</h1>"


@auth.route("/forbidden", methods = ["POST", "GET"])
@login_required
def forbidden():
    return "<h>this is forbidden</h>"
