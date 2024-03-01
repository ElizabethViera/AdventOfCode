import sys
sys.setrecursionlimit(12870000)

currentLocation = 0
steps = 0
ones = set()

def A():
    global currentLocation
    global steps
    global ones
    if steps == 0: # my input number
        raise ValueError('answer = ', len(ones))
    if currentLocation not in ones:
        ones.add(currentLocation)
        currentLocation += 1
        steps += 1
        B()
    else:
        ones.remove(currentLocation)
        currentLocation -= 1
        steps += 1
        B()

def B():
    global currentLocation
    global steps
    global ones
    if steps == 0: # my input number
        raise ValueError('answer = ', len(ones))
    if currentLocation not in ones:
        ones.add(currentLocation)
        currentLocation -= 1
        steps += 1
        C()
    else:
        ones.remove(currentLocation)
        currentLocation += 1
        steps += 1
        E()

def C():
    global currentLocation
    global steps
    global ones
    if steps == 0: # my input number
        raise ValueError('answer = ', len(ones))
    if currentLocation not in ones:
        ones.add(currentLocation)
        currentLocation += 1
        steps += 1
        E()
    else:
        ones.remove(currentLocation)
        currentLocation -= 1
        steps += 1
        D()

def D():
    global currentLocation
    global steps
    global ones
    if steps == 0: # my input number
        raise ValueError('answer = ', len(ones))
    if currentLocation not in ones:
        ones.add(currentLocation)
        currentLocation -= 1
        steps += 1
        A()
    else:
        currentLocation -= 1
        steps += 1
        A()

def E():
    global currentLocation
    global steps
    global ones
    if steps == 0: # my input number
        raise ValueError('answer = ', len(ones))
    if currentLocation not in ones:
        currentLocation += 1
        steps += 1
        A()
    else:
        ones.remove(currentLocation)
        currentLocation += 1
        steps += 1
        F()

def F():
    global currentLocation
    global steps
    global ones
    if steps == 0: # my input number
        raise ValueError('answer = ', len(ones))
    if currentLocation not in ones:
        ones.add(currentLocation)
        currentLocation += 1
        steps += 1
        E()
    else:
        currentLocation += 1
        steps += 1
        A()

A()