from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models.db import db

from models.user import User
from models.cart import Cart
from models.medication_list import MedicationList
from resources.product import Products

from resources.user import Users
from resources.cart import Carts
from resources.medication_list import MedicationLists
from resources.product import Products

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://fahad:admin@localhost:5432/pharmacy_db"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(Users, '/users')
api.add_resource(Carts, '/carts')
api.add_resource(MedicationLists, '/medication_lists')
api.add_resource(Products, '/products')




app.run(debug=True)