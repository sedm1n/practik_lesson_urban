def countdown(i):

    if i <= 0:
        return
    countdown(i - 1)


def factorial(var):
    if var == 1:
        return 1
    else:
        return var * factorial(var - 1)


def mysum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop() + mysum(arr)


def mylen(arr: list):
    i = 0
    if arr == []:
        return 0
    else:
        i += 1
        # arr.pop()
        return i + mylen(arr[1:])


def mymax(arr):

    if not arr:
        return 0
    max_res = mymax(arr[1:])

    if max_res == 0:
        return arr[0]
    else:
        return arr[0] if arr[0] > max_res else max_res

        return

    mymax(arr)


def calclulation_fibonachi(arr):

    if not arr:
        return None
    
    arr[0] arr