from flask_restful import Resource
from flask import request
from models.message import Message
from models.db import db

class Messages(Resource):
    def post(self):
        data = request.get_json()
        user_id = data.get('user_id')
        receiver_id = data.get('receiver_id')
        content = data.get('content', '')
        new_message = Message(user_id=user_id, receiver_id=receiver_id, content=content)
        new_message.create()
        return new_message.json(), 201