def maxTripSum(array):
    array = sorted(list(set(array)))
    return sum(array[-3:])




print(maxTripSum([3,2,6,8,2,3]))
# print()
