from datetime import datetime
from models.db import db

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    #receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String(255))

    def __init__(self, content):
        #self.user_id = user_id
        # self.product_id = product_id
        #self.receiver_id = receiver_id
        self.content = content

    def json(self):
        return {"id": self.id,
            #"user_id": self.user_id,
            #"receiver_id": self.receiver_id,
            # "product_id": self.product_id,
            "Content": self.content}
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @classmethod
    def find_all(cls):
        return Message.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return db.get_or_404(cls, id, description=f'Record with id:{id} is not available')