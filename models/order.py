from datetime import datetime
from models.db import db

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, total_amount):
        self.user_id = user_id
        # self.product_id = product_id
        self.total_amount = total_amount

    def json(self):
        return {"id": self.id,
            "user_id": self.user_id,
            # "product_id": self.product_id,
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
        return db.get_or_404(cls, id, description=f'Record with id:{id} is not available')