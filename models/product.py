from datetime import datetime
from models.db import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    brand = db.column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer)
    available = db.Column(db.Boolean)
    image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())

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