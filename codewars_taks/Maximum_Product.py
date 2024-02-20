def adjacent_element_product(array):
    new_array = []
    return max([array[i]*array[i+1] for i in range(len(array)-1)])
''.
print(adjacent_element_product([5, 1, 2, 3, 1, 4]))