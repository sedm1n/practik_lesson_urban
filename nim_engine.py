from random import randint

_holder = []
def put_stones():
    global _holder
    _holder = []
    for i in range(5):
        _holder.append(randint(1,20))
    pass
def take_from_bunch(position, quantity):
    if 1 <= position < len(_holder):
        _holder[position] -= quantity
def get_bunches():
    return _holder
    pass
def is_game_over():
    return sum(_holder) == 0


