# Напишите 2 функции:
# Функция которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом
# и "Составное" в противном случае.
# Пример:
# result = sum_three(2, 3, 6)
# print(result)

def is_prime(func):
    def sur(*args):
        num = func(*args)
        for i in range(2, num-1):
            if not num % i:
                return f"Составное \n{num}"
            return f"Простое \n {num}"
    return sur
@is_prime
def sum_three(one, two, three):
    sum1 = one+two+three
    return sum1

result = sum_three(1,1,9)
print(result)