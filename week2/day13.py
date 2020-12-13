with open('day13.txt') as fp:
    earliest = int(fp.readline())
    buses = fp.readline().strip().split(',')
    earliest = 939
    buses = '7,13,x,x,59,x,31,19'.split(',')
    ids = [int(bus) for bus in buses if bus != 'x']

    
def idxwait(buses):
    timestamp = earliest
    while True:
        departs = list(filter(lambda bus: timestamp % bus == 0, ids))
        if departs:
            return departs[0] * (timestamp - earliest)
        timestamp += 1


def offset_match(buses):
    timestamp = 1000000#100000000000000
    while timestamp % ids[0] != 0:
        timestamp += 1

    offsets = list(map(lambda bus: buses.index(str(bus)), ids))
    while True:
        departs = [ids[0]]
        for i in range(1, len(ids)):
            if (timestamp + offsets[i]) % ids[i] != 0:
                break
            departs.append(ids[i])

        if departs == ids:
            return timestamp
        timestamp += ids[0]


print(idxwait(buses))
print(offset_match(buses))
