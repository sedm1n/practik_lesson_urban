# Импортируйте модуль warnings.
# Реализуйте функцию для расчёта деления,
# которая будет генерировать предупреждение,
# если делитель близок к нулю (например, меньше 0.01),
# предупреждая об опасности деления на ноль.
# Сгенерируйте UserWarning в этом случае.
# Используйте разные фильтры для управления поведением программы
# при появлении такого предупреждения: always, ignore, error
import warnings
warnings.filterwarnings('ignore')
def devide(arr):

    for i in arr:
        if i > 1:
            print(8/i)
        else:
            warnings.warn("Значение делителя близко к 0 ")
        print(i)



devide((1,2,3,4,0.9))