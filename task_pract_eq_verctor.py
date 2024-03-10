class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            print('sdfsdf')
            return self.x == other[0] and self.y == other[1]
        return NotImplemented
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y


v = Vector(1,4)
c = Vector(1, 4)
print(v == (1, 4))