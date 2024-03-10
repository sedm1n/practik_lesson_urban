class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @classmethod
    def square(cls, side):
        return cls(length=side, width=side)


rec = Rectangle(3, 5)
print(rec.width)
print(rec.length)
rec2 = Rectangle.square(4)
print(rec2.length)