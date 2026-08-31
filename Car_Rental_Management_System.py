"""
TOPIC :- CAR RENTAL MANAGEMENT SYSTEM

Develop a Python application to manage rental cars.
CO1 – Object-Oriented Programming
Create the following classes : Car , Car Number , Model , Rent Per Day 
Categorize cars as : Luxury , Sedan , Hatchback 
Implement methods to display car details , RentalAgency , Add car details , Display available cars.
"""

class Car:
    def __init__(self, car_number, model, rent_per_day, category):
        self.car_number = car_number
        self.model = model
        self.rent_per_day = rent_per_day
        self.category = category

    def display(self):
        print("Car Number:", self.car_number)
        print("Model:", self.model)
        print("Rent Per Day:", self.rent_per_day)
        print("Category:", self.category)
        print("------------------------")


class RentalAgency:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def display_cars(self):
        print("Available Cars")
        print("========================")

        for car in self.cars:
            car.display()


# Creating RentalAgency object
agency = RentalAgency()

# Creating Car objects
car1 = Car("MH12AB1234", "BMW", 5000, "Luxury")
car2 = Car("MH14CD5678", "Honda City", 2500, "Sedan")
car3 = Car("MH12EF9012", "Swift", 1500, "Hatchback")

# Adding cars to agency
agency.add_car(car1)
agency.add_car(car2)
agency.add_car(car3)

# Displaying available cars
agency.display_cars()