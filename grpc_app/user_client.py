import grpc
from pydantic import BaseModel
import uvicorn
from grpc_app.deps import grpc_stub_dependency
from .grpc_generated.users_pb2 import *
from .grpc_generated.users_pb2_grpc import *
from fastapi import Depends, FastAPI, HTTPException
from google.protobuf.json_format import MessageToDict
from .settings import SERVER_ADDRESS
from fastapi.middleware.cors import CORSMiddleware

class UserCreate(BaseModel):
    name: str
    email: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users")
async def get_users(stub : UserServiceStub = Depends(grpc_stub_dependency)):
    response = stub.ListUsers(ListUsersRequest()) 
    return MessageToDict(response)
    
@app.get("/users/{id}")
async def get_user(id: int, stub : UserServiceStub = Depends(grpc_stub_dependency)):
    try:
        grpcResponse = stub.GetUser(GetUserRequest(id = id))
        dictResponse = MessageToDict(grpcResponse)
        return dictResponse if len(dictResponse.keys()) > 0 else HTTPException(status_code=404)
    except:
        return HTTPException(status_code=404)

@app.post("/users")
async def new_user(user: UserCreate, stub : UserServiceStub = Depends(grpc_stub_dependency)):
    response = stub.NewUser(NewUserRequest(**dict(user)))
    return MessageToDict(response)

@app.delete("/users")
async def delete_user(id: int, stub : UserServiceStub = Depends(grpc_stub_dependency)):
    response = stub.DeleteUser(DeleteRequest(id = int(id)))
    return MessageToDict(response)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)