from flask import render_template, redirect, url_for, request, flash
import os
from .. import db
from . import auth
from ..models import Todo


@auth.route("/register", methods=["GET", "POST"])
def register():
    pass

@auth.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("auth/login.html")
