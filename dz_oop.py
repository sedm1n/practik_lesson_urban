class House:
    def __init__(self):
        self.numberOfFloors = 10

my_house = House()

for i in range(my_house.numberOfFloors):
    print("Текущий этаж равен: ", i+1)