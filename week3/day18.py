from operator import add, sub, mul

with open('day18.txt') as fp:
    lines = fp.read().splitlines()

def parse(string):
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
                    elements.append(evaluate(parse(substring)))
                    substring = ''
                else:
                    substring = ' '.join([substring, part])
            else:
                substring = ' '.join([substring, part])
    return elements#[2, '*', 3, '+', 20]
    

def evaluate(elements):
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


def solve_lines(lines):
    results = []
    for line in lines:
        results.append(evaluate(parse(line)))
    return sum(results)


print("Sum of all expressions:", solve_lines(lines))

# assert solve_lines(["2 * 3 + (4 * 5)"]) == 26
# assert solve_lines(["5 + (8 * 3 + 9 + 3 * 4 * 3)"]) == 437
# assert solve_lines(["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"]) == 12240
# assert solve_lines(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]) == 13632
