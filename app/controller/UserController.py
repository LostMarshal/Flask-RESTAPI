from app.model.user import Users
from app import response, db
from flask import request

def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
    
def transform(users):
    array = []
    for i in users:
        array.append({
            "id" : i.id,
            "name" : i.name,
            "email" : i.email,
       })
    return array

def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'User tidak ditemukan')
        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], 'Gagal mengambil data')
    
def singleTransform(users):
    data = {
        "id" : users.id,
        "name" : users.name,
        "email" : users.email,
    }
    return data

def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        users = Users(name = name, email = email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.ok('', 'Berhasil membuat data')
    
    except Exception as e:
        print(e)
        return response.badRequest([], 'Gagal membuat data')
    
def update(id):
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        users = Users.query.filter_by(id = id).first()
        users.email = email
        users.name = name
        users.setPassword(password)

        db.session.commit()

        return response.ok('', 'Berhasil update data')
    except Exception as e:
        print(e)
        return response.badRequest([], 'Gagal update data')

def delete(id):
    try:
        User = Users.query.filter_by(id = id).first()
        if not User:
            return response.badRequest([], 'Data tidak ditemukan')
        
        db.session.delete(User)
        db.session.commit()

        return response.ok('', 'Berhasil menghapus data')
    except Exception as e:
        print(e)
        return response.badRequest([], 'Gagal menghapus data')