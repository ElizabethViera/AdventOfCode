x0 = 135
x1 = 155
y0 = -102
y1 = -78

# x0 = 20
# x1 = 30
# y0 = -10
# y1 = -5


def getHighestPoint(vy):
    return sum(range(vy+1))


def doesHitTarget(vx, vy):
    solution_positions = []
    x_pos = 0
    y_pos = 0
    while vx > 0:
        y_pos += vy
        x_pos += vx
        if x_pos in range(x0, x1+1):
            if y_pos in range(y0, y1+1):
                return True
        vx -= 1
        vy -= 1
    while y_pos >= y0:
        y_pos += vy
        if x_pos in range(x0, x1+1):
            if y_pos in range(y0, y1+1):
                return True
        vy -= 1
    return False


solutions = 0
for x in range(156):
    for y in range(-103, 600):
        if doesHitTarget(x, y):
            solutions += 1
print(solutions)
