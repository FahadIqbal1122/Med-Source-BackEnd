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

    def __init__(self, user_id, total_amount, product_id):
        self.user_id = user_id
        self.products = [Product.find_by_id(pid) for pid in product_id]
        self.total_amount = 0.0

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
    
    @classmethod
    def find_all(cls):
        return MedicationList.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return db.get_or_404(cls, id, description=f'Record with id:{id} is not available')
    
    @classmethod
    def delete_by_id(cls, id):
        medication_list = cls.find_by_id(id)
        if medication_list:
            db.session.delete(medication_list)
            db.session.commit()
            return True
        else:
            raise ValueError(f"Medication List with ID {id} not found.")
        
    @classmethod
    def update_medication_list(cls, id):
        medication_list = db.get_or_404(cls, id, description=f'Record with id:{id} is not available')
        data = request.get_json()
        existing_products = [db.get_or_404(Product, pid.id, description=f'Product with id:{pid.id} is not available') for pid in medication_list.products]
        for prod in existing_products:
            medication_list.products.remove(prod)

        for pid in data.get('product_ids', []):
            product = db.get_or_404(Product, pid, description=f'Product with id:{pid} is not available')
            medication_list.products.append(product)

        medication_list.total_amount = sum([product.price for product in medication_list.products])

        db.session.commit()
        return medication_list.json()