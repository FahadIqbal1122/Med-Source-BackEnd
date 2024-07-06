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
        cart = Request_Product(**data)
        cart.create()
        return cart.json(), 201

class check_Request(Resource):
    def get(self, id):
        data= Request_Product.find_by_id(id)
        return data.json()