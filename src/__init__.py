from flask import Flask
from src.config import Config
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
app.config['JWT_SECRET_KEY'] =  Config.JWT_SECRET_KEY
jwt = JWTManager(app)


def register_blueprint(app):
    from src.routes.general import general_blueprint
    from src.routes.email import email
    app.register_blueprint(general_blueprint)
    app.register_blueprint(email)


register_blueprint(app)
