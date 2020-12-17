from collections import defaultdict

with open('day17.txt') as fp:
    region = fp.read().splitlines()
    initial = set()
    for y in range(len(region)):
        for x in range(len(region[y])):
            if region[y][x] == '#':
                initial.add((x, y, 0, 0))


def active_cubes(dim4 = False):
    active = initial.copy()
    w_space = (-1, 0, 1) if dim4 else [0]
    vectors = [(x, y, z, w) for x in (-1, 0, 1) \
                            for y in (-1, 0, 1) \
                            for z in (-1, 0, 1) \
                            for w in w_space if (x, y, z, w) != (0, 0, 0, 0)]
    for _ in range(1, 7):
        span = defaultdict(int)
        for (x, y, z, w) in active:
            for dx, dy, dz, dw in vectors:
                span[(x + dx, y + dy, z + dz, w + dw)] += 1
                
        update = set()
        for coord in span:
            if coord in active:
                if 2 <= span[coord] <= 3:
                    update.add(coord)
            else:
                if span[coord] == 3:
                    update.add(coord)
        active = update.copy()
    return len(active)


print("Active cubes in 3D:", active_cubes(dim4 = False))
print("Active cubes in 4D:", active_cubes(dim4 = True))
