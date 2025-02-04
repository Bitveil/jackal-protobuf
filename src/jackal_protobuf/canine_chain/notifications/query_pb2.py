"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ...google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ...cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ...canine_chain.notifications import params_pb2 as canine__chain_dot_notifications_dot_params__pb2
from ...canine_chain.notifications import notification_pb2 as canine__chain_dot_notifications_dot_notification__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&canine_chain/notifications/query.proto\x12\x1a\x63\x61nine_chain.notifications\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\'canine_chain/notifications/params.proto\x1a-canine_chain/notifications/notification.proto\"\r\n\x0bQueryParams\"O\n\x13QueryParamsResponse\x12\x38\n\x06params\x18\x01 \x01(\x0b\x32\".canine_chain.notifications.ParamsB\x04\xc8\xde\x1f\x00\";\n\x11QueryNotification\x12\n\n\x02to\x18\x01 \x01(\t\x12\x0c\n\x04\x66rom\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x03\"a\n\x19QueryNotificationResponse\x12\x44\n\x0cnotification\x18\x01 \x01(\x0b\x32(.canine_chain.notifications.NotificationB\x04\xc8\xde\x1f\x00\"S\n\x15QueryAllNotifications\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xa3\x01\n\x1dQueryAllNotificationsResponse\x12\x45\n\rnotifications\x18\x01 \x03(\x0b\x32(.canine_chain.notifications.NotificationB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"h\n\x1eQueryAllNotificationsByAddress\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x12\n\n\x02to\x18\x02 \x01(\t\"\xac\x01\n&QueryAllNotificationsByAddressResponse\x12\x45\n\rnotifications\x18\x01 \x03(\x0b\x32(.canine_chain.notifications.NotificationB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\xfd\x05\n\x05Query\x12\x95\x01\n\x06Params\x12\'.canine_chain.notifications.QueryParams\x1a/.canine_chain.notifications.QueryParamsResponse\"1\x82\xd3\xe4\x93\x02+\x12)/jackal/canine-chain/notifications/params\x12\xc1\x01\n\x0cNotification\x12-.canine_chain.notifications.QueryNotification\x1a\x35.canine_chain.notifications.QueryNotificationResponse\"K\x82\xd3\xe4\x93\x02\x45\x12\x43/jackal/canine-chain/notifications/notifications/{to}/{from}/{time}\x12\xba\x01\n\x10\x41llNotifications\x12\x31.canine_chain.notifications.QueryAllNotifications\x1a\x39.canine_chain.notifications.QueryAllNotificationsResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/jackal/canine-chain/notifications/notifications\x12\xda\x01\n\x19\x41llNotificationsByAddress\x12:.canine_chain.notifications.QueryAllNotificationsByAddress\x1a\x42.canine_chain.notifications.QueryAllNotificationsByAddressResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/jackal/canine-chain/notifications/notifications/{to}B:Z8github.com/jackalLabs/canine-chain/x/notifications/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'canine_chain.notifications.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/jackalLabs/canine-chain/x/notifications/types'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYNOTIFICATIONRESPONSE'].fields_by_name['notification']._loaded_options = None
  _globals['_QUERYNOTIFICATIONRESPONSE'].fields_by_name['notification']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLNOTIFICATIONSRESPONSE'].fields_by_name['notifications']._loaded_options = None
  _globals['_QUERYALLNOTIFICATIONSRESPONSE'].fields_by_name['notifications']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLNOTIFICATIONSBYADDRESSRESPONSE'].fields_by_name['notifications']._loaded_options = None
  _globals['_QUERYALLNOTIFICATIONSBYADDRESSRESPONSE'].fields_by_name['notifications']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002+\022)/jackal/canine-chain/notifications/params'
  _globals['_QUERY'].methods_by_name['Notification']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Notification']._serialized_options = b'\202\323\344\223\002E\022C/jackal/canine-chain/notifications/notifications/{to}/{from}/{time}'
  _globals['_QUERY'].methods_by_name['AllNotifications']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllNotifications']._serialized_options = b'\202\323\344\223\0022\0220/jackal/canine-chain/notifications/notifications'
  _globals['_QUERY'].methods_by_name['AllNotificationsByAddress']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllNotificationsByAddress']._serialized_options = b'\202\323\344\223\0027\0225/jackal/canine-chain/notifications/notifications/{to}'
  _globals['_QUERYPARAMS']._serialized_start=287
  _globals['_QUERYPARAMS']._serialized_end=300
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=302
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=381
  _globals['_QUERYNOTIFICATION']._serialized_start=383
  _globals['_QUERYNOTIFICATION']._serialized_end=442
  _globals['_QUERYNOTIFICATIONRESPONSE']._serialized_start=444
  _globals['_QUERYNOTIFICATIONRESPONSE']._serialized_end=541
  _globals['_QUERYALLNOTIFICATIONS']._serialized_start=543
  _globals['_QUERYALLNOTIFICATIONS']._serialized_end=626
  _globals['_QUERYALLNOTIFICATIONSRESPONSE']._serialized_start=629
  _globals['_QUERYALLNOTIFICATIONSRESPONSE']._serialized_end=792
  _globals['_QUERYALLNOTIFICATIONSBYADDRESS']._serialized_start=794
  _globals['_QUERYALLNOTIFICATIONSBYADDRESS']._serialized_end=898
  _globals['_QUERYALLNOTIFICATIONSBYADDRESSRESPONSE']._serialized_start=901
  _globals['_QUERYALLNOTIFICATIONSBYADDRESSRESPONSE']._serialized_end=1073
  _globals['_QUERY']._serialized_start=1076
  _globals['_QUERY']._serialized_end=1841
# @@protoc_insertion_point(module_scope)
