import re
from functools import lru_cache

with open('day07.txt') as fp:
    batch = fp.read().strip().split('\n')
    line_regex = re.compile(r"(?P<color>[a-z ]+) bags contain (?P<content>.+).")
    content_regex = re.compile(r"(?P<amount>\d+) (?P<color_inside>[a-z ]+) bag")
    bag_dict = dict()
    for line in batch:
        color, content = line_regex.match(line).groups()
        content_dict = dict()
        if 'no other' not in content:
            for item in content.split(', '):
                amount, color_inside = content_regex.match(item).groups()
                content_dict[color_inside] = int(amount)
        bag_dict[color] = content_dict


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
