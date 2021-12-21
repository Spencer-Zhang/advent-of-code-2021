cave_map = {}

with open('input.txt') as f:
  for line in f.readlines():
    nodes = line.strip().split("-")
    for node in nodes:
      if not node in cave_map:
        cave_map[node] = []
    cave_map[nodes[0]].append(nodes[1])
    cave_map[nodes[1]].append(nodes[0])

def find_next_paths(path, revisited, finished_paths):
  current_node = path[-1]

  if current_node == "end":
    finished_paths.append(path)
    return []

  next_nodes = cave_map[current_node]
  next_paths = []

  lower_limit = 1 if revisited else 2

  for n in next_nodes:
    if n == "start":
      continue
    elif n == n.lower() and path.count(n) >= lower_limit:
      continue
    else:
      if not revisited and (n == n.upper() or path.count(n) == 0):
        next_paths.append((list(path) + [n], False))
      else:
        next_paths.append((list(path) + [n], True))
  return next_paths

finished_paths = []

paths = [(["start"], False)]
while len(paths) > 0:
  path, revisited = paths.pop(0)
  paths += find_next_paths(path, revisited, finished_paths)

# print cave_map
print len(finished_paths)
# for path in finished_paths:
#   print path