#Exercise:1
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        return f"{super().display_info()}, Number of Doors: {self.number_of_doors}"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_laze):
        super().__init__(make, model, year)
        self.type_of_laze = type_of_laze

    def display_info(self):
        return f"{super().display_info()}, Type of Laze: {self.type_of_laze}"

# Example usage:
car = Car('Toyota', 'Corolla', 2021, 4)
motorcycle = Motorcycle('Harley-Davidson', 'Street 750', 2020, 'Cruiser')

print(car.display_info())
print(motorcycle.display_info())

#Exercise2
#To show how polymorphism works in python
def print_vehicle_info(vehicle):
    print(vehicle.display_info())

# Example usage:
car = Car('Toyota', 'Corolla', 2021, 4)
motorcycle = Motorcycle('Harley-Davidson', 'Street 750', 2020, 'Cruiser')

print_vehicle_info(car)
print_vehicle_info(motorcycle)

#Exercise 3
def print_all_vehicle_info(vehicles):
    for vehicle in vehicles:
        print(vehicle.display_info())

# Example usage:
car = Car('Toyota', 'Corolla', 2021, 4)
motorcycle = Motorcycle('Harley-Davidson', 'Street 750', 2020, 'Cruiser')
vehicles = [car, motorcycle]

print_all_vehicle_info(vehicles)
