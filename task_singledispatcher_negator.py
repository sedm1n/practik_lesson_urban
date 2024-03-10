from functools import singledispatchmethod

class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(value):
        return ValueError('Eroor ')
    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def from_intfloatneg(value):
        return -value
    @neg.register(bool)
    @staticmethod
    def from_bool(value):
        return not value


print(Negator.neg(1))
print(Negator.neg(-3))
print(Negator.neg(True))1