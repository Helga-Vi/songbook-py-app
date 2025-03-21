from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Access the database
db = client['test_database']

# Access the collection
collection = db['test_collection']

# Insert a document
document = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
result = collection.insert_one(document)
print(f"Inserted document with ID: {result.inserted_id}")

# Find all documents
all_documents = collection.find()
for doc in all_documents:
    print(doc)

# Update a document
update_result = collection.update_one(
    {"name": "John Doe"},
    {"$set": {"age": 31}}
)
print(f"Updated {update_result.matched_count} document(s)")

# Delete a document
delete_result = collection.delete_one({"name": "John Doe"})
print(f"Deleted {delete_result.deleted_count} document(s)")

# Close the connection
client.close()