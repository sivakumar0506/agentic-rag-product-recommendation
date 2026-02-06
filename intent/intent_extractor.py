from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
import os
import json
import re

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def extract_intent(user_text):
    prompt = f"""
Extract user intent from the sentence below.

Sentence:
"{user_text}"

Return ONLY valid JSON with:
- needs (list)
- preferences (list)

Example:
{{
  "needs": ["gaming"],
  "preferences": ["good camera", "strong battery"]
}}
"""

    response = llm.invoke(prompt)
    content = response.content.strip()
    
    # Extract JSON from markdown code blocks if present
    json_match = re.search(r'```(?:json)?\s*({.*?})\s*```', content, re.DOTALL)
    if json_match:
        content = json_match.group(1)
    
    # Try to find JSON object in the response
    json_match = re.search(r'{.*}', content, re.DOTALL)
    if json_match:
        content = json_match.group(0)
    
    return json.loads(content)
