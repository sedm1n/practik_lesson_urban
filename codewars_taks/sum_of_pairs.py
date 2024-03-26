def sum_pairs(ints, s):
    # new_arr = [[x, y] for x,num in enumerate(ints) for y in range(x + 1, len(ints)) if num + ints[y] == s]
    # if not new_arr: return None
    # new_arr.sort(key=lambda x: x[1])
    # return [ints[new_arr[0][0]], ints[new_arr[0][1]]]

    # num_index_map = {}
    # for x, num in enumerate(ints):
    #     target = s - num
    #     if target in num_index_map:
    #         y = num_index_map[target]
    #         return [num, ints[y]]
    #     num_index_map[num] = x
    # return None
    cache = set()
    for i in ints:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)


print(sum_pairs([10, 5, 2, 3, 7, 5], 10))