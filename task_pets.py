class Pets:
    list_ex = []
    def __init__(self, name):
        self.name = name
        Pets.list_ex.append(self)

    @classmethod
    def first_pet(cls):
        return cls.list_ex[0].name if cls.list_ex != [] else None
    @classmethod
    def last_pet(cls):
        return cls.list_ex[-1].name
    @classmethod
    def len_pets(cls):
        return len(cls.list_ex)



# q = Pets('sdfsf')
# w = Pets('lkjlkj')
# w1 = Pets('lkjlkj')
# print(Pets.len_pets())
print(Pets.first_pet())