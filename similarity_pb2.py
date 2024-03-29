# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sample.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0csample.proto\"\"\n\x11Similarity_Factor\x12\r\n\x05score\x18\x01 \x01(\x01\"+\n\x05Image\x12\x10\n\x04rgb1\x18\x01 \x03(\x01\x42\x02\x10\x01\x12\x10\n\x04rgb2\x18\x02 \x03(\x01\x42\x02\x10\x01\x32:\n\x0cSampleServer\x12*\n\nSimilarity\x12\x06.Image\x1a\x12.Similarity_Factor\"\x00\x62\x06proto3')
)




_SIMILARITY_FACTOR = _descriptor.Descriptor(
  name='Similarity_Factor',
  full_name='Similarity_Factor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='score', full_name='Similarity_Factor.score', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=16,
  serialized_end=50,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rgb1', full_name='Image.rgb1', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rgb2', full_name='Image.rgb2', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=52,
  serialized_end=95,
)

DESCRIPTOR.message_types_by_name['Similarity_Factor'] = _SIMILARITY_FACTOR
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Similarity_Factor = _reflection.GeneratedProtocolMessageType('Similarity_Factor', (_message.Message,), dict(
  DESCRIPTOR = _SIMILARITY_FACTOR,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:Similarity_Factor)
  ))
_sym_db.RegisterMessage(Similarity_Factor)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
  DESCRIPTOR = _IMAGE,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:Image)
  ))
_sym_db.RegisterMessage(Image)


_IMAGE.fields_by_name['rgb1']._options = None
_IMAGE.fields_by_name['rgb2']._options = None

_SAMPLESERVER = _descriptor.ServiceDescriptor(
  name='SampleServer',
  full_name='SampleServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=97,
  serialized_end=155,
  methods=[
  _descriptor.MethodDescriptor(
    name='Similarity',
    full_name='SampleServer.Similarity',
    index=0,
    containing_service=None,
    input_type=_IMAGE,
    output_type=_SIMILARITY_FACTOR,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SAMPLESERVER)

DESCRIPTOR.services_by_name['SampleServer'] = _SAMPLESERVER

# @@protoc_insertion_point(module_scope)
