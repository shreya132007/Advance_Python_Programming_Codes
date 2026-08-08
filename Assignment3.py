# TITLE : Design Patterns in Python

"""
Write a program to implement a Configurable Payment Processing System Using Strategy Pattern.
"""


from abc import ABC, abstractmethod

# Strategy Interface
class Payment_strategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class Credit_card_payment(Payment_strategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} using Credit Card")


# Concrete Strategy 2
class Debit_card_payment(Payment_strategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} using Debit Card")


# Concrete Strategy 3
class Upi_payment(Payment_strategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} using UPI")


# Concrete Strategy 4
class Net_banking(Payment_strategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} using Net Banking")


# Context Class
class Payment_processor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy is None:
            print("Please select a payment method.")
        else:
            self.strategy.pay(amount)


# Main Program
processor = Payment_processor()

amount = float(input("Enter payment amount: ₹"))

print("\nSelect Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. Net Banking")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    processor.set_strategy(Credit_card_payment())
elif choice == 2:
    processor.set_strategy(Debit_card_payment())
elif choice == 3:
    processor.set_strategy(Upi_payment())
elif choice == 4:
    processor.set_strategy(Net_banking())
else:
    print("Invalid choice!")
    exit()

processor.process_payment(amount)

#output
# Enter payment amount: ₹100

# Select Payment Method
# 1. Credit Card
# 2. Debit Card
# 3. UPI
# 4. Net Banking
# Enter your choice (1-4): 3
# Payment of ₹100.0 using UPI