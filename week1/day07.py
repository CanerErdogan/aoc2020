import re
from functools import lru_cache

with open('day07.txt') as fp:
    strip_dot = lambda entry: entry.strip('.')
    batch = list(map(strip_dot, fp.read().strip().split('\n')))
    regex = re.compile(r"(?P<amount>\d+) (?P<color>[a-z ]+)")

    bag_dict = dict()
    for line in batch:
        rule = line.replace(' bags', '').replace(' bag', '').split(' contain')
        bag = rule[0]
        contents = rule[1].strip().split(', ')
        content_dict = dict()
        for content in contents:
            if content != 'no other':
                amount = int(regex.match(content).group('amount'))
                color = regex.match(content).group('color')
                content_dict.update({color: amount})
        bag_dict[bag] = content_dict

print(bag_dict)

@lru_cache
def check_gold(color):
    for bag in bag_dict[color].keys():
        if bag == 'shiny gold':
            return True
        else:
            if check_gold(bag):
                return True
            # has_gold += 1
    #     else:
    #         has_gold += check_gold(bag)
    # return has_gold



def contains_any_cold(bag_dict):
    count = 0
    print(len(bag_dict.items()))
    for color, contents in bag_dict.items():
        if check_gold(color):
            count += 1
    return count

print(contains_any_cold(bag_dict))
# print(*bag_dict, sep='\n')
