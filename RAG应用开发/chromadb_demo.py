import chromadb

db = chromadb.PersistentClient(path="chroma.db")

collections = db.list_collections()

print(collections)