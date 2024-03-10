class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gender = gender
        self._gender = 'male'
    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, gender):
        if gender in ('male', 'female'):
            self._gender = gender
        else:
            print('Я не знаю что вы имели ввиду')
            self._gender = 'male'
    def __str__(self):
        if self.gender == 'male':
            return  'Grzdanin Male'
        elif self.gender == 'female':
            return 'Grazdanka Female'



b = Person('Ivan', 'Petrovich')
print(b.gender)
b.gender = 'female'
print(b.gender)
a = Person('Maria', 'Senra', 'female')
c = Person('swrwer', 'hwrwer', True)
print(b)
print(a)
