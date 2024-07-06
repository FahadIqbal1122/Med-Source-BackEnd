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
        product_ids = data.get('product_ids', [])
        total_amount = data.get('total_amount')
        cart = Cart(product_ids, total_amount)
        cart.create()
        return cart.json(), 201
    
class SingleCart(Resource):
    def get(self, id):
        data = Cart.find_by_id(id)
        return data.json()

    def delete(self, id):
        data = Cart.delete_by_id(id)
        return data
    
    def put(self, id):
        updated = Cart.update_cart(id)
        return updated