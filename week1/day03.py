with open('day03.txt') as fp:
  area = fp.readlines()

def trees_count(area):
  x = -3
  trees = 0
  for line in area:
    x += 3
    row = line.replace('\n', '')
    if row[x % len(row)] == '#':
      trees += 1
  return trees


print(trees_count(area))


def trees_multiplied(area):
  slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  result = 1
  for slope in slopes:
    x, y = -slope[0], -slope[1]
    trees = 0
    while y < len(area) - slope[1]:
      x += slope[0]
      y += slope[1]
      row = area[y].replace('\n', '')
      if row[x % len(row)] == '#':
        trees += 1
    result *= trees
  return result


print(trees_multiplied(area))
