class Toyota:
    def __init__(self):
        self.color = "Red"
        self.price = "1 000 000"
        self.max_velocity = '200'
        self.engine_rpm = '0'
        self.current_velocity = "0 km/h"
        self.engine_rpm

    def start(self):
        print("Motor is start")
        self.engine_rpm = 900

    def go(self):
        print("поехали")
        self.engine_rpm = 2000
        self.current_velocity = "20 km/h"

my_car = Toyota()
print('Color', my_car.color)
print('Price',my_car.price)
print('Max velocity = ', my_car.max_velocity)
print('Rpm', my_car.engine_rpm)
print("Current velocity = ", my_car.current_velocity)

my_car.start()
print('Rpm = ', my_car.engine_rpm)
my_car.go()
print('Rpm = ', my_car.engine_rpm)
print("Current velocity = ", my_car.current_velocity)
my_car.color = 'Black'
print(my_car.color)