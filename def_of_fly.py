
def get_multiplier(n):
    if n == 2:
        def multiplier(x):
            return x*2
    elif n == 3:
        def multiplier(x):
            return x*3
    else:
        raise Exception("Error")
    return multiplier

my_numbers = [1,3,4,5,6,7,8,9]
by_2 = get_multiplier(2)
by_3 = get_multiplier(3)

result = map(by_2, my_numbers)
print(list(result))
res2 = map(lambda x: x*5, my_numbers)
print(list(res2))
myf = lambda x: x+50
print(myf(14))