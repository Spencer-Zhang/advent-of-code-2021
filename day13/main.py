def reflect(original, axis):
  if original < axis:
    return original
  else:
    return 2 * axis - original

def replace_char_at_index(sample_str, n):
    sample_str = sample_str[0:n] + "X" + sample_str[n+1: ]


with open('input.txt') as f:
  input_lines = f.readlines()
  coordinates = set()
  
  while len(input_lines) > 0:
    line = input_lines.pop(0).strip()
    if line == "":
      break
    coordinate = map(lambda x: int(x), line.split(","))
    coordinates.add((coordinate[0], coordinate[1]))

  while len(input_lines) > 0:
    new_set = set()
    instruction = input_lines.pop(0).strip().split()
    fold = instruction[2].split("=")
    for c in coordinates:
      if fold[0] == "x":
        new_set.add((reflect(c[0], int(fold[1])), c[1]))
      if fold[0] == "y":
        new_set.add((c[0], reflect(c[1], int(fold[1]))))
    coordinates = new_set

print coordinates

# largest_x = 0
# largest_y = 0
# for c in coordinates:
#   largest_x = max(largest_x, c[0])
#   largest_y = max(largest_y, c[1])

grid = []
for i in range(6):
  grid.append(" " * 40)
for c in coordinates:
  grid[c[1]] = grid[c[1]][0:c[0]] + "X" + grid[c[1]][c[0]+1: ]

for g in grid:
  print g