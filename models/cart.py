from datetime import datetime
from models.db import db
from flask import request
from models.cartandproductsassoc import cart_product
from models.product import Product

class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    products = db.relationship("Product", secondary=cart_product, back_populates="carts")

    def __init__(self, product_id, total_amount):
        #self.user_id = user_id
        self.total_amount = total_amount
        self.products = [Product.find_by_id(pid) for pid in product_id]

    def json(self):
        return {"id": self.id,
            #"user_id": self.user_id,
            "products": [product.json() for product in self.products],
            "total_amount": self.total_amount}
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @classmethod
    def find_all(cls):
        return Cart.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return db.get_or_404(cls, id, description=f'Record with id:{id} is not available')

    @classmethod
    def delete_by_id(cls, id):
        cart = cls.find_by_id(id)
        if cart:
            db.session.delete(cart)
            db.session.commit()
            return True
        else:
            raise ValueError(f"Cart with ID {id} not found.")
        
    @classmethod
    def update_cart(cls, id):
        cart = db.get_or_404(cls, id, description=f'Record with id:{id} is not available')
        data = request.get_json()
        cart.total_amount = data['total_amount']
        db.session.commit()
        return cart.json()