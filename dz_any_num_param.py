def test(a,b,*args,**kwargs):
    print(a,b,args,kwargs)

test(1,2,3,3,24,5,'dfsfsdf',True,name='vasya',age=34)


def factorial(n:int):
    if n == 1:
        return 1
    fact_n = n * factorial(n-1)
    return fact_n

print(factorial(5))