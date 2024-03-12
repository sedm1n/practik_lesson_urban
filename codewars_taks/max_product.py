def max_product(lst, n_largest_elements):
    result = 1
    lst = sorted(lst)
    for i in lst[-n_largest_elements:]:
        result *= i

    return result

rom functools import reduce
from operator import mul
from heapq import nlargest

def maxProduct (lst, n):
    return reduce(mul, nlargest(n, lst))

print(max_product([8,6,4,6], 3))