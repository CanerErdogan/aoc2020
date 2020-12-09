with open('day09.txt') as fp:
    input_list = fp.read().strip().split('\n')
    numbers = list(map(int, input_list))

# a = range(10)
# for i in range(10 - 5):
#     sliced = a[i : i + 5]
#     target = a[i + 5]
#     print(target, list(sliced))

def first_weakness(numbers):
    for i in range(len(numbers) - 25):
        target = numbers[i + 25]
        batch = list(filter(lambda num: num < target, numbers[i : i + 25]))
        for number in batch:
            found = False
            remainder = target - number
            if remainder in batch:
                found = True
                break
        if not found:
            return target


def encryption_weakness(numbers, weakness):
    for i in range(numbers.index(weakness)-1, 0, -1):
        for j in range(1, i):
            batch = numbers[i - j : i]
            if sum(batch) > weakness:
                break
            if sum(batch) == weakness:
                return min(batch) + max(batch)
    


weakness = first_weakness(numbers)
print("First weakness:", weakness)
print("Encryption weakness:", encryption_weakness(numbers, weakness))
