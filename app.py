from dotenv import load_dotenv
load_dotenv()

import re
from intent.intent_extractor import extract_intent
from agents.recommendation_agent import recommend

def extract_budget(text):
    match = re.search(r'(\d{4,6})', text)
    if match:
        return int(match.group(1))
    return 30000  # default

if __name__ == "__main__":
    user_input = input("Describe what you want: ")

    budget = extract_budget(user_input)
    intent = extract_intent(user_input)

    search_query = " ".join(intent["needs"] + intent["preferences"])

    result = recommend(search_query, budget)
    print("\n" + result)
