fileContents = open("AdventOfCode2023/Day 24/sampleInput.txt")
arr = fileContents.read().split("\n")
from fractions import Fraction

from dataclasses import dataclass
@dataclass
class pos3:
    x: Fraction
    y: Fraction
    z: Fraction

    def crossProduct(self, v:"pos3") -> "pos3":
        return pos3(self.y*v.z-self.z*v.y, self.z*v.x-self.x*v.z, self.x*v.y-self.y*v.x)

    def dotProduct(self,b:"pos3") -> Fraction:
        return self.x*b.x + self.y*b.y + self.z*b.z
    
    def addVec(self,b:"pos3") -> "pos3":
        return pos3(self.x + b.x, self.y + b.y, self.z + b.z)

    def subVec(self,b:"pos3") -> "pos3":
        return pos3(self.x - b.x, self.y - b.y, self.z - b.z)
    
    def scaleVec(self,s:Fraction) -> "pos3":
        return pos3(self.x*s, self.y*s, self.z*s)

    def getResult(self):
        return self.x + self.y + self.z
    

hails: dict[int, dict[str, pos3]] = dict()
for i,hail in enumerate(arr):
    pos = hail.split('@')[0].strip().split(',')
    pos = [int(x.strip()) for x in pos]
    vel = hail.split('@')[1].strip().split(',')
    vel = [int(x.strip()) for x in vel]
    hails[i] = dict()
    hails[i]['pos'] = pos3(Fraction(pos[0]), Fraction(pos[1]), Fraction(pos[2]))
    hails[i]['vel'] = pos3(Fraction(vel[0]), Fraction(vel[1]), Fraction(vel[2]))


stationary_hail = hails[0]
velocity_mod = stationary_hail['vel']

def translateVelocity(h: dict[int, dict[str, pos3]], v: pos3)-> dict[int, dict[str, pos3]]:
    new_h: dict[int, dict[str, pos3]] = dict()
    for hail in h:
        new_h[hail] = dict()
        new_h[hail]['vel'] = h[hail]['vel'].subVec(v)
        new_h[hail]['pos'] = h[hail]['pos']
    return new_h

hails_from_stationary = translateVelocity(hails, velocity_mod)

plane1, plane2, plane3 = hails_from_stationary[0]['pos'], hails_from_stationary[1]['pos'], hails_from_stationary[1]['pos'].addVec(hails_from_stationary[1]['vel'])
third_pos = hails_from_stationary[2]['pos']
third_vel = hails_from_stationary[2]['vel']

def planeRayIntersect(p1:pos3, p2:pos3, p3:pos3, pos:pos3, vel:pos3) -> Fraction:
    ...
    c21 = p2.subVec(p1)
    c32 = p3.subVec(p2)
    n = c21.crossProduct(c32)
    # (q - p1) dot n is zero iff q on plane
    # q = pos + t * vel
    # (pos + t * vel - p1) dot n = 0
    # pos dot n + t * (vel dot n) - p1 dot n = 0
    # t = (-pos dot n + p1 dot n)/ vel dot n
    t =(-pos.dotProduct(n) + p1.dotProduct(n))/vel.dotProduct(n)
    return t


third_t = planeRayIntersect(plane1, plane2, plane3, third_pos, third_vel)
# point of intersection
third_i = third_pos.addVec(third_vel.scaleVec(third_t))

fourth_pos, fourth_vel = hails_from_stationary[3]['pos'], hails_from_stationary[3]['vel']

fourth_t = planeRayIntersect(plane1, plane2, plane3, fourth_pos, fourth_vel)
fourth_i = fourth_pos.addVec(fourth_vel.scaleVec(fourth_t))

t_delta = fourth_t - third_t
i_delta = fourth_i.subVec(third_i)

velocity = i_delta.scaleVec(1/t_delta)

result = third_i.subVec(velocity.scaleVec(third_t))
print(result.getResult())
