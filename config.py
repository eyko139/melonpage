import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "string"
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "achgag418@gmail.com"
    MAIL_PASSWORD = "grag123grag"
    FLASKY_MAIL_SUBJECT_PREFIX = "You added a new task"
    FLASKY_MAIL_SENDER = "achgag418@gmail.com"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI  = "sqlite:///" + os.path.join(basedir, "bibi.db")

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI  = "sqlite:///" + os.path.join(basedir, "testing.db")




config = {
        "development": DevelopmentConfig,
        "default": DevelopmentConfig,
        "testing": TestingConfig,
        }
