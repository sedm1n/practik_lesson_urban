voted = {}
def check_voter(name):
    if voted.get(name):
        print('Пошел нахер!')
    else:
        voted[name]=True
        print(f"Good man {name}")

check_voter('ivan')
check_voter('mana')
check_voter('ivan')