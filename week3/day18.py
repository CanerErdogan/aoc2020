from operator import add, sub, mul
from functools import reduce

with open('day18.txt') as fp:
    lines = fp.read().splitlines()


def parse(string, evaluation):
    parts = string.split(' ')
    elements = []
    substring = ''
    brace = 0
    for part in parts:
        if brace == 0:
            if part.isnumeric():
                elements.append(int(part))
            elif part in '*+-':
                elements.append(part)
            else:
                brace += part.count('(')
                substring = part[1:]
        else:
            if '(' in part:
                brace += part.count('(')
                substring = ' '.join([substring, part])
            elif ')' in part:
                brace -= part.count(')')
                if brace == 0:
                    substring = ' '.join([substring, part[:-1]])
                    elements.append(evaluation(parse(substring, evaluation)))
                    substring = ''
                else:
                    substring = ' '.join([substring, part])
            else:
                substring = ' '.join([substring, part])
    return elements
    

def no_precedence(elements):
    left = right = oper = None
    for element in elements:
        if not left:
            left = element
        elif not oper:
            if element == '*':
                oper = mul
            else:
                oper = add if element == '+' else sub
        elif not right:
            right = element
            left = oper(left, right)
            oper = right = None
    return left


def precedence(elements):
    left = right = oper = None
    update = elements.copy()
    while '+' in update or '-' in update:
        update = []
        for element in elements:
            if not left:
                left = element
                update.append(left)
            elif not oper:
                if element == '*':
                    if not update or update[-1] == '*':
                        update.extend([left, element])
                    else:
                        update.append(element)
                    left = None
                else:
                    oper = add if element == '+' else sub
            elif not right:
                right = element
                left = oper(left, right)
                if not update or update[-1] == '*':
                    update.append(left)
                else:
                    update[-1] = left
                oper = right = None
    return reduce(mul, [e for e in update if e != '*'])


def solve_lines(lines, evaluation):
    results = []
    for line in lines:
        results.append(evaluation(parse(line, evaluation)))
    return sum(results)


print("Without precedence:", solve_lines(lines, evaluation = no_precedence))
print("With precedence:", solve_lines(lines, evaluation = precedence))

# assert solve_lines(["2 * 3 + (4 * 5)"]) == 26
# assert solve_lines(["5 + (8 * 3 + 9 + 3 * 4 * 3)"]) == 437
# assert solve_lines(["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"]) == 12240
# assert solve_lines(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]) == 13632

# assert solve_lines(["2 * 3 + (4 * 5)"], precedence) == 46
# assert solve_lines(["5 + (8 * 3 + 9 + 3 * 4 * 3)"], precedence) == 1445
# assert solve_lines(["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"], precedence) == 669060
# assert solve_lines(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"], precedence) == 23340
