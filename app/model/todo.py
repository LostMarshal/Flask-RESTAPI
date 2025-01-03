from app import db
from datetime import datetime
from app.model.user import Users

class Todos(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    todo = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default = datetime.utcnow, onupdate = datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable = False)

    def __repr__(self):
        return '<Todos {}>'.format(self.todo)