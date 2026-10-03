class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    # encapsulation

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"


# inheritance


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
# print(my_car.fuel_type())

my_tesla = ElectricCar("Tesla", "Model S", "87kWh")
# print(my_tesla.brand)
# print(my_tesla.get_brand())
# print(my_tesla.full_name())
# print(my_tesla.fuel_type())

print(Car.general_description())

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))


class Battery:
    def battery_info(self):
        return 'this is battery'


class Engine:
    def engine_info(self):
        return 'this is engine'


class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("tesla",'model s')
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())