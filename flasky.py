import os 
from app import create_app, db
from app.models import Todo, User, Role, Post
from flask_migrate import Migrate
from flask_migrate import upgrade

app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Todo=Todo, User=User, Role=Role, Post=Post)

@app.cli.command()
def deploy():
    upgrade()

@app.cli.command()
def test():
    #running the unittests
    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)
