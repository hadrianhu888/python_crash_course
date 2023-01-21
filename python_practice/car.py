class Car: 
    def __init__(self,make,model,year): 
        self.make = make
        self.year = year
        self.model = model
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year}, {self.make}, {self.year}"
        return long_name.title()
    
    def read_odometer(self): 
        print(f"Odometer reading: {self.odometer_reading} miles on it.")
    
    def update_odometer_reading(self,mileage):
        if mileage > self.odometer_reading: 
            self.odometer_reading = mileage 
        else: 
            print(f"You cannot roll back an odometer reading!")
    
    def increment_odometer_reading (self,miles):
        self.odometer_reading += miles
        print(f"The car has traveled : {self.odometer_reading} miles.")

class Battery:     
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a battery size of {self.battery_size}-kWh.")
    def get_range (self): 
        if self.battery_size == 75: 
            range = 260
        elif self.battery_size == 100: 
            range = 315
        text = f"The car with {self.battery_size} has a range of {range} km."
        print(text)
    def upgrade_battery(self):
        self.battery_size = 100
                        
class Electric_Car (Car): 
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery= Battery()
    def describe_battery(self,battery):
        self.battery_size = battery
        print(f"This car has a battery size of {self.battery_size}-kWh battery")    
    def fill_gas_tank(self): 
        print(f"Electric cars do not need to have to fill a gas tank.")
        
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer_reading(32)
my_new_car.read_odometer()
my_new_car.increment_odometer_reading(12)

myTesla = Electric_Car('tesla', 'model s', '2019')
print(myTesla.get_descriptive_name())
myTesla.fill_gas_tank()
myTesla.describe_battery(75)
myTesla.battery.describe_battery()
myTesla.battery.get_range()

myTesla = Electric_Car('tesla', 'model s', '2019')
print(myTesla.get_descriptive_name())
myTesla.fill_gas_tank()
myTesla.describe_battery(75)
myTesla.battery.describe_battery()
myTesla.battery.get_range()
myTesla.battery.upgrade_battery()
myTesla.battery.get_range()



