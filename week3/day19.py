from functools import lru_cache
from itertools import product

with open('day19.txt') as fp:
    lines = fp.read().splitlines()
    # lines = ['0: 4 1 5', '1: 2 3 | 3 2', '2: 4 4 | 5 5', '3: 4 5 | 5 4', '4: "a"', '5: "b"', \
    #          '', 'ababbb', 'bababa', 'abbbab', 'aaabbb', 'aaaabbb']
    rule_strings = lines[:lines.index('')]
    messages = lines[lines.index('') + 1:]
    rules = dict()
    for string in rule_strings:
        key, description = string.split(':')
        rules[int(key)] = description.replace('"', '').strip()


@lru_cache
def candidates(rule):
    strings = []
    if rule.isalpha():
        strings.append(rule)
    else:
        for subrule in rule.split('|'):
            criteria = map(int, subrule.split())
            combs = []
            for crit in criteria:
                combs.append(candidates(rules[crit]))
            strings.extend(list(map(lambda comb: ''.join(comb), product(*combs))))
    return strings


def check_messages(messages):
    valid = 0
    possible = candidates(rules[0])
    for message in messages:
        if message in possible:
            valid += 1
    return valid


print("Matching messages:", check_messages(messages))
