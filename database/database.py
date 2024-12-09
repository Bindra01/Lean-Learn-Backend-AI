
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ansuman-shukla:ansuman@cluster0.zkpcq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["questions_db"]
mcq_collection = db["mcq_collection"]
tf_collection = db["tf_collection"]
fill_collection = db["fill_collection"]
formula_collection = db["formula_collection"]

print(client.list_database_names())


