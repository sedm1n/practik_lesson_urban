class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f" dlina {self.width} shirina {self.height}"

    def __repr__(self):
        return f"({self.width}, {self.height})"


rec = Rectangle(4, 6)
print(str(rec))
print(repr(rec))