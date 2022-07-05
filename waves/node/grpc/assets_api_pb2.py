# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waves/node/grpc/assets_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waves import transaction_pb2 as waves_dot_transaction__pb2
from waves.node.grpc import accounts_api_pb2 as waves_dot_node_dot_grpc_dot_accounts__api__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n waves/node/grpc/assets_api.proto\x12\x0fwaves.node.grpc\x1a\x17waves/transaction.proto\x1a\"waves/node/grpc/accounts_api.proto\" \n\x0c\x41ssetRequest\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\"D\n\nNFTRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\x16\n\x0e\x61\x66ter_asset_id\x18\x03 \x01(\x0c\"W\n\x0bNFTResponse\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x36\n\nasset_info\x18\x02 \x01(\x0b\x32\".waves.node.grpc.AssetInfoResponse\"\x92\x02\n\x11\x41ssetInfoResponse\x12\x0e\n\x06issuer\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x04 \x01(\x05\x12\x12\n\nreissuable\x18\x05 \x01(\x08\x12\x14\n\x0ctotal_volume\x18\x06 \x01(\x03\x12+\n\x06script\x18\x07 \x01(\x0b\x32\x1b.waves.node.grpc.ScriptData\x12\x13\n\x0bsponsorship\x18\x08 \x01(\x03\x12\x33\n\x11issue_transaction\x18\x0b \x01(\x0b\x32\x18.waves.SignedTransaction\x12\x17\n\x0fsponsor_balance\x18\n \x01(\x03\x32\xa4\x01\n\tAssetsApi\x12L\n\x07GetInfo\x12\x1d.waves.node.grpc.AssetRequest\x1a\".waves.node.grpc.AssetInfoResponse\x12I\n\nGetNFTList\x12\x1b.waves.node.grpc.NFTRequest\x1a\x1c.waves.node.grpc.NFTResponse0\x01\x42s\n\x1a\x63om.wavesplatform.api.grpcZCgithub.com/wavesplatform/gowaves/pkg/grpc/generated/waves/node/grpc\xaa\x02\x0fWaves.Node.Grpcb\x06proto3')



_ASSETREQUEST = DESCRIPTOR.message_types_by_name['AssetRequest']
_NFTREQUEST = DESCRIPTOR.message_types_by_name['NFTRequest']
_NFTRESPONSE = DESCRIPTOR.message_types_by_name['NFTResponse']
_ASSETINFORESPONSE = DESCRIPTOR.message_types_by_name['AssetInfoResponse']
AssetRequest = _reflection.GeneratedProtocolMessageType('AssetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ASSETREQUEST,
  '__module__' : 'waves.node.grpc.assets_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.AssetRequest)
  })
_sym_db.RegisterMessage(AssetRequest)

NFTRequest = _reflection.GeneratedProtocolMessageType('NFTRequest', (_message.Message,), {
  'DESCRIPTOR' : _NFTREQUEST,
  '__module__' : 'waves.node.grpc.assets_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.NFTRequest)
  })
_sym_db.RegisterMessage(NFTRequest)

NFTResponse = _reflection.GeneratedProtocolMessageType('NFTResponse', (_message.Message,), {
  'DESCRIPTOR' : _NFTRESPONSE,
  '__module__' : 'waves.node.grpc.assets_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.NFTResponse)
  })
_sym_db.RegisterMessage(NFTResponse)

AssetInfoResponse = _reflection.GeneratedProtocolMessageType('AssetInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _ASSETINFORESPONSE,
  '__module__' : 'waves.node.grpc.assets_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.AssetInfoResponse)
  })
_sym_db.RegisterMessage(AssetInfoResponse)

_ASSETSAPI = DESCRIPTOR.services_by_name['AssetsApi']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.wavesplatform.api.grpcZCgithub.com/wavesplatform/gowaves/pkg/grpc/generated/waves/node/grpc\252\002\017Waves.Node.Grpc'
  _ASSETREQUEST._serialized_start=114
  _ASSETREQUEST._serialized_end=146
  _NFTREQUEST._serialized_start=148
  _NFTREQUEST._serialized_end=216
  _NFTRESPONSE._serialized_start=218
  _NFTRESPONSE._serialized_end=305
  _ASSETINFORESPONSE._serialized_start=308
  _ASSETINFORESPONSE._serialized_end=582
  _ASSETSAPI._serialized_start=585
  _ASSETSAPI._serialized_end=749
# @@protoc_insertion_point(module_scope)