import re

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


def scanning_error_rate():
    errors = []
    for ticket in nearby_tickets:
        for value in ticket:
            valid = False
            for rule in rules.values():
                if (rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]):
                    valid = True
                    break
            if not valid:
                errors.append(value)
                break
    return sum(errors)


print("Scanning error rate:", scanning_error_rate())
