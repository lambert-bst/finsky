# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buy_instruments.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import check_promo_offer_pb2 as check__promo__offer__pb2
import create_instrument_pb2 as create__instrument__pb2
import instrument_setup_info_proto_pb2 as instrument__setup__info__proto__pb2
import billing_profile_protos_pb2 as billing__profile__protos__pb2
import challenge_proto_pb2 as challenge__proto__pb2
import common_device_pb2 as common__device__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='buy_instruments.proto',
  package='BuyInstruments',
  syntax='proto2',
  serialized_pb=_b('\n\x15\x62uy_instruments.proto\x12\x0e\x42uyInstruments\x1a\x17\x63heck_promo_offer.proto\x1a\x17\x63reate_instrument.proto\x1a!instrument_setup_info_proto.proto\x1a\x1c\x62illing_profile_protos.proto\x1a\x15\x63hallenge_proto.proto\x1a\x13\x63ommon_device.proto\"9\n\x17\x43heckInstrumentResponse\x12\x1e\n\x16userHasValidInstrument\x18\x01 \x01(\x08\"\xb1\x01\n\x16RedeemGiftCardResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x17\n\x0fuserMessageHtml\x18\x02 \x01(\t\x12\x13\n\x0b\x62\x61lanceHtml\x18\x03 \x01(\t\x12:\n\x10\x61\x64\x64ressChallenge\x18\x04 \x01(\x0b\x32 .ChallengeProto.AddressChallenge\x12\x1d\n\x15\x63heckoutTokenRequired\x18\x05 \x01(\x08\"~\n\x1bInstrumentSetupInfoResponse\x12@\n\tsetupInfo\x18\x01 \x03(\x0b\x32-.InstrumentSetupInfoProto.InstrumentSetupInfo\x12\x1d\n\x15\x63heckoutTokenRequired\x18\x02 \x01(\x08\")\n\x15\x43heckIabPromoResponse\x12\x10\n\x08\x65ligible\x18\x01 \x01(\x08\"^\n\x17UpdateInstrumentRequest\x12,\n\ninstrument\x18\x01 \x01(\x0b\x32\x18.CommonDevice.Instrument\x12\x15\n\rcheckoutToken\x18\x02 \x01(\t\"\xaf\x01\n\x18\x43reateInstrumentResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x17\n\x0fuserMessageHtml\x18\x02 \x01(\t\x12\x14\n\x0cinstrumentId\x18\x03 \x01(\t\x12T\n\x19\x63reateInstrumentFlowState\x18\x04 \x01(\x0b\x32\x31.CreateInstrument.DeviceCreateInstrumentFlowState\"\x7f\n\x16\x42illingProfileResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12<\n\x0e\x62illingProfile\x18\x02 \x01(\x0b\x32$.BillingProfileProtos.BillingProfile\x12\x17\n\x0fuserMessageHtml\x18\x03 \x01(\t\"\xfa\x01\n%GetInitialInstrumentFlowStateResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x17\n\x0fuserMessageHtml\x18\x02 \x01(\t\x12T\n\x19\x63reateInstrumentFlowState\x18\x03 \x01(\x0b\x32\x31.CreateInstrument.DeviceCreateInstrumentFlowState\x12R\n\x18\x63reateInstrumentMetadata\x18\x04 \x01(\x0b\x32\x30.CreateInstrument.DeviceCreateInstrumentMetadata\"\xf3\x01\n\x18UpdateInstrumentResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x14\n\x0cinstrumentId\x18\x02 \x01(\t\x12\x17\n\x0fuserMessageHtml\x18\x03 \x01(\t\x12=\n\x0f\x65rrorInputField\x18\x04 \x03(\x0b\x32$.ChallengeProto.InputValidationError\x12\x1d\n\x15\x63heckoutTokenRequired\x18\x05 \x01(\x08\x12:\n\rredeemedOffer\x18\x06 \x01(\x0b\x32#.CheckPromoOffer.RedeemedPromoOffer\"\xef\x01\n\x17\x43reateInstrumentRequest\x12\x46\n\nflowHandle\x18\x01 \x01(\x0b\x32\x32.CreateInstrument.DeviceCreateInstrumentFlowHandle\x12<\n\x10profileFormInput\x18\x02 \x01(\x0b\x32\".CreateInstrument.ProfileFormInput\x12N\n\x19usernamePasswordFormInput\x18\x03 \x01(\x0b\x32+.CreateInstrument.UsernamePasswordFormInputB2\n com.google.android.finsky.protosB\x0e\x42uyInstruments')
  ,
  dependencies=[check__promo__offer__pb2.DESCRIPTOR,create__instrument__pb2.DESCRIPTOR,instrument__setup__info__proto__pb2.DESCRIPTOR,billing__profile__protos__pb2.DESCRIPTOR,challenge__proto__pb2.DESCRIPTOR,common__device__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHECKINSTRUMENTRESPONSE = _descriptor.Descriptor(
  name='CheckInstrumentResponse',
  full_name='BuyInstruments.CheckInstrumentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userHasValidInstrument', full_name='BuyInstruments.CheckInstrumentResponse.userHasValidInstrument', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=257,
)


_REDEEMGIFTCARDRESPONSE = _descriptor.Descriptor(
  name='RedeemGiftCardResponse',
  full_name='BuyInstruments.RedeemGiftCardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='BuyInstruments.RedeemGiftCardResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userMessageHtml', full_name='BuyInstruments.RedeemGiftCardResponse.userMessageHtml', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='balanceHtml', full_name='BuyInstruments.RedeemGiftCardResponse.balanceHtml', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='addressChallenge', full_name='BuyInstruments.RedeemGiftCardResponse.addressChallenge', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checkoutTokenRequired', full_name='BuyInstruments.RedeemGiftCardResponse.checkoutTokenRequired', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=260,
  serialized_end=437,
)


_INSTRUMENTSETUPINFORESPONSE = _descriptor.Descriptor(
  name='InstrumentSetupInfoResponse',
  full_name='BuyInstruments.InstrumentSetupInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='setupInfo', full_name='BuyInstruments.InstrumentSetupInfoResponse.setupInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checkoutTokenRequired', full_name='BuyInstruments.InstrumentSetupInfoResponse.checkoutTokenRequired', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=439,
  serialized_end=565,
)


_CHECKIABPROMORESPONSE = _descriptor.Descriptor(
  name='CheckIabPromoResponse',
  full_name='BuyInstruments.CheckIabPromoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='eligible', full_name='BuyInstruments.CheckIabPromoResponse.eligible', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=567,
  serialized_end=608,
)


_UPDATEINSTRUMENTREQUEST = _descriptor.Descriptor(
  name='UpdateInstrumentRequest',
  full_name='BuyInstruments.UpdateInstrumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instrument', full_name='BuyInstruments.UpdateInstrumentRequest.instrument', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checkoutToken', full_name='BuyInstruments.UpdateInstrumentRequest.checkoutToken', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=704,
)


_CREATEINSTRUMENTRESPONSE = _descriptor.Descriptor(
  name='CreateInstrumentResponse',
  full_name='BuyInstruments.CreateInstrumentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='BuyInstruments.CreateInstrumentResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userMessageHtml', full_name='BuyInstruments.CreateInstrumentResponse.userMessageHtml', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instrumentId', full_name='BuyInstruments.CreateInstrumentResponse.instrumentId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='createInstrumentFlowState', full_name='BuyInstruments.CreateInstrumentResponse.createInstrumentFlowState', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=707,
  serialized_end=882,
)


_BILLINGPROFILERESPONSE = _descriptor.Descriptor(
  name='BillingProfileResponse',
  full_name='BuyInstruments.BillingProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='BuyInstruments.BillingProfileResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='billingProfile', full_name='BuyInstruments.BillingProfileResponse.billingProfile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userMessageHtml', full_name='BuyInstruments.BillingProfileResponse.userMessageHtml', index=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=884,
  serialized_end=1011,
)


_GETINITIALINSTRUMENTFLOWSTATERESPONSE = _descriptor.Descriptor(
  name='GetInitialInstrumentFlowStateResponse',
  full_name='BuyInstruments.GetInitialInstrumentFlowStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='BuyInstruments.GetInitialInstrumentFlowStateResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userMessageHtml', full_name='BuyInstruments.GetInitialInstrumentFlowStateResponse.userMessageHtml', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='createInstrumentFlowState', full_name='BuyInstruments.GetInitialInstrumentFlowStateResponse.createInstrumentFlowState', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='createInstrumentMetadata', full_name='BuyInstruments.GetInitialInstrumentFlowStateResponse.createInstrumentMetadata', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1014,
  serialized_end=1264,
)


_UPDATEINSTRUMENTRESPONSE = _descriptor.Descriptor(
  name='UpdateInstrumentResponse',
  full_name='BuyInstruments.UpdateInstrumentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='BuyInstruments.UpdateInstrumentResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instrumentId', full_name='BuyInstruments.UpdateInstrumentResponse.instrumentId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userMessageHtml', full_name='BuyInstruments.UpdateInstrumentResponse.userMessageHtml', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errorInputField', full_name='BuyInstruments.UpdateInstrumentResponse.errorInputField', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checkoutTokenRequired', full_name='BuyInstruments.UpdateInstrumentResponse.checkoutTokenRequired', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='redeemedOffer', full_name='BuyInstruments.UpdateInstrumentResponse.redeemedOffer', index=5,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1267,
  serialized_end=1510,
)


_CREATEINSTRUMENTREQUEST = _descriptor.Descriptor(
  name='CreateInstrumentRequest',
  full_name='BuyInstruments.CreateInstrumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flowHandle', full_name='BuyInstruments.CreateInstrumentRequest.flowHandle', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='profileFormInput', full_name='BuyInstruments.CreateInstrumentRequest.profileFormInput', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usernamePasswordFormInput', full_name='BuyInstruments.CreateInstrumentRequest.usernamePasswordFormInput', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1513,
  serialized_end=1752,
)

_REDEEMGIFTCARDRESPONSE.fields_by_name['addressChallenge'].message_type = challenge__proto__pb2._ADDRESSCHALLENGE
_INSTRUMENTSETUPINFORESPONSE.fields_by_name['setupInfo'].message_type = instrument__setup__info__proto__pb2._INSTRUMENTSETUPINFO
_UPDATEINSTRUMENTREQUEST.fields_by_name['instrument'].message_type = common__device__pb2._INSTRUMENT
_CREATEINSTRUMENTRESPONSE.fields_by_name['createInstrumentFlowState'].message_type = create__instrument__pb2._DEVICECREATEINSTRUMENTFLOWSTATE
_BILLINGPROFILERESPONSE.fields_by_name['billingProfile'].message_type = billing__profile__protos__pb2._BILLINGPROFILE
_GETINITIALINSTRUMENTFLOWSTATERESPONSE.fields_by_name['createInstrumentFlowState'].message_type = create__instrument__pb2._DEVICECREATEINSTRUMENTFLOWSTATE
_GETINITIALINSTRUMENTFLOWSTATERESPONSE.fields_by_name['createInstrumentMetadata'].message_type = create__instrument__pb2._DEVICECREATEINSTRUMENTMETADATA
_UPDATEINSTRUMENTRESPONSE.fields_by_name['errorInputField'].message_type = challenge__proto__pb2._INPUTVALIDATIONERROR
_UPDATEINSTRUMENTRESPONSE.fields_by_name['redeemedOffer'].message_type = check__promo__offer__pb2._REDEEMEDPROMOOFFER
_CREATEINSTRUMENTREQUEST.fields_by_name['flowHandle'].message_type = create__instrument__pb2._DEVICECREATEINSTRUMENTFLOWHANDLE
_CREATEINSTRUMENTREQUEST.fields_by_name['profileFormInput'].message_type = create__instrument__pb2._PROFILEFORMINPUT
_CREATEINSTRUMENTREQUEST.fields_by_name['usernamePasswordFormInput'].message_type = create__instrument__pb2._USERNAMEPASSWORDFORMINPUT
DESCRIPTOR.message_types_by_name['CheckInstrumentResponse'] = _CHECKINSTRUMENTRESPONSE
DESCRIPTOR.message_types_by_name['RedeemGiftCardResponse'] = _REDEEMGIFTCARDRESPONSE
DESCRIPTOR.message_types_by_name['InstrumentSetupInfoResponse'] = _INSTRUMENTSETUPINFORESPONSE
DESCRIPTOR.message_types_by_name['CheckIabPromoResponse'] = _CHECKIABPROMORESPONSE
DESCRIPTOR.message_types_by_name['UpdateInstrumentRequest'] = _UPDATEINSTRUMENTREQUEST
DESCRIPTOR.message_types_by_name['CreateInstrumentResponse'] = _CREATEINSTRUMENTRESPONSE
DESCRIPTOR.message_types_by_name['BillingProfileResponse'] = _BILLINGPROFILERESPONSE
DESCRIPTOR.message_types_by_name['GetInitialInstrumentFlowStateResponse'] = _GETINITIALINSTRUMENTFLOWSTATERESPONSE
DESCRIPTOR.message_types_by_name['UpdateInstrumentResponse'] = _UPDATEINSTRUMENTRESPONSE
DESCRIPTOR.message_types_by_name['CreateInstrumentRequest'] = _CREATEINSTRUMENTREQUEST

CheckInstrumentResponse = _reflection.GeneratedProtocolMessageType('CheckInstrumentResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKINSTRUMENTRESPONSE,
  __module__ = 'buy_instruments_pb2'
  # @@protoc_insertion_point(class_scope:BuyInstruments.CheckInstrumentResponse)
  ))
