from app import app
from app.controller import UserController
from flask import request

@app.route("/users/<id>", methods=['GET', 'PUT', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)

@app.route("/users", methods=['POST', 'GET'])
def users():
    if request.method == 'POST':
        return UserController.store() 
    else:
        return UserController.index()