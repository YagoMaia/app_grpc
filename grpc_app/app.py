from flask import Flask
from .deps import grpc_stub_dependency
from .grpc_generated.users_pb2 import *
from .grpc_generated.users_pb2_grpc import *
from google.protobuf.json_format import MessageToDict
from .schemas import *

app = Flask(__name__)

@app.route('/')
def index():
    return "Home"

@app.route('/list_users')
def list_users():
    stub = grpc_stub_dependency()
    response = stub.ListUsers(ListUsersRequest()) 
    return MessageToDict(response)

@app.route('/create_user', methods=['POST'])
def create_user():
    form = FormNewUser()
    stub = grpc_stub_dependency()
    if form.validate_on_submit():
        response = stub.NewUser(NewUserRequest(form.name.data, form.email.data))
        return MessageToDict(response)
    return "Criando usuario"

@app.route('/excluir_usuario', methods=['POST'])
def delete_user():
    stub = grpc_stub_dependency()
    form = FormDeleteUser()
    if form.validate_on_submit():
        response = stub.DeleteUser(DeleteRequest(id = int(form.id.data)))
        return MessageToDict(response)
    return "excluir_usuario"

@app.route('/atualizar_usuario', methods=['POST'])
def update_user():
    stub = grpc_stub_dependency()
    form = FormUpdateUser()
    if form.validate_on_submit():
        response = stub.Update(DeleteRequest(id = int(form.id.data)))
        return MessageToDict(response)
    return "atualizar_usuario"

@app.route('/user/<user_id>')
def user_by_id(user_id):
    stub = grpc_stub_dependency()
    form = FormGetUser()
    if form.validate_on_submit():
        response = stub.GetUser(GetUserRequest(id = id))
        return MessageToDict(response)
    return "usuario com id"