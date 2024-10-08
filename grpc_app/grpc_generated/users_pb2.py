# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/users.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12protos/users.proto\"/\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"-\n\x0eNewUserRequest\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"\"\n\x0fNewUserResponse\x12\x0f\n\x07\x63reated\x18\x01 \x01(\x08\"\x1c\n\x0eGetUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\":\n\x0fGetUserResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"\x12\n\x10ListUsersRequest\")\n\x11ListUsersResponse\x12\x14\n\x05users\x18\x01 \x03(\x0b\x32\x05.User\"\x1b\n\rDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"!\n\x0e\x44\x65leteResponse\x12\x0f\n\x07\x64\x65leted\x18\x01 \x01(\x08\"$\n\rUpdateRequest\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\"!\n\x0eUpdateResponse\x12\x0f\n\x07updated\x18\x01 \x01(\x08\x32\x85\x02\n\x0bUserService\x12.\n\x07GetUser\x12\x0f.GetUserRequest\x1a\x10.GetUserResponse\"\x00\x12.\n\x07NewUser\x12\x0f.NewUserRequest\x1a\x10.NewUserResponse\"\x00\x12\x34\n\tListUsers\x12\x11.ListUsersRequest\x1a\x12.ListUsersResponse\"\x00\x12/\n\nDeleteUser\x12\x0e.DeleteRequest\x1a\x0f.DeleteResponse\"\x00\x12/\n\nUpdateUser\x12\x0e.UpdateRequest\x1a\x0f.UpdateResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.users_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USER']._serialized_start=22
  _globals['_USER']._serialized_end=69
  _globals['_NEWUSERREQUEST']._serialized_start=71
  _globals['_NEWUSERREQUEST']._serialized_end=116
  _globals['_NEWUSERRESPONSE']._serialized_start=118
  _globals['_NEWUSERRESPONSE']._serialized_end=152
  _globals['_GETUSERREQUEST']._serialized_start=154
  _globals['_GETUSERREQUEST']._serialized_end=182
  _globals['_GETUSERRESPONSE']._serialized_start=184
  _globals['_GETUSERRESPONSE']._serialized_end=242
  _globals['_LISTUSERSREQUEST']._serialized_start=244
  _globals['_LISTUSERSREQUEST']._serialized_end=262
  _globals['_LISTUSERSRESPONSE']._serialized_start=264
  _globals['_LISTUSERSRESPONSE']._serialized_end=305
  _globals['_DELETEREQUEST']._serialized_start=307
  _globals['_DELETEREQUEST']._serialized_end=334
  _globals['_DELETERESPONSE']._serialized_start=336
  _globals['_DELETERESPONSE']._serialized_end=369
  _globals['_UPDATEREQUEST']._serialized_start=371
  _globals['_UPDATEREQUEST']._serialized_end=407
  _globals['_UPDATERESPONSE']._serialized_start=409
  _globals['_UPDATERESPONSE']._serialized_end=442
  _globals['_USERSERVICE']._serialized_start=445
  _globals['_USERSERVICE']._serialized_end=706
# @@protoc_insertion_point(module_scope)
