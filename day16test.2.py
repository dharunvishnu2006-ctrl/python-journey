class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} kmph")

class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)
        self.num_doors = num_doors

    def car_info(self):
        print(f"Car with {self.num_doors} doors")

class Bike(Vehicle):
    def __init__(self, brand, speed, has_gear):
        super().__init__(brand, speed)
        self.has_gear = has_gear

    def bike_info(self):
        if self.has_gear:
            print("Bike with gear")
        else:
            print("Bike without gear")

car = Car("Toyota", 120, 4)
bike = Bike("Honda", 80, True)

car.describe()
car.car_info()

bike.describe()
bike.bike_info()