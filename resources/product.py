from flask_restful import Resource
from flask import request
from models.product import Product
from models.db import db

class Products(Resource):
    def get(self):
        data = Product.find_all()
        results = [u.json() for u in data]
        return results
    
    def post(self):
        data = request.get_json()
        product = Product(**data)
        product.create()
        return product.json(), 201
    
class oneProduct(Resource):
    def get(self, id):
        data= Product.find_by_id(id)
        return data.json()
    
    def put(self, id):
        data = request.get_json()
        print(data)
        request_product = Product.find_by_id(id)
        request_product.update(**data)
        return request_product.json(), 200
    
    def delete(self, id):
        response = Product.delete_by_id(id)
        return response