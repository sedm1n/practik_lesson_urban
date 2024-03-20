import random
from collections import defaultdict
from random import randint
from threading import Thread

FISH = (None, 'Plotva', 'Shuka', 'lesh', 'okun')


def fishing(name, worms):
    count = defaultdict(int)
    for worm in range(worms):
        print(f"Чел забросил {name}, worm # {worm}, ждем", flush=True)
        _ = 3 ** (randint(50, 70) * 10000)
        fish = random.choice(FISH)
        if fish is None:
            print(f"{name}: Тьфу сожрали червяка", flush=True)
        else:
            print(f"{name}, Ага у меня {fish} ", flush=True)
            count[fish] += 1

    print(f"Итого рыбак {name} vpimal", flush=True)
    for fish, i in count.items():
        print(f"{fish}: {i}", flush=True)


thread = Thread(target=fishing, kwargs=dict(name='Vasya', worms=10))

thread.start()

fishing('Kolya', 10)

thread.join()
