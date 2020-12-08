import re
from functools import lru_cache

with open('day07.txt') as fp:
    batch = list(map(lambda entry: entry.strip('.'),
        fp.read().strip().split('\n')))
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


@lru_cache
def check_gold(color):
    for bag in bag_dict[color].keys():
        if bag == 'shiny gold':
            return True
        if check_gold(bag):
            return True


def contains_any_gold(bag_dict):
    return len([bag for bag in bag_dict.keys() if check_gold(bag)])


@lru_cache
def bags_inside(color):
    count = 0
    for color_inside, amount in bag_dict[color].items():
        count += amount * (1 + bags_inside(color_inside))
    return count


print("Bags containing shiny gold:", contains_any_gold(bag_dict))
print("Bags in shiny gold:", bags_inside('shiny gold'))
