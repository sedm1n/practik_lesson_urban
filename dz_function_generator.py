#
# Задание:
# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические ф
# ункции (например, деление, умножение) в зависимости от переданных аргументов.

def function_fabric(n):
    match n:
        case 'sum':
            def my_add(x,y):
                return x+y
            return my_add
        case 'mul':
            def my_mul(x,y):
                return x*y
            return my_mul
        case 'dev':
            def my_dev(x,y):
                return x/y
            return my_dev


my_num = [1,23,4,6,7,8,]

fun1 = function_fabric('mul')
print(fun1(3,5))
fun1 = function_fabric('sum')
print(fun1(3,5))
fun1 = function_fabric('dev')
print(fun1(3,5))


# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции
# и написать такую же функцию с использованием def. Например, возведение числа в квадрат

my_lambda = lambda x: x**2
print(my_lambda(5))
def my_def(x):
    return x**2
print(my_def(5))

# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются в __init__
# и методом __call__, который возвращает площадь прямоугольника, то есть a*b.

class Rect:
    def __init__(self, a):
        self.a = a
    def __call__(self, b):
        return self.a * b

my_obj = Rect(4)
print(my_obj(3))




# Пример создания вызываемого объекта
# class Repeater:
#    def __init__(self, value):
#        self.value = value
#    def __call__(self, n):
#        return [self.value] * n
#
# repeat_five = Repeater(5)
# print(repeat_five(3)) # Выводит [5, 5, 5]