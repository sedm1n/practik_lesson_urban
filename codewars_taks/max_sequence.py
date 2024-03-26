# def maxSequence(arr):
#     max,curr=0,0
#     for x in arr:
#         curr+=x
#         if curr<0:curr=0
#         if curr>max: max=curr
#     return max
def max_sequence(arr):
    lowest = ans = total = 0
    for i in arr:
        total += i
        lowest = min(lowest, total)
        ans = max(ans, total - lowest)
    return ans



print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))