def find_in_array(seq, predicate):
    flag =0
    for i, element in enumerate(seq):
        if predicate(element,i):
            return i
    return -1

true_if_even = lambda v, i: v % 2 == 0

print(find_in_array([], true_if_even))