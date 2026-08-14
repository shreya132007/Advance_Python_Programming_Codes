"""
7. Product Inventory System

Develop a Python application to manage product records.
Requirements
1. Create a Product class with:Product ID, Product Name, Price
2. Categorize products as:Expensive, Affordable
3. Create an Inventory class.
4. Display all products.
"""

class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

        # Categorize product
        if price >= 50000:
            self.category = "Expensive"
        else:
            self.category = "Affordable"

    def display(self):
        print(f"ID: {self.product_id}")
        print(f"Name: {self.product_name}")
        print(f"Price: ₹{self.price}")
        print(f"Category: {self.category}")
        print("-" * 30)


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all(self):
        print("\n--- Product Inventory ---")
        for product in self.products:
            product.display()


# Create Inventory object
inventory = Inventory()

# Add products
inventory.add_product(Product(101, "Laptop", 65000))
inventory.add_product(Product(102, "Mouse", 800))
inventory.add_product(Product(103, "Smartphone", 45000))
inventory.add_product(Product(104, "Tablet", 55000))

# Display all products
inventory.display_all()