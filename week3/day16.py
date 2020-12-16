import re
from collections import defaultdict

with open('day16.txt') as fp:
    lines = [line for line in fp.read().splitlines() if line]
    rule_regex = re.compile(
        r"(?P<rule>[a-z ]+): (?P<l0>\d+)-(?P<h0>\d+) or (?P<l1>\d+)-(?P<h1>\d+)")
    rules = dict()
    while True:
        line = lines.pop(0)
        if line == 'your ticket:':
            your_ticket = tuple(map(int, lines.pop(0).split(',')))
            break
        rule_match = rule_regex.match(line)
        rules[rule_match.group('rule')] = (
            (int(rule_match.group('l0')), int(rule_match.group('h0'))),
            (int(rule_match.group('l1')), int(rule_match.group('h1'))))

    while line != 'nearby tickets:':
        line = lines.pop(0)

    nearby_tickets = []
    for line in lines:
        nearby_tickets.append(tuple(map(int, line.split(','))))


def scan_tickets():
    errors = []
    discard = []
    for i, ticket in enumerate(nearby_tickets):
        for value in ticket:
            valid = False
            for rule in rules.values():
                if (rule[0][0] <= value <= rule[0][1] or \
                    rule[1][0] <= value <= rule[1][1]):
                    valid = True
                    break
            if not valid:
                errors.append(value)
                discard.append(i)
                break
    valid_tickets = [ticket for i, ticket in enumerate(nearby_tickets) if i not in discard]
    return sum(errors), valid_tickets


def multiply_departures(valid_tickets):
    candidates = defaultdict(set)
    for rule, limits in rules.items():
        for i, key in enumerate(rules.keys()):
            column = [fields[i] for fields in valid_tickets]
            if all((limits[0][0] <= value <= limits[0][1] or \
                    limits[1][0] <= value <= limits[1][1]) for value in column):
                candidates[i].add(rule)

    default_ticket = {key: None for key in rules.keys()}
    cand_keys = list(candidates.keys())
    cand_values = list(candidates.values())
    keys_found = set()
    for candidate in sorted(cand_values, key=len):
        index = cand_keys[cand_values.index(candidate)]
        found_key = candidate.difference(keys_found).pop()
        keys_found.add(found_key)
        default_ticket[found_key] = index

    result = 1
    for key in default_ticket.keys():
        if key.startswith('departure'):
            result *= your_ticket[default_ticket[key]]
    return result


error, valid_tickets = scan_tickets()
print("Scanning error rate:", error)
print("Departures multiplied:", multiply_departures(valid_tickets))
