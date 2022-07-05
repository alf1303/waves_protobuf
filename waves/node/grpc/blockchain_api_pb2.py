# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waves/node/grpc/blockchain_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$waves/node/grpc/blockchain_api.proto\x12\x0fwaves.node.grpc\x1a\x1bgoogle/protobuf/empty.proto\")\n\x17\x41\x63tivationStatusRequest\x12\x0e\n\x06height\x18\x01 \x01(\x05\"\xad\x01\n\x18\x41\x63tivationStatusResponse\x12\x0e\n\x06height\x18\x01 \x01(\x05\x12\x17\n\x0fvoting_interval\x18\x02 \x01(\x05\x12\x18\n\x10voting_threshold\x18\x03 \x01(\x05\x12\x12\n\nnext_check\x18\x04 \x01(\x05\x12:\n\x08\x66\x65\x61tures\x18\x05 \x03(\x0b\x32(.waves.node.grpc.FeatureActivationStatus\"\xab\x03\n\x17\x46\x65\x61tureActivationStatus\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12[\n\x11\x62lockchain_status\x18\x03 \x01(\x0e\x32@.waves.node.grpc.FeatureActivationStatus.BlockchainFeatureStatus\x12O\n\x0bnode_status\x18\x04 \x01(\x0e\x32:.waves.node.grpc.FeatureActivationStatus.NodeFeatureStatus\x12\x19\n\x11\x61\x63tivation_height\x18\x05 \x01(\x05\x12\x19\n\x11supporting_blocks\x18\x06 \x01(\x05\"E\n\x17\x42lockchainFeatureStatus\x12\r\n\tUNDEFINED\x10\x00\x12\x0c\n\x08\x41PPROVED\x10\x01\x12\r\n\tACTIVATED\x10\x02\"D\n\x11NodeFeatureStatus\x12\x13\n\x0fNOT_IMPLEMENTED\x10\x00\x12\x0f\n\x0bIMPLEMENTED\x10\x01\x12\t\n\x05VOTED\x10\x02\")\n\x12\x42\x61seTargetResponse\x12\x13\n\x0b\x62\x61se_target\x18\x01 \x01(\x03\"\x1e\n\rScoreResponse\x12\r\n\x05score\x18\x01 \x01(\x0c\x32\x97\x02\n\rBlockchainApi\x12j\n\x13GetActivationStatus\x12(.waves.node.grpc.ActivationStatusRequest\x1a).waves.node.grpc.ActivationStatusResponse\x12L\n\rGetBaseTarget\x12\x16.google.protobuf.Empty\x1a#.waves.node.grpc.BaseTargetResponse\x12L\n\x12GetCumulativeScore\x12\x16.google.protobuf.Empty\x1a\x1e.waves.node.grpc.ScoreResponseBs\n\x1a\x63om.wavesplatform.api.grpcZCgithub.com/wavesplatform/gowaves/pkg/grpc/generated/waves/node/grpc\xaa\x02\x0fWaves.Node.Grpcb\x06proto3')



_ACTIVATIONSTATUSREQUEST = DESCRIPTOR.message_types_by_name['ActivationStatusRequest']
_ACTIVATIONSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['ActivationStatusResponse']
_FEATUREACTIVATIONSTATUS = DESCRIPTOR.message_types_by_name['FeatureActivationStatus']
_BASETARGETRESPONSE = DESCRIPTOR.message_types_by_name['BaseTargetResponse']
_SCORERESPONSE = DESCRIPTOR.message_types_by_name['ScoreResponse']
_FEATUREACTIVATIONSTATUS_BLOCKCHAINFEATURESTATUS = _FEATUREACTIVATIONSTATUS.enum_types_by_name['BlockchainFeatureStatus']
_FEATUREACTIVATIONSTATUS_NODEFEATURESTATUS = _FEATUREACTIVATIONSTATUS.enum_types_by_name['NodeFeatureStatus']
ActivationStatusRequest = _reflection.GeneratedProtocolMessageType('ActivationStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONSTATUSREQUEST,
  '__module__' : 'waves.node.grpc.blockchain_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.ActivationStatusRequest)
  })
_sym_db.RegisterMessage(ActivationStatusRequest)

ActivationStatusResponse = _reflection.GeneratedProtocolMessageType('ActivationStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONSTATUSRESPONSE,
  '__module__' : 'waves.node.grpc.blockchain_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.ActivationStatusResponse)
  })
_sym_db.RegisterMessage(ActivationStatusResponse)

FeatureActivationStatus = _reflection.GeneratedProtocolMessageType('FeatureActivationStatus', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREACTIVATIONSTATUS,
  '__module__' : 'waves.node.grpc.blockchain_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.FeatureActivationStatus)
  })
_sym_db.RegisterMessage(FeatureActivationStatus)

BaseTargetResponse = _reflection.GeneratedProtocolMessageType('BaseTargetResponse', (_message.Message,), {
  'DESCRIPTOR' : _BASETARGETRESPONSE,
  '__module__' : 'waves.node.grpc.blockchain_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.BaseTargetResponse)
  })
_sym_db.RegisterMessage(BaseTargetResponse)

ScoreResponse = _reflection.GeneratedProtocolMessageType('ScoreResponse', (_message.Message,), {
  'DESCRIPTOR' : _SCORERESPONSE,
  '__module__' : 'waves.node.grpc.blockchain_api_pb2'
  # @@protoc_insertion_point(class_scope:waves.node.grpc.ScoreResponse)
  })
_sym_db.RegisterMessage(ScoreResponse)

_BLOCKCHAINAPI = DESCRIPTOR.services_by_name['BlockchainApi']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.wavesplatform.api.grpcZCgithub.com/wavesplatform/gowaves/pkg/grpc/generated/waves/node/grpc\252\002\017Waves.Node.Grpc'
  _ACTIVATIONSTATUSREQUEST._serialized_start=86
  _ACTIVATIONSTATUSREQUEST._serialized_end=127
  _ACTIVATIONSTATUSRESPONSE._serialized_start=130
  _ACTIVATIONSTATUSRESPONSE._serialized_end=303
  _FEATUREACTIVATIONSTATUS._serialized_start=306
  _FEATUREACTIVATIONSTATUS._serialized_end=733
  _FEATUREACTIVATIONSTATUS_BLOCKCHAINFEATURESTATUS._serialized_start=594
  _FEATUREACTIVATIONSTATUS_BLOCKCHAINFEATURESTATUS._serialized_end=663
  _FEATUREACTIVATIONSTATUS_NODEFEATURESTATUS._serialized_start=665
  _FEATUREACTIVATIONSTATUS_NODEFEATURESTATUS._serialized_end=733
  _BASETARGETRESPONSE._serialized_start=735
  _BASETARGETRESPONSE._serialized_end=776
  _SCORERESPONSE._serialized_start=778
  _SCORERESPONSE._serialized_end=808
  _BLOCKCHAINAPI._serialized_start=811
  _BLOCKCHAINAPI._serialized_end=1090
# @@protoc_insertion_point(module_scope)
