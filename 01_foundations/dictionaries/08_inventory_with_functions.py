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

# get the product
def get_product():
    
    choices = ["sandwich", "coffee", "tea"]

    while True:
        
        print("Which item do you want")
        product = input("(Tea | Coffee | Sandwich): ").lower()

        if product in choices:
            return product
        else:
            print("Not on the list bud!")

def sale(products, product):
    while True:

        try:
            qty = int(input("Items sold: "))
            break
        except ValueError:
            print("Not a valid entry")

    products[product]["stock"] = products[product]["stock"] - qty

    return products[product]["stock"]

    

def main():
    product = get_product()
    print("Product:", product)

    sold = sale(products, product)
    print(product, sold)

if __name__ == "__main__":
    main()


