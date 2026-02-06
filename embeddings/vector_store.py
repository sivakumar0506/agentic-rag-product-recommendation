import json
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

def create_vector_store():
    with open("data/products.json") as f:
        products = json.load(f)

    docs = []
    for p in products:
        text = f"{p['name']} {p['description']} price {p['price']}"
        docs.append(Document(page_content=text, metadata=p))

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(docs, embeddings)
    db.save_local("faiss_store")

if __name__ == "__main__":
    create_vector_store()
