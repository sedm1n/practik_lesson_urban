class Parent:
    class_var_1 = 12
    _class_var_2 = 23
    __class_var_3 = 34
    def __init__(self):
        self.var1 = 45
        self._var2 = 345
        self.__var3 = 452
    def paren_method(self):
        print(self.class_var_1)
        print(self._class_var_2)
        print(self.__class_var_3)
        print(self.var1)
        print(self._var2)
        print(self.__var3)

class Child(Parent):

    def child_method(self):
        print(self.class_var_1)
        print(self._class_var_2)
        # print(self.__class_var_3)
        print(self.var1)
        print(self._var2)
        # print(self.__var3)

obj = Child()
obj.child_method()
obj.paren_method()