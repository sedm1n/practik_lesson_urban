def find_smallest(arr):
    smallest = arr[0] #для хранения наименьшего значения
    smallest_index = 0 # храним индекс наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionsort(arr: list):
    newarr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr


print(selectionsort([3,5,7,19,1]))