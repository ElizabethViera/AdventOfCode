inputHash = 'ffykfhsq'

import hashlib

count = 0

result = [-1, -1, -1, -1, -1, -1, -1, -1]
i = 0
while count < 8:
 i += 1
 testHash = inputHash + str(i)
 hashedTest = hashlib.md5(testHash.encode()).hexdigest()[:7]
 if (hashedTest).startswith('00000'):
    if hashedTest[5] in '01234567':
        index = int(hashedTest[5])
        character = hashedTest[6]
        if result[index] == -1:
            result[index] = character
            count += 1
print(result)