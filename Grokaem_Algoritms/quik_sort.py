# Алгоритм быстрой сортировки



def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  #выбираем опорный эллемент
        less = [i for i in array[1:] if i <= pivot]         #создаем левый подмассим чисел меньше опорного
        greater = [i for i in array[1:] if i > pivot]       #правый подмассив
        return quick_sort(less)+[pivot]+quick_sort(greater)   # рекурсивный вызов

print(quick_sort([1,13,5,61,7,8,12,]))
# если массив состоит 11з элементов [2, 3, 7, 8, 1 0] , сначала каждый эле­
# мент умножается на 2, затем каждый элемент умножается на 3, затем
# на 7 и т. д.

