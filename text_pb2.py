# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: text.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntext.proto\"\x1c\n\x0cTextRequest1\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1d\n\rTextResponse1\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1c\n\x0cTextRequest2\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1d\n\rTextResponse2\x12\x0c\n\x04text\x18\x01 \x01(\t2i\n\x0bTextService\x12,\n\tsendText1\x12\r.TextRequest1\x1a\x0e.TextResponse1\"\x00\x12,\n\tsendText2\x12\r.TextRequest2\x1a\x0e.TextResponse2\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'text_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TEXTREQUEST1._serialized_start=14
  _TEXTREQUEST1._serialized_end=42
  _TEXTRESPONSE1._serialized_start=44
  _TEXTRESPONSE1._serialized_end=73
  _TEXTREQUEST2._serialized_start=75
  _TEXTREQUEST2._serialized_end=103
  _TEXTRESPONSE2._serialized_start=105
  _TEXTRESPONSE2._serialized_end=134
  _TEXTSERVICE._serialized_start=136
  _TEXTSERVICE._serialized_end=241
# @@protoc_insertion_point(module_scope)