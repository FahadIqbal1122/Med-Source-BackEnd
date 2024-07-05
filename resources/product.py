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