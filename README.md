This is a basic example of an e-commerce system implemented using Object-Oriented Programming (OOP) principles in Python.

Classes
Product
Represents a product with the following attributes:

product_id: Unique identifier for the product.
name: Name of the product.
price: Price of the product.
stock: Current stock quantity of the product.
Methods:

__init__(self, product_id, name, price, stock): Initializes a new Product object.
update_stock(self, quantity): Updates the stock quantity by adding the given quantity (can be positive or negative).
display_info(self): Prints the product's information.
ShoppingCart
Represents a shopping cart that holds products.

Attributes:

items: A dictionary to store products and their quantities. The keys are product_id and the values are dictionaries containing the product object and the quantity.
Methods:

__init__(self): Initializes an empty ShoppingCart.
add_item(self, product, quantity): Adds a specified quantity of a product to the cart. It also updates the product's stock.
remove_item(self, product, quantity): Removes a specified quantity of a product from the cart. If the quantity to remove is greater than or equal to the quantity in the cart, it removes all of that product. It also updates the product's stock.
get_total(self): Calculates and returns the total price of all items in the cart.
display_cart(self): Prints the contents of the shopping cart and the total price.
Example Usage
The code includes an example demonstrating how to create Product objects,add and remove items from the ShoppingCart, and display the product information and cart contents.

