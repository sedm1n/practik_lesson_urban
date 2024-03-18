class Family:
    def __init__(self):
        self.mom = 'Mama'
        self.dad = 'Papa'
        self.son = 'Son'
    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i +=1
        if self.i == 1:
            return f'{self.dad}'
        if self.i == 2:
            return f'{self.mom}'
        if self.i == 3:
            return f'{self.son}'
        if self.i == 4:
            return f'Funny family'
        raise StopIteration("vse capez")


def fibonaci(n):
    result =[]
    a, b = 0,1
    for _ in range(n):
        result.append(a)
        a, b = b, a+b
    return result


class Fibonacci():
    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self
    def __next__(self):
        self.i +=1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a+self.b
        return self.a

fib_iterator = Fibonacci(10)
print(fib_iterator)

for value in fib_iterator:
    print(value)