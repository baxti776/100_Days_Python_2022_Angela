class Car:
    def __init__(self, make, model, year):
        """Initialize attributes of car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Displaying car descriptive name"""
        print(f"Car model : {self.model.title()}")
        print(f"Manufacture Date: {self.year}")
        print(f"Car name : {self.make.title()}")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 65

    def describe_battery(self):
        """Printing statement describing battert size """
        print(f"Your car battery {self.battery_size} kWh battery.")


name = Car('tesla', 'tesla X78', 2021)
print(name.get_descriptive_name())

name.describe_battery()
