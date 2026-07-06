
product = dict.fromkeys(["name","unit_price","quantity"])
product_list = []
print("""Welcome sir to our new program 
    Here you enter the informations of each product 
    you want to buy then we calculate the cart""")

while True:
    product["name"] = input("Enter the name of the product: ")
    product["unit_price"] = float(input("\nEnter the unit price of the product: "))
    product["quantity"] = int(input("\nEnter the quantity of the product: "))
    product_list.append(product.copy())
    continue_shopping = input("\nDo you want to add another product? (yes/no): ")
    if(continue_shopping == "yes"):
        continue
    break
total_price = 0
for article in product_list:
    total_price += article["unit_price"] * article["quantity"]

total_price = total_price if total_price < 50000 else total_price * 0.9
fomated_price = f"{total_price:_.2f}".replace('_',' ')
print(f"Total price of shopping cart is : {fomated_price}\n thank you for your confidence")
