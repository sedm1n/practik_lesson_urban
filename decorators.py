import time
def time_track(func):
    def surrogate( *args, **kwargs):
        start= time.time()
        result = func(*args, **kwargs)
        sen = time.time()
        elaps = round(sen-start,4)
        print(f"Function work is {elaps}")
        return result
    return surrogate
@time_track
def digits(*args):
    total = 1
    for num in args:
        total+=num**5000
    return total


result = digits(3431,1341,5415)
