class Pet:
    def __init__(self, name):
        self.laps = 4
        self.has_tail = True
        self.name = name
    def inspect(self):
        print(self.__class__.__name__, self.name )
        print("Всего лап {}".format(self.laps))
        print(" Хвост есть ", 'Да' if self.has_tail else 'Нет')

class Cat(Pet):
    # def __init__(self):
            # super().__init__():
    def sound(self):
        print("Мяу!!!")
class Dog(Pet):
    # def __init__(self):
        # super().__init__()
    def sound(self):
        print('Гавв')

my_pet = Pet('Bomba')
# my_pet.sound()
my_pet.inspect()