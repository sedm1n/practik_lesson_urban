def nth_smallest(arr, pos):
    arr =  sorted(arr)
    print(arr)
    return arr[pos-1]

print(nth_smallest([15,20,7,10,4,3],3))