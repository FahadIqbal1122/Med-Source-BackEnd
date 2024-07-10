from datetime import datetime
from models.db import db
from models.cartandproductsassoc import cart_product
from models.listandprodassoc import list_product
from models.orderandproductsassocs import order_product
from models.requestandproductassocs import request_product_assoc

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(80))
    brand = db.Column(db.String(80))
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer)
    available = db.Column(db.Boolean)
    image = db.Column(db.String(255))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable = True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    carts = db.relationship("Cart", secondary=cart_product, back_populates="products")
    medication_list = db.relationship("MedicationList", secondary=list_product, back_populates="products")
    orders = db.relationship("Order", secondary=order_product, back_populates="products")
    request_products= db.relationship("Request_Product", secondary=request_product_assoc, back_populates="products")


    def __init__(self, name, description, category, brand, price, quantity, available, image):
        self.name = name
        self.description = description
        self.category = category
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.available = available
        self.image = image

    def json(self):
        return {"id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "brand": self.brand,
            "price": self.price,
            "quantity": self.quantity,
            "available": self.available,
            "image": self.image,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)}
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, name, description, category, brand, price, quantity, available, image):
        self.name = name
        self.description = description
        self.category = category
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.available = available
        self.image = image
        db.session.commit()
        return self
        
    @classmethod
    def find_all(cls):
        return Product.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return db.get_or_404(cls, id, description=f'Record with id:{id} is not available')
    
    @classmethod
    def delete_by_id(cls, id):
        product = cls.find_by_id(id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        else:
            raise ValueError(f"Product with ID {id} not found.")
