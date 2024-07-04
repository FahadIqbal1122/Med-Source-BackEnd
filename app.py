from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models.db import db
from models.user import User
from resources.user import Users

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://osama:admin@localhost:5432/pharmacyDb"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(Users, '/users')






app.run(debug=True)