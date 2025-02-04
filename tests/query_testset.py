import grpc
import jackal_protobuf.canine_chain.filetree.query_pb2 as filetree_query_pb2
import jackal_protobuf.canine_chain.filetree.query_pb2_grpc as filetree_query_pb2_grpc
import jackal_protobuf.canine_chain.jklmint.query_pb2 as jklmint_query_pb2
import jackal_protobuf.canine_chain.jklmint.query_pb2_grpc as jklmint_query_pb2_grpc
import jackal_protobuf.canine_chain.notifications.query_pb2 as notifications_query_pb2
import jackal_protobuf.canine_chain.notifications.query_pb2_grpc as notifications_query_pb2_grpc
import jackal_protobuf.canine_chain.oracle.query_pb2 as oracle_query_pb2
import jackal_protobuf.canine_chain.oracle.query_pb2_grpc as oracle_query_pb2_grpc
import jackal_protobuf.canine_chain.rns.query_pb2 as rns_query_pb2
import jackal_protobuf.canine_chain.rns.query_pb2_grpc as rns_query_pb2_grpc
import jackal_protobuf.canine_chain.storage.query_pb2 as storage_query_pb2
import jackal_protobuf.canine_chain.storage.query_pb2_grpc as storage_query_pb2_grpc

channel = grpc.secure_channel('grpc.jackal.nodestake.org:443', grpc.ssl_channel_credentials())


# This specific query is problematic, due to wrong deserialization of response by grpc module, it may throw wrong deserialization exception or just hang.
# "Problematic" data may be contained inside file.contents field of a file, like escaped or weird bytestring representations.
# Contents field in files is deprecated on Jackal Protocol, using every other query method on files with empty contents field works fine.
# Filetree module query
def FiletreeQuery():
    try:
        stub = filetree_query_pb2_grpc.QueryStub(channel) 
        request = filetree_query_pb2.QueryAllFiles()
        return stub.AllFiles(request)
    except Exception as e:
        print(e)

# Jklmint module query
def JklmintQuery():
    try:
        stub = jklmint_query_pb2_grpc.QueryStub(channel) 
        request = jklmint_query_pb2.QueryInflation()
        return stub.Inflation(request)
    except Exception as e:
        print(e)

# Notifications module query
def NotificationsQuery():
    try:
        stub = notifications_query_pb2_grpc.QueryStub(channel) 
        request = notifications_query_pb2.QueryAllNotifications()
        return stub.AllNotifications(request)
    except Exception as e:
        print(e)

# Oracle module query
def OracleQuery():
    try:
        stub = oracle_query_pb2_grpc.QueryStub(channel) 
        request = oracle_query_pb2.QueryAllFeeds()
        return stub.AllFeeds(request)
    except Exception as e:
        print(e)

# Rns module query
def RnsQuery():
    try:
        stub = rns_query_pb2_grpc.QueryStub(channel)
        request = rns_query_pb2.QueryAllNames()
        return stub.AllNames(request)
    except Exception as e:
        print(e)

def StorageQuery():
    try:
        stub = storage_query_pb2_grpc.QueryStub(channel)
        request = storage_query_pb2.QueryAllFiles()
        return stub.AllFiles(request)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print("Filetree OK!") if FiletreeQuery() else print("Filetree Exception")
    print("Oracle OK!") if OracleQuery() else print("Oracle Exception")
    print("Jklmint OK!") if JklmintQuery() else print("Jklmint Exception")
    print("Notifications OK!") if NotificationsQuery() else print("Notifications Exception")
    print("Rns OK!") if RnsQuery() else print("Rns Exception")
