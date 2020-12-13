with open('day13.txt') as file:
    data = file.read().splitlines()

timestamp = int(data[0])
busses = [int(l) if l != "x" else None for l in data[1].split(",")]

# Part 1

best_bus = None
min_wait_time = float('inf')

for bus in busses:
    if bus:
        wait_time = bus - timestamp % bus
        if min_wait_time > wait_time:
            min_wait_time = wait_time
            best_bus = bus

print(best_bus * min_wait_time)

# Part 2

timestamp = 0

while not all([(timestamp + k) % bus == 0 for k, bus in enumerate(busses) if bus]):
    valid_busses = [bus for k, bus in enumerate(
        busses) if bus and (timestamp + k) % bus == 0]
    prod = 1
    for bus in valid_busses:
        prod *= bus
    timestamp += prod

print(timestamp)