_sym_db.RegisterMessage(CheckInstrumentResponse)

RedeemGiftCardResponse = _reflection.GeneratedProtocolMessageType('RedeemGiftCardResponse', (_message.Message,), dict(
  DESCRIPTOR = _REDEEMGIFTCARDRESPONSE,
  __module__ = 'buy_instruments_pb2'
  # @@protoc_insertion_point(class_scope:BuyInstruments.RedeemGiftCardResponse)
  ))
_sym_db.RegisterMessage(RedeemGiftCardResponse)

InstrumentSetupInfoResponse = _reflection.GeneratedProtocolMessageType('InstrumentSetupInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _INSTRUMENTSETUPINFORESPONSE,
  __module__ = 'buy_instruments_pb2'
  # @@protoc_insertion_point(class_scope:BuyInstruments.InstrumentSetupInfoResponse)
  ))
_sym_db.RegisterMessage(InstrumentSetupInfoResponse)

CheckIabPromoResponse = _reflection.GeneratedProtocolMessageType('CheckIabPromoResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKIABPROMORESPONSE,
  __module__ = 'buy_instruments_pb2'
  # @@protoc_insertion_point(class_scope:BuyInstruments.CheckIabPromoResponse)
  ))
_sym_db.RegisterMessage(CheckIabPromoResponse)

