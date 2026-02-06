from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from tools.retriever import retrieve_products
from tools.budget_filter import filter_by_budget
from tools.comparator import compare_products
import os

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def recommend(search_query, budget):
    products = retrieve_products(search_query)
    filtered = filter_by_budget(products, budget)
    top_products = compare_products(filtered)
    
    if not top_products:
        return "No products found matching your criteria."
    
    best = top_products[0]
    others = top_products[1:] if len(top_products) > 1 else []
    
    others_text = "\n".join([f"{i+1}. {p['name']} — ₹{p['price']}" for i, p in enumerate(others)])
    
    prompt = f"""
User wants: "{search_query}" under budget ₹{budget}

Best product: {best['name']} (₹{best['price']}) - {best['description']}

Other options:
{others_text}

Format your response EXACTLY like this:
Best Recommendation:
[Product Name]

Reason:
- [short reason 1]
- [short reason 2] 
- [short reason 3]

Other options:
1. [Product Name] — [one key feature]
2. [Product Name] — [one key feature]

Keep reasons under 6 words each.
"""
    
    response = llm.invoke(prompt)
    return response.content
