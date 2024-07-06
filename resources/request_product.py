from flask_restful import Resource
from flask import request
from models.request_product import Request_Product
from models.db import db

class Request_Products(Resource):
    def get(self):
        print(request.method)
        print(request.method)
        data = Request_Product.find_all()
        results = [u.json() for u in data]
        return results
    
    def post(self):
        data = request.get_json()
        cart = Request_Product(**data)
        cart.create()

class check_Request(Resource):
    def get(self, id):
        data= Request_Product.find_by_id(id)
        return data.json()
    
    def put(self, id):
        data = request.get_json()
        request_product = Request_Product.find_by_id(id)
        request_product.update(**data)
        return request_product.json(), 200
    
    def delete(self, id):
        response = Request_Product.delete_by_id(id)
        return response

class check_Request(Resource):
    def get(self, id):
        data= Request_Product.find_by_id(id)
        return data.json()
    
    def put(self, id):
        data = request.get_json()
        request_product = Request_Product.find_by_id(id)
        request_product.update(**data)
        return request_product.json(), 200
    
    def delete(self, id):
        response = Request_Product.delete_by_id(id)
        return response
