class Music:
    def __init__(self, name):
        self.registers: dict[str, int] = dict()
        self.registers['p'] = name
        self.instruction = 0
        self.receivedValues = []

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

    def rcv(self, register):
        if self.receivedValues != []:
            self.registers[register] = self.receivedValues.pop(0)
            self.instruction += 1
        else:
            #sleep for a while and check again
            # wait for value
            pass

    def snd(self, register):
        return self.registers[register]
    
def orchestrate():
    m0 = Music(0)
    m1 = Music(1)