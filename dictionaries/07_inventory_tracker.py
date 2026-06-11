# Practise nested dictionaries using products instead of study topics.

products = {
        "coffee": {
            "price": 3.50,
            "stock": 10
        },
        "tea": {
            "price": 2.75,
            "stock": 8
        },
        "sandwich": {
                "price": 5.00,
                "stock": 6
                }
}

print("-"*60)
for product, details in products.items():
    print("Product:", product)
    print("Price:", details["price"])
    print("Stock:", details["stock"])
    print("-"*60)

products["coffee"]["stock"] -= 2
products["tea"]["stock"] -= 1


print("-"*60)
for product, details in products.items():
    if details["stock"] < 8:
        print("Stock is low")

    print("Product:", product)
    print("Price:", details["price"])
    print("Stock:", details["stock"])
    print("-"*60)

