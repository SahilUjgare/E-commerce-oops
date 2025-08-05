# creating class of Product

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store products and their quantities

    def add_item(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}
        product.update_stock(-quantity)
        print(f"Added {quantity} of {product.name} to the cart.")

    def remove_item(self, product, quantity):
        if product.product_id in self.items:
            if self.items[product.product_id]['quantity'] <= quantity:
                product.update_stock(self.items[product.product_id]['quantity'])
                del self.items[product.product_id]
                print(f"Removed all {product.name} from the cart.")
            else:
                self.items[product.product_id]['quantity'] -= quantity
                product.update_stock(quantity)
                print(f"Removed {quantity} of {product.name} from the cart.")
        else:
            print(f"{product.name} not found in the cart.")

    def get_total(self):
        total = 0
        for item_data in self.items.values():
            total += item_data['product'].price * item_data['quantity']
        return total

    def display_cart(self):
        if not self.items:
            print("Shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item_data in self.items.values():
                product = item_data['product']
                quantity = item_data['quantity']
                print(f"- {product.name} (Quantity: {quantity})")
            print(f"Total: ${self.get_total():.2f}")

# Example Usage:
product1 = Product("001", "Laptop", 1200.00, 10)
product2 = Product("002", "Mouse", 25.00, 50)

cart = ShoppingCart()

product1.display_info()
product2.display_info()

cart.add_item(product1, 2)
cart.add_item(product2, 5)
cart.add_item(product1, 1) # Add more of the same item

cart.display_cart()

cart.remove_item(product2, 2)
cart.remove_item(product1, 5) # Try to remove more than available

cart.display_cart()

product1.display_info() # Check updated stock
product2.display_info() # Check updated stock
