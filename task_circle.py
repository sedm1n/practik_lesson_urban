class Circle:
    def __init__(self, radius):
        self.radius = radius
    @classmethod
    def from_diametr(cls, diametr):
        return cls(diametr/2)

cir = Circle(5)
print(cir.radius)
cir2 = Circle.from_diametr(3)
print(cir2.radius)