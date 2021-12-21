from collections import defaultdict
from copy import copy

# with open('example.txt') as f:
with open('input.txt') as f:
  input_lines = f.readlines()
  risk_map = []
  for line in input_lines:
    risk_map.append([int(c) for c in line.strip()])

dim = len(risk_map[0])

def increase(row, i):
  new_row = []
  for n in row:
    next_n = n + i
    if next_n > 9:
      next_n -= 9
    new_row.append(next_n)
  return new_row

expanded_map = []
for row in risk_map:
  new_row = []
  for i in range(0,5):
    new_row += increase(row, i)
  expanded_map.append(new_row)

for i in range(4 * dim):
  expanded_map.append(increase(expanded_map[i], 1))

dim *= 5
risk_map = expanded_map

# for row in expanded_map:
#   print "".join(map(str,row))

risk_to_node_map = defaultdict(list)
risk_to_node_map[0] = [(0,0)]
visited = set()

def increase_risk(x, y):
  global dim, risk_to_node_map, visited, risk_map, current_risk
  if x < 0 or x >= dim or y < 0 or y >= dim:
    return
  if (x,y) in visited:
    return
  target_risk = risk_map[y][x] + current_risk
  risk_to_node_map[target_risk].append((x,y))
  visited.add((x,y))


for current_risk in range(0, 5000):
  for x, y in risk_to_node_map[current_risk]:
    if x == dim-1 and y == dim-1:
      print current_risk
      exit

    increase_risk(x-1, y)
    increase_risk(x+1, y)
    increase_risk(x, y-1)
    increase_risk(x, y+1)
