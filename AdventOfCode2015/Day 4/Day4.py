import hashlib

result = hashlib.md5(b'abcdef609043')
print(result.hexdigest()[:5])
number = 1
while(True):
    number += 1
    candidate = 'yzbqklnj' + str(number)
    result = hashlib.md5(candidate.encode('utf-8')).hexdigest()[:6]
    if result == '000000':
        print(number)
        break
