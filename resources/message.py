from flask_restful import Resource
from flask import request
from models.message import UserMessage
from models.db import db

class UserMessages(Resource):

    def get(self):
        messages = UserMessage.find_all()
        return [message.json() for message in messages]

    def post(self):
        data = request.get_json()
        user_id = data.get('user_id')
        receiver_id = data.get('receiver_id')
        content = data.get('content', '')
        new_message = UserMessage(user_id=user_id, receiver_id=receiver_id, content=content)
        new_message.create()
        return new_message.json(), 201