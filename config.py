from pymongo.mongo_client import MongoClient
import urllib

usernmae = urllib.parse.quote("goodghost340")
passwd = urllib.parse.quote("riot@vky342")

uri = "mongodb+srv://%s:%s@blogcust.yl7ag.mongodb.net/?retryWrites=true&w=majority&appName=blogcust&ssl=true&ssl_cert_reqs=CERT_NONE" % (usernmae, passwd)

# Create a new client and connect to the server
client = MongoClient(uri)
db = client["blogcust"]
mycollection = db["CONTENTS"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)