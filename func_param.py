def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(34,'list', False)
print_params(b = 'Clr',c = True, a = 234)
print_params(b = 25)
print_params(c = [1,2,3])
print_params()

value_list = ['1' ,4 , True]
value_dict = {'a':54, 'b': 'sdfsdf', 'c': False}
print_params(*value_list)
print_params(**value_dict)