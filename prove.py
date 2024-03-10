class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):

    return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

        @name.deleter
        def name(self):
        # делитер
            del self._name