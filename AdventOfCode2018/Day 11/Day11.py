SERIAL_NUMBER = 11 # Fake serial number

powers = dict()

for x in range(1,301):
    for y in range(1,301):
        rack_id = x+10
        power_level = rack_id*y
        power_level += SERIAL_NUMBER
        power_level *= rack_id
        if power_level >= 100:
            power_level //= 100
            power_level %= 10
        else:
            power_level = 0
        power_level -= 5
        powers[(x,y)] = power_level

def getNbyN(x,y,n):
    result = []
    for i in range(n):
        for j in range(n):
            result.append((x+i, y+j))
    return result

best_result = 0
coords = (-1,-1)

for power in powers:
    for n in range(100):
        three_by_three = getNbyN(power[0], power[1], n)
        square = [powers[neighbor] for neighbor in three_by_three if neighbor in powers]
        if len(square) != len(three_by_three):
            break
        result = sum(square)
        if result > best_result:
            print("new best result!", power, n)
            best_result = result
            coords = (power[0], power[1], n)
print(coords)