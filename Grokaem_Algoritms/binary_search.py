def binary_search(array, item):
    low = 0
    it = 0
    high = len(array)-1
    while low <= high:
        it += 1
        mid = (low+high)//2
        guess = array[mid]
        if guess == item:
            return f"index item {mid}, value item = {array[mid]} it = {it}"
        elif guess > item:
            high = mid-1
        else:
            low = mid + 1


my_list=[]
{my_list.append(i) for i in range(1, 16)}

print(binary_search(my_list, 7))