from datetime import datetime
from models.db import db

class Request_Product(db.Model):
    __tablename__ = 'request_products'
    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    #product_id = db.Column(db.ARRAY(db.String), db.ForeignKey('product.id'), nullable=False)
    request_status = db.Column(db.Boolean, default=False)
    quantity = db.Column (db.Integer, default =0)

    def __init__(self, request_status, quantity):
        #self.user_id = user_id
        # self.product_id = product_id
        self.request_status = request_status
        self.quantity = quantity

    def json(self):
        return {"id": self.id,
            #"user_id": self.user_id,
            # "product_id": self.product_id,
            "Status": self.request_status,
            "Quantity": self.quantity}
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @classmethod
    def find_all(cls):

        return Request_Product.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return db.get_or_404(cls, id, description=f'Record with id:{id} is not available')
    
    def update(self, request_status, quantity):
        print(f"this is the self of update {self}")
        self.request_status = request_status
        self.quantity = quantity
        db.session.commit()
        return self
    
    @classmethod
    def delete_by_id(cls, id):
        record = cls.query.get_or_404(id, description=f'Record with id:{id} is not available')
        db.session.delete(record)
        db.session.commit()
        return {"message": "Record deleted successfully"}