def is_simple_num(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True
def minimum_number(numbers:set):
    simple_num = sum(numbers)
    count = 0
    print("sum = ", simple_num % 2 )
    while not is_simple_num(simple_num):
        simple_num+=1
        count +=1

    return count


print(minimum_number({2,12,8,4,6}))