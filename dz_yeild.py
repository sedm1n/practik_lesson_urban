# Напишите функцию-генератор all_variants, к
# оторая будет возвращать все подпоследовательности переданной строки.
# В функцию передаётся только сама строка.
# Примечание
# Используйте оператор yield


def all_variants(s):
    length = len(s)
    for i in range(1, length + 1):
        for j in range(length - i + 1):
            yield s[j:j + i]


var = all_variants('abc')
for val in var:
    print(val)
