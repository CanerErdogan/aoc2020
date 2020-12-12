with open('day12.txt') as fp:
    lines = fp.read().splitlines()
    instructions = [[line[0], int(line[1:])] for line in lines]


def move_absolute(instructions):
    directions = ['E', 'S', 'W', 'N']
    dir_idx = 0
    position = [0, 0]

    for instruction in instructions:
        rotation = instruction[1] / 90 if instruction[0] in 'LR' else 0
        wise = -1 if instruction[0] == 'L' else 1
        dir_idx += int(rotation * wise)
        direction = directions[dir_idx % len(directions)]

        vertical = instruction[1] if instruction[0] in 'NS' or \
                                    direction in 'NS' and instruction[0] == 'F' else 0
        horizontal = instruction[1] if instruction[0] in 'EW' or \
                                    direction in 'EW' and instruction[0] == 'F' else 0
        sign = 1 if instruction[0] in 'NE' or \
                    direction in 'NE' and instruction[0] == 'F' else -1
        
        position[0] += horizontal * sign
        position[1] += vertical * sign

    return abs(position[0]) + abs(position[1])


def use_waypoint(instructions):
    position = [0, 0]
    waypoint = [10, 1]

    for instruction in instructions:
        if instruction[0] == 'F':
            position[0] += instruction[1] * waypoint[0]
            position[1] += instruction[1] * waypoint[1]
        else:
            if instruction[0] in 'LR':
                wise = -1 if instruction[0] == 'L' else 1
                transform = int(instruction[1] / 90 * wise) % 4
                if transform == 1:
                    waypoint = [waypoint[1], -waypoint[0]]
                elif transform == 2:
                    waypoint = [-waypoint[0], -waypoint[1]]
                elif transform == 3:
                    waypoint = [-waypoint[1], waypoint[0]]
                    
            vertical = instruction[1] if instruction[0] in 'NS' else 0
            horizontal = instruction[1] if instruction[0] in 'EW' else 0
            sign = 1 if instruction[0] in 'NE' else -1
            
            waypoint[0] += horizontal * sign
            waypoint[1] += vertical * sign

    return abs(position[0]) + abs(position[1])


print("Absolute movement:", move_absolute(instructions))
print("Waypoint movement:", use_waypoint(instructions))
