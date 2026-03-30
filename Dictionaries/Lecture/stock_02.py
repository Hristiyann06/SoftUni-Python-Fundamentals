products = input().split()
stock_list = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    products[key] = int(value)

products_search_engine = input("Search for product: ").split(" ")

for product in products_search_engine:
    if product in stock_list:
        print(f"We have {stock_list[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")