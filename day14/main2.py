from collections import defaultdict
from copy import copy

# with open('example.txt') as f:
with open('input.txt') as f:
  input_lines = f.readlines()

  polymer = input_lines.pop(0).strip()
  input_lines.pop(0)

  instructions = {}
  while len(input_lines) > 0:
    next_line = input_lines.pop(0).strip().split(" -> ")
    instructions[next_line[0]] = next_line[1]

duo_count = defaultdict(int)

for x in range(len(polymer) - 1):
  duo_count[polymer[x:x+2]] += 1

for i in range(40):
  print i
  next_count = copy(duo_count)
  
  for target in instructions:
    insert = instructions[target]
    first = target[0] + insert
    second = insert + target[1]
    next_count[target] -= duo_count[target]
    next_count[first] += duo_count[target]
    next_count[second] += duo_count[target]
  
  duo_count = next_count


c_count = defaultdict(int)
for duo in duo_count:
  c_count[duo[0]] += duo_count[duo]
  c_count[duo[1]] += duo_count[duo]
c_count[polymer[0]] += 1
c_count[polymer[-1]] += 1

for c in c_count:
  c_count[c] = c_count[c]/2

most_common = c_count.keys()[0]
least_common = c_count.keys()[0]


print(c_count)
for c in c_count.keys():
  if c_count[c] > c_count[most_common]:
    most_common = c
  if c_count[c] < c_count[least_common]:
    least_common = c

print most_common
print least_common
print c_count[most_common] - c_count[least_common]