import math
fileContents = open("Day 12/input")
arr = fileContents.read().split('\n')


def rotate_waypoint(up, left, degrees, ship_up, ship_left):
    left_diff = way_point_left - ship_left
    up_diff = way_point_up - ship_up
    degrees %= 360
    if degrees == 90:
        return ship_up + left_diff, ship_left - up_diff
    if degrees == 180:
        return ship_up - up_diff, ship_left - left_diff
    if degrees == 270:
        return ship_up - left_diff, ship_left + up_diff
    if degrees == 0:
        return up, left


def move_way_point(instruct_type, amount, up, left):
    if instruct_type == "N":
        up += amount
    elif instruct_type == "S":
        up -= amount
    elif instruct_type == "E":
        left += amount
    elif instruct_type == "W":
        left -= amount
    else:
        pass
    return up, left


def move_boat(way_point_up, way_point_left, boat_up, boat_left, amount):
    for i in range(amount):
        left_diff = way_point_left - boat_left
        up_diff = way_point_up - boat_up
        boat_up, boat_left, way_point_up, way_point_left = way_point_up, way_point_left, way_point_up + \
            up_diff, way_point_left + left_diff
    print("move_boat ", way_point_up, way_point_left, boat_up, boat_left)
    return way_point_up, way_point_left, boat_up, boat_left


ship_up = 0
ship_left = 0
way_point_up = 1
way_point_left = 10
for instruct in arr:

    instruct_type = instruct[:1]
    amount = int(instruct[1:])

    if instruct_type == "L":
        way_point_up, way_point_left = rotate_waypoint(
            way_point_up, way_point_left, amount, ship_up, ship_left)
    elif instruct_type == "R":
        way_point_up, way_point_left = rotate_waypoint(
            way_point_up, way_point_left, -1*amount, ship_up, ship_left)
    elif instruct_type == "F":
        way_point_up, way_point_left, ship_up, ship_left = move_boat(
            way_point_up, way_point_left, ship_up, ship_left, amount)
    else:
        way_point_up, way_point_left = move_way_point(
            instruct_type, amount, way_point_up, way_point_left)
    print(instruct_type, ship_left, ship_up, way_point_left, way_point_up)
print(abs(ship_up) + abs(ship_left))
