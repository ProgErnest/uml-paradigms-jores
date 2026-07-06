
class Product:
    def __init__(self, name, unit_price, quantity):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity
    def get_total_price(self):
        return self.unit_price * self.quantity
    def display_product_info(self):
        print(f"Name: {self.name}\nUnit price: {self.unit_price}\nQuantity: {self.quantity}")
class Cart:
    def __init__(self):
        self.products = []
        self.total_price = 0
    def add_product(self, product):
        self.products.append(product)
    def get_total_price(self):
        for product in self.products:
            self.total_price += product.get_total_price()
        return self.total_price
    def apply_discount(self):
        if self.total_price > 50000:
            self.total_price *= 0.9
    def display_informations(self):
        for product in self.products:
            product.display_product_info()
        print(f"\n\n The total price is {self.total_price}")

if __name__ == "__main__":
    shopping_cart = Cart()
    while True:
        product_name = input("Enter the name of the product: ")
        product_unit_price = float(input("\nEnter the unit price of the product: "))
        product_quantity = int(input("\nEnter the quantity of the product: "))
        product = Product(product_name, product_unit_price, product_quantity)
        continue_shopping = input("\nDo you want to add another product? (yes/no): ")
        shopping_cart.add_product(product)
        if(continue_shopping == "yes"):
            continue
        break

total_price = shopping_cart.get_total_price()
discounted_price = shopping_cart.apply_discount()
new_total_price = shopping_cart.get_total_price()
result= f"Your total cart is :{total_price}" if(total_price == new_total_price) else f"You have a dicscount your new price is {new_total_price}"
print(result)
shopping_cart.display_informations()