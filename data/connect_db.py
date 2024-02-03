from pymongo import MongoClient
url_connection = "mongodb+srv://octaviovaldez:123octavis@cluster0.rzukclz.mongodb.net/"
CLIENT = MongoClient(url_connection)
DB = CLIENT["MovieWebSiteDB"]
COLLECTION = DB["Movies"]
