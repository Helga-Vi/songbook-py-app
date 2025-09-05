from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['songbook_db']
collection = db['messages']
