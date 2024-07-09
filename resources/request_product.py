from flask_restful import Resource
from flask import request
from models.request_product import Request_Product
from models.db import db

class Request_Products(Resource):
    def get(self):
        print(request.method)
        data = Request_Product.find_all()
        results = [u.json() for u in data]
        return results
    
    def post(self):
        data = request.get_json()
        product_ids = data.get('product_ids', [])    
        user_id = data.get('user_id')
        cart = Request_Product( product_ids, user_id)
        cart.create()
        print(cart.json())
        return cart.json(), 201

class check_Request(Resource):
    def get(self, id):
        data = Request_Product.find_by_user_id(id)
        if data:
            results = [request_product.json() for request_product in data]
            return results, 200
        return {"message": "No requests found for the provided user ID"}, 404
    
    def put(self, id):
        data = request.get_json()
        request_product = Request_Product.find_by_id(id)
        request_product.update(**data)
        return request_product.json(), 200
    
    def delete(self, id):
        response = Request_Product.delete_by_id(id)
        return response

