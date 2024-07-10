from flask_restful import Resource
from flask import request, jsonify, make_response
from models.user import User
from models.db import db
from sqlalchemy.orm import joinedload
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

class GetUser(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if user:
            return {
                "logged_user": user_id,
                "username": user.first_name,
                "email": user.email,
                "phone_number": user.phone_number,
                "patient": user.patient
            }, 200
        else:
            return {"message": "User not found"}, 404
class Users(Resource):
    def get(self):
        data = User.find_all()
        results = [u.json() for u in data]
        return results
    
    def post(self):
        data = request.get_json()
        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=hashed_password,
            phone_number=data['phone_number'],
            patient=data['patient']

        )
        user.create()
        return user.json(), 201
    
class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user and check_password_hash(user.digest, data['password']):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200
        return {"message": "Invalid email or password"}, 401
        
class SingleUser(Resource):
    def get(self, id):
        data = User.find_by_id(id)
        return data.json()

    def delete(self, id):
        data = User.delete_user(id)
        return data

    def put(self, id):
        updated = User.update_user(id)
        return updated.json(), 201
