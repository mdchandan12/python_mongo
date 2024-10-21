from pymongo import MongoClient
import random
import string

# Step 1: Connect to MongoDB
client = MongoClient('localhost', 27017)  # Adjust if you have a different connection string

# Step 2: Create a database and collection
db = client['my_database']  # Replace 'my_database' with your database name
collection = db['my_collection']  # Replace 'my_collection' with your collection name

# Step 3: Generate and insert 50 documents
for _ in range(50):
    # Create a random document
    document = {
        'name': ''.join(random.choices(string.ascii_letters, k=10)),
        'age': random.randint(18, 65),
        'email': ''.join(random.choices(string.ascii_letters + string.digits, k=5)) + '@example.com'
    }
    collection.insert_one(document)

print("Inserted 50 documents into the database.")


# Step 3: Fetch all records
documents = collection.find()


# Step 4: Print all records
for document in documents:
    print(document)
    
    
# Step 3: Update some records
# For example, update all documents where age is greater than 30, setting their age to 30
result = collection.update_many(
    {'age': {'$gt': 30}},  # Filter: all documents with age > 30
    {'$set': {'age': 30}}  # Update: set age to 30
)

# Print the number of documents updated
print(f"Updated {result.modified_count} documents.")

# Optional: Fetch and print the updated documents to verify
updated_documents = collection.find({'age': 30})
for document in updated_documents:
     print(document)  