from datetime import datetime
from models.db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(255))
    message_list = db.Column(db.ARRAY(db.String))
    digest = db.Column(db.String(255))
    phone_number=db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())

    def __init__(self, first_name, last_name, email, password, phone_number):
        self.f_name= first_name
        self.l_name = last_name
        self.email = email
        self.digest = password
        self.phone_number = phone_number

    def json(self):
        return {"id": self.id,
            "name": self.f_name,
            "email": self.email,
            "Mobile": self.phone_number,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)}
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @classmethod
    def find_all(cls):
        return User.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return db.get_or_404(cls, id, description=f'Record with id:{id} is not available')