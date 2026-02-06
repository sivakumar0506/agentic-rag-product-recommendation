def compare_products(products):
    products = sorted(products, key=lambda x: x["price"])
    return products[:3]
