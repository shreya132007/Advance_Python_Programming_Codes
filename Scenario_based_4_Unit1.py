"""
4. Mobile Store Management System

Develop a Python application to maintain mobile phone details.
Requirements
1. Create a Mobile class with:Brand, Model, Price
2. Categorize mobiles as:Premium, Mid-range, Budget
3. Create a Store class.
4. Add mobiles.
5. Display all mobiles.
"""


class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, "
              f"Price: ₹{self.price}, Category: {self.category()}")


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_all(self):
        print("\n--- Mobile Store ---")
        for mobile in self.mobiles:
            mobile.display()


# Create store
store = Store()

# Add mobiles
store.add_mobile(Mobile("Apple", "iPhone 15", 70000))
store.add_mobile(Mobile("Samsung", "Galaxy A55", 30000))
store.add_mobile(Mobile("Redmi", "Note 13", 15000))

# Display all mobiles
store.display_all()