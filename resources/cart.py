from flask_restful import Resource
from flask import request
from models.cart import Cart
from models.db import db

class Carts(Resource):
    def get(self):
        data = Cart.find_all()
        results = [u.json() for u in data]
        return results
    
    def post(self):
        data = request.get_json()
        cart = Cart(**data)
        cart.create()
        return cart.json(), 201