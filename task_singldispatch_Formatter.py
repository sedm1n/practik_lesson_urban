from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(value):
        raise TypeError("sfsddfsdf")

    @format.register(int)
    @staticmethod
    def _for_int(value):
        return f"This is integer number {value}"

    @format.register(float)
    @staticmethod
    def _for_float(value):
        return f'This is float number {value}'

    @format.register(str)
    @staticmethod
    def _for_str(value):
        return f"This is str  {value}"

    @format.register(list)
    @staticmethod
    def _for_list(value: list):
        return f"This is list  {value}"


print(Formatter.format([2]))
