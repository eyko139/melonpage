from flask import render_template, redirect, request, url_for, flash
import os
from werkzeug.utils import secure_filename
from .. import db
from . import main
from .forms import SubmitForm
from ..models import Todo, Post
from datetime import datetime
from .. import moment
from flask_login import login_required, current_user
from ..models import User

UPLOAD_FOLDER = "~/Projects"
ALLOWED_EXTENSIONS = {"png", "jpeg", "jpg"}


@main.route("/", methods = ["GET"])
def index():
    return render_template("index.html", current_time=datetime.utcnow().strftime("%Y-%m-%d %H:%M"))
@main.route("/adder", methods = ["GET", "POST"])
def adder():
    form = SubmitForm()
    if form.validate_on_submit():
        try:
            urgency = request.form.get("urgency")
            end_time_str = request.form.get("end_time")
            due_time = request.form.get("timepick")
            combined_time = end_time_str + due_time 

            combined_date = datetime.strptime(combined_time, "%m/%d/%Y%H:%M")
            



            dothat = Todo(name=form.name.data, task=form.task.data, urgency=urgency, starting_time=datetime.utcnow().strftime("%d-%m-%Y %H:%M"), end_time=combined_date)
            db.session.add(dothat)
            db.session.commit()
            flash("Added Todo")
            return redirect(url_for("main.adder"))
        except:
            flash("Error with the selected due Time, required format HH:MM", "error")
    return render_template("adder.html", form = form, current_time=datetime.utcnow().strftime("%Y-%m-%d %H:%M"))


@main.route("/list", methods = ["GET", "POST"])
def list():
    todos=Todo.query.all()
    posts = Post.query.all()
    if request.method == "POST":
        if request.form.get("delete"):
                will_delete = Todo.query.filter_by(id=request.form["delete"]).first()
                db.session.delete(will_delete)
                db.session.commit()
                flash(u"Deleted Todo", "error")
                return redirect(url_for("main.list"))
        if request.form.get("done"):
                finished_todo = Todo.query.filter_by(id=request.form["done"]).first()
                finished_todo.status = True
                finished_todo.completion_time = datetime.now() 
                db.session.commit()
                flash("Finished Todo", "completed")
                return redirect(url_for("main.list"))

        if "post_comment" in request.form:
                post = Post(body=request.form["comment_body"],
                            author=current_user._get_current_object(),
                            related_todo=request.form["post_comment"])
                db.session.add(post)
                db.session.commit()
                flash("Added comment", "add")
                return redirect(url_for("main.list"))
        

    return render_template("list.html", todos=todos, current_time=datetime.utcnow(), posts=posts) 

@main.route("/completed", methods = ["GET", "POST"])
def completed():
    todos = Todo.query.all()
    if request.method == "POST":
        if request.form.get("delete"):
            will_delete = Todo.query.filter_by(id=request.form["delete"]).first()
            db.session.delete(will_delete)
            db.session.commit()
            flash(u"Permanently deleted Todo", "error")
            return redirect(url_for("main.completed"))

    return render_template("completed.html", todos=todos)

@main.route("/finance", methods = ["GET", "POST"])
@login_required
def finance():
    return render_template("finance.html")

@main.route("/upload", methods = ["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":
        file = request.files["fileupload"]
        file.save(os.path.join("app/static/receipts", str(datetime.now())))
        return redirect(url_for("main.upload"))

    files = os.listdir("app/static/receipts")
    return render_template("upload.html", files=files)

@main.route("/maos", methods = ["GET", "POST"])
def maos():
    return render_template("maos.html")

@main.route("/maos/<mao>", methods = ["GET", "POST"])
def mao_compare():
    maos = os.listdir("app/static/pics")
    return render_template("mao_compare.html")

@main.route("/user/<username>")
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template("user.html", user=user)
