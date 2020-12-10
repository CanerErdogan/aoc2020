from collections import defaultdict

with open('day10.txt') as fp:
    adapters = sorted(list(map(int, fp.read().splitlines())))
    adapters.append(adapters[-1] + 3)

def diff1x3(adapters):
    diff1 = diff3 = 0
    rating = 0
    for adapter in adapters:
        diff = adapter - rating
        if diff == 1:
            diff1 += 1
        if diff == 3:
            diff3 += 1
        rating = adapter
    return diff1 * diff3


def arrange(adapters):
    attempts = defaultdict(int)
    attempts[0] = 1
    for adapter in adapters:
        attempts[adapter] = sum([attempts[adapter - d] for d in [1, 2, 3]])
    return attempts[adapters[-1]]


print("Differences 1 times 3:", diff1x3(adapters))
print("Possible arrangements:", arrange(adapters))
