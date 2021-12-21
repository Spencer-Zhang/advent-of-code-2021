from collections import defaultdict
from copy import copy

# with open('example.txt') as f:
with open('input.txt') as f:
  input_lines = f.readlines()
  fish_list = map(int, input_lines[0].strip().split(","))

fish_map = defaultdict(int)

for f in fish_list:
  fish_map[f] += 1
print fish_map

for i in range(1, 257):
  next_map = defaultdict(int)
  for f in range(len(fish_list)):
    for j in range(1, 9):
      next_map[j-1] = fish_map[j]
  next_map[8] = fish_map[0]
  next_map[6] += fish_map[0]
  fish_map = next_map

  print i, sum([fish_map[i] for i in range(0, 9)])