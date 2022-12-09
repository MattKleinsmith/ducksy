from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from .models import db, User
from .config import Config
from .routes import api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
app.register_blueprint(api.bp)
db.init_app(app)
migrate = Migrate(app, db)


login = LoginManager(app)
login.login_view = "session.login"


@app.route("/")
def index():
    return "<h1>Root page</h1>"


@app.route("/success")
def success():
    return "<h1>Successful login</h1>"


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
