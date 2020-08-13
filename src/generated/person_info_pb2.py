# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generated/person_info.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='generated/person_info.proto',
  package='persons',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bgenerated/person_info.proto\x12\x07persons\"D\n\nPersonInfo\x12\x0b\n\x03\x61ge\x18\x01 \x01(\x05\x12\x19\n\x03sex\x18\x02 \x01(\x0e\x32\x0c.persons.Sex\x12\x0e\n\x06height\x18\x03 \x01(\x05*\x1a\n\x03Sex\x12\x05\n\x01M\x10\x00\x12\x05\n\x01\x46\x10\x01\x12\x05\n\x01O\x10\x02\x62\x06proto3'
)

_SEX = _descriptor.EnumDescriptor(
  name='Sex',
  full_name='persons.Sex',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='M', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='F', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='O', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=110,
  serialized_end=136,
)
_sym_db.RegisterEnumDescriptor(_SEX)

Sex = enum_type_wrapper.EnumTypeWrapper(_SEX)
M = 0
F = 1
O = 2



_PERSONINFO = _descriptor.Descriptor(
  name='PersonInfo',
  full_name='persons.PersonInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='age', full_name='persons.PersonInfo.age', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sex', full_name='persons.PersonInfo.sex', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='persons.PersonInfo.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=108,
)

_PERSONINFO.fields_by_name['sex'].enum_type = _SEX
DESCRIPTOR.message_types_by_name['PersonInfo'] = _PERSONINFO
DESCRIPTOR.enum_types_by_name['Sex'] = _SEX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PersonInfo = _reflection.GeneratedProtocolMessageType('PersonInfo', (_message.Message,), {
  'DESCRIPTOR' : _PERSONINFO,
  '__module__' : 'generated.person_info_pb2'
  # @@protoc_insertion_point(class_scope:persons.PersonInfo)
  })
_sym_db.RegisterMessage(PersonInfo)


# @@protoc_insertion_point(module_scope)