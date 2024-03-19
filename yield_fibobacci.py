
def fibonachi(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b, a+b


def qua(*args):
    data = list(args)
    while data:
        next_ = data.pop(0)
        new_value= (yield next_)
        if new_value is not None:
            data.append(new_value)


q = qua('vasya', 'masha', 'petya', 'irina')

for name in q:
    print(f"Inviting {name}")
    if name == 'irina':
        print("A kto poslesniy ")
        name = q.send('Margo')
        print(f"Ivite {name}")