# Создайте родительский(базовый) класс Vehicle,
# который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000
# и функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите
# свойство price и vehicle_type, а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию
# print vehicle_type, price
class Vehicle:
    def __init__(self):
        self.venhicle_type = "none"

class Car:
    def __init__(self):
        self.price = 1000000
        self.horse = 0

    def horse_powers(self):
        return self.horse


class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 400000
        self.venhicle_type = "sfdsdf"

    def horse_powers(self):
        return self.horse
def main():
    nissan_ca = Nissan()
    print("Type {}, Price {}, Power {}".format(
        nissan_ca.venhicle_type, nissan_ca.price, nissan_ca.horse_powers()))

if __name__ == '__main__':
    main()