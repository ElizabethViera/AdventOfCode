from threading import Thread
from queue import Queue

class Music:
    def __init__(self, name, instructions):
        self.registers: dict[str, int] = dict()
        self.name = name
        self.registers['p'] = name
        self.instruction = 0
        self.allInstructions = instructions
        self.receivedValues = Queue()
        self.other = None
        self.sends = 0

    def registerOther(self, other):
        self.other = other

    def run(self):
        while self.instruction in self.allInstructions:
            ins = self.allInstructions[self.instruction]
            if ins.startswith('snd'):
                self.snd(ins.split(' ')[1])
            elif ins.startswith('rcv'):
                self.rcv(ins.split(' ')[1])
            elif ins.startswith('set'):
                x,y = ins.split(' ')[1], ins.split(' ')[2]
                if y in self.registers:
                    y = self.registers[y]
                self.set(x, int(y))
            elif ins.startswith('add'):
                x,y = ins.split(' ')[1], ins.split(' ')[2]
                if y in self.registers:
                    y = self.registers[y]
                self.add(x, int(y))
            elif ins.startswith('mul'):
                x,y = ins.split(' ')[1], ins.split(' ')[2]
                if y in self.registers:
                    y = self.registers[y]
                self.mul(x, int(y))
            elif ins.startswith('mod'):
                x,y = ins.split(' ')[1], ins.split(' ')[2]
                if y in self.registers:
                    y = self.registers[y]
                self.mod(x, int(y))
            elif ins.startswith('jgz'):
                x, y = ins.split(' ')[1], ins.split(' ')[2]
                if x in self.registers:
                    x = self.registers[x]
                x = int(x)
                if y in self.registers:
                    y = self.registers[y]
                y = int(y)
                self.jgz(x, y)

    def set(self, register, value):
        self.registers[register] = value
        self.instruction += 1

    def add(self, register, value):
        if register not in self.registers:
            self.registers[register] = 0
        self.registers[register] += value
        self.instruction += 1
    
    def mul(self, register, value):
        if register not in self.registers:
            self.registers[register] = 0
        self.registers[register] *= value
        self.instruction += 1

    def mod(self, register, value):
        if register not in self.registers:
            self.registers[register] = 0
        self.registers[register] %= value
        self.instruction += 1

    def jgz(self, register, offset):
        if register in self.registers:
            if self.registers[register] > 0:
                self.instruction += offset
        elif register > 0:
            self.instruction += offset
        else:
            self.instruction += 1

    def rcv(self, register):
        try:
            self.registers[register] = self.receivedValues.get(timeout=2)
            self.instruction += 1
        except:
            print(self.name, ' is sleeping, current answer is ', self.sends)

        

    def snd(self, register):
        self.sends += 1
        if self.other is None:
            raise ValueError('Other is None')
        self.other.receivedValues.put(self.registers[register])
        self.instruction += 1
    
fileContents = open("AdventOfCode2017/Day 18/input.txt")
arr = fileContents.read().split('\n')

instructions = dict()
for i, c in enumerate(arr):
    instructions[i] = c
    
def orchestrate():
    m0 = Music(0, instructions)
    m1 = Music(1, instructions)
    m0.registerOther(m1)
    m1.registerOther(m0)
    t0 = Thread(target=m0.run)
    t1 = Thread(target=m1.run)
    t0.start()
    t1.start()

orchestrate()