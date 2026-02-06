# Agentic RAG Product Recommendation System

This project implements an Agentic Retrieval-Augmented Generation (RAG)
based product recommendation system using Groq LLM, FAISS vector database,
and LangChain.

## Features
- Natural language user queries
- Automatic extraction of user needs, preferences, and budget
- Semantic product retrieval using embeddings
- Budget-based filtering
- Explainable recommendations

## Tech Stack
- Python
- Groq (LLaMA 3)
- LangChain
- FAISS
- HuggingFace Embeddings

## How to Run
```bash
pip install -r requirements.txt
python embeddings/vector_store.py
python app.py
```
it displays:
Describe what you want:
type like -> give me a android phone under 30000 budget with good camera and gaming performance

//output:
Best Recommendation:
Realme C55

Reason:
- Good camera
- Strong battery
- Low price

Other options:
1. Realme Narzo 60 — Fast charging
2. OnePlus Nord CE 3 — Smooth gaming
