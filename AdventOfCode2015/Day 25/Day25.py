row = ((3010)**2 + 3010 + 2)//2
col = ((3019)*(3020))//2
# row, col = 4531556 4558690, difference = 27134

total = 4558690
for i in range(3009):
    total += (3019+i)

print(total)

total = 10
for i in range(2):
    total += 4+i
print(total)

# we think this is the number: 18168397

currentNumber = 20151125
for i in range(18168396):
    m = currentNumber * 252533
    r2 = m%33554393
    currentNumber = r2

print(currentNumber)