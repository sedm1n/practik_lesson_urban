# Цель задания:
# Освоить механизмы создания и потоков в Python.
# Практически применить знания, создав класс наследника от Thread
# и запустив его в потоке.
#
# Инструкции:
# Напишите программу с использованием механизмов многопоточности,
# которая создает два потока-рыцаря.
#
# Каждый рыцарь должен иметь имя (name) и умение(skill). Умение рыцаря определяет,
# сколько времени потребуется рыцарю, чтобы выполнить свою защитную миссию для королевства.
# Враги будут нападать в количестве 100 человек. Каждый день рыцарь может ослабить
# вражеское войско на skill-человек.
# Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
# Чем выше умение, тем быстрее рыцарь защитит королевство.
#
# Пример:
# knight1 = Knight("Sir Lancelot", 10) # Низкий уровень умения
# knight2 = Knight("Sir Galahad", 20) # Высокий уровень умения
# knight1.start()
# knight2.start()
# knight1.join()
# knight2.join()
import time
from threading import Thread
class Knights(Thread):
    
    def __init__(self, name, skill, *args,**kwargs):
        super(Knights,self).__init__(*args,**kwargs)
        self.ENEMIES = 100

        self.name = name
        self.skill = skill
        self.days = 0
        print(f"{self.name} на нас напали!")

    def run(self):

        while self.ENEMIES > 0:
            self.ENEMIES -= self.skill
            print(f'{self.name} сражаемся, осталось {self.ENEMIES} воинов')
            time.sleep(1)
            self.days +=1
        print(f"{self.name} Всего дней прошло {self.days}")

knight1 = Knights('Vasya',10)
knight2 = Knights('Petya',20)

knight1.start()
knight2.start()
print("Бой начался")
knight1.join()
knight2.join()
