from flask import Blueprint

covid = Blueprint("covid", __name__)

from . import views
