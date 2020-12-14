import re
from collections import defaultdict
from itertools import combinations

with open('day14.txt') as fp:
    lines = fp.read().splitlines()
    re_mask = re.compile(r"[01X]+")
    re_mem = re.compile(r"\[(?P<address>\d+)\] = (?P<value>\d+)")


def version1():
    memory = defaultdict(int)
    for line in lines:
        if line.startswith('mask'):
            mask = re_mask.search(line).group()
            mask_and = int(mask.replace('X', '1'), 2)
            mask_or = int(mask.replace('X', '0'), 2)
        elif line.startswith('mem'):
            mem_match = re_mem.search(line)
            address = int(mem_match.group('address'))
            value = int(mem_match.group('value'))
            memory[address] = (value & mask_and) | mask_or
    return sum(memory.values())


def version2():
    memory = defaultdict(int)
    for line in lines:
        if line.startswith('mask'):
            mask = re_mask.search(line).group()
            mask_or = int(mask.replace('X', '1'), 2)
            x_loc = [len(mask) - i - 1 for i, c in enumerate(mask) if c == 'X']
            diff = sum([2**bit for bit in x_loc])
        elif line.startswith('mem'):
            mem_match = re_mem.search(line)
            address = int(mem_match.group('address'))
            value = int(mem_match.group('value'))
            table = []
            for i in range(len(x_loc) + 1):
                table.extend(list(combinations(x_loc, i)))
            for comb in table:
                sub_address = (address | mask_or) - diff
                for bit in comb:
                    sub_address += 2**bit
                memory[sub_address] = value
    return sum(memory.values())
    

print("Version 1:", version1())
print("Version 2:", version2())
