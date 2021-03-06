



from gremlin_python.driver import client, serializer
import sys, traceback

from flask import Flask
app = Flask(__name__)
_gremlin_cleanup_graph = "g.V().drop()"

_gremlin_insert_vertices = [
    "g.addV('person').property('id', 'thom@m.com')",
    "g.addV('person').property('id', 'mary@m.com')",
    "g.addV('person').property('id', 'ben@m.com')"
]

_gremlin_insert_edges = [
    "g.V('thom@m.com').addE('emails').to(g.V('mary@m.com')).property('date', '13/01/02').property('subject', 'Trump is great')",
    "g.V('thom@m.com').addE('emails').to(g.V('ben@m.com')).property('date', '14/02/02').property('subject', 'Hillary should be ***')"
]

_gremlin_update_vertices = [
    "g.V('thomas').property('age', 44)"
]

_gremlin_count_vertices = "g.V().count()"

_gremlin_traversals = {
    "Get all persons older than 40"          : "g.V().hasLabel('person')",
    "Get all persons and their first name"   : "g.E()",
    "Get all persons that Thomas knows"      : "g.V('thom@m.com').out('emails').hasLabel('person').values('id')",
    "Get the path from Thomas to Robin"      : "g.V('thom@m.com').repeat(out()).until(has('id', 'ben@m.com')).path()"
}

_gremlin_drop_operations = {
    "Drop Edge - Thomas no longer knows Mary" : "g.V('thomas').outE('knows').where(inV().has('id', 'mary')).drop()",
    "Drop Vertex - Drop Thomas"               : "g.V('thomas').drop()"
}

def cleanup_graph(client):
    print("\tRunning this Gremlin query:\n\t{0}".format(_gremlin_cleanup_graph))
    callback = client.submitAsync(_gremlin_cleanup_graph)
    if callback.result() is not None:
        print("\tCleaned up the graph!")
    print("\n")

def insert_vertices(client):
    for query in _gremlin_insert_vertices:
        print("\tRunning this Gremlin query:\n\t{0}\n".format(query))
        callback = client.submitAsync(query)
        if callback.result() is not None:
            print("\tInserted this vertex:\n\t{0}\n".format(callback.result().one()))
        else:
            print("Something went wrong with this query: {0}".format(query))
    print("\n")

def insert_edges(client):
    for query in _gremlin_insert_edges:
        print("\tRunning this Gremlin query:\n\t{0}\n".format(query))
        callback = client.submitAsync(query)
        if callback.result() is not None:
            print("\tInserted this edge:\n\t{0}\n".format(callback.result().one()))
        else:
            print("Something went wrong with this query:\n\t{0}".format(query))
    print("\n")

def update_vertices(client):
    for query in _gremlin_update_vertices:
        print("\tRunning this Gremlin query:\n\t{0}\n".format(query))
        callback = client.submitAsync(query)
        if callback.result() is not None:
            print("\tUpdated this vertex:\n\t{0}\n".format(callback.result().one()))
        else:
            print("Something went wrong with this query:\n\t{0}".format(query))
    print("\n")

def count_vertices(client):
    print("\tRunning this Gremlin query:\n\t{0}".format(_gremlin_count_vertices))
    callback = client.submitAsync(_gremlin_count_vertices)
    if callback.result() is not None:
        msg = str(callback.result().one())
    else:
        print("Something went wrong with this query: {0}".format(_gremlin_count_vertices))
    return msg

def execute_traversals(client):
    for key in _gremlin_traversals:
        print("\t{0}:".format(key))
        print("\tRunning this Gremlin query:\n\t{0}\n".format(_gremlin_traversals[key]))
        callback = client.submitAsync(_gremlin_traversals[key])
        for result in callback.result():
            print("\t{0}".format(str(result)))
        print("\n")

def execute_drop_operations(client):
    for key in _gremlin_drop_operations:
        print("\t{0}:".format(key))
        print("\tRunning this Gremlin query:\n\t{0}".format(_gremlin_drop_operations[key]))
        callback = client.submitAsync(_gremlin_drop_operations[key])
        for result in callback.result():
            print(result)
        print("\n")
"""
try:

    
    print("Welcome to Azure Cosmos DB + Gremlin on Python!")
    
    # Drop the entire Graph
    input("We're about to drop whatever graph is on the server. Press any key to continue...")
    cleanup_graph(client)

    # Insert all vertices
    input("Let's insert some vertices into the graph. Press any key to continue...")
    insert_vertices(client)

    # Create edges between vertices
    input("Now, let's add some edges between the vertices. Press any key to continue...")
    insert_edges(client)
    
    # Execute traversals and get results 
    input("Cool! Let's run some traversals on our graph. Press any key to continue...")
    execute_traversals(client)
    # Update a couple of vertices
    input("Ah, sorry. I made a mistake. Let's change the ages of these two vertices. Press any key to continue...")
    update_vertices(client)

    # Count all vertices
    input("Okay. Let's count how many vertices we have. Press any key to continue...")
    count_vertices(client)



    # Drop a few vertices and edges
    input("So, life happens and now we will make some changes to the graph. Press any key to continue...")
    execute_drop_operations(client)

    # Count all vertices again
    input("How many vertices do we have left? Press any key to continue...")
    count_vertices(client)
except Exception as e:
    print('There was an exception: {0}'.format(e))
    traceback.print_exc(file=sys.stdout)
    sys.exit(1)

print("\nAnd that's all! Sample complete")
input("Press Enter to continue...")
"""
def grem():
    msg = "test"    
    return msg

@app.route("/")
def hello():
    
    from gremlin_python.driver import client, serializer
    client = client.Client('wss://enronhack.gremlin.cosmosdb.azure.com:443/','g', 
        username="/dbs/mail/colls/mail", 
        password="uYf1V0bSUHF5HSb5e0qgIyFTVONwyAXf4BRFbs5Z2rDNlFaTauta2ctQbubdNy2bMaQpQQOdyB8Laza01IeWNA==",
	message_serializer=serializer.GraphSONSerializersV2d0()        
        )
    msg = count_vertices(client)
    return msg
