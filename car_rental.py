# car_rental.py
from datetime import datetime

class CarRental:
    def __init__(self, stock=0):
        """Constructor to initialize the stock of cars"""
        self.stock = stock

    def display_cars(self):
        """Displays the available cars for rent"""
        print(f"We have currently {self.stock} cars available to rent.")
        return self.stock

    def rent_hourly(self, num_of_cars):
        """Rent cars on an hourly basis"""
        if num_of_cars <= 0:
            print("The number of cars should be positive!")
            return None
        elif num_of_cars > self.stock:
            print(f"Sorry, we only have {self.stock} cars available to rent.")
            return None
        else:
            self.stock -= num_of_cars
            now = datetime.now()
            print(f"Rented {num_of_cars} car(s) on hourly basis at {now.hour} hours.")
            return now

    def rent_daily(self, num_of_cars):
        """Rent cars on a daily basis"""
        if num_of_cars <= 0:
            print("The number of cars should be positive!")
            return None
        elif num_of_cars > self.stock:
            print(f"Sorry, we only have {self.stock} cars available to rent.")
            return None
        else:
            self.stock -= num_of_cars
            now = datetime.now()
            print(f"Rented {num_of_cars} car(s) on daily basis at {now}.")
            return now

    def rent_weekly(self, num_of_cars):
        """Rent cars on a weekly basis"""
        if num_of_cars <= 0:
            print("The number of cars should be positive!")
            return None
        elif num_of_cars > self.stock:
            print(f"Sorry, we only have {self.stock} cars available to rent.")
            return None
        else:
            self.stock -= num_of_cars
            now = datetime.now()
            print(f"Rented {num_of_cars} car(s) on weekly basis at {now}.")
            return now

    def return_cars(self, request):
        """Process the return of rented cars and generate the bill"""
        rental_time, rental_basis, num_of_cars = request
        if rental_time and rental_basis and num_of_cars:
            self.stock += num_of_cars
            now = datetime.now()
            rental_period = now - rental_time

            if rental_basis == 1:  # hourly
                bill = rental_period.seconds // 3600 * 5 * num_of_cars
            elif rental_basis == 2:  # daily
                bill = rental_period.days * 20 * num_of_cars
            elif rental_basis == 3:  # weekly
                bill = (rental_period.days // 7) * 60 * num_of_cars

            print(f"Your bill is ${bill}. Thank you for returning the car(s)!")
            return bill
        else:
            print("Are you sure you rented a car with us?")
            return None


class Customer:
    def __init__(self):
        self.cars = 0
        self.rental_basis = 0
        self.rental_time = None

    def request_car(self):
        """Request the number of cars to rent"""
        cars = input("How many cars would you like to rent? ")
        try:
            cars = int(cars)
        except ValueError:
            print("The number of cars should be a positive integer.")
            return -1
        if cars < 1:
            print("The number of cars should be greater than zero.")
            return -1
        else:
            self.cars = cars
            return self.cars

    def return_car(self):
        """Return the cars to the rental shop"""
        if self.rental_time and self.rental_basis and self.cars:
            return self.rental_time, self.rental_basis, self.cars
        else:
            return None
