from flask_login import UserMixin
from flask import current_app
import datetime
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    users = db.relationship("User", backref="role", lazy="dynamic")
    
    def __repr__(self):
        return "{}".format(self.name)
    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, index=True)
    email = db.Column(db.String(128), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    member_since = db.Column(db.DateTime(), default=datetime.datetime.now)
    about_me = db.Column(db.Text())

    def __repr__(self):
        return "User:{}, email: {}, role: {}".format(self.username, self.email, self.role_id)
    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    #this registers the function with Flask Login, it will be called to retrieve info about the currently logged-in user
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config["SECRET_KEY"], expiration)
        return s.dumps({"confirm": self.id}).decode("utf-8")

    def confirm(self, token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token.encode("utf-8"))
        except:
            return False
        if data.get("confirm") != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, unique = False)
    task = db.Column(db.String(128), index = True, unique = False)
    #is_completed = db.Column(db.Boolean, default = False, nullable=True)
    start_time = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)
    starting_time = db.Column(db.String(128), index = True, unique = False)
    urgency = db.Column(db.String(128), index = True, unique = False)
    end_time = db.Column(db.DateTime(128), nullable=True, unique= False, index=True)
    status = db.Column(db.Boolean, default=False)
    completion_time = db.Column(db.DateTime(timezone=True))
    #insert onupdate current_timestamp
    #due_date = db.Column(db.Date, nullable=True)
    newcol = db.Column(db.String(128))
    def __repr__(self):
        return "Task: {} - {}".format(self.name, self.task)


#this is even worse

