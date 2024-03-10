class Quadrat:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    @property
    def x1(self):
        if (2*self.b-4*(self.a+self.c)) < 0:
            return None
        return (2*self.a) - self.b - (self.b*2)-4*(self.a+self.c)
    @property
    def x2(self):
        if (2*self.b-4*(self.a+self.c)) < 0:
            return None
        return (2*self.a) - self.b + (self.b*2)-4*(self.a+self.c)
    # @property
    # def view(self):
    #
from math import sqrt


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.coefficients = a, b, c

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, coefficients):
        self.a, self.b, self.c = coefficients
        self._root = self.b ** 2 - 4 * self.a * self.c

    @property
    def x1(self):
        if self._root < 0:
            return None
        return (-self.b - sqrt(self._root)) / (2 * self.a)

    @property
    def x2(self):
        if self._root < 0:
            return None
        return (-self.b + sqrt(self._root)) / (2 * self.a)

    @property
    def view(self):
        return f'{self.a}x^2 {"-+"[self.b >= 0]} {abs(self.b)}x {"-+"[self.c >= 0]} {abs(self.c)}'
poly = Quadrat(1, 2, -3)
print(poly.x1)
print(poly.x2)