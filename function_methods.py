def get_russian_name():
    return ['kola', "vasya", 'petya']

def get_british_name():
    return ['John', 'silver']

def print_name(message, getname):
    print(message, getname())


list_function = [get_british_name, get_russian_name]



def  adder(*args):
    return sum(args)

def multiplw(*args):
    res = 1
    for arg in args:
        res *=arg
    return res

def process_numbers(numbers, handler):
    result = handler(*numbers)
    print('result ', result)


def mul_by_2(x):
    return x*2

def mul_by_3(x):
    return x*3

def ood(x):
    return x%2

my_nums = [1,2,3,4,5,6,7,8]

result= filter(ood, my_nums)
result= map(mul_by_2, filter(ood, my_nums))
result= sum(map(mul_by_2, filter(ood, my_nums)))
print(result)
