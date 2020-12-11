from collections import defaultdict

with open('day11.txt') as fp:
    initial_rows = fp.read().splitlines()
    vectors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def occupancy(near, rows, x, y):
    occupied = 0
    for vx, vy in vectors:
        unit = 1
        dx = vx
        dy = vy
        while x + dx >= 0 and x + dx < len(rows[y]) and \
              y + dy >= 0 and y + dy < len(rows):
            if rows[y + dy][x + dx] == '#':
                occupied += 1
                break
            elif near or rows[y + dy][x + dx] == 'L':
                break
            unit += 1
            dx = vx * unit
            dy = vy * unit

    return occupied


def arrange_seats(initial_rows, near=True):
    tolerance = 4 if near else 5
    rows = initial_rows.copy()
    while True:
        total_occupied = 0
        new_rows = []
        for y in range(len(rows)):
            new_row = ''
            for x in range(len(rows[y])):
                seat = rows[y][x]
                if seat == '.':
                    new_row += '.'
                else:
                    occupied = occupancy(near, rows, x, y)
                    if seat == 'L' and occupied == 0:
                        new_row += '#'
                        total_occupied += 1
                    elif seat == '#' and occupied >= tolerance:
                        new_row += 'L'
                    else:
                        new_row += seat
            new_rows.append(new_row)
        if new_rows == rows:
            return sum(row.count('#') for row in rows)
        rows = new_rows


print("Total occupied for near:", arrange_seats(initial_rows, True))
print("Total occupied for far:", arrange_seats(initial_rows, False))
