from collections import defaultdict
from functools import reduce

my_list = [1,4,6,12,5,14,53,33,11]
my_list2 = [2,3,6,22,5,14,3,17,111]
my_list.sort(key=lambda x: x if x % 2 else 1)

two_list = list(zip(my_list,my_list2 ))
# print(two_list)
two_list.sort()
# print(two_list)
two_list.sort(key=lambda x: x[1])
# print(two_list)

foods = [
    ['sugar',12],
    ['wine', 1],
    ['wine', 1],
    ['beer', 5],
    ['butter', 15],
    ['butter', 15],
    ['rice', 99],
    ['rice', 99],
]

count = defaultdict(int)

for name, quantyti in foods:
    count[name] += quantyti

# print(foods)
# print(count)
b = map(lambda x: x*2, my_list)
m = reduce(lambda x, y: x+y, my_list)
print(my_list)
print(m)
for i in b:
    print(i)

strings = ["Hello", "world", "how", "are", "you"]

# Используем reduce с initializer
result = reduce(lambda x, y: x + " " + y, strings, "Start:")
result += " :End"

print(result)