from concurrent import futures
import grpc
from grpc_generated.users_pb2 import *
from grpc_generated.users_pb2_grpc import *
from core import worker

class UserServicer(UserServiceServicer):
	def GetUser(self, request : GetUserRequest, context):
		task = worker.buscar_usuario_por_id.delay(request.id)
		response = task.get()
		return response

	def NewUser(self, request : NewUserRequest, context):
		task = worker.inserir_usuario.delay(request.id)
		response = task.get()
		return response
		
	def ListUsers(self, request: ListUsersRequest, context):
		task = worker.listar_usuarios.delay(request.id)
		response = task.get()
		return response
	
	def DeleteUser(self, request : DeleteRequest, context):
		task = worker.excluir_usuario.delay(request.id)
		response = task.get()
		return response
def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	add_UserServiceServicer_to_server(UserServicer(), server)
	server.add_insecure_port('localhost:50051')
	print('Server On')
	server.start()
	server.wait_for_termination()

if __name__ == '__main__':
  	serve()