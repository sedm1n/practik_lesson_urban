def rowWeights(array):
    sum1, sum2 = 0, 0
    for i in range(len(array)):
        if i % 2:
            sum1 += array[i]
        else:
            sum2 += array[i]
    return sum2, sum1

print(rowWeights([13, 27, 49]))