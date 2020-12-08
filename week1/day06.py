from functools import reduce

with open('day06.txt') as fp:
    record = fp.read().split('\n\n')


def count_any_yes(record):
    clear_newline = lambda entry: entry.replace('\n', '')
    batch = list(map(clear_newline, record))
    groups = []
    for answers in batch:
        new_group = set()
        for answer in answers:
            new_group.add(answer)
        groups.append(new_group.copy())
        new_group.clear()

    return sum([len(group) for group in groups])


def count_all_yes(record):
    batch = map(str.split, record)
    groups = []
    for group_answers in batch:
        group_answers = list(map(set, group_answers))
        all_yes = reduce(set.intersection, group_answers)
        groups.append(all_yes)

    return sum([len(group) for group in groups])


print("One answered yes:", count_any_yes(record))
print("All answered yes:", count_all_yes(record))
