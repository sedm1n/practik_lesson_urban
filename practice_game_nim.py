from nim_engine import put_stones, is_game_over, take_from_bunch, get_bunches
from termcolor import cprint

put_stones()
user_number = 1

while True:
    print("Текущая позиция")
    print(get_bunches())
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint("Ход игрока {}".format(user_number),color=user_color)
    pos = input("Откуда берем?")
    qua = input("Сколько берем?")
    step_sucess = take_from_bunch(quantity=int(qua), position=int(pos))
    if step_sucess:
        user_number = 2 if user_number == 1 else user_number = 1
    else:
        cprint("Невозможный ход",color='red')
    user_number = 2 if user_number == 1 else 1
print("Выиграл игрок № ",user_number)