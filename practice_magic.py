class Vector:
    def __init__(self, *args):
        self.__val = None
        self.values = args

    @property
    def values(self):
        if self.__val == None:
            return "Пустой вектор"
        else:
            return self.__val

    @values.setter
    def values(self, val):
        if all(isinstance(v, int) for v in val ):
            self.__val = val
        else:
            print("Error value is not int", type(val))


b = Vector(23,34,34,54,2.34)
print(b.values)
