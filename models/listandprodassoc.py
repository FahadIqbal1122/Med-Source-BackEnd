from models.db import db

list_product = db.Table('list_product',
    db.Column('list_id', db.Integer, db.ForeignKey('medication_list.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)