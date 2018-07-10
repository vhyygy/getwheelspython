from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from getwheels.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
ma = Marshmallow()


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	
	db.init_app(app)
	ma.init_app(app)
	bcrypt.init_app(app)
	mail.init_app(app)

	from getwheels.users.routes import users

	app.register_blueprint(users)

	return app