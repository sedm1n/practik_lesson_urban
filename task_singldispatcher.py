from functools import singledispatchmethod
from datetime import date

class BrithInfo:
    @singledispatchmethod
    def __init__(self, brith_date):
        self.age = 0
        self.brith_date = 0
        self._age = None


    @__init__.register(str)
    def _from_iso(self, brith_date):
        self.brith_date = date.fromisoformat(brith_date)

    @__init__.register(list)
    def _from_list(self, brith_date):
        self.brith_date = date(*brith_date)

    @property
    def age(self):
        return date.today().year - self.brith_date.year
        pass


b = BrithInfo('2014-12-01')
a = BrithInfo([2011, 1, 2])
print(b.brith_date)
print(a.brith_date)
print(a.age)
