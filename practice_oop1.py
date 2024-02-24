from random import randint

from termcolor import cprint


class Men():
    def __init__(self, name):
        self.name = name
        self.fulnes = 30
        self.house = None

    def eat(self):
        if self.house.food >= 10:
            print("{} поел ".format(self.name))
            self.fulnes += 21
            self.house.food -= 11
        else:
            print("Нет еды")

    def __str__(self):
        return "Имя {} сытость {} запас еды {} запас денег {}".format(self.name,
                                                                      self.fulnes, self.house.food,
                                                                      self.house.money)

    def work(self):
        print("{} Ходил на работу ".format(self.name))
        self.house.money += 10
        self.fulnes -= 10

    def play_dota(self):
        print("{} Играл в доту".format(self.name))
        self.fulnes -= 10

    def go_into_house(self, house):
        self.house = house
        cprint("У {} Въехал в дом {} ".format(self.name, self.house), color='blue')
        self.fulnes -= 11

    def act(self):
        dice = randint(1, 6)
        if self.fulnes < 10:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money <= 20:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_dota()

    def shopping(self):
        if self.house.money >= 10:
            self.house.food += 11
            self.house.money -= 17
            self.fulnes -= 11
            print("{} Сходил в магазин ".format(self.name))
        else:
            cprint("У {} Деньги закончились ".format(self.name), color='blue')


class House:
    def __init__(self):
        self.food = 60
        self.money = 50

    def __str__(self):
        return "запас еды {} запас денег {}".format(
            self.food, self.money)


citizens = [
    Men('Bevis'),
    Men('Buthead'),
    Men('Keni'),
    Men('Martin'),
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_into_house(house=my_sweet_home)

for day in range(1, 345):
    print("************* Day {} *************".format(day))
    for citizen in citizens:
        citizen.act()
    print("******************* End day ********************************")
    for citizen in citizens:
        print(citizen)
