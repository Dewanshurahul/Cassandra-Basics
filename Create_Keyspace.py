from cassandra.cluster import Cluster

try:
    cluster = Cluster()
    print('Connection Established !!!')
except:
    print("Cnnection didn't get created !!!")

try:
    session = cluster.connect('crud')
    print('Session Successfully Created !!!')
except:
    print("Session didn't get Created !!!")

name = raw_input("Enter Keyspace name to create: ")
query = "CREATE KEYSPACE %s WITH replication = {'class':'SimpleStrategy', 'replication_factor' :1};" % (name)
print("Query is: ",query)
try:
    session.execute(query)
    print("KeySapce Created Sucessfully !!!")
except:
    print("Query didn't get Executed !!!")
