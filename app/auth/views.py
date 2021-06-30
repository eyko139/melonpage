from flask import render_template, redirect, request, flash, url_for
from flask_login import login_required, login_user, current_user, logout_user
from app.models import User
from .. import db
from ..email import send_email

from . import auth

@auth.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["user_mail"].lower()).first()
        if user is not None and user.verify_password(request.form["user_password"]):
            login_user(user)
            flash("Loggin successful")
            return redirect(url_for("main.index"))
        else:
            flash("Wrong Username/Password", "error")
    return render_template("auth/login.html")

@auth.route("/logout", methods = ["POST", "GET"])
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("main.index"))

@auth.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        if User.query.filter_by(username=request.form["username_input"]).first() == None and User.query.filter_by(email=request.form["usermail_input".lower()]).first() == None:
            user = User(username=request.form["username_input"],
                        email=request.form["usermail_input"].lower(),
                        password=request.form["userpassword_input"])
            db.session.add(user)
            db.session.commit()
            flash("Registration successful, authentication currently NOT required. You can now login!")
            token = user.generate_confirmation_token()
            send_email(user.email, "Confirm Your Account", "auth/email/confirm", user=user, token=token)
            return redirect(url_for("main.index"))
        else:
            flash("Username already taken or email already registerd", "error")
    return render_template("auth/register.html")


@auth.route("/confirm/<token>")
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for("main.index"))
    if current_user.confirm(token):
        db.session.commit()
        flash("Confirmation successful")
    else:
        flash("something went wrong")
    return redirect(url_for("main.index"))

@auth.route("/forbidden", methods = ["POST", "GET"])
@login_required
def forbidden():
    return "<h>this is forbidden</h>"
