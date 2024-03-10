class QuadratikPoly:
    def __init__(self, a , b, c):
        self.a = a
        self.b = b
        self.c = c
    @classmethod
    def from_iterable(cls, *value):
        return cls(value)
    @classmethod
    def from_str(cls, str_val:str):
        a,b,c = str_val.split()
        return cls(a,b,c)


q = QuadratikPoly(2,3,6)
print(q.a)
q2 = QuadratikPoly.from_str('6 5 7')
print(q2.a)