from app import db
from datetime import datetime
from app.model.user import Users

class Category_products(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    category = db.Column(db.String(255), nullable = False)
    product_id = db.Column(db.BigInteger, db.ForeignKey('products.id'), nullable = False)
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default = datetime.utcnow, onupdate = datetime.utcnow)

    def __repr__(self):
        return '<Category_products {}>'.format(self.category)