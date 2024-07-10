from datetime import datetime
from models.db import db
from flask import request
from models.cartandproductsassoc import cart_product
from models.product import Product

class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    total_amount = db.Column(db.Float, nullable=False)
    products = db.relationship("Product", secondary=cart_product, back_populates="carts")
    user = db.relationship("User", back_populates="cart", uselist=True)

    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.products = []
        self.calculate_total_amount()

    def json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "products": [product.json() for product in self.products],
            "total_amount": self.total_amount
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def calculate_total_amount(self):
        self.total_amount = sum(product.price for product in self.products)

    def update_products(self, product_ids):
        new_products = [Product.find_by_id(pid) for pid in product_ids]
        self.products.extend(new_products)
        self.calculate_total_amount()

    def remove_product(self, product_id):
        product = Product.query.get(product_id)
        print(product)
        if product:
            if product in self.products:
                self.products.remove(product)
                self.calculate_total_amount()
                return self
        
    @classmethod    
    def find_by_user_id(cls, user_id):
        temp=cls.query.filter_by(user_id=user_id).first()
        return temp
    
    @classmethod
    def find_all(cls):
        return Cart.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(user_id=id).first()

    @classmethod
    def update_cart(cls, id):
        cart = cls.find_by_user_id(id)
        if not cart:
            return None
        data = request.get_json()
        product_ids = data.get('product_id', [])
        cart.update_products(product_ids)
        db.session.commit()
        return cart
    
    @classmethod
    def remove_from_cart(cls, user_id, product_id):
        cart = cls.find_by_user_id(user_id)
        if not cart:
            return {"message": f"Cart for user ID {user_id} not found"}, 404
        cart.remove_product(product_id)
        db.session.commit()
        return cart.json(), 200
