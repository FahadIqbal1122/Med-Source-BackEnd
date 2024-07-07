from datetime import datetime
from models.db import db
from flask import request
from models.orderandproductsassocs import order_product
import models.product as Product

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    products = db.relationship("Product", secondary=order_product, back_populates="orders")

    def __init__(self, user_id, product_id, total_amount):
        self.user_id = user_id
        self.products = [Product.find_by_id(pid) for pid in product_id]
        self.total_amount = total_amount

    def json(self):
        return {"id": self.id,
            "user_id": self.user_id,
            "products": [product.json() for product in self.products],
            "total_amount": self.total_amount}
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @classmethod
    def find_all(cls):
        return Order.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        order = Order.query.filter_by(id=id).first()
        return order
    
    @classmethod
    def delete_by_id(cls, id):
        order = cls.find_by_id(id)
        if order:
            db.session.delete(order)
            db.session.commit()
            return True
        else:
            raise ValueError(f"Order with ID {id} not found.")
        
    @classmethod
    def update_order(cls, id):
        order = db.get_or_404(cls, id, description=f'Record with id:{id} is not available')
        data = request.get_json()
        order.total_amount = data['total_amount']
        db.session.commit()
        return order.json()