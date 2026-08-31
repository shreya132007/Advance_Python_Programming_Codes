"""
TOPIC :- HOTEL FOOD ORDERING SYSTEM

Develop a Python application to maintain hotel food order records.
CO1 – Object-Oriented Programming
Create the following classes: Order , Customer Name , Food Item , Order Amount 
Categorize orders as : Veg , Non-Veg 
Implement methods to display order details : Restaurant , Add order records , Display all orders.
"""

class Order:
    def __init__(self, customer_name, food_item, order_amount, category):
        self.customer_name = customer_name
        self.food_item = food_item
        self.order_amount = order_amount
        self.category = category

    def display(self):
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Order Amount:", self.order_amount)
        print("Category:", self.category)
        print("------------------------")


class Restaurant:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def display_orders(self):
        print("All Order Records")
        print("========================")

        for order in self.orders:
            order.display()


# Creating Restaurant object
restaurant = Restaurant()

# Creating Order objects
order1 = Order("Shreya", "Paneer Tikka", 250, "Veg")
order2 = Order("Rahul", "Chicken Biryani", 300, "Non-Veg")
order3 = Order("Aman", "Veg Pizza", 200, "Veg")

# Adding orders to restaurant
restaurant.add_order(order1)
restaurant.add_order(order2)
restaurant.add_order(order3)

# Displaying all orders
restaurant.display_orders()