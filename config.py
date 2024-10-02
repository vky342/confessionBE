from pymongo.mongo_client import MongoClient
import urllib

usernmae = urllib.parse.quote("kunalsahu071")
passwd = urllib.parse.quote("root@vky342")

uri = "mongodb+srv://%s:%s@confessiontest.dpwqu.mongodb.net/?retryWrites=true&w=majority&appName=confessiontest&ssl=true&ssl_cert_reqs=CERT_NONE" % (usernmae, passwd)

# Create a new client and connect to the server
client = MongoClient(uri)
db = client["confessiontest"]
mycollection = db["Submits"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB! confession test")
except Exception as e:
    print(e)