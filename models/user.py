from datetime import datetime
from models.db import db
from flask import request
from models.order import Order

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(255))
    digest = db.Column(db.String(255))
    phone_number=db.Column(db.Integer)
    patient = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    cart = db.relationship("Cart", back_populates="user", uselist=False)
    orders = db.relationship("Order", back_populates="user", cascade="all, delete-orphan")
    requests = db.relationship("Request_Product", cascade="all", back_populates="user")


    def __init__(self, first_name, last_name, email, password, phone_number, patient=False):
        self.first_name= first_name
        self.last_name = last_name
        self.email = email
        self.digest = password
        self.phone_number = phone_number
        self.patient = patient

    def json(self):
        
        return {"id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "Mobile": self.phone_number,
            "patient": self.patient,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)}
        
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @classmethod
    def find_all(cls):
        return User.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        user = User.query.filter_by(id=id).first()
        return user
    
    @classmethod
    def update_user(cls, id):
        user = db.get_or_404(cls, id, description=f'Record with id:{id} is not available')
        data = request.get_json()
        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.digest = data['password']
        user.phone_number = data['phone_number']
        db.session.commit()
        return user.json()

    @classmethod
    def delete_user(cls, id):
        user = db.get_or_404(cls, id, description=f'Record with id:{id} is not available')
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User Deleted'}, 204
    