from flask_restful import Resource
from flask import request
from models.order import Order
from models.db import db

class Orders(Resource):
    def get(self):
        data = Order.find_all()
        results = [u.json() for u in data]
        return results
    
    def post(self):
        data = request.get_json()
        cart = Order(**data)
        cart.create()
        return cart.json(), 201