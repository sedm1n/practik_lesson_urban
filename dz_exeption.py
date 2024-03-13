def string_to_int(s): # добавить обработку ValueError
   try:
        return int(s)
   except ValueError:
       print(f"Переданное знаечение {s} не может быть преобразовано в Int")

def read_file(filename): # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
           return file.read()
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")

def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Делить на ноль нельзя!")
    except TypeError:
        print("НЕ верный тип ")
def access_list_element(lst, index): # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        print(f"index out of range {index}")
    except TypeError:
        print(f"Ошибка типа")

string_to_int('d')
read_file('dfsfs')
divide_numbers(1,0)
divide_numbers(1,'df')
access_list_element([1,4], 14)
