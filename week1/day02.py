import re
import operator

with open('day02.txt', 'r') as fp:
  lines = fp.read()
  regex = r"(?P<lower>\d+)-(?P<upper>\d+) (?P<char>\w): (?P<password>\w+)"
  matches = re.findall(regex, lines)


def char_count():
  correct = list(filter(lambda match:
    match[3].count(match[2]) >= int(match[0]) and
    match[3].count(match[2]) <= int(match[1]), matches))
  return len(correct)


print(char_count())

def position_check():
  correct = list(filter(lambda match: operator.xor(
    match[3][int(match[0]) - 1] == match[2],
    match[3][int(match[1]) - 1] == match[2]), matches))
  return len(correct)


print(position_check())
