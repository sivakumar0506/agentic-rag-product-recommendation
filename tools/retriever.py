from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local("faiss_store", embeddings, allow_dangerous_deserialization=True)

def retrieve_products(query):
    docs = db.similarity_search(query, k=5)
    return [d.metadata for d in docs]
