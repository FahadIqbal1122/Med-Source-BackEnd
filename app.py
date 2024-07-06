from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models.db import db

from models.user import User
from models.cart import Cart
from models.message import Message
from models.request_product import Request_Product
from models.medication_list import MedicationList
from models.product import Product
from models.order import Order

from resources.user import Users, SingleUser
from resources.cart import Carts, SingleCart
from resources.medication_list import MedicationLists, SingleMedicationList
from resources.message import Messages
from resources.request_product import Request_Products , check_Request , check_Request
from resources.product import Products , oneProduct , oneProduct
from resources.order import Orders, SingleOrder
from resources.request_product import Request_Products , check_Request
from resources.product import Products , oneProduct
from resources.order import Orders
from resources.request_product import Request_Products , check_Request
from resources.product import Products
from resources.order import Orders

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://osama:admin@localhost:5432/pharmacy_db"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(Users, '/users')
api.add_resource(SingleUser, '/users/<int:id>')
api.add_resource(Carts, '/carts')
api.add_resource(SingleCart, '/carts/<int:id>')
api.add_resource(MedicationLists, '/medication_lists')
api.add_resource(SingleMedicationList, '/medication_lists/<int:id>')
api.add_resource(Messages, '/messages')
api.add_resource(Request_Products, '/request')
api.add_resource(check_Request , '/request/<int:id>')
api.add_resource(check_Request , '/request/<int:id>')
api.add_resource(Products, '/products')
api.add_resource(oneProduct, '/products/<int:id>')
api.add_resource(Orders, '/orders')
api.add_resource(SingleOrder, '/orders/<int:id>')



app.run(debug=True)