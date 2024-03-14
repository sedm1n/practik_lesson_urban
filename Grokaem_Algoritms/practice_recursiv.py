def countdown(i):
    print(i)
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
        arr.pop()
        return i + mylen(arr)


def mymax(arr):

    if mylen(arr)==0:
        return 0
    else:
        if
        return arr.pop()
