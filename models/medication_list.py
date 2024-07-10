from datetime import datetime
from models.db import db
from flask import request
from models.listandprodassoc import list_product
from models.product import Product


class MedicationList(db.Model):
    __tablename__ = 'medication_list'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    products = db.relationship("Product", secondary=list_product, back_populates="medication_list")

    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.products = []
        self.calculate_total_amount()

    def json(self):
        return {"id": self.id,
            "user_id": self.user_id,
            "products": [product.json() for product in self.products],
            "total_amount": self.total_amount,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)}
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def calculate_total_amount(self):
        self.total_amount = sum(product.price for product in self.products)
    
    def update_products(self, product_ids):
        new_products = [Product.find_by_id(pid) for pid in product_ids]
        self.products.extend(new_products)

    def remove_product(self, product_id):
        product = Product.query.get(product_id)
        print(product)
        if product:
            if product in self.products:
                self.products.remove(product)
                return self

    
    @classmethod
    def find_by_user_id(cls, user_id):
        temp=cls.query.filter_by(user_id=user_id).first()
        return temp
    
    @classmethod
    def find_all(cls):
        return MedicationList.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return db.get_or_404(cls, id, description=f'Record with id:{id} is not available')
        
    @classmethod
    def update_medication_list(cls, id):
        medication_list = cls.find_by_user_id(id)
        data = request.get_json()
        product_ids = data.get('product_ids', [])
        medication_list.update_products(product_ids)
        db.session.commit()
        return medication_list.json()
        
    @classmethod
    def remove_from_medication_list(cls, user_id, product_id):
        medication_list = cls.find_by_user_id(user_id)
        if not medication_list:
            return {"message": f"Medication List for user ID {user_id} not found"}, 404
        medication_list.remove_product(product_id)
        db.session.commit()
        return medication_list.json(), 200

