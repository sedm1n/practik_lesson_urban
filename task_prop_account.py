class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password

    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, value):
        raise AttributeError('Not mutable')

    @property
    def passsword(self):
        return self._password
    @passsword.setter
    def password(self, value):
        self._password = hash(value)



acc = Account('Acc', 'pwd')
print(acc.login)
print(acc.password)

acc.password = 'asfdsf8'
print(acc.password)