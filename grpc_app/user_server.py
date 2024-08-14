from concurrent import futures
import grpc
import psycopg2
import psycopg2.extras
from db.db import Db
from grpc_generated.users_pb2 import *
from grpc_generated.users_pb2_grpc import *
from core import worker

class UserServicer(UserServiceServicer):
	def GetUser(self, request : GetUserRequest, context):
		try: 
			db = Db()
			cursor = db._connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
			cursor.execute('SELECT * FROM users WHERE id=%s', (request.id,))
			row = cursor.fetchone()
			if row is None: 
				return GetUserResponse()
			return GetUserResponse(**dict(row))
		except:
			return GetUserResponse()

	def NewUser(self, request : NewUserRequest, context):
		try:
			db = Db()
			cursor = db._connection.cursor()
			cursor.execute('INSERT INTO users (name, email) VALUES (%s,%s)', (request.name,request.email,))
			db._connection.commit()
			return NewUserResponse(created = True)
		except:
			return NewUserResponse(created = False)
		
	def ListUsers(self, request, context):
		try:
			db = Db()
			cursor = db._connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
			cursor.execute('SELECT * FROM users')
			rows = cursor.fetchall()
			users = [User(**dict(user)) for user in rows]
			response = ListUsersResponse(users = users)
			return response
		except Exception as erro:
			print(erro)
			return ListUsersResponse(users= [])
	
	def DeleteUser(self, request, context):
		try:
			db = Db()
			cursor = db._connection.cursor()
			cursor.execute('DELETE FROM users WHERE id=%s', (request.id,))
			db._connection.commit()
			return DeleteResponse(deleted = True)
		except:
			return DeleteResponse(deleted = False)

def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	add_UserServiceServicer_to_server(UserServicer(), server)
	server.add_insecure_port('localhost:50051')
	print('Server On')
	server.start()
	server.wait_for_termination()

if __name__ == '__main__':
  	serve()