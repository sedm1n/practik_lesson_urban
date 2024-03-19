# Напишите функцию-генератор all_variants, к
# оторая будет возвращать все подпоследовательности переданной строки.
# В функцию передаётся только сама строка.
# Примечание
# Используйте оператор yield


def get_variants(text: str):

    for i in range(len(text)):
        for y in range(i + 1, len(text) + 1):

            yield text[i:y]


var = get_variants('abc')

for val in var:
    print(val)
