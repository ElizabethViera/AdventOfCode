s = '00101000101111010'

def transformS(s):
    a = s
    b = s[::-1].replace('1', 'c').replace('0', 'd').replace('c', '0').replace('d', '1')
    return a + '0' + b
    

while len(s) < 35651584:
    s = transformS(s)
s = s[:35651584]

def generateCheckSum(s):
    cs = ''
    for i in range(0, len(s), 2):
        if s[i] == s[i+1]:
            cs += '1'
        else:
            cs += '0'
    if len(cs)%2 == 0:
        return generateCheckSum(cs)
    else:
        return cs

print(generateCheckSum(s))
