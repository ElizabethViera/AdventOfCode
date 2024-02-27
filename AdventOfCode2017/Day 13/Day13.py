fileContents = open("AdventOfCode2017/Day 13/input.txt")
arr = fileContents.read().split('\n')

from dataclasses import dataclass
import math

@dataclass
class Info:
    period: int
    bad_times: list[bool]

    def or_info(self, other: 'Info'):
        new_len = math.lcm(len(self.bad_times), len(other.bad_times))
        new_bad_times = [self.bad_times[i%self.period] or other.bad_times[i%other.period] for i in range(new_len)]
        return Info(period=new_len, bad_times=new_bad_times)


everything_previous = Info(period=1, bad_times=[False])
for i, line in enumerate(arr):
    offset = int(line.split(':')[0])
    period = 2*int(line.split(' ')[1])-2
    new_bad_times = [i == (-offset)%period for i in range(period)]
    everything_previous = everything_previous.or_info(Info(period=period, bad_times = new_bad_times))
    print(i, everything_previous.period)
    
print(everything_previous.bad_times.index(False))


