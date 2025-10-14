from car import Car

my_new_car = Car('chevrolet', 'mustang cobra', 2020)
print(my_new_car.get_describe_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()