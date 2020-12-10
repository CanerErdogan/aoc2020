with open('day10.txt') as fp:
    adapters = list(map(int, fp.read().strip().split('\n')))

# adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

def diff1x3(adapters):
    diff1 = diff3 = 0
    rating = 0
    while True:
        if rating + 1 in adapters:
            rating += 1
            diff1 += 1
            continue
        if rating + 3 in adapters:
            rating += 3
            diff3 += 1
            continue
        if rating == max(adapters):
            rating += 3
            diff3 += 1
            return diff1 * diff3


print("Differences 1 times 3:", diff1x3(adapters))
