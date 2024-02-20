from class3 import Verification
from tkinter import Tk, Button


class V2(Verification):
    def __init__(self, login, password):
        super().__init__(login, password)
        self.__save()
    def show(self):
        return (self.login, self.password)
    def __save(self):
        with open('users') as r:
            for i in r:
                if f"{self.login} : {self.password}\n" == i:
                    raise ValueError("Такой пароль уже есть")
        super().save()

x = V2("vaayn",'sflsdjfldj')
