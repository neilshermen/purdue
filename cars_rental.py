# cars_rental.py
# Created On Wed 8/28/2024

from datetime import datetime, timedelta

class CarRental:
    def __init__(self, stock=0):
        """
        Constructor for CarRental class.
        stock: Number of available cars
        """
        self.stock = stock
        self.rental_time = None
        self.rental_basis = None
        self.num_of_cars = 0

    def display_available_cars(self):
        """Displays the number of available cars."""
        print(f"Available cars: {self.stock}")
        return self.stock

    def rent_car_on_hourly_basis(self, num_of_cars):
        """
        Rents cars on an hourly basis.
        num_of_cars: Number of cars to rent
        """
        if num_of_cars <= 0:
            print("Number of cars should be positive.")
            return None
        elif num_of_cars > self.stock:
            print(f"Requested cars are more than available stock: {self.stock}")
            return None
        else:
            self.rental_basis = 'hourly'
            self.rental_time = datetime.now()
            self.num_of_cars = num_of_cars
            self.stock -= num_of_cars
            print(f"Rented {num_of_cars} car(s) on an hourly basis at {self.rental_time}.")
            return self.rental_time

    def rent_car_on_daily_basis(self, num_of_cars):
        """
        Rents cars on a daily basis.
        num_of_cars: Number of cars to rent
        """
        if num_of_cars <= 0:
            print("Number of cars should be positive.")
            return None
        elif num_of_cars > self.stock:
            print(f"Requested cars are more than available stock: {self.stock}")
            return None
        else:
            self.rental_basis = 'daily'
            self.rental_time = datetime.now()
            self.num_of_cars = num_of_cars
            self.stock -= num_of_cars
            print(f"Rented {num_of_cars} car(s) on a daily basis at {self.rental_time}.")
            return self.rental_time

    def rent_car_on_weekly_basis(self, num_of_cars):
        """
        Rents cars on a weekly basis.
        num_of_cars: Number of cars to rent
        """
        if num_of_cars <= 0:
            print("Number of cars should be positive.")
            return None
        elif num_of_cars > self.stock:
            print(f"Requested cars are more than available stock: {self.stock}")
            return None
        else:
            self.rental_basis = 'weekly'
            self.rental_time = datetime.now()
            self.num_of_cars = num_of_cars
            self.stock -= num_of_cars
            print(f"Rented {num_of_cars} car(s) on a weekly basis at {self.rental_time}.")
            return self.rental_time

    def return_car(self):
        """
        Returns the cars and generates the bill.
        """
        if self.rental_time is None:
            print("You did not rent a car.")
            return None
        
        now = datetime.now()
        rental_period = now - self.rental_time

        bill = 0
        if self.rental_basis == 'hourly':
            bill = round(rental_period.total_seconds() / 3600) * 5 * self.num_of_cars
        elif self.rental_basis == 'daily':
            bill = round(rental_period.days) * 20 * self.num_of_cars
        elif self.rental_basis == 'weekly':
            bill = round(rental_period.days / 7) * 60 * self.num_of_cars
        
        print(f"Returning {self.num_of_cars} car(s).")
        print(f"Total bill: ${bill}")
        
        self.stock += self.num_of_cars
        self.rental_time = None
        self.rental_basis = None
        self.num_of_cars = 0

        return bill


class Customer:
    def __init__(self):
        """
        Constructor for Customer class.
        """
        self.num_of_cars = 0
        self.rental_basis = None
        self.rental_time = None

    def request_car(self):
        """
        Requests cars from the car rental.
        """
        num_of_cars = int(input("How many cars would you like to rent? "))
        if num_of_cars < 1:
            print("Number of cars should be greater than zero.")
            return None
        else:
            self.num_of_cars = num_of_cars
        return self.num_of_cars

    def return_car(self):
        """
        Returns the rented cars.
        """
        if self.num_of_cars == 0:
            print("No cars to return.")
            return 0
        return self.num_of_cars