UpdateInstrumentRequest = _reflection.GeneratedProtocolMessageType('UpdateInstrumentRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEINSTRUMENTREQUEST,
  __module__ = 'buy_instruments_pb2'
  # @@protoc_insertion_point(class_scope:BuyInstruments.UpdateInstrumentRequest)
  ))
_sym_db.RegisterMessage(UpdateInstrumentRequest)

CreateInstrumentResponse = _reflection.GeneratedProtocolMessageType('CreateInstrumentResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEINSTRUMENTRESPONSE,
  __module__ = 'buy_instruments_pb2'
  # @@protoc_insertion_point(class_scope:BuyInstruments.CreateInstrumentResponse)
  ))
_sym_db.RegisterMessage(CreateInstrumentResponse)

BillingProfileResponse = _reflection.GeneratedProtocolMessageType('BillingProfileResponse', (_message.Message,), dict(
  DESCRIPTOR = _BILLINGPROFILERESPONSE,
  __module__ = 'buy_instruments_pb2'
  # @@protoc_insertion_point(class_scope:BuyInstruments.BillingProfileResponse)
  ))
_sym_db.RegisterMessage(BillingProfileResponse)

GetInitialInstrumentFlowStateResponse = _reflection.GeneratedProtocolMessageType('GetInitialInstrumentFlowStateResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETINITIALINSTRUMENTFLOWSTATERESPONSE,
  __module__ = 'buy_instruments_pb2'
  # @@protoc_insertion_point(class_scope:BuyInstruments.GetInitialInstrumentFlowStateResponse)
  ))
_sym_db.RegisterMessage(GetInitialInstrumentFlowStateResponse)

UpdateInstrumentResponse = _reflection.GeneratedProtocolMessageType('UpdateInstrumentResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEINSTRUMENTRESPONSE,
  __module__ = 'buy_instruments_pb2'
  # @@protoc_insertion_point(class_scope:BuyInstruments.UpdateInstrumentResponse)
  ))
_sym_db.RegisterMessage(UpdateInstrumentResponse)

CreateInstrumentRequest = _reflection.GeneratedProtocolMessageType('CreateInstrumentRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEINSTRUMENTREQUEST,
  __module__ = 'buy_instruments_pb2'
  # @@protoc_insertion_point(class_scope:BuyInstruments.CreateInstrumentRequest)
  ))
_sym_db.RegisterMessage(CreateInstrumentRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\016BuyInstruments'))
# @@protoc_insertion_point(module_scope)