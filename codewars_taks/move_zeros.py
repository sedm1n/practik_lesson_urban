def move_zeros(lst:list):
    # cnt = lst.count(0)
    # while lst.count(0):
    #     lst.pop(lst.index(0))

    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(0)
    return lst

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))