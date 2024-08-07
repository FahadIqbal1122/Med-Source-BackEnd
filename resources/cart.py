from flask_restful import Resource
from flask import request
from models.cart import Cart
from models.db import db
from sqlalchemy.orm import joinedload
from models.product import Product

class Carts(Resource):
    def get(self):
        data = Cart.find_all()
        results = [u.json() for u in data]
        return results
    
    def post(self):
        data = request.get_json()
        user_id = data.get("user_id")
        product_id = data.get('product_id', [])
        cart = Cart(user_id, product_id)
        cart.create()
        return cart.json(), 201
    
class SingleCart(Resource):
    def get(self, id):
        data = Cart.find_by_user_id(id)
        return data.json()
  
    
    def put(self, id):
        updated = Cart.update_cart(id)
        if not updated:
            return {"message": "Cart not found"}, 404
        return updated
    
class DelSingleCart(Resource):

    def put(self, user_id, product_id):
        remove = Cart.remove_from_cart(user_id,product_id)
        return remove