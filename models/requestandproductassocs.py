from models.db import db

request_product_assoc = db.Table('request_product_assoc',
    db.Column('order_id', db.Integer, db.ForeignKey('request_products.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)