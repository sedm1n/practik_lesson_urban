def stutter1(text):
    return text[:2] + '-' + text


def stutter_factory(n):
    def stutter(text):
        return (text[:2] + '-') * n + text

    return stutter


animal = 'animal'

stutter_2 = stutter_factory(n=2)
# print(stutter_2(animal))


# Создаем список функций

stut = [stutter_factory(n=n) for n in range(1,4)]
print(stut)
for func in stut:
    print(func(animal))

animal2 = ['bobre', 'dog', 'bird']

mes = [func(anim) for anim in animal2 for func in stut ]
print(mes)