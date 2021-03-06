# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tribune_tts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tribune_tts.proto',
  package='techmo.tribune',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11tribune_tts.proto\x12\x0etechmo.tribune\"%\n\x11ListVoicesRequest\x12\x10\n\x08language\x18\x01 \x01(\t\"?\n\x12ListVoicesResponse\x12)\n\x06voices\x18\x01 \x03(\x0b\x32\x19.techmo.tribune.VoiceInfo\"S\n\x11SynthesizeRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x30\n\x06\x63onfig\x18\x02 \x01(\x0b\x32 .techmo.tribune.SynthesizeConfig\"}\n\x10SynthesizeConfig\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x31\n\x0c\x61udio_config\x18\x02 \x01(\x0b\x32\x1b.techmo.tribune.AudioConfig\x12$\n\x05voice\x18\x03 \x01(\x0b\x32\x15.techmo.tribune.Voice\"\x9b\x01\n\x0b\x41udioConfig\x12\x35\n\x0e\x61udio_encoding\x18\x01 \x01(\x0e\x32\x1d.techmo.tribune.AudioEncoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05\x12\r\n\x05pitch\x18\x03 \x01(\x02\x12\r\n\x05range\x18\x04 \x01(\x02\x12\x0c\n\x04rate\x18\x05 \x01(\x02\x12\x0e\n\x06volume\x18\x06 \x01(\x02\"_\n\x05Voice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x06gender\x18\x02 \x01(\x0e\x32\x16.techmo.tribune.Gender\x12 \n\x03\x61ge\x18\x03 \x01(\x0e\x32\x13.techmo.tribune.Age\"N\n\tVoiceInfo\x12\x1b\n\x13supported_languages\x18\x01 \x03(\t\x12$\n\x05voice\x18\x02 \x01(\x0b\x32\x15.techmo.tribune.Voice\"d\n\x12SynthesizeResponse\x12(\n\x05\x61udio\x18\x01 \x01(\x0b\x32\x19.techmo.tribune.AudioData\x12$\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x15.techmo.tribune.Error\"7\n\tAudioData\x12\x19\n\x11sample_rate_hertz\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"2\n\x11PutLexiconRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\":\n\x12PutLexiconResponse\x12$\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x15.techmo.tribune.Error\"$\n\x14\x44\x65leteLexiconRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"=\n\x15\x44\x65leteLexiconResponse\x12$\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x15.techmo.tribune.Error\"!\n\x11GetLexiconRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"K\n\x12GetLexiconResponse\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12$\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x15.techmo.tribune.Error\"\'\n\x13ListLexiconsRequest\x12\x10\n\x08language\x18\x01 \x01(\t\"%\n\x14ListLexiconsResponse\x12\r\n\x05names\x18\x01 \x03(\t\"E\n\x05\x45rror\x12\'\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x19.techmo.tribune.ErrorCode\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t**\n\rAudioEncoding\x12\t\n\x05PCM16\x10\x00\x12\x0e\n\nOGG_VORBIS\x10\x01*6\n\x06Gender\x12\x16\n\x12GENDER_UNSPECIFIED\x10\x00\x12\n\n\x06\x46\x45MALE\x10\x01\x12\x08\n\x04MALE\x10\x02*<\n\x03\x41ge\x12\x13\n\x0f\x41GE_UNSPECIFIED\x10\x00\x12\t\n\x05\x41\x44ULT\x10\x01\x12\t\n\x05\x43HILD\x10\x02\x12\n\n\x06SENILE\x10\x03*}\n\tErrorCode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07LICENCE\x10\x01\x12\x12\n\x0eMISSING_OBJECT\x10\x02\x12\x08\n\x04SSML\x10\x03\x12\x16\n\x12TEXT_NORMALIZATION\x10\x04\x12\x11\n\rTRANSCRIPTION\x10\x05\x12\r\n\tSYNTHESIS\x10\x06\x32\xf2\x04\n\x03TTS\x12S\n\nListVoices\x12!.techmo.tribune.ListVoicesRequest\x1a\".techmo.tribune.ListVoicesResponse\x12^\n\x13SynthesizeStreaming\x12!.techmo.tribune.SynthesizeRequest\x1a\".techmo.tribune.SynthesizeResponse0\x01\x12S\n\nSynthesize\x12!.techmo.tribune.SynthesizeRequest\x1a\".techmo.tribune.SynthesizeResponse\x12S\n\nPutLexicon\x12!.techmo.tribune.PutLexiconRequest\x1a\".techmo.tribune.PutLexiconResponse\x12\\\n\rDeleteLexicon\x12$.techmo.tribune.DeleteLexiconRequest\x1a%.techmo.tribune.DeleteLexiconResponse\x12S\n\nGetLexicon\x12!.techmo.tribune.GetLexiconRequest\x1a\".techmo.tribune.GetLexiconResponse\x12Y\n\x0cListLexicons\x12#.techmo.tribune.ListLexiconsRequest\x1a$.techmo.tribune.ListLexiconsResponseb\x06proto3')
)

_AUDIOENCODING = _descriptor.EnumDescriptor(
  name='AudioEncoding',
  full_name='techmo.tribune.AudioEncoding',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PCM16', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OGG_VORBIS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1323,
  serialized_end=1365,
)
_sym_db.RegisterEnumDescriptor(_AUDIOENCODING)

AudioEncoding = enum_type_wrapper.EnumTypeWrapper(_AUDIOENCODING)
_GENDER = _descriptor.EnumDescriptor(
  name='Gender',
  full_name='techmo.tribune.Gender',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GENDER_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MALE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1367,
  serialized_end=1421,
)
_sym_db.RegisterEnumDescriptor(_GENDER)

Gender = enum_type_wrapper.EnumTypeWrapper(_GENDER)
_AGE = _descriptor.EnumDescriptor(
  name='Age',
  full_name='techmo.tribune.Age',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AGE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADULT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHILD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENILE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1423,
  serialized_end=1483,
)
_sym_db.RegisterEnumDescriptor(_AGE)

Age = enum_type_wrapper.EnumTypeWrapper(_AGE)
_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='techmo.tribune.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LICENCE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_OBJECT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SSML', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_NORMALIZATION', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSCRIPTION', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNTHESIS', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1485,
  serialized_end=1610,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
PCM16 = 0
OGG_VORBIS = 1
GENDER_UNSPECIFIED = 0
FEMALE = 1
MALE = 2
AGE_UNSPECIFIED = 0
ADULT = 1
CHILD = 2
SENILE = 3
UNKNOWN = 0
LICENCE = 1
MISSING_OBJECT = 2
SSML = 3
TEXT_NORMALIZATION = 4
TRANSCRIPTION = 5
SYNTHESIS = 6



_LISTVOICESREQUEST = _descriptor.Descriptor(
  name='ListVoicesRequest',
  full_name='techmo.tribune.ListVoicesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='techmo.tribune.ListVoicesRequest.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=37,
  serialized_end=74,
)


_LISTVOICESRESPONSE = _descriptor.Descriptor(
  name='ListVoicesResponse',
  full_name='techmo.tribune.ListVoicesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='voices', full_name='techmo.tribune.ListVoicesResponse.voices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=76,
  serialized_end=139,
)


_SYNTHESIZEREQUEST = _descriptor.Descriptor(
  name='SynthesizeRequest',
  full_name='techmo.tribune.SynthesizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='techmo.tribune.SynthesizeRequest.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='techmo.tribune.SynthesizeRequest.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=141,
  serialized_end=224,
)


_SYNTHESIZECONFIG = _descriptor.Descriptor(
  name='SynthesizeConfig',
  full_name='techmo.tribune.SynthesizeConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='techmo.tribune.SynthesizeConfig.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audio_config', full_name='techmo.tribune.SynthesizeConfig.audio_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voice', full_name='techmo.tribune.SynthesizeConfig.voice', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=226,
  serialized_end=351,
)


_AUDIOCONFIG = _descriptor.Descriptor(
  name='AudioConfig',
  full_name='techmo.tribune.AudioConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio_encoding', full_name='techmo.tribune.AudioConfig.audio_encoding', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sample_rate_hertz', full_name='techmo.tribune.AudioConfig.sample_rate_hertz', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='techmo.tribune.AudioConfig.pitch', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='techmo.tribune.AudioConfig.range', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate', full_name='techmo.tribune.AudioConfig.rate', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='techmo.tribune.AudioConfig.volume', index=5,
      number=6, type=2, cpp_type=6, label=1,
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
  serialized_start=354,
  serialized_end=509,
)


_VOICE = _descriptor.Descriptor(
  name='Voice',
  full_name='techmo.tribune.Voice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='techmo.tribune.Voice.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='techmo.tribune.Voice.gender', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='techmo.tribune.Voice.age', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=511,
  serialized_end=606,
)


_VOICEINFO = _descriptor.Descriptor(
  name='VoiceInfo',
  full_name='techmo.tribune.VoiceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='supported_languages', full_name='techmo.tribune.VoiceInfo.supported_languages', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voice', full_name='techmo.tribune.VoiceInfo.voice', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=608,
  serialized_end=686,
)


_SYNTHESIZERESPONSE = _descriptor.Descriptor(
  name='SynthesizeResponse',
  full_name='techmo.tribune.SynthesizeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio', full_name='techmo.tribune.SynthesizeResponse.audio', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='techmo.tribune.SynthesizeResponse.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=688,
  serialized_end=788,
)


_AUDIODATA = _descriptor.Descriptor(
  name='AudioData',
  full_name='techmo.tribune.AudioData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_rate_hertz', full_name='techmo.tribune.AudioData.sample_rate_hertz', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='techmo.tribune.AudioData.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=790,
  serialized_end=845,
)


_PUTLEXICONREQUEST = _descriptor.Descriptor(
  name='PutLexiconRequest',
  full_name='techmo.tribune.PutLexiconRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='techmo.tribune.PutLexiconRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='techmo.tribune.PutLexiconRequest.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=847,
  serialized_end=897,
)


_PUTLEXICONRESPONSE = _descriptor.Descriptor(
  name='PutLexiconResponse',
  full_name='techmo.tribune.PutLexiconResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='techmo.tribune.PutLexiconResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=899,
  serialized_end=957,
)


_DELETELEXICONREQUEST = _descriptor.Descriptor(
  name='DeleteLexiconRequest',
  full_name='techmo.tribune.DeleteLexiconRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='techmo.tribune.DeleteLexiconRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=959,
  serialized_end=995,
)


_DELETELEXICONRESPONSE = _descriptor.Descriptor(
  name='DeleteLexiconResponse',
  full_name='techmo.tribune.DeleteLexiconResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='techmo.tribune.DeleteLexiconResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=997,
  serialized_end=1058,
)


_GETLEXICONREQUEST = _descriptor.Descriptor(
  name='GetLexiconRequest',
  full_name='techmo.tribune.GetLexiconRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='techmo.tribune.GetLexiconRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1060,
  serialized_end=1093,
)


_GETLEXICONRESPONSE = _descriptor.Descriptor(
  name='GetLexiconResponse',
  full_name='techmo.tribune.GetLexiconResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='techmo.tribune.GetLexiconResponse.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='techmo.tribune.GetLexiconResponse.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1095,
  serialized_end=1170,
)


_LISTLEXICONSREQUEST = _descriptor.Descriptor(
  name='ListLexiconsRequest',
  full_name='techmo.tribune.ListLexiconsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='techmo.tribune.ListLexiconsRequest.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1172,
  serialized_end=1211,
)


_LISTLEXICONSRESPONSE = _descriptor.Descriptor(
  name='ListLexiconsResponse',
  full_name='techmo.tribune.ListLexiconsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='techmo.tribune.ListLexiconsResponse.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1213,
  serialized_end=1250,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='techmo.tribune.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='techmo.tribune.Error.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='techmo.tribune.Error.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1252,
  serialized_end=1321,
)

_LISTVOICESRESPONSE.fields_by_name['voices'].message_type = _VOICEINFO
_SYNTHESIZEREQUEST.fields_by_name['config'].message_type = _SYNTHESIZECONFIG
_SYNTHESIZECONFIG.fields_by_name['audio_config'].message_type = _AUDIOCONFIG
_SYNTHESIZECONFIG.fields_by_name['voice'].message_type = _VOICE
_AUDIOCONFIG.fields_by_name['audio_encoding'].enum_type = _AUDIOENCODING
_VOICE.fields_by_name['gender'].enum_type = _GENDER
_VOICE.fields_by_name['age'].enum_type = _AGE
_VOICEINFO.fields_by_name['voice'].message_type = _VOICE
_SYNTHESIZERESPONSE.fields_by_name['audio'].message_type = _AUDIODATA
_SYNTHESIZERESPONSE.fields_by_name['error'].message_type = _ERROR
_PUTLEXICONRESPONSE.fields_by_name['error'].message_type = _ERROR
_DELETELEXICONRESPONSE.fields_by_name['error'].message_type = _ERROR
_GETLEXICONRESPONSE.fields_by_name['error'].message_type = _ERROR
_ERROR.fields_by_name['code'].enum_type = _ERRORCODE
DESCRIPTOR.message_types_by_name['ListVoicesRequest'] = _LISTVOICESREQUEST
DESCRIPTOR.message_types_by_name['ListVoicesResponse'] = _LISTVOICESRESPONSE
DESCRIPTOR.message_types_by_name['SynthesizeRequest'] = _SYNTHESIZEREQUEST
DESCRIPTOR.message_types_by_name['SynthesizeConfig'] = _SYNTHESIZECONFIG
DESCRIPTOR.message_types_by_name['AudioConfig'] = _AUDIOCONFIG
DESCRIPTOR.message_types_by_name['Voice'] = _VOICE
DESCRIPTOR.message_types_by_name['VoiceInfo'] = _VOICEINFO
DESCRIPTOR.message_types_by_name['SynthesizeResponse'] = _SYNTHESIZERESPONSE
DESCRIPTOR.message_types_by_name['AudioData'] = _AUDIODATA
DESCRIPTOR.message_types_by_name['PutLexiconRequest'] = _PUTLEXICONREQUEST
DESCRIPTOR.message_types_by_name['PutLexiconResponse'] = _PUTLEXICONRESPONSE
DESCRIPTOR.message_types_by_name['DeleteLexiconRequest'] = _DELETELEXICONREQUEST
DESCRIPTOR.message_types_by_name['DeleteLexiconResponse'] = _DELETELEXICONRESPONSE
DESCRIPTOR.message_types_by_name['GetLexiconRequest'] = _GETLEXICONREQUEST
DESCRIPTOR.message_types_by_name['GetLexiconResponse'] = _GETLEXICONRESPONSE
DESCRIPTOR.message_types_by_name['ListLexiconsRequest'] = _LISTLEXICONSREQUEST
DESCRIPTOR.message_types_by_name['ListLexiconsResponse'] = _LISTLEXICONSRESPONSE
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.enum_types_by_name['AudioEncoding'] = _AUDIOENCODING
DESCRIPTOR.enum_types_by_name['Gender'] = _GENDER
DESCRIPTOR.enum_types_by_name['Age'] = _AGE
DESCRIPTOR.enum_types_by_name['ErrorCode'] = _ERRORCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListVoicesRequest = _reflection.GeneratedProtocolMessageType('ListVoicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTVOICESREQUEST,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.ListVoicesRequest)
  })
_sym_db.RegisterMessage(ListVoicesRequest)

ListVoicesResponse = _reflection.GeneratedProtocolMessageType('ListVoicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTVOICESRESPONSE,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.ListVoicesResponse)
  })
_sym_db.RegisterMessage(ListVoicesResponse)

SynthesizeRequest = _reflection.GeneratedProtocolMessageType('SynthesizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESIZEREQUEST,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.SynthesizeRequest)
  })
_sym_db.RegisterMessage(SynthesizeRequest)

SynthesizeConfig = _reflection.GeneratedProtocolMessageType('SynthesizeConfig', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESIZECONFIG,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.SynthesizeConfig)
  })
_sym_db.RegisterMessage(SynthesizeConfig)

AudioConfig = _reflection.GeneratedProtocolMessageType('AudioConfig', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOCONFIG,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.AudioConfig)
  })
_sym_db.RegisterMessage(AudioConfig)

Voice = _reflection.GeneratedProtocolMessageType('Voice', (_message.Message,), {
  'DESCRIPTOR' : _VOICE,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.Voice)
  })
_sym_db.RegisterMessage(Voice)

VoiceInfo = _reflection.GeneratedProtocolMessageType('VoiceInfo', (_message.Message,), {
  'DESCRIPTOR' : _VOICEINFO,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.VoiceInfo)
  })
_sym_db.RegisterMessage(VoiceInfo)

SynthesizeResponse = _reflection.GeneratedProtocolMessageType('SynthesizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESIZERESPONSE,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.SynthesizeResponse)
  })
_sym_db.RegisterMessage(SynthesizeResponse)

AudioData = _reflection.GeneratedProtocolMessageType('AudioData', (_message.Message,), {
  'DESCRIPTOR' : _AUDIODATA,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.AudioData)
  })
_sym_db.RegisterMessage(AudioData)

PutLexiconRequest = _reflection.GeneratedProtocolMessageType('PutLexiconRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTLEXICONREQUEST,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.PutLexiconRequest)
  })
_sym_db.RegisterMessage(PutLexiconRequest)

PutLexiconResponse = _reflection.GeneratedProtocolMessageType('PutLexiconResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTLEXICONRESPONSE,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.PutLexiconResponse)
  })
_sym_db.RegisterMessage(PutLexiconResponse)

DeleteLexiconRequest = _reflection.GeneratedProtocolMessageType('DeleteLexiconRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETELEXICONREQUEST,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.DeleteLexiconRequest)
  })
_sym_db.RegisterMessage(DeleteLexiconRequest)

DeleteLexiconResponse = _reflection.GeneratedProtocolMessageType('DeleteLexiconResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETELEXICONRESPONSE,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.DeleteLexiconResponse)
  })
_sym_db.RegisterMessage(DeleteLexiconResponse)

GetLexiconRequest = _reflection.GeneratedProtocolMessageType('GetLexiconRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLEXICONREQUEST,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.GetLexiconRequest)
  })
_sym_db.RegisterMessage(GetLexiconRequest)

GetLexiconResponse = _reflection.GeneratedProtocolMessageType('GetLexiconResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLEXICONRESPONSE,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.GetLexiconResponse)
  })
_sym_db.RegisterMessage(GetLexiconResponse)

ListLexiconsRequest = _reflection.GeneratedProtocolMessageType('ListLexiconsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTLEXICONSREQUEST,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.ListLexiconsRequest)
  })
_sym_db.RegisterMessage(ListLexiconsRequest)

ListLexiconsResponse = _reflection.GeneratedProtocolMessageType('ListLexiconsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTLEXICONSRESPONSE,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.ListLexiconsResponse)
  })
_sym_db.RegisterMessage(ListLexiconsResponse)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'tribune_tts_pb2'
  # @@protoc_insertion_point(class_scope:techmo.tribune.Error)
  })
_sym_db.RegisterMessage(Error)



_TTS = _descriptor.ServiceDescriptor(
  name='TTS',
  full_name='techmo.tribune.TTS',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1613,
  serialized_end=2239,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListVoices',
    full_name='techmo.tribune.TTS.ListVoices',
    index=0,
    containing_service=None,
    input_type=_LISTVOICESREQUEST,
    output_type=_LISTVOICESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SynthesizeStreaming',
    full_name='techmo.tribune.TTS.SynthesizeStreaming',
    index=1,
    containing_service=None,
    input_type=_SYNTHESIZEREQUEST,
    output_type=_SYNTHESIZERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Synthesize',
    full_name='techmo.tribune.TTS.Synthesize',
    index=2,
    containing_service=None,
    input_type=_SYNTHESIZEREQUEST,
    output_type=_SYNTHESIZERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PutLexicon',
    full_name='techmo.tribune.TTS.PutLexicon',
    index=3,
    containing_service=None,
    input_type=_PUTLEXICONREQUEST,
    output_type=_PUTLEXICONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteLexicon',
    full_name='techmo.tribune.TTS.DeleteLexicon',
    index=4,
    containing_service=None,
    input_type=_DELETELEXICONREQUEST,
    output_type=_DELETELEXICONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetLexicon',
    full_name='techmo.tribune.TTS.GetLexicon',
    index=5,
    containing_service=None,
    input_type=_GETLEXICONREQUEST,
    output_type=_GETLEXICONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListLexicons',
    full_name='techmo.tribune.TTS.ListLexicons',
    index=6,
    containing_service=None,
    input_type=_LISTLEXICONSREQUEST,
    output_type=_LISTLEXICONSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TTS)

DESCRIPTOR.services_by_name['TTS'] = _TTS

# @@protoc_insertion_point(module_scope)
