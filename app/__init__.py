from flask import Flask

app = Flask(__name__)

from app.auth.authentication import auth_blueprint

app.register_blueprint(auth_blueprint)
