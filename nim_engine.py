from random import randint
MAX_BUNCHES = 5
MAX_BUNCHES_SIZE = 20
_holder = {}
def settings():
    pass
def put_stones():
    global _holder
    _holder = {}
    for i in range(1,MAX_BUNCHES+1):
        _holder[i] = randint(1,MAX_BUNCHES_SIZE)
    pass
def take_from_bunch(position, quantity):
    if position in _holder:
        _holder[position] -= quantity
        return True
    else:
        return False
def get_bunches():
    res = []
    for key in sorted(_holder.keys()):
        res.append(_holder[key])
    return res
    pass
def is_game_over():
    return sum(_holder) == 0


