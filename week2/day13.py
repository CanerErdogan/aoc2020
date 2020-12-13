from functools import reduce
from operator import mul

with open('day13.txt') as fp:
    earliest = int(fp.readline())
    buses = fp.readline().strip().split(',')
    ids = [int(bus) for bus in buses if bus != 'x']

    
def idxwait(buses):
    timestamp = earliest
    while True:
        departs = list(filter(lambda bus: timestamp % bus == 0, ids))
        if departs:
            return departs[0] * (timestamp - earliest)
        timestamp += 1


def offset_match(buses):
    timestamp = 0
    offsets = list(map(lambda bus: buses.index(str(bus)), ids))    

    while True:
        departs = list(filter(lambda bus: \
            (timestamp + offsets[ids.index(bus)]) % bus == 0, ids))
        if departs == ids:
            return timestamp + offsets[0]
        timestamp += reduce(mul, departs)


print("Earliest x wait:", idxwait(buses))
print("Offsets match:", offset_match(buses))
