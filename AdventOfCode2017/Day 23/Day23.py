from threading import Thread
from queue import Queue

class Music:
    def __init__(self, instructions):
        self.registers: dict[str, int] = dict()
        self.registers['a'] = 1
        self.registers['b'] = 109900
        self.registers['c'] = 126900
        self.registers['d'] = 2
        self.registers['e'] = 0
        self.registers['f'] = 1
        self.registers['g'] = 0
        self.registers['h'] = 0
        self.counts = 0
        self.instruction = 0
        self.allInstructions = instructions


    def run(self):
        while self.instruction in self.allInstructions:
            ins = self.allInstructions[self.instruction]
            if ins.startswith('set'):
                x,y = ins.split(' ')[1], ins.split(' ')[2]
                if y in self.registers:
                    y = self.registers[y]
                self.set(x, int(y))
            elif ins.startswith('sub'):
                x,y = ins.split(' ')[1], ins.split(' ')[2]
                if y in self.registers:
                    y = self.registers[y]
                self.sub(x, int(y))
            elif ins.startswith('mul'):
                x,y = ins.split(' ')[1], ins.split(' ')[2]
                if y in self.registers:
                    y = self.registers[y]
                self.mul(x, int(y))
            elif ins.startswith('jnz'):
                x, y = ins.split(' ')[1], ins.split(' ')[2]
                if x in self.registers:
                    x = self.registers[x]
                x = int(x)
                if y in self.registers:
                    y = self.registers[y]
                y = int(y)
                self.jnz(x, y)

    def set(self, register, value):
        self.registers[register] = value
        self.instruction += 1

    def sub(self, register, value):
        if register not in self.registers:
            self.registers[register] = 0
        self.registers[register] -= value
        self.instruction += 1
    
    def mul(self, register, value):
        self.counts += 1
        if register not in self.registers:
            self.registers[register] = 0
        self.registers[register] *= value
        self.instruction += 1

    def mod(self, register, value):
        if register not in self.registers:
            self.registers[register] = 0
        self.registers[register] %= value
        self.instruction += 1

    def jnz(self, register, offset):
        print(register, offset, self.registers)
        if register in self.registers:
            if self.registers[register] != 0:
                self.instruction += offset
        elif register != 0:
            self.instruction += offset
        else:
            self.instruction += 1

    
fileContents = open("AdventOfCode2017/Day 23/input.txt")
arr = fileContents.read().split('\n')

instructions = dict()
for i, c in enumerate(arr):
    instructions[i] = c
    
def orchestrate():
    m = Music(instructions)
    m.run()
    print(m.registers['h'])

orchestrate()