# Задание
# Напишите класс-итератор EvenNumbers для перебора чётных чисел
# в определённом числовом диапазоне.
# При создании и инициализации объекта этого класса создаются атрибуты:
# start – начальное значение (если значение не передано, то 0)
# end – конечное значение (если значение не передано, то 1)
# Примечание
# Значение атрибута start всегда меньше значения атрибута end
# В решении задачи не использовать list

class EvenNumber:
    def __init__(self, start=0, end=1):
        self.start, self.end = start, end

    def __iter__(self):
        self.i = self.start-1
        return self

    def __next__(self):
        self.i +=1
        if self.i >= self.end:
            raise StopIteration()
        while self.i % 2:
            self.i+=1
        return self.i






even_range = EvenNumber(start= 10, end= 25)

for i in even_range:
    print(i)