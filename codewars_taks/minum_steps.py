def minimum_steps(numbers, value):
    numbers = sorted(numbers)
    k = 0
    result = 0
    for i in numbers:
        result += i
        if result >= value:
            return k
        k += 1






print(minimum_steps([19,98,69,28,75,45,17,98,67], 464))