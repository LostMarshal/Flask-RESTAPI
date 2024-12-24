from app import db
from datetime import datetime
from app.model.user import Users

class Products(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255), nullable = False)
    price = db.Column(db.Float, nullable = False)
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default = datetime.utcnow, onupdate = datetime.utcnow)

    def __repr__(self):
        return '<Products {}>'.format(self.name)