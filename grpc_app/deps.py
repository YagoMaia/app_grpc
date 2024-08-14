from fastapi import Depends
import grpc

from .grpc_generated.users_pb2_grpc import UserServiceStub
from .settings import SERVER_ADDRESS

def grpc_stub_dependency():
    with grpc.insecure_channel(SERVER_ADDRESS) as channel:
        stub = UserServiceStub(channel)
        yield stub