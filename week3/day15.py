from collections import defaultdict, deque


def nth_number(n):
    numbers = [0, 1, 5, 10, 3, 12, 19]
    turns = defaultdict(lambda: deque(maxlen=2))
    turn = 1
    while numbers:
        spoken = numbers.pop(0)
        turns[spoken].append(turn)
        turn += 1
    while turn <= n:
        if len(turns[spoken]) > 1:
            spoken = turns[spoken][-1] - turns[spoken][-2]
        else:
            spoken = 0
        turns[spoken].append(turn)
        turn += 1
    return spoken


print("2020th number:", nth_number(2020))
print("30Mth number:", nth_number(30000000))
