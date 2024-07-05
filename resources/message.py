from flask_restful import Resource
from flask import request
from models.message import Message
from models.db import db

class Messages(Resource):
    def get(self):
        data = Message.find_all()
        results = [u.json() for u in data]
        return results
    
    def post(self):
        data = request.get_json()
        cart = Message(**data)
        cart.create()
        return cart.json(), 201