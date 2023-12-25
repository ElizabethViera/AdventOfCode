import hashlib

def get2016Hashed(s: str) -> str:
    result = s
    for i in range(2017):
        result = hashlib.md5(result.encode())
        result = str(result.hexdigest())
    return result

salt = 'abc'
i = 0
bigString = dict()
for i in range(30000):
    result = get2016Hashed(salt+str(i))
    bigString[i] = result

    
def search1000(s, k):
    for i in range(1,1001):
        if s in bigString[k+i]:
            return True
    return False

def search1(k):
    for e,c in enumerate(bigString[k]):
        if e > 1 and c == bigString[k][e-1] and c == bigString[k][e-2]:
            stringToFind = c*5
            return search1000(stringToFind, k)
    return False
                
total = 0
for k in bigString:
    if search1(k):
        total += 1
        if total == 64:
            print(k)
            raise(ValueError)


