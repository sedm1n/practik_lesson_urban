class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._fullname = name+surname

    @property
    def fullname(self):
        return self.name +" "+self.surname
    @fullname.setter
    def fullname(self, value):
        self.name, self.surname = value.split()

b = Person('Name', 'SUrname')
print(b.fullname)
b.name = 'sdfsdf'
b.fullname = 'Ivan Petrov'
print(b.fullname)
b.name = 'sidor'
print(b.fullname)