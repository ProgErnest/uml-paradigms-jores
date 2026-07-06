
def multiply(x,y):
    return x*y
product_list = [
    {"name": 'Banana',"unit_price": 100,"quantity": 10},
    {"name": 'Potato',"unit_price": 500,"quantity": 20},
    {"name": 'Bread',"unit_price": 150,"quantity": 5},
    {"name": 'Beans',"unit_price": 300,"quantity": 25},
    {"name": 'Beignet',"unit_price": 50,"quantity": 6}
]
print("""Welcome sir to our new program 
    Here you enter the informations of each product 
    you want to buy then we calculate the cart""")


total_price = sum(map(lambda product: product["unit_price"] * product["quantity"], product_list))


fomated_price = f"{total_price:_.2f}".replace('_',' ') if total_price<50000 else f"you {total_price*0.9:_.2f}".replace('_',' ')
print(f"Total price of shopping cart is : {fomated_price}\n thank you for your confidence")
