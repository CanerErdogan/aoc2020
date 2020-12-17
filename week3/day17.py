with open('day17.txt') as fp:
    region = fp.read().splitlines()
    # region = [".#.", "..#", "###"]
    vectors = [(x, y, z) for x in (-1, 0, 1) \
                         for y in (-1, 0, 1) \
                         for z in (-1, 0, 1) if (x, y, z) != (0, 0, 0)]
    active = set()
    for y in range(len(region)):
        for x in range(len(region[y])):
            if region[y][x] == '#':
                active.add((x, y, 0))

for cycle in range(1, 7):
    span = []
    for (x, y, z) in active:
        for dx, dy, dz in vectors:
            span.append((x + dx, y + dy, z + dz))
            
    updated = set()
    for coord in span:
        if coord in active:
            if 2 <= span.count(coord) <= 3:
                updated.add(coord)
        else:
            if span.count(coord) == 3:
                updated.add(coord)
    active = updated.copy()

print(len(active))
