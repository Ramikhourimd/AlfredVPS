from pymilvus import MilvusClient
import requests

# 1. Connect to your local Alfred Milvus DB
client = MilvusClient(uri="/Users/ramikhouri/Desktop/Alfred/data/milvus_lite.db")

# 2. Get the embedding for your search query from Ollama
search_text = "meetings about the new dashboard UI"
response = requests.post("http://localhost:11434/api/embeddings", json={
    "model": "nomic-embed-text",
    "prompt": search_text
})
query_vector = response.json()["embedding"]

# 3. Search the vector database for the 5 most semantically similar files!
results = client.search(
    collection_name="vault_embeddings",
    data=[query_vector],
    limit=5,
    output_fields=["id", "path"] # returns the file paths
)

for result in results[0]:
    print(f"Match: {result['entity']['path']} (Score: {result['distance']})")
