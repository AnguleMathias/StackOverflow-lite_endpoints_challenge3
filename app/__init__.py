from flask import Flask
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)

from app.auth.authentication import auth_blueprint
from app.views.questions import question_blueprint
from app.views.answers import answer_blueprint
from app.views.comments import comment_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(question_blueprint)
app.register_blueprint(answer_blueprint)
app.register_blueprint(comment_blueprint)
app.config['ENV'] = os.getenv('ENV')

app.config['JWT_SECRET_KEY'] = 'qwertyuiop'
from flask_jwt_extended import JWTManager
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
