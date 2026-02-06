def filter_by_budget(products, budget):
    return [p for p in products if p["price"] <= budget]
