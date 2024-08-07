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
        user_id = data.get('user_id')
        product_ids = data.get('product_ids', [])
        total_amount = data.get('total_amount')
        order = Order(user_id,product_ids, total_amount)
        order.create()
        return order.json(), 201
    
class SingleOrder(Resource):
    def get(self, id):
        data = Order.find_by_id(id)
        return data.json()
    
    def delete(self, id):
        data = Order.delete_by_id(id)
        return data
    
    def put(self, id):
        print(request.data)
        data = request.get_json()
        product_ids = data.get('product_ids', [])
        user_id = data.get('user_id')
        total_amount = data.get('total_amount')
        order = Order(user_id, product_ids, total_amount)
        order.update_order(id)
        return order.json()