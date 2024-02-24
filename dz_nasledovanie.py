# Создайте родительский(базовый) класс Car, который
# имеет свойство price = 1000000 и функцию def horse_powers,
# которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car - класс Nissan и
# переопределите свойство price, а также переопределите функцию
# horse_powers
# Дополнительно создайте класс Kia, который также будет наследником
# класса Car и переопределите также свойство price, а также
# переопределите функцию horse_powers
# Получившийся код прикрепите к заданию текстом

class Car:
    price = 1000000
    hors_power = 999

    def horse_powers(self):
        return self.hors_power

class Nissan(Car):
    price = 500000
    hors_power = 123
    def horse_powers(self):
        return self.hors_power
class Kia(Car):
    price = 600000
    hors_power = 234
    def horse_powers(self):
        return self.hors_power


my_car = Kia()
car = Car()

print("Модщность {} стоимость {} ".format(
    my_car.price, my_car.horse_powers()))

print(car.horse_powers())