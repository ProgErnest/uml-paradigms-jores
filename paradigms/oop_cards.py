
class Product:

    def __init__(self, name, unit_price, quantity):
        self.__name = name
        self.__unit_price = unit_price
        self.__quantity = quantity

    def get_total_price(self):
        return self.__unit_price * self.__quantity
    
    def display_product_info(self):
        print(f"Name: {self.__name}\nUnit price: {self.__unit_price}\nQuantity: {self.__quantity}")


class Cart:
    def __init__(self):
        self.__products = []
        self.__total_price = 0

    def add_product(self, product):
        self.__products.append(product)

    def get_total_price(self):
        self.__total_price = 0
        for product in self.__products:
            self.__total_price += product.get_total_price()
        return self.__total_price
    
    def apply_discount(self):
        if self.__total_price > 50000:
            self.__total_price = self.__total_price * 0.9
            print("A discount has been applied")
            return self.__total_price
        else:
            print("No discount")
            return self.__total_price


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
    result= f"Your total cart is :{discounted_price:_.2f} FCFA\n thank you for your confidence".replace('_',' ')
    print(result)
