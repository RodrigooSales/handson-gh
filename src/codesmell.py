class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
 
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        # Code to update quantity in other places
 
    def calculate_total_price(self):
        return self.price * self.quantity
 
 
class Cart:
    def __init__(self):
        self.products = []
 
    def add_product(self, product):
        self.products.append(product)
        # Code to update cart-related data
 
    def remove_product(self, product):
        self.products.remove(product)
        # Code to update cart-related data
 
    def calculate_cart_total(self):
        total = 0
        for product in self.products:
            total += product.calculate_total_price()
        return total