# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dragon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dragon.proto',
  package='dragon',
  serialized_pb=_b('\n\x0c\x64ragon.proto\x12\x06\x64ragon\"\xfe\x01\n\x0bTensorProto\x12\x0c\n\x04\x64ims\x18\x01 \x03(\x05\x12\x36\n\tdata_type\x18\x02 \x01(\x0e\x32\x1c.dragon.TensorProto.DataType:\x05\x46LOAT\x12\x16\n\nfloat_data\x18\x03 \x03(\x02\x42\x02\x10\x01\x12\x16\n\nint32_data\x18\x04 \x03(\x05\x42\x02\x10\x01\x12\x11\n\tbyte_data\x18\x05 \x01(\x0c\x12\x13\n\x0bstring_data\x18\x06 \x03(\x0c\x12\x0c\n\x04name\x18\x07 \x01(\t\"C\n\x08\x44\x61taType\x12\t\n\x05\x46LOAT\x10\x01\x12\t\n\x05INT32\x10\x02\x12\x08\n\x04\x42YTE\x10\x03\x12\n\n\x06STRING\x10\x04\x12\x0b\n\x07\x46LOAT16\x10\x0c\"3\n\x0cTensorProtos\x12#\n\x06protos\x18\x01 \x03(\x0b\x32\x13.dragon.TensorProto\"\x80\x01\n\x08\x41rgument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\t\n\x01\x66\x18\x02 \x01(\x02\x12\t\n\x01i\x18\x03 \x01(\x05\x12\x0b\n\x03i64\x18\t \x01(\x03\x12\t\n\x01s\x18\x04 \x01(\t\x12\t\n\x01\x62\x18\x08 \x01(\x08\x12\x0e\n\x06\x66loats\x18\x05 \x03(\x02\x12\x0c\n\x04ints\x18\x06 \x03(\x05\x12\x0f\n\x07strings\x18\x07 \x03(\t\"z\n\x0c\x44\x65viceOption\x12,\n\x0b\x64\x65vice_type\x18\x01 \x01(\x0e\x32\x12.dragon.DeviceType:\x03\x43PU\x12\x14\n\tdevice_id\x18\x02 \x01(\x05:\x01\x30\x12\x16\n\x0brandom_seed\x18\x03 \x01(\r:\x01\x33\x12\x0e\n\x06\x65ngine\x18\x04 \x01(\t\"\x94\x01\n\x0bOperatorDef\x12\r\n\x05input\x18\x01 \x03(\t\x12\x0e\n\x06output\x18\x02 \x03(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x1d\n\x03\x61rg\x18\x05 \x03(\x0b\x32\x10.dragon.Argument\x12+\n\rdevice_option\x18\x06 \x01(\x0b\x32\x14.dragon.DeviceOption\"=\n\x0eGradientTarget\x12\x0c\n\x04\x63ost\x18\x01 \x01(\t\x12\x0b\n\x03wrt\x18\x02 \x01(\t\x12\x10\n\x08\x65xternal\x18\x03 \x01(\t\"Y\n\x0cUpdateTarget\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0e\n\x06tensor\x18\x03 \x03(\t\x12\x1d\n\x03\x61rg\x18\x04 \x03(\x0b\x32\x10.dragon.Argument\"\x94\x02\n\x0cTensorFiller\x12\x0e\n\x06tensor\x18\x01 \x01(\t\x12\x16\n\x04type\x18\x02 \x01(\t:\x08\x63onstant\x12\x10\n\x05value\x18\x03 \x01(\x02:\x01\x30\x12\x0e\n\x03low\x18\x04 \x01(\x02:\x01\x30\x12\x0f\n\x04high\x18\x05 \x01(\x02:\x01\x31\x12\x0f\n\x04mean\x18\x06 \x01(\x02:\x01\x30\x12\x0e\n\x03std\x18\x07 \x01(\x02:\x01\x31\x12\x10\n\x05scale\x18\x08 \x01(\x02:\x01\x33\x12@\n\rvariance_norm\x18\t \x01(\x0e\x32!.dragon.TensorFiller.VarianceNorm:\x06\x46\x41N_IN\"4\n\x0cVarianceNorm\x12\n\n\x06\x46\x41N_IN\x10\x00\x12\x0b\n\x07\x46\x41N_OUT\x10\x01\x12\x0b\n\x07\x46\x41N_AVG\x10\x02\"\xfb\x01\n\x08GraphDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1f\n\x02op\x18\x02 \x03(\x0b\x32\x13.dragon.OperatorDef\x12\x12\n\ngraph_type\x18\x03 \x01(\t\x12+\n\rdevice_option\x18\x05 \x01(\x0b\x32\x14.dragon.DeviceOption\x12\x1d\n\x03\x61rg\x18\x06 \x03(\x0b\x32\x10.dragon.Argument\x12\x0e\n\x06target\x18\x07 \x03(\t\x12(\n\x08g_target\x18\x08 \x03(\x0b\x32\x16.dragon.GradientTarget\x12&\n\x08u_target\x18\t \x03(\x0b\x32\x14.dragon.UpdateTarget*)\n\nDeviceType\x12\x07\n\x03\x43PU\x10\x00\x12\x08\n\x04\x43UDA\x10\x01\x12\x08\n\x04\x43NML\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_DEVICETYPE = _descriptor.EnumDescriptor(
  name='DeviceType',
  full_name='dragon.DeviceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CPU', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUDA', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CNML', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1427,
  serialized_end=1468,
)
_sym_db.RegisterEnumDescriptor(_DEVICETYPE)

DeviceType = enum_type_wrapper.EnumTypeWrapper(_DEVICETYPE)
CPU = 0
CUDA = 1
CNML = 2


_TENSORPROTO_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='dragon.TensorProto.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BYTE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT16', index=4, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=212,
  serialized_end=279,
)
_sym_db.RegisterEnumDescriptor(_TENSORPROTO_DATATYPE)

_TENSORFILLER_VARIANCENORM = _descriptor.EnumDescriptor(
  name='VarianceNorm',
  full_name='dragon.TensorFiller.VarianceNorm',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAN_IN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAN_OUT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAN_AVG', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1119,
  serialized_end=1171,
)
_sym_db.RegisterEnumDescriptor(_TENSORFILLER_VARIANCENORM)


_TENSORPROTO = _descriptor.Descriptor(
  name='TensorProto',
  full_name='dragon.TensorProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dims', full_name='dragon.TensorProto.dims', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='dragon.TensorProto.data_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_data', full_name='dragon.TensorProto.float_data', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='int32_data', full_name='dragon.TensorProto.int32_data', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='byte_data', full_name='dragon.TensorProto.byte_data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_data', full_name='dragon.TensorProto.string_data', index=5,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='dragon.TensorProto.name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TENSORPROTO_DATATYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=279,
)


_TENSORPROTOS = _descriptor.Descriptor(
  name='TensorProtos',
  full_name='dragon.TensorProtos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protos', full_name='dragon.TensorProtos.protos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=332,
)


_ARGUMENT = _descriptor.Descriptor(
  name='Argument',
  full_name='dragon.Argument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dragon.Argument.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f', full_name='dragon.Argument.f', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i', full_name='dragon.Argument.i', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i64', full_name='dragon.Argument.i64', index=3,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s', full_name='dragon.Argument.s', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='dragon.Argument.b', index=5,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='floats', full_name='dragon.Argument.floats', index=6,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ints', full_name='dragon.Argument.ints', index=7,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strings', full_name='dragon.Argument.strings', index=8,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=463,
)


_DEVICEOPTION = _descriptor.Descriptor(
  name='DeviceOption',
  full_name='dragon.DeviceOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_type', full_name='dragon.DeviceOption.device_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='dragon.DeviceOption.device_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='random_seed', full_name='dragon.DeviceOption.random_seed', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='engine', full_name='dragon.DeviceOption.engine', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=587,
)


_OPERATORDEF = _descriptor.Descriptor(
  name='OperatorDef',
  full_name='dragon.OperatorDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='dragon.OperatorDef.input', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output', full_name='dragon.OperatorDef.output', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='dragon.OperatorDef.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='dragon.OperatorDef.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arg', full_name='dragon.OperatorDef.arg', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_option', full_name='dragon.OperatorDef.device_option', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=738,
)


_GRADIENTTARGET = _descriptor.Descriptor(
  name='GradientTarget',
  full_name='dragon.GradientTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cost', full_name='dragon.GradientTarget.cost', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wrt', full_name='dragon.GradientTarget.wrt', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external', full_name='dragon.GradientTarget.external', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=740,
  serialized_end=801,
)


_UPDATETARGET = _descriptor.Descriptor(
  name='UpdateTarget',
  full_name='dragon.UpdateTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dragon.UpdateTarget.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='dragon.UpdateTarget.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='dragon.UpdateTarget.tensor', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arg', full_name='dragon.UpdateTarget.arg', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=803,
  serialized_end=892,
)


_TENSORFILLER = _descriptor.Descriptor(
  name='TensorFiller',
  full_name='dragon.TensorFiller',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor', full_name='dragon.TensorFiller.tensor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='dragon.TensorFiller.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("constant").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='dragon.TensorFiller.value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='low', full_name='dragon.TensorFiller.low', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high', full_name='dragon.TensorFiller.high', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mean', full_name='dragon.TensorFiller.mean', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='std', full_name='dragon.TensorFiller.std', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='dragon.TensorFiller.scale', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variance_norm', full_name='dragon.TensorFiller.variance_norm', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TENSORFILLER_VARIANCENORM,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=895,
  serialized_end=1171,
)


_GRAPHDEF = _descriptor.Descriptor(
  name='GraphDef',
  full_name='dragon.GraphDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dragon.GraphDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='op', full_name='dragon.GraphDef.op', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graph_type', full_name='dragon.GraphDef.graph_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_option', full_name='dragon.GraphDef.device_option', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arg', full_name='dragon.GraphDef.arg', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='dragon.GraphDef.target', index=5,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='g_target', full_name='dragon.GraphDef.g_target', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='u_target', full_name='dragon.GraphDef.u_target', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1174,
  serialized_end=1425,
)

_TENSORPROTO.fields_by_name['data_type'].enum_type = _TENSORPROTO_DATATYPE
_TENSORPROTO_DATATYPE.containing_type = _TENSORPROTO
_TENSORPROTOS.fields_by_name['protos'].message_type = _TENSORPROTO
_DEVICEOPTION.fields_by_name['device_type'].enum_type = _DEVICETYPE
_OPERATORDEF.fields_by_name['arg'].message_type = _ARGUMENT
_OPERATORDEF.fields_by_name['device_option'].message_type = _DEVICEOPTION
_UPDATETARGET.fields_by_name['arg'].message_type = _ARGUMENT
_TENSORFILLER.fields_by_name['variance_norm'].enum_type = _TENSORFILLER_VARIANCENORM
_TENSORFILLER_VARIANCENORM.containing_type = _TENSORFILLER
_GRAPHDEF.fields_by_name['op'].message_type = _OPERATORDEF
_GRAPHDEF.fields_by_name['device_option'].message_type = _DEVICEOPTION
_GRAPHDEF.fields_by_name['arg'].message_type = _ARGUMENT
_GRAPHDEF.fields_by_name['g_target'].message_type = _GRADIENTTARGET
_GRAPHDEF.fields_by_name['u_target'].message_type = _UPDATETARGET
DESCRIPTOR.message_types_by_name['TensorProto'] = _TENSORPROTO
DESCRIPTOR.message_types_by_name['TensorProtos'] = _TENSORPROTOS
DESCRIPTOR.message_types_by_name['Argument'] = _ARGUMENT
DESCRIPTOR.message_types_by_name['DeviceOption'] = _DEVICEOPTION
DESCRIPTOR.message_types_by_name['OperatorDef'] = _OPERATORDEF
DESCRIPTOR.message_types_by_name['GradientTarget'] = _GRADIENTTARGET
DESCRIPTOR.message_types_by_name['UpdateTarget'] = _UPDATETARGET
DESCRIPTOR.message_types_by_name['TensorFiller'] = _TENSORFILLER
DESCRIPTOR.message_types_by_name['GraphDef'] = _GRAPHDEF
DESCRIPTOR.enum_types_by_name['DeviceType'] = _DEVICETYPE

TensorProto = _reflection.GeneratedProtocolMessageType('TensorProto', (_message.Message,), dict(
  DESCRIPTOR = _TENSORPROTO,
  __module__ = 'dragon_pb2'
  # @@protoc_insertion_point(class_scope:dragon.TensorProto)
  ))
_sym_db.RegisterMessage(TensorProto)

TensorProtos = _reflection.GeneratedProtocolMessageType('TensorProtos', (_message.Message,), dict(
  DESCRIPTOR = _TENSORPROTOS,
  __module__ = 'dragon_pb2'
  # @@protoc_insertion_point(class_scope:dragon.TensorProtos)
  ))
_sym_db.RegisterMessage(TensorProtos)

Argument = _reflection.GeneratedProtocolMessageType('Argument', (_message.Message,), dict(
  DESCRIPTOR = _ARGUMENT,
  __module__ = 'dragon_pb2'
  # @@protoc_insertion_point(class_scope:dragon.Argument)
  ))
_sym_db.RegisterMessage(Argument)

DeviceOption = _reflection.GeneratedProtocolMessageType('DeviceOption', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEOPTION,
  __module__ = 'dragon_pb2'
  # @@protoc_insertion_point(class_scope:dragon.DeviceOption)
  ))
_sym_db.RegisterMessage(DeviceOption)

OperatorDef = _reflection.GeneratedProtocolMessageType('OperatorDef', (_message.Message,), dict(
  DESCRIPTOR = _OPERATORDEF,
  __module__ = 'dragon_pb2'
  # @@protoc_insertion_point(class_scope:dragon.OperatorDef)
  ))
_sym_db.RegisterMessage(OperatorDef)

GradientTarget = _reflection.GeneratedProtocolMessageType('GradientTarget', (_message.Message,), dict(
  DESCRIPTOR = _GRADIENTTARGET,
  __module__ = 'dragon_pb2'
  # @@protoc_insertion_point(class_scope:dragon.GradientTarget)
  ))
_sym_db.RegisterMessage(GradientTarget)

UpdateTarget = _reflection.GeneratedProtocolMessageType('UpdateTarget', (_message.Message,), dict(
  DESCRIPTOR = _UPDATETARGET,
  __module__ = 'dragon_pb2'
  # @@protoc_insertion_point(class_scope:dragon.UpdateTarget)
  ))
_sym_db.RegisterMessage(UpdateTarget)

TensorFiller = _reflection.GeneratedProtocolMessageType('TensorFiller', (_message.Message,), dict(
  DESCRIPTOR = _TENSORFILLER,
  __module__ = 'dragon_pb2'
  # @@protoc_insertion_point(class_scope:dragon.TensorFiller)
  ))
_sym_db.RegisterMessage(TensorFiller)

GraphDef = _reflection.GeneratedProtocolMessageType('GraphDef', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHDEF,
  __module__ = 'dragon_pb2'
  # @@protoc_insertion_point(class_scope:dragon.GraphDef)
  ))
_sym_db.RegisterMessage(GraphDef)


_TENSORPROTO.fields_by_name['float_data'].has_options = True
_TENSORPROTO.fields_by_name['float_data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_TENSORPROTO.fields_by_name['int32_data'].has_options = True
_TENSORPROTO.fields_by_name['int32_data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
