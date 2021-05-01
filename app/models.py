from flask import current_app
import datetime
from . import db

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
    def __repr__(self):
        return "Task: {} - {}".format(self.name, self.task)
