bigNumber = 29000000

def getFirstPrimeFactor(n: int)  -> int:
    for i in range(2,n+1):
        if i*i > n:
            return n
        if n//i == n/i:
            return i
    raise(ValueError(n))

def getHighestP(n: int,p:int) -> int:
    total = 0
    while n%p == 0:
        total += 1
        n = n//p
    return total

from functools import cache

@cache
def getSumOfFactors(n: int) -> int:
    if n == 1:
        return 1
    p = getFirstPrimeFactor(n)
    highestP = getHighestP(n, p)
    x = getSumOfFactors(n//(pow(p,highestP)))
    return x * sum(pow(p,i) for i in range(0, highestP + 1) if n//(pow(p, highestP)) < 50)


for i in range(1, bigNumber):
    candidate = getSumOfFactors(i)
    if candidate*11 >= bigNumber:
        print(i)
        break