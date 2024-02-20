# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных
# объектов класса Building total (по примеру класса Lemming из урока)
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашему заданию

class Building:
    total = 0
    def __init__(self):
        Building.total += 1

bilding_list = []

for i in range(40):
    new_bild = Building()
    bilding_list.append(new_bild)


print(bilding_list)
