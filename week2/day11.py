##.L#LL.LLLLLLLLLLLLLLLLL.LLLLL.LLLL.LLLLLLLLLLLLL.LLL.LLLLLLLLLLLL#

from collections import defaultdict

with open('day11.txt') as fp:
    initial_rows = fp.read().splitlines()
    # initial_rows = ['L.LL.LL.LL',
    #                 'LLLLLLL.LL',
    #                 'L.L.L..L..',
    #                 'LLLL.LL.LL',
    #                 'L.LL.LL.LL',
    #                 'L.LLLLL.LL',
    #                 '..L.L.....',
    #                 'LLLLLLLLLL',
    #                 'L.LLLLLL.L',
    #                 'L.LLLLL.LL']


surrounds = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
def occupancy(rows, x, y):
    occupied = 0
    for dx, dy in surrounds:
        if x + dx >= 0 and x + dx < len(rows[y]) and \
            y + dy >= 0 and y + dy < len(rows):
            if rows[y + dy][x + dx] == '#':
                occupied += 1
    return occupied

def arrange_seats(initial_rows):
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
                    occupied = occupancy(rows, x, y)
                    if seat == 'L' and occupied == 0:
                        new_row += '#'
                        total_occupied += 1
                    elif seat == '#' and occupied >= 4:
                        new_row += 'L'
                    else:
                        new_row += seat
            new_rows.append(new_row)
        if new_rows == rows:
            return sum(row.count('#') for row in rows)
        rows = new_rows
    # print(*rows, sep='\n')
    
    

print("Total occupied:", arrange_seats(initial_rows))
