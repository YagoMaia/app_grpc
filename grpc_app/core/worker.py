from celery import Celery
from db.db import DB
from .queries import Queries
from grpc_generated.users_pb2_grpc import *

app = Celery('task', broker = "rabbitmq://localhost:6379")
query = Queries()

@app.task(name='inserir_usuario')
def inserir_usuario(name : str, email : str):
    try:
        db = DB()
        cursor = db.cursor()
        create = cursor.execute(query.inserir_usuario, (name, email))
        db.close()
        return NewUserResponse(created=create)
    except:
        return NewUserResponse(created=False)
    
@app.task(name = 'excluir_usuario')
def excluir_usuario(id: int):
    try:
        db = DB()
        cursor = db.cursor()
        deleted = cursor.execute(query.excluir_usuario, (id,))
        db.close()
        return DeleteResponse(deleted = deleted)
    except:
        return DeleteResponse(deleted = False)
    
@app.task(name = 'atualizar_usuario')
def atualizar_usuario(id: int, name: str, email: str):
    try:
        db = DB()
        cursor = db.cursor()
        updated = cursor.execute(query.atualizar_usuario, (name, email, id))
        db.close()
        return UpdateResponse(updated = updated)
    except:
        return UpdateResponse(updated = False)
    
@app.task(name = 'listar_usuarios')
def listar_usuarios():
    try:
        db = DB()
        cursor = db.cursor()
        rows = cursor.execute(query.listar_usuarios).fetchall()
        users = [dict(r) for r in rows]
        db.close()
        return ListUsersResponse(users = users)
    except:
        return ListUsersResponse(users = [])
    
@app.task(name = 'buscar_usuario_por_id')
def buscar_usuario_por_id(id: int):
    try:
        db = DB()
        cursor = db.cursor()
        row = cursor.execute(query.buscar_usuario_por_id, (id,)).fetchone()
        user = dict(row) if row else {}
        db.close()
        return GetUserResponse(**user)
    except:
        return GetUserResponse